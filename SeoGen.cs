using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Web;
using System.Web.Script.Serialization;

class SeoGen {
  static string Base, Py, Domain, Brand, PhoneDisplay, PhoneTel, Email, OgImage, LastMod;
  static Dictionary<string,string> Blurbs = new Dictionary<string,string>();

  static string Esc(string s) => HttpUtility.HtmlEncode(s ?? "");

  static string M(string py, string pat) => Regex.Match(py, pat).Groups[1].Value;

  static string PyCat(string inner) {
    var sb = new StringBuilder();
    foreach (Match pm in Regex.Matches(inner, "\"(?:\\\\.|[^\"\\\\])*\""))
      sb.Append(pm.Value.Trim('"').Replace("\\\"", "\""));
    return sb.ToString();
  }

  static string GetBlurb(string id) {
    var m = Regex.Match(Py, "\"" + Regex.Escape(id) + "\":\\s*\\((.*?)\\r?\\n\\s*\\),", RegexOptions.Singleline);
    return m.Success ? PyCat(m.Groups[1].Value) : "";
  }

  static string Head(string title, string desc, string path) {
    var url = Domain + path;
    return "  <meta charset=\"UTF-8\">\n  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n  <title>" + Esc(title) + "</title>\n  <meta name=\"description\" content=\"" + Esc(desc) + "\">\n  <meta name=\"robots\" content=\"index, follow\">\n  <meta name=\"theme-color\" content=\"#1d4f8f\">\n  <link rel=\"canonical\" href=\"" + url + "\">\n  <link rel=\"icon\" href=\"favicon.svg\" type=\"image/svg+xml\">\n  <link rel=\"apple-touch-icon\" href=\"images/og-default.svg\">\n  <meta property=\"og:type\" content=\"website\">\n  <meta property=\"og:title\" content=\"" + Esc(title) + "\">\n  <meta property=\"og:description\" content=\"" + Esc(desc) + "\">\n  <meta property=\"og:url\" content=\"" + url + "\">\n  <meta property=\"og:image\" content=\"" + OgImage + "\">\n  <meta property=\"og:locale\" content=\"he_IL\">\n  <meta property=\"og:site_name\" content=\"" + Esc(Brand) + "\">\n  <link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n  <link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n  <link href=\"https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600;700;800&display=swap\" rel=\"stylesheet\">\n  <link rel=\"stylesheet\" href=\"styles.css\">";
  }

  static string SiteHeader() {
    var nav = M(Py, "nav_extra or \"\"\"<ul>([\\s\\S]*?)</ul>\"\"\"");
    return "      <div class=\"site-header\">\n        <a href=\"index.html\" class=\"logo\">" + Brand + "</a>\n        <nav class=\"site-nav\" aria-label=\"nav\">\n          <ul>" + nav + "</ul>\n        </nav>\n        <a class=\"header-cta\" href=\"tel:" + PhoneTel + "\">" + PhoneDisplay + "</a>\n      </div>";
  }

  static string Breadcrumbs(List<Tuple<string,string>> items) {
    var aria = M(Py, "class=\"breadcrumbs\" aria-label=\"([^\"]+)\"");
    var sb = new StringBuilder("<nav class=\"breadcrumbs\" aria-label=\"" + aria + "\">");
    for (int i = 0; i < items.Count; i++) {
      if (i > 0) sb.Append("<span class=\"bc-sep\" aria-hidden=\"true\">›</span>");
      if (i == items.Count - 1) sb.Append("<span aria-current=\"page\">").Append(Esc(items[i].Item1)).Append("</span>");
      else sb.Append("<a href=\"").Append(items[i].Item2).Append("\">").Append(Esc(items[i].Item1)).Append("</a>");
    }
    sb.Append("</nav>");
    return sb.ToString();
  }

  static string Json(object o) => new JavaScriptSerializer { MaxJsonLength = int.MaxValue }.Serialize(o);

  static string FaqHtml(List<Tuple<string,string>> qa) {
    var title = M(Py, "class=\"section-title-bar\">([^<]+)</h2>\\s*\\n\\s*<dl class=\"faq-list\"");
    var sb = new StringBuilder("      <h2 class=\"section-title-bar\">" + title + "</h2>\n      <dl class=\"faq-list\">\n");
    foreach (var x in qa) sb.Append("        <div class=\"faq-item\"><dt>").Append(Esc(x.Item1)).Append("</dt><dd>").Append(Esc(x.Item2)).Append("</dd></div>\n");
    sb.Append("      </dl>");
    return sb.ToString();
  }

  static string Sticky() => Regex.Match(Py, "def sticky_bar\\(\\)[\\s\\S]*?return f\"\"\"([\\s\\S]*?)\"\"\"").Groups[1].Value.Replace("{PHONE_TEL}", PhoneTel);
  static string Footer() => Regex.Match(Py, "def footer_block\\(\\)[\\s\\S]*?return f\"\"\"([\\s\\S]*?)\"\"\"").Groups[1].Value.Replace("{BRAND}", Brand).Replace("{PHONE_TEL}", PhoneTel).Replace("{PHONE_DISPLAY}", PhoneDisplay);

  static string CityMeta(string city, string text) {
    var baseText = (text ?? "").Trim();
    var suffix = M(Py, "if len\\(base\\) < 120:\\s*base \\+= f\"([^\"]+)\"");
    if (baseText.Length < 120) baseText += suffix.Replace("{city}", city);
    if (baseText.Length > 160) return baseText.Substring(0, 160);
    return baseText;
  }

  static List<Tuple<string,string>> CityFaq(string name) {
    var block = M(Py, "def render_city_page\\([\\s\\S]*?faq = \\[([\\s\\S]*?)\\]\\s*\\n\\s*bc_html");
    var list = new List<Tuple<string,string>>();
    foreach (Match tm in Regex.Matches(block, "\\(f?\"((?:\\\\.|[^\"\\\\])*)\",\\s*\"((?:\\\\.|[^\"\\\\])*)\"\\)")) {
      var q = tm.Groups[1].Value.Replace("\\\"", "\"").Replace("{name}", name);
      var a = tm.Groups[2].Value.Replace("\\\"", "\"");
      list.Add(Tuple.Create(q, a));
    }
    return list;
  }

  static string RenderCity(Dictionary<string,object> city, string regionName, string regionId, List<Dictionary<string,object>> regionCities) {
    string name = city["name"].ToString(), file = city["file"].ToString(), text = city["text"].ToString(), path = "/" + file;
    var titleTpl = M(Py, "title = f\"((?:\\\\.|[^\"\\\\])*)\"");
    var title = titleTpl.Replace("{name}", name).Replace("{BRAND}", Brand);
    var desc = CityMeta(name, text);
    string blurb; Blurbs.TryGetValue(regionId, out blurb);
    var faq = CityFaq(name);
    var bc = new List<Tuple<string,string>> { Tuple.Create(M(Py, "bc_html = \\[\\(\"([^\"]+)\""), "index.html"), Tuple.Create(M(Py, ", \\(\"([^\"]+)\", \"areas.html\"\\)"), "areas.html"), Tuple.Create(name, file) };
    var skip = M(Py, "class=\"skip-link\">([^<]+)");
    var h1 = M(Py, "<h1>([^<]+\\{esc\\(name\\)\\})</h1>").Replace("{esc(name)}", Esc(name));
    var h2 = M(Py, "<h2>([^<]+\\{esc\\(name\\)\\}[^<]*)</h2>").Replace("{esc(name)}", Esc(name));
    var h3a = Regex.Matches(Py, "<h3>([^<]+\\{esc\\(name\\)\\}[^<]*)</h3>")[0].Groups[1].Value.Replace("{esc(name)}", Esc(name));
    var h3b = Regex.Matches(Py, "<h3>([^<]+)</h3>\\s*<ol>")[1].Groups[1].Value;
    var ul = M(Py, "<h3>[^<]*\\{esc\\(name\\)\\}[^<]*</h3>\\s*<ul>([\\s\\S]*?)</ul>");
    var ol = M(Py, "<h3>[^<]*</h3>\\s*<ol>([\\s\\S]*?)</ol>");
    var svcP = M(Py, "<p>HD[\\s\\S]*?\\{esc\\(name\\)\\}[\\s\\S]*?</p>").Replace("{esc(name)}", Esc(name)).Replace("{BRAND}", Brand);
    var nearbyTitle = M(Py, "nearby_cities_html[\\s\\S]*?return \\(\\s*'([^']+)'");
    var nearby = new StringBuilder();
    int n = 0;
    foreach (var c in regionCities) {
      if (c["file"].ToString() == file) continue;
      if (n++ >= 5) break;
      nearby.Append("<a href=\"").Append(c["file"]).Append("\">").Append(Esc(c["name"].ToString())).Append("</a>\n        ");
    }
    var nearbyHtml = n > 0 ? "      <h3>" + nearbyTitle + "</h3>\n      <nav class=\"city-links\" aria-label=\"" + nearbyTitle + "\">\n        " + nearby + "\n      </nav>" : "";
    var bcSchema = Json(new { context = "https://schema.org", type = "BreadcrumbList", itemListElement = new object[] { } });
    // build page
    var sb = new StringBuilder();
    sb.Append("<!DOCTYPE html>\n<html lang=\"he\" dir=\"rtl\">\n<head>\n").Append(Head(title, desc, path)).Append("\n</head>\n<body class=\"has-sticky-bar\">\n");
    sb.Append("  <a href=\"#main-content\" class=\"skip-link\">").Append(skip).Append("</a>\n  <header class=\"hero page-hero\"><div class=\"container\">\n");
    sb.Append(SiteHeader()).Append("\n      <div class=\"page-intro\">\n      ").Append(Breadcrumbs(bc)).Append("\n");
    sb.Append("        <p class=\"eyebrow\">").Append(Esc(regionName)).Append(" · ").Append(Esc(name)).Append("</p>\n");
    sb.Append("        <h1>").Append(h1).Append("</h1>\n        <p class=\"subtitle\">").Append(Esc(text)).Append("</p>\n");
    sb.Append("        <div class=\"hero-buttons\"><a class=\"button primary\" href=\"tel:").Append(PhoneTel).Append("\">").Append(PhoneDisplay).Append("</a><a class=\"button whatsapp wa-direct\" href=\"#\">wa</a></div>\n");
    sb.Append("      </div></div></header>\n  <main id=\"main-content\">\n    <section class=\"container section\"><div class=\"page-content-grid\"><div>\n");
    sb.Append("          <h2>").Append(h2).Append("</h2>\n          <p>").Append(Esc(text)).Append("</p><p>").Append(Esc(blurb)).Append("</p>\n          <p>").Append(svcP).Append("</p>\n");
    sb.Append("          <h3>").Append(h3a).Append("</h3><ul>").Append(ul).Append("</ul><h3>").Append(h3b).Append("</h3><ol>").Append(ol).Append("</ol>\n");
    if (n > 0) sb.Append(nearbyHtml).Append("\n");
    sb.Append("          <p><a href=\"areas.html\">back</a></p></div><div class=\"media-placeholder\"><span>").Append(Esc(name)).Append("</span></div></div></section>\n");
    sb.Append("    <section class=\"container section faq\" id=\"faq\">\n").Append(FaqHtml(faq)).Append("\n    </section>\n");
    sb.Append("    <section class=\"container section\" id=\"contact-form\">").Append(Regex.Match(Py, "def contact_form[\\s\\S]*?return f\"\"\"([\\s\\S]*?)\"\"\"").Groups[1].Value.Replace("{esc(city)}", Esc(name)).Replace("{city_val}", Esc(name)).Replace("{service_field}", "")).Append("</section>\n  </main>\n");
    sb.Append(Footer()).Append(Sticky());
    sb.Append("\n  <script type=\"application/ld+json\">").Append(BreadcrumbSchema(bc, path, name)).Append("</script>\n");
    sb.Append("  <script type=\"application/ld+json\">").Append(LocalBusiness(name, desc)).Append("</script>\n");
    sb.Append("  <script type=\"application/ld+json\">").Append(FaqSchema(faq)).Append("</script>\n  <script src=\"contact-form.js\" defer></script>\n</body></html>\n");
    return sb.ToString();
  }

  static string BreadcrumbSchema(List<Tuple<string,string>> bc, string path, string name) {
    var items = new List<object> {
      new { type="ListItem", position=1, name=bc[0].Item1, item=Domain+"/" },
      new { type="ListItem", position=2, name=bc[1].Item1, item=Domain+"/areas.html" },
      new { type="ListItem", position=3, name=name, item=Domain+path }
    };
    return Json(new Dictionary<string,object>{{"@context","https://schema.org"},{"@type","BreadcrumbList"},{"itemListElement",items}});
  }
  static string LocalBusiness(string city, string desc) => Json(new Dictionary<string,object>{{"@context","https://schema.org"},{"@type","LocalBusiness"},{"name",Brand},{"description",desc},{"telephone","+972528805053"},{"email",Email},{"url",Domain+"/"},{"image",OgImage},{"areaServed",new Dictionary<string,string>{{"@type","City"},{"name",city}}}});
  static string FaqSchema(List<Tuple<string,string>> qa) {
    var ents = qa.Select(q => new Dictionary<string,object>{{"@type","Question"},{"name",q.Item1},{"acceptedAnswer",new Dictionary<string,string>{{"@type","Answer"},{"text",q.Item2}}}}).ToList();
    return Json(new Dictionary<string,object>{{"@context","https://schema.org"},{"@type","FAQPage"},{"mainEntity",ents}});
  }

  static void Main(string[] args) {
    Base = args.Length > 0 ? args[0] : Directory.GetCurrentDirectory();
    var enc = new UTF8Encoding(false);
    Py = File.ReadAllText(Path.Combine(Base, "generate_seo.py"), enc);
    Domain = M(Py, "DOMAIN = \"([^\"]+)\"");
    Brand = M(Py, "BRAND = \"([^\"]+)\"");
    PhoneDisplay = M(Py, "PHONE_DISPLAY = \"([^\"]+)\"");
    PhoneTel = M(Py, "PHONE_TEL = \"([^\"]+)\"");
    Email = M(Py, "EMAIL = \"([^\"]+)\"");
    OgImage = Domain + "/images/og-default.svg";
    LastMod = DateTime.Now.ToString("yyyy-MM-dd");
    foreach (var id in new[]{"gush-dan","sharon","jerusalem","north","south"}) Blurbs[id]=GetBlurb(id);
    var ser = new JavaScriptSerializer { MaxJsonLength = int.MaxValue };
    dynamic data = ser.DeserializeObject(File.ReadAllText(Path.Combine(Base, "cities.json"), enc));
    int cityCount = 0;
    var urls = new List<Tuple<string,string>> { Tuple.Create("/", "1.0"), Tuple.Create("/areas.html", "0.9") };
    foreach (var region in (object[])data["regions"]) {
      var rd = (Dictionary<string,object>)region;
      var cities = ((object[])rd["cities"]).Cast<Dictionary<string,object>>().ToList();
      foreach (var city in cities) {
        var html = RenderCity(city, rd["name"].ToString(), rd["id"].ToString(), cities);
        File.WriteAllText(Path.Combine(Base, city["file"].ToString()), html, enc);
        urls.Add(Tuple.Create("/" + city["file"], "0.8"));
        cityCount++;
      }
    }
    // services minimal - read blocks
    foreach (var f in new[]{"pigeon-spikes.html","bird-netting.html","electric-bird-deterrent.html","solar-panels-protection.html"}) {
      var m = Regex.Match(Py, "\\{\\s*\"file\":\\s*\"" + Regex.Escape(f) + "\"[\\s\\S]*?\"slug\":\\s*\"([^\"]+)\"");
      urls.Add(Tuple.Create(m.Groups[1].Value, "0.9"));
    }
    // sitemap
    var x = new StringBuilder("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">\n");
    foreach (var u in urls) {
      x.Append("  <url>\n    <loc>").Append(Domain).Append(u.Item1).Append("</loc>\n    <lastmod>").Append(LastMod).Append("</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>").Append(u.Item2).Append("</priority>\n  </url>\n");
    }
    x.Append("</urlset>\n");
    File.WriteAllText(Path.Combine(Base, "sitemap.xml"), x.ToString(), enc);
    Console.WriteLine("Generated " + cityCount + " city pages (services/areas pending in C# port)");
  }
}