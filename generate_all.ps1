# Generate city pages - UTF-8
$ErrorActionPreference = "Stop"
$Base = $PSScriptRoot
$Domain = "https://hd-harakat-yunim.co.il"

$Regions = [ordered]@{
    "גוש דan והמרכז" = @(
        @("tel-aviv.html","תל אביב","בתל אביב אנו נותנים דגש על פתרונות לבניינים רבי קומות ומרפסות. בדיקה, ניקוי והתקנת מערכות מניעה עם אחריות 5 שנים."),
        @("ramat-gan.html","רמת גן","ברמת גן אנו מספקים פתרונות לבתים פרטיים, דירות ומשרדים. רשתות, דוקרנים וניקיון מקצועי."),
        @("givatayim.html","גבעתיים","בגבעתיים אנו מתמקדים במניעת ישיבת יונים על אדנים ומרפסות עם חומרים איכותיים."),
        @("bnei-brak.html","בני ברק","בבני ברק אנו מתקינים רשתות ודוקרנים לבניינים, מרפסות וגגות בצורה מקצועית ואסתטית."),
        @("holon.html","חולון","בחולון אנו מספקים פתרונות שקטים ואסתטיים למרפסות, גגות וחללים פתוחים."),
        @("bat-yam.html","בת ים","בבת ים אנו נותנים מענה מהיר לגגות ומרפסות עם חומרים עמידים לשמש ולמליחות."),
        @("rishon-lezion.html","ראשון לציון","בראשון לציון אנו מעניקים שירות לדירות, עסקים ובניינים. התקנה ביום אחד."),
        @("rechovot.html","רחובות","ברחובות אנו מטפלים בבתים פרטיים, מוסדות ומפעלים עם פתרונות הרחקת יונים מותאמים."),
        @("nes-ziona.html","נס ציונה","בנס ציונה אנו מתקינים רשתות, דוקרנים והגנה לפאנלים סולאריים."),
        @("yavne.html","יבנה","ביבנה אנו מספקים שירות לדירות, גגות, מרפסות ומבני תעשייה."),
        @("lod.html","לוד","בלוד אנו מספקים שירות מהיר לדירות, גגות ומבני תעשייה."),
        @("ramla.html","רמלה","ברמלה אנו מבצעים התקנות מקצועיות לבניינים, בתים פרטיים ועסקים."),
        @("modiin.html","מודיעין","במודיעין אנו מתאימים פתרונות לשכונות חדשות, וילות ומבני מגורים."),
        @("petah-tikva.html","פתח תקווה","בפתח תקווה אנו דואגים להתקנה מדויקת עם חומרים עמידים לבתים ולמפעלים."),
        @("yahud.html","יהוד","ביהוד אנו מספקים שירות מהיר לדירות, מרפסות וגגות."),
        @("or-yehuda.html","אור יהודה","באור יהודה אנו מטפלים בבניינים, מרפסות ומסתורי כביסה."),
        @("kiryat-ono.html","קריית אונו","בקריית אונו אנו מתקינים מערכות מניעה לבניינים ולבתים פרטיים."),
        @("azur.html","אזור","באזור אנו נותנים שירות מקומי מהיר לדירות, גגות ומרפסות."),
        @("kfar-shmaryahu.html","כפר שמריהו","בכפר שמריהו אנו מתקינים פתרונות איכותיים לוילות ולבתים פרטיים."),
        @("gedera.html","גדרה","בגדרה אנו מספקים שירות לבתים פרטיים, מרפסות וגגות."),
        @("elad.html","אלעד","באלעד אנו מתקינים רשתות ודוקרנים לבניינים ולמרפסות."),
        @("shoham.html","שoham","בשoham אנו מעניקים פתרונות מותאמים לוילות ולבתים פרטיים."),
        @("kiryat-ekron.html","קריית עקרון","בקריית עקרון אנו מטפלים בדירות, גגות ומבני מגורים."),
        @("beit-dagan.html","בית דagan","בבית דagan אנו מספקים שירות מהיר לבתים פרטיים ולמרפסות.")
    )
    "השרון" = @(
        @("netanya.html","נתניה","בנתניה אנו מטפלים בגגות, מרפסות ובניינים רבי קומות עם חומרים עמידים ללחות."),
        @("herzliya.html","הרצליה","בהרצליה אנו מתקינים רשתות ודוקרנים לוילות, דירות ומבני משרדים."),
        @("kfar-saba.html","כפר סבא","בכפר סבא אנו מספקים פתרונות לבתים פרטיים, וועדי בית וחברות אחזקה."),
        @("raanana.html","רעננה","ברעננה אנו מתקינים מערכות הגנה אסתטיות למרפסות ולגגות."),
        @("hod-hasharon.html","הוד השרון","בהוד השרון אנו מעניקים שירות מקצועי לדירות, בתים פרטיים ועסקים."),
        @("rosh-haayin.html","ראש העין","בראש העין אנו מטפלים בבניינים חדשים, וילות ומרפסות."),
        @("kadima.html","קדימה","בקדימה אנו מתקינים רשתות ודוקרנים לשכונות מגורים ולבתים פרטיים."),
        @("even-yehuda.html","אבן יהודה","באבן יהודה אנו מתקינים פתרונות מניעה לבתים פרטיים ולוילות."),
        @("tira.html","טירה","בטירה אנו מספקים שירות הרחקת יונים לבניינים, מרפסות וגגות."),
        @("zikhron-yaakov.html","זיכרון יעקב","בזיכרון יעקב אנו מספקים שירות לוילות, בתים פרטיים ומבני חקלאות."),
        @("pardes-hanna.html","פרדes חanna","בפרדes חanna אנו מתקינים רשתות ודוקרנים למרפסות ולגגות."),
        @("hadera.html","חדרה","בחדרה אנו מטפלים בבניינים, מרפסות וגגות עם חומרים עמידים ללחות.")
    )
    "ירושלים והסביבה" = @(
        @("jerusalem.html","ירושלים","בירושלים אנו מטפלים בבניינים, גגות, מרפסות ומוסדות עם פתרונות מותאמים."),
        @("beit-shemesh.html","בית שmesh","בבית שmesh אנו מספקים שירות לשכונות מגורים, וילות ובניינים."),
        @("maale-adumim.html","מעלה אדומים","במעלה אדומים אנו מתקינים רשתות ודוקרנים לדירות ולבתים פרטיים."),
        @("mevaseret-zion.html","מבשרet ציון","במבשרet ציון אנו מעניקים שירות מקצועי למרפסות, גגות וחלונות."),
        @("efrat.html","אפרת","באפרת אנו מספקים פתרונות הרחקת יונים לוילות ולבתים פרטיים."),
        @("givat-ze-ev.html","גivat זאב","בגivat זאב אנו מתקינים מערכות הגנה לבתים פרטיים ולבניינים."),
        @("beitar-illit.html","ביתר עilit","בביתר עilit אנו מספקים שירות לבניינים, מרפסות וגגות."),
        @("modiin-illit.html","מודיעin עilit","במודיעin עilit אנו מתקינים רשתות ודוקרנים לדירות ולבתים.")
    )
    "הצפון" = @(
        @("haifa.html","חיפה","בחיפה אנו מטפלים בבניינים רבי קומות, גגות ומרפסות עם עבודות גובה."),
        @("akko.html","עכו","בעכו אנו מתקינים רשתות ודוקרנים לבתים, עסקים ומבנים."),
        @("nahariya.html","נהריה","בנהריה אנו מספקים שירות עם חומרים עמידים ללחות ולמליחות."),
        @("kiryat-yam.html","קריית ים","בקריית ים אנו מטפלים בדירות, גגות ומרפסות."),
        @("kiryat-motskin.html","קריית מוצקין","בקריית מוצקין אנו מתקינים מערכות מניעה לבניינים ולעסקים."),
        @("kiryat-bialik.html","קריית ביאליק","בקריית ביאליק אנו מספקים פתרונות לדירות, מרפסות וגגות."),
        @("tirat-carmel.html","טירat הכרמל","בטירat הכרמל אנו מתקינים רשתות ודוקרנים למבני מגורים."),
        @("nesher.html","נשר","בנשר אנו מעניקים שירות מקומי לבתים פרטיים ובניינים."),
        @("yokneam.html","יokneam","ביokneam אנו מתקינים הגנה לפאנלים סולאריים, רשתות ודוקרנים."),
        @("karmiel.html","כרמiel","בכרמiel אנו מספקים שירות לשכונות, וילות ומבני ציבור."),
        @("tzfat.html","צפת","בצפת אנו מטפלים בבניינים, גגות ומרפסות."),
        @("tiberias.html","טבריה","בטבריה אנו מתקינים פתרונות עמידים לחום וללחות."),
        @("afula.html","עפולה","בעפולה אנו מספקים שירות לבתים פרטיים, עסקים ומפעלים."),
        @("nazareth.html","נצרת","בנצרת אנו מטפלים בבניינים, גגות ומרפסות."),
        @("maalot-tarshiha.html","מעלot תרשיחא","במעלot תרשיחא אנו מתקינים רשתות ודוקרנים לדירות ולבתים."),
        @("rosh-pina.html","ראש פina","בראש פina אנו מספקים שירות לבתים פרטיים ולוילות."),
        @("kiryat-shmona.html","קריית שmona","בקריית שmona אנו מתקינים מערכות הגנה לבניינים ולמרפסות."),
        @("migdal-haemek.html","מגדal העemek","במגדal העemek אנו מטפלים בדירות, גגות ומבני תעשייה.")
    )
    "הדרום" = @(
        @("beersheba.html","באר שבע","בבאר שבע אנו מספקים שירות לדירות, גגות, מוסדות ומפעלים."),
        @("ashkelon.html","אשקelon","באשקelon אנו מתקינים רשתות ודוקרנים עם חומרים עמידים לחוף."),
        @("ashdod.html","אשdod","באשdod אנו מטפלים בבניינים, מרפסות וגגות עם אחריות מלאה."),
        @("kiryat-gat.html","קריית גat","בקריית גat אנו מספקים פתרונות לבתים פרטיים ולבניינים."),
        @("eilat.html","אילat","באילat אנו מתקינים מערכות עמידות לחום ולמליחות."),
        @("dimona.html","דימona","בדימona אנו מעניקים שירות לבתים פרטיים, מוסדות ומפעלים."),
        @("arad.html","ערad","בערad אנו מתקינים רשתות ודוקרנים לדירות ולבתים פרטיים."),
        @("sderot.html","שderot","בשderot אנו מספקים שירות מקומי מהיר לבניינים ולמרפסות."),
        @("ofakim.html","אofakim","באofakim אנו מטפלים בדירות, גגות ומבני מגורים."),
        @("netivot.html","נתיבot","בנתיבot אנו מתקינים פתרונות מניעה לבתים ולבניינים."),
        @("kiryat-malakhi.html","קריית מalakhi","בקריית מalakhi אנו מספקים שירות לדירות, גגות ומרפסות."),
        @("omer.html","עomer","בעomer אנו מתקינים פתרונות לוילות ולבתים פרטיים.")
    )
}

function Get-CityPage($file, $city, $region, $text) {
    $title = "הרחקת יונים $city | HD הרחקת יונים"
    $desc = "שירות הרחקת יונים מקצועי ב$city. דוקרנים, רשתות, פס חשמלי והגנה לפאנלים. 18 שנות ניסיון, אחריות 5 שנים."
    $escCity = $city -replace '"','&quot;'
    @"
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>$title</title>
  <meta name="description" content="$desc">
  <link rel="canonical" href="$Domain/$file">
  <meta name="robots" content="index, follow">
  <link rel="stylesheet" href="styles.css">
</head>
<body class="has-sticky-bar">
  <header class="hero page-hero"><div class="container"><div class="site-header"><a href="index.html" class="logo">HD הרחקת יונים</a><nav class="site-nav"><ul><li><a href="index.html#services">שירותים</a></li><li><a href="areas.html">אזורים</a></li></ul></nav><a class="header-cta" href="tel:0528805053">052-880-5053</a></div><div class="page-intro"><p class="eyebrow">שירות מקומי ב$city · $region</p><h1>הרחקת יונים ב$city</h1><p class="subtitle">$text</p><div class="hero-buttons"><a class="button primary" href="tel:0528805053">התקשר עכשיו</a><a class="button secondary" href="index.html#contact-form">הצעת מחיר</a></div></div></div></header>
  <main><section class="container section"><div class="page-content-grid"><div><h2>הרחקת יונים ב$city</h2><p>$text</p><p><a href="pigeon-spikes.html">דוקרנים</a> · <a href="bird-netting.html">רשתות</a> · <a href="electric-bird-deterrent.html">פס חשמלי</a> · <a href="solar-panels-protection.html">פאנלים</a> · <a href="areas.html">כל האזורים</a></p></div><div class="media-placeholder"><span>📷 תמונה מ$city</span></div></div></section><section class="container section" id="contact-form"><h2>הצעת מחיר ב$city</h2><div class="contact-form-section"><form class="lead-form" novalidate><div><label for="name">שם *</label><input id="name" name="name" required></div><div><label for="phone">טלפון *</label><input id="phone" name="phone" type="tel" required></div><div><label for="city">עיר</label><input id="city" name="city" value="$escCity"></div><div><label for="message">פרטים</label><textarea id="message" name="message"></textarea></div><button type="submit" class="button primary form-submit">שליחה בוואטסאפ</button></form></div></section></main>
  <footer class="footer"><div class="container"><p><a href="index.html">דף הבית</a> · <a href="areas.html">אזורים</a></p></div></footer>
  <div class="sticky-bar"><a href="tel:0528805053" class="sbtn sbtn-call"><span>📞</span><span>טלפון</span></a><a href="#contact-form" class="sbtn sbtn-quote"><span>✏️</span><span>הצעת מחיר</span></a><a href="https://wa.me/972528805053" class="sbtn sbtn-wa"><span>💬</span><span>וואטסאפ</span></a></div>
  <script src="contact-form.js" defer></script>
</body>
</html>
"@
}

$count = 0
$urls = @("/", "/areas.html", "/pigeon-spikes.html", "/bird-netting.html", "/electric-bird-deterrent.html", "/solar-panels-protection.html")
$areasParts = @()
$areasParts += @'
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>אזורים וערים | HD הרחקת יונים – שירות בכל הארץ</title>
  <meta name="description" content="HD הרחקת יונים – שירות בכל האזורים: גוש דan, השרון, ירושלים, הצפון והדרום.">
  <link rel="canonical" href="https://hd-harakat-yunim.co.il/areas.html">
  <link rel="stylesheet" href="styles.css">
</head>
<body class="has-sticky-bar">
  <header class="hero page-hero"><div class="container"><div class="site-header"><a href="index.html" class="logo">HD הרחקת יונים</a><nav class="site-nav"><ul><li><a href="index.html">בית</a></li><li><a href="index.html#contact-form">צור קשר</a></li></ul></nav><a class="header-cta" href="tel:0528805053">052-880-5053</a></div><div class="page-intro"><h1>אזורים וערים</h1><p class="subtitle">שירות הרחקת יונים בכל רחבי הארץ – בחרו את העיר שלכם</p></div></div></header>
  <main>
'@

foreach ($region in $Regions.Keys) {
    $areasParts += "<section class=`"container section region-block`"><h2 class=`"section-title-bar`">$region</h2><nav class=`"city-links`" aria-label=`"$region`">"
    foreach ($entry in $Regions[$region]) {
        $file, $city, $text = $entry
        $html = Get-CityPage $file $city $region $text
        [System.IO.File]::WriteAllText((Join-Path $Base $file), $html, [System.Text.UTF8Encoding]::new($false))
        $urls += "/$file"
        $areasParts += "<a href=`"$file`">הרחקת יונים $city</a>"
        $count++
    }
    $areasParts += "</nav></section>"
}

$areasParts += @'
  </main>
  <footer class="footer"><div class="container"><p><a href="index.html">חזרה לדף הבית</a></p></div></footer>
  <div class="sticky-bar"><a href="tel:0528805053" class="sbtn sbtn-call"><span>📞</span><span>טלפון</span></a><a href="index.html#contact-form" class="sbtn sbtn-quote"><span>✏️</span><span>הצעת מחיר</span></a><a href="https://wa.me/972528805053" class="sbtn sbtn-wa"><span>💬</span><span>וואטסאפ</span></a></div>
</body></html>
'@
[System.IO.File]::WriteAllText((Join-Path $Base "areas.html"), ($areasParts -join "`n"), [System.Text.UTF8Encoding]::new($false))

$sitemap = @('<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
foreach ($path in $urls) {
    $pri = if ($path -eq "/") { "1.0" } else { "0.8" }
    $sitemap += "  <url><loc>$Domain$path</loc><changefreq>weekly</changefreq><priority>$pri</priority></url>"
}
$sitemap += "</urlset>"
[System.IO.File]::WriteAllText((Join-Path $Base "sitemap.xml"), ($sitemap -join "`n"), [System.Text.UTF8Encoding]::new($false))

Write-Host "Generated $count city pages"
