# -*- coding: utf-8 -*-
"""Generate SEO-optimized city, service, and areas pages from cities.json."""
from __future__ import annotations

import json
from datetime import date
from html import escape
from pathlib import Path

DOMAIN = "https://hd-harakat-yunim.co.il"
BRAND = "HD הרחקת יונים"
PHONE_DISPLAY = "052-880-5053"
PHONE_TEL = "0528805053"
EMAIL = "h_devid@walla.com"
OG_IMAGE = f"{DOMAIN}/images/og-default.svg"
LASTMOD = date.today().isoformat()
BASE = Path(__file__).parent

REGION_BLURBS = {
    "gush-dan": (
        "בגוש דאן והמרכז מצויים ריכוזי בנייה גבוהים, מרפסות רבות וגגות שטוחים — "
        "אזורים שבהם יונים נוהגות לקנן ולהתמקם. אנו מספקים פתרונות מותאמים לבניינים, "
        "דירות, משרדים ועסקים."
    ),
    "sharon": (
        "באזור השרון, עם קרבה לים וללחות, חשוב להשתמש בחומרים עמידים ללחות, UV ולמליחות. "
        "אנו מתקינים מערכות שמחזיקות מעמד לאורך שנים בתנאי חוף ושרון."
    ),
    "jerusalem": (
        "בירושלים והסביבה אנו מתמודדים עם מבנים מגוונים — מבניינים עירוניים ועד וילות "
        "בשכונות חדשות. הפתרונות שלנו מותאמים לגובה, לגגות ולמרפסות בכל סוגי הנדל\"ן."
    ),
    "north": (
        "בצפון הארץ, בין לחות חיפאית לחום עמקי, נדרשת התאמה מדויקת של חומרים ושיטות התקנה. "
        "אנו מבצעים גם עבודות גובה, סנפלינג ומנופים במקרים הנדרשים."
    ),
    "south": (
        "בדרום הארץ, עם חום עז וקרבה לים בחופים, אנו משתמשים בחומרים עמידים במיוחד לשמש "
        "ולמליחות — לשמירה על ביצועי המערכת לאורך זמן."
    ),
}


def esc(text: str) -> str:
    return escape(text, quote=True)


def head_block(
    title: str,
    description: str,
    canonical_path: str,
    og_type: str = "website",
) -> str:
    url = f"{DOMAIN}{canonical_path}"
    return f"""  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <meta name="robots" content="index, follow">
  <meta name="theme-color" content="#1d4f8f">
  <link rel="canonical" href="{url}">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="images/og-default.svg">
  <meta property="og:type" content="{og_type}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{OG_IMAGE}">
  <meta property="og:locale" content="he_IL">
  <meta property="og:site_name" content="{esc(BRAND)}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="styles.css">"""


def site_header(nav_extra: str = "") -> str:
    nav = nav_extra or """<ul>
            <li><a href="index.html#services">שירותים</a></li>
            <li><a href="areas.html">אזורים</a></li>
            <li><a href="index.html#contact-form">הצעת מחיר</a></li>
          </ul>"""
    return f"""      <div class="site-header">
        <a href="index.html" class="logo">{BRAND}</a>
        <nav class="site-nav" aria-label="תפריט ראשי">
          {nav}
        </nav>
        <a class="header-cta" href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a>
      </div>"""


def breadcrumbs(items: list[tuple[str, str]]) -> str:
    parts = ['<nav class="breadcrumbs" aria-label="מיקום בעמוד">']
    for i, (label, href) in enumerate(items):
        if i == len(items) - 1:
            parts.append(f'<span aria-current="page">{esc(label)}</span>')
        else:
            parts.append(f'<a href="{href}">{esc(label)}</a>')
            parts.append('<span class="bc-sep" aria-hidden="true">›</span>')
    parts.append("</nav>")
    return "\n      ".join(parts)


def breadcrumb_schema(items: list[tuple[str, str]]) -> str:
    elements = []
    for i, (name, path) in enumerate(items, start=1):
        elements.append(
            {
                "@type": "ListItem",
                "position": i,
                "name": name,
                "item": f"{DOMAIN}{path}" if path.startswith("/") else path,
            }
        )
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": elements,
    }
    return json.dumps(data, ensure_ascii=False)


def local_business_schema(city: str, description: str) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": BRAND,
        "description": description,
        "telephone": "+972528805053",
        "email": EMAIL,
        "url": DOMAIN + "/",
        "image": OG_IMAGE,
        "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressCountry": "IL"},
        "areaServed": {"@type": "City", "name": city},
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "08:00",
            "closes": "20:00",
        },
    }
    return json.dumps(data, ensure_ascii=False)


def service_schema(name: str, description: str, url_path: str) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "description": description,
        "provider": {
            "@type": "LocalBusiness",
            "name": BRAND,
            "telephone": "+972528805053",
            "url": DOMAIN + "/",
        },
        "areaServed": {"@type": "Country", "name": "Israel"},
        "url": DOMAIN + url_path,
    }
    return json.dumps(data, ensure_ascii=False)


def faq_schema(questions: list[tuple[str, str]]) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in questions
        ],
    }
    return json.dumps(data, ensure_ascii=False)


def faq_html(questions: list[tuple[str, str]]) -> str:
    items = []
    for q, a in questions:
        items.append(f'        <div class="faq-item"><dt>{esc(q)}</dt><dd>{esc(a)}</dd></div>')
    return (
        '      <h2 class="section-title-bar">שאלות נפוצות</h2>\n'
        '      <dl class="faq-list">\n'
        + "\n".join(items)
        + "\n      </dl>"
    )


def sticky_bar() -> str:
    return f"""  <div class="sticky-bar" role="region" aria-label="יצירת קשר מהירה">
    <a href="tel:{PHONE_TEL}" class="sbtn sbtn-call"><span aria-hidden="true">📞</span><span>טלפון</span></a>
    <a href="#contact-form" class="sbtn sbtn-quote"><span aria-hidden="true">✏️</span><span>הצעת מחיר</span></a>
    <a href="#" class="sbtn sbtn-wa wa-direct" target="_blank" rel="noopener noreferrer"><span aria-hidden="true">💬</span><span>וואטסאפ</span></a>
  </div>"""


def footer_block() -> str:
    return f"""  <footer class="footer">
    <div class="container">
      <div class="footer-bottom">
        <p>{BRAND} | <a href="index.html">עמוד ראשי</a> · <a href="areas.html">כל האזורים</a> · <a href="tel:{PHONE_TEL}">{PHONE_DISPLAY}</a></p>
      </div>
    </div>
  </footer>"""


def contact_form(city: str = "", service: str = "") -> str:
    city_val = esc(city)
    service_field = (
        f'<input type="hidden" name="service" value="{esc(service)}">'
        if service
        else """<div>
            <label for="service">סוג שירות</label>
            <select id="service" name="service">
              <option value="">בחרו שירות</option>
              <option value="דוקרני יונים">דוקרני יונים</option>
              <option value="רשתות יונים">רשתות יונים</option>
              <option value="פס חשמלי">פס חשמלי</option>
              <option value="הגנה לפאנלים סולאריים">הגנה לפאנלים סולאריים</option>
            </select>
          </div>"""
    )
    return f"""      <div class="contact-form-section">
        <form class="lead-form" id="lead" novalidate>
          <div>
            <label for="name">שם מלא *</label>
            <input id="name" name="name" type="text" autocomplete="name" required placeholder="הזינו שם מלא">
          </div>
          <div>
            <label for="phone">טלפון *</label>
            <input id="phone" name="phone" type="tel" autocomplete="tel" required placeholder="050-0000000">
          </div>
          <div>
            <label for="city">עיר / ישוב</label>
            <input id="city" name="city" type="text" value="{city_val}" placeholder="לדוגמה: תל אביב">
          </div>
          {service_field}
          <div>
            <label for="message">פרטים נוספים</label>
            <textarea id="message" name="message" placeholder="ספרו על הבעיה — מרפסת, גג, בניין וכו'"></textarea>
          </div>
          <button type="submit" class="button whatsapp form-submit">שליחה בוואטסאפ</button>
          <p class="form-note">בלחיצה תיפתח הודעת וואטסאפ עם פרטי הטופס. לא מחייב.</p>
        </form>
      </div>"""


def nearby_cities_html(cities: list[dict], current_file: str, limit: int = 5) -> str:
    links = []
    for c in cities:
        if c["file"] == current_file:
            continue
        links.append(f'<a href="{c["file"]}">{esc(c["name"])}</a>')
        if len(links) >= limit:
            break
    if not links:
        return ""
    return (
        '      <h3>ערים נוספות באזור</h3>\n'
        '      <nav class="city-links" aria-label="ערים נוספות באזור">\n        '
        + "\n        ".join(links)
        + "\n      </nav>"
    )


def city_meta_description(city: str, text: str) -> str:
    base = text.strip()
    if len(base) < 120:
        extra = f" דוקרנים ורשתות ב{city}. אחריות 5 שנים."
        base = base + extra if len(base) + len(extra) <= 160 else base + " אחריות 5 שנים."
    if len(base) > 160:
        trimmed = base[:157]
        if " " in trimmed:
            trimmed = trimmed.rsplit(" ", 1)[0]
        base = trimmed + "…"
    return base


def render_city_page(city: dict, region_name: str, region_id: str, region_cities: list[dict]) -> str:
    name = city["name"]
    file = city["file"]
    text = city["text"]
    path = f"/{file}"
    title = f"הרחקת יונים ב{name} | דוקרנים ורשתות | {BRAND}"
    description = city_meta_description(name, text)
    region_blurb = REGION_BLURBS.get(region_id, "")
    nearby = nearby_cities_html(region_cities, file)
    faq = [
        (f"כמה עולה הרחקת יונים ב{name}?", "המחיר תלוי בסוג הפתרון, בגודל השטח ובמורכבות ההתקנה. אנו מגיעים לבדיקה ונותנים הצעת מחיר ללא התחייבות."),
        (f"כמה זמן לוקח שירות ב{name}?", "רוב ההתקנות מתבצעות ביום אחד, בהתאם להיקף העבודה."),
        ("האם הפתרונות הומאניים?", "בהחלט. אנו משתמשים בשיטות הרחקה שלא פוגעות ביונים — דוקרנים, רשתות ופס חשמלי בטוח."),
    ]
    bc_html = [("דף הבית", "index.html"), ("אזורים", "areas.html"), (name, file)]
    bc_schema = [("דף הבית", "/"), ("אזורים", "/areas.html"), (name, path)]

    return f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
{head_block(title, description, path)}
</head>
<body class="has-sticky-bar">
  <a href="#main-content" class="skip-link">דלג לתוכן הראשי</a>
  <header class="hero page-hero">
    <div class="container">
{site_header()}
      <div class="page-intro">
      {breadcrumbs(bc_html)}
        <p class="eyebrow">{esc(region_name)} · {esc(name)}</p>
        <h1>הרחקת יונים ב{esc(name)}</h1>
        <p class="subtitle">{esc(text)}</p>
        <div class="hero-buttons">
          <a class="button primary" href="tel:{PHONE_TEL}">התקשר עכשיו {PHONE_DISPLAY}</a>
          <a class="button whatsapp wa-direct" href="#">וואטסאפ</a>
        </div>
      </div>
    </div>
  </header>
  <main id="main-content">
    <section class="container section">
      <div class="page-content-grid">
        <div>
          <h2>שירות הרחקת יונים מקצועי ב{esc(name)}</h2>
          <p>{esc(text)}</p>
          <p>{esc(region_blurb)}</p>
          <p>HD הרחקת יונים מספקת ב{esc(name)} פתרונות מלאים: <a href="pigeon-spikes.html">דוקרני יונים</a>, <a href="bird-netting.html">רשתות יונים</a>, <a href="electric-bird-deterrent.html">פס חשמלי</a> ו<a href="solar-panels-protection.html">הגנה לפאנלים סולאריים</a>. כל החומרים מיוצרים בישראל, עמידים ל-UV ומגיעים עם <strong>אחריות 5 שנים</strong>.</p>
          <h3>מה אנו מציעים ב{esc(name)}?</h3>
          <ul>
            <li>בדיקה מקצועית והצעת מחיר ללא עלות</li>
            <li>התקנה נקייה ואסתטית — מרפסות, גגות, חלונות ומסתורי כביסה</li>
            <li>עבודות גובה: סנפלינג, מנופים ובמות הרמה</li>
            <li>שירות לוועדי בית, בתים פרטיים ועסקים</li>
            <li>זמינות גבוהה — 24/7 (חוץ משבת)</li>
          </ul>
          <h3>תהליך העבודה</h3>
          <ol>
            <li><strong>פנייה</strong> — טלפון, וואטסאפ או טופס באתר</li>
            <li><strong>בדיקה</strong> — הערכת המצב והמלצה על הפתרון המתאים</li>
            <li><strong>הצעת מחיר</strong> — שקופה וללא התחייבות</li>
            <li><strong>התקנה</strong> — בדרך כלל ביום אחד, עם גימור מקצועי</li>
          </ol>
{nearby}
          <p><a href="areas.html">← לרשימת כל הערים והאזורים</a></p>
        </div>
        <div class="media-placeholder" role="img" aria-label="תמונת עבודה בהרחקת יונים ב{name}">
          <span>📷 תמונת עבודה ב{esc(name)}<br><small>יתווסף בקרוב</small></span>
        </div>
      </div>
    </section>
    <section class="container section faq" id="faq">
{faq_html(faq)}
    </section>
    <section class="container section" id="contact-form">
      <h2 class="section-title-bar">הצעת מחיר ב{esc(name)}</h2>
      <p class="section-subtitle">מלאו פרטים ונחזור אליכם בהקדם</p>
{contact_form(city=name)}
    </section>
  </main>
{footer_block()}
{sticky_bar()}
  <script type="application/ld+json">
{breadcrumb_schema(bc_schema)}
  </script>
  <script type="application/ld+json">
{local_business_schema(name, description)}
  </script>
  <script type="application/ld+json">
{faq_schema(faq)}
  </script>
  <script src="contact-form.js" defer></script>
</body>
</html>
"""


SERVICE_PAGES = [
    {
        "file": "pigeon-spikes.html",
        "slug": "/pigeon-spikes.html",
        "h1": "דוקרני יונים",
        "title": "דוקרני יונים מקצועיים | נירוסטה עמיד UV | HD הרחקת יונים",
        "description": "התקנת דוקרני נירוסטה נגד יונים – ייצור ישראלי, עמידות UV, אחריות 5 שנים. אדנים, מרפסות ומסתורי כביסה. שירות בכל הארץ.",
        "subtitle": "דוקרני נירוסטה איכותיים שמונעים מהיונים לנחות ולהתמקם. מיוצרים בישראל, עמידים לקרינת UV ומותאמים לאקלים הים-תיכוני.",
        "service_name": "דוקרני יונים",
        "content": [
            "דוקרני נירוסטה איכותיים שמונעים מהיונים לנחות ולהתמקם. מיוצרים בישראל, עמידים לקרינת UV ומותאמים לאקלים הים-תיכוני – אינם מחלידים. פתרון יעיל ומוכח שמתאים לאדני חלון, מסתורי כביסה ומרפסות.",
            "HD הרחקת יונים מתקינה דוקרנים בצורה דיסקרטית ואסתטית, עם אחריות מלאה ל-5 שנים. מתאים לבתים פרטיים, וועדי בית, עסקים ומוסדות.",
            "הדוקרנים שלנו מיוצרים בישראל (כחול-לבן) תחת בקרת איכות קפדנית. הם עמידים לשמש, גשם ולחות — ומחזיקים שנים ללא חלודה או שינוי צבע.",
        ],
        "h2": "דוקרני יונים מקצועיים",
        "process": ["סיור וזיהוי נקודות נחיתה", "ניקוי והכנת המשטח", "התקנה מדויקת בנירוסטה", "בדיקה ומסירה עם אחריות"],
        "faq": [
            ("האם הדוקרנים פוגעים ביונים?", "לא. הם מונעים נחיתה בצורה הומאנית ללא פגיעה בבעלי החיים."),
            ("כמה זמן הדוקרנים מחזיקים?", "חומרי נירוסטה עמידי UV – שנים רבות ללא חלודה בתנאי חוץ ישראליים."),
            ("דוקרנים או רשתות — מה עדיף?", "תלוי במיקום: דוקרנים לאדנים ומסגרות; רשתות למרפסות ופתחים גדולים. נייעץ בבדיקה."),
            ("האם ההתקנה בולטת?", "לא. אנו מתקינים בצורה דיסקרטית ששומרת על מראה המבנה."),
        ],
        "image_alt": "התקנת דוקרני יונים מנירוסטה על אדן חלון",
        "links": [("bird-netting.html", "רשתות יונים"), ("electric-bird-deterrent.html", "פס חשמלי"), ("solar-panels-protection.html", "הגנה לפאנלים סולאריים")],
    },
    {
        "file": "bird-netting.html",
        "slug": "/bird-netting.html",
        "h1": "רשתות יונים",
        "title": "רשתות יונים מקצועיות | UV עמיד | HD הרחקת יונים",
        "description": "התקנת רשתות יונים UV מקצועיות – מרפסות, חלונות ומסתורי כביסה. ייצור ישראלי, אסתטי והומאני. אחריות 5 שנים.",
        "subtitle": "רשתות מקצועיות עמידות לקרינת UV, מותאמות לאקלים הים-תיכוני. אסתטיות, הומאניות ומראה נקי.",
        "service_name": "רשתות יונים",
        "content": [
            "רשתות מקצועיות עמידות לקרינת UV, מותאמות לאקלים הים-תיכוני. אסתטיות והומאניות, שומרות על אוורור ומראה נקי וכמעט שאינן נראות בנוף. פתרון יעיל ומוכח למרפסות, מסתורי כביסה וחלונות.",
            "HD הרחקת יונים מתקינה רשתות לכל סוגי המבנים — בתים פרטיים, בניינים, עסקים ומפעלים. עבודות גובה, סנפלינג ומנופים לפי הצורך.",
            "הרשתות שקופות למחצה, מאפשרות אוורור מלא ולא חוסמות אור. הן מונעות כניסת יונים לחלל המרפסת או החלון ללא פגיעה בבעלי החיים.",
        ],
        "h2": "רשתות יונים מקצועיות",
        "process": ["מדידה והתאמה אישית", "התקנת פרופיל אלומיניום", "מתיחת רשת UV איכותית", "גימור נקי ואסתטי"],
        "faq": [
            ("האם הרשת חוסמת אוורור?", "לא. הרשת שקופה ומאפשרת אוורור מלא."),
            ("כמה זמן הרשת מחזיקה?", "רשתות UV עמידות – שנים רבות בתנאי חוץ ישראליים."),
            ("האם הרשת נראית מהרחוב?", "כמעט לא — רשתות איכותיות כמעט בלתי נראות ממרחק."),
            ("האם מתאים למסתור כביסה?", "בוודאי — אחד הפתרונות הנפוצים והיעילים ביותר."),
        ],
        "image_alt": "התקנת רשת יונים על מרפסת בדירה",
        "links": [("pigeon-spikes.html", "דוקרני יונים"), ("electric-bird-deterrent.html", "פס חשמלי"), ("solar-panels-protection.html", "הגנה לפאנלים סולאריים")],
    },
    {
        "file": "electric-bird-deterrent.html",
        "slug": "/electric-bird-deterrent.html",
        "h1": "פס חשמלי",
        "title": "פס חשמלי נגד יונים | הומאני ואסתטי | HD הרחקת יונים",
        "description": "התקנת פס חשמלי הומאני נגד יונים – גגות, מרפסות וחלונות. בטיחותי, דיסקרטי, אחריות 5 שנים. שירות בכל הארץ.",
        "subtitle": "מערכת הרחקה הומאנית המבוססת על פולסים נמוכים, עם דגש על בטיחות וגימור אסתטי.",
        "service_name": "פס חשמלי",
        "content": [
            "מערכת הרחקה הומאנית המבוססת על פולסים נמוכים, עם דגש על בטיחות וגימור אסתטי. פתרון דקורטיבי ודיסקרטי שאינו בולט ואינו פוגע במראה המבנה — מתאים במיוחד לגגות, חלונות ומרפסות.",
            "HD הרחקת יונים מתקין פס חשמלי מקצועי לבתים פרטיים, עסקים וחברות אחזקה. חומרים עמידים לשמש ולחלודה, עם אחריות מלאה.",
            "הפס החשמלי מרחיק יונים באמצעות פולס קל שלא מזיק לבני אדם או לציפורים. הוא אידיאלי כשמראה המבנה חשוב ודוקרנים או רשתות פחות מתאימים.",
        ],
        "h2": "פס חשמלי נגד יונים",
        "process": ["תכנון מסלול ההתקנה", "התקנת פס ומקור מתח", "בדיקת בטיחות", "הדרכה קצרה לתפעול"],
        "faq": [
            ("האם הפס החשמלי בטוח?", "כן. פולסים נמוכים שלא מזיקים לבני אדם או ליונים."),
            ("האם מתאים לבתים פרטיים?", "בוודאי — פתרון דיסקרטי למרפסות וגגות."),
            ("האם הפס בולט ויזואלית?", "לא. התקנה דיסקרטית שמשתלבת במבנה."),
            ("מה ההבדל מדוקרנים?", "פס חשמלי מתאים כשצריך פתרון כמעט בלתי נראה; דוקרנים לאדנים ומסגרות."),
        ],
        "image_alt": "התקנת פס חשמלי נגד יונים על גג",
        "links": [("pigeon-spikes.html", "דוקרני יונים"), ("bird-netting.html", "רשתות יונים"), ("solar-panels-protection.html", "הגנה לפאנלים סולאריים")],
    },
    {
        "file": "solar-panels-protection.html",
        "slug": "/solar-panels-protection.html",
        "h1": "הגנה לפאנלים סולאריים",
        "title": "הגנה לפאנלים סולאריים מפני יונים | HD הרחקת יונים",
        "description": "הגנה מקצועית לפאנלים סולאריים מפני יונים ולכלוך. רשת היקפית ייעודית, לא פוגעת בייצור. אחריות 5 שנים.",
        "subtitle": "מניעת קינון ולשלשת מתחת לפאנלים באמצעות רשת היקפית ייעודית שאינה פוגעת בביצועי המערכת.",
        "service_name": "הגנה לפאנלים סולאריים",
        "content": [
            "מניעת קינון ולשלשת מתחת לפאנלים באמצעות רשת היקפית ייעודית שאינה פוגעת בביצועי המערכת. התקנה נקייה ואחידה, אסתטית וכמעט בלתי-נראית, לשמירה על הגג ועל הפאנלים לאורך זמן.",
            "יונים מתחת לפאנלים עלולים לגרום לירידה בייצור אנרגיה, נזק לציוד ולכלוך מתמשך. HD הרחקת יונים מספקת פתרון מותאם לגגות ביתיים, עסקיים וחוות סולאריות.",
            "הרשת ההיקפית מונעת כניסת יונים לחלל שמתחת לפאנלים מבלי לחסום אור או אוורור — כך שהמערכת הסולארית ממשיכה לעבוד ביעילות מלאה.",
        ],
        "h2": "הגנה לפאנלים סולאריים מפני יונים",
        "process": ["בדיקת מערכת הפאנלים", "התקנת רשת היקפית מותאמת", "סגירת נקודות כניסה", "בדיקת תקינות ואחריות"],
        "faq": [
            ("האם הרשת פוגעת בייצור?", "לא. רשת היקפית שלא חוסמת אור או אוורור."),
            ("האם מתאים לגגות תעשייתיים?", "כן — גגות ביתיים, מסחריים וחוות סולאריות."),
            ("למה יונים נמשכות לפאנלים?", "הצל והחום שמתחת לפאנלים יוצרים מקלט אידיאלי לקינון."),
            ("האם הרשת נראית מהרחוק?", "כמעט לא — התקנה דיסקרטית שמשתלבת במערכת."),
        ],
        "image_alt": "הגנה לפאנלים סולאריים מפני יונים באמצעות רשת היקפית",
        "links": [("pigeon-spikes.html", "דוקרני יונים"), ("bird-netting.html", "רשתות יונים"), ("electric-bird-deterrent.html", "פס חשמלי")],
    },
]


def render_service_page(svc: dict) -> str:
    path = svc["slug"]
    bc_html = [("דף הבית", "index.html"), ("שירותים", "index.html#services"), (svc["h1"], svc["file"])]
    bc_schema = [("דף הבית", "/"), ("שירותים", "/#services"), (svc["h1"], path)]
    links_html = " · ".join(f'<a href="{f}">{esc(label)}</a>' for f, label in svc["links"])
    process_html = "\n".join(f"            <li>{esc(step)}</li>" for step in svc["process"])
    content_html = "\n          ".join(f"<p>{esc(p)}</p>" for p in svc["content"])

    return f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
{head_block(svc["title"], svc["description"], path)}
</head>
<body class="has-sticky-bar">
  <a href="#main-content" class="skip-link">דלג לתוכן הראשי</a>
  <header class="hero page-hero">
    <div class="container">
{site_header()}
      <div class="page-intro">
      {breadcrumbs(bc_html)}
        <p class="eyebrow">שירות מקצועי בכל הארץ</p>
        <h1>{esc(svc["h1"])}</h1>
        <p class="subtitle">{esc(svc["subtitle"])}</p>
        <div class="hero-buttons">
          <a class="button primary" href="tel:{PHONE_TEL}">התקשר עכשיו</a>
          <a class="button secondary" href="index.html#contact-form">הצעת מחיר</a>
        </div>
      </div>
    </div>
  </header>
  <main id="main-content">
    <section class="container section">
      <div class="page-content-grid">
        <div>
          <h2>{esc(svc["h2"])}</h2>
          {content_html}
          <h3>תהליך ההתקנה</h3>
          <ol>
{process_html}
          </ol>
          <p>שירותים נוספים: {links_html}</p>
          <p><a href="areas.html">שירות בכל הערים והאזורים ←</a></p>
        </div>
        <div class="media-placeholder" role="img" aria-label="{esc(svc["image_alt"])}">
          <span>📷 {esc(svc["image_alt"])}<br><small>יתווסף בקרוב</small></span>
        </div>
      </div>
    </section>
    <section class="container section faq" id="faq">
{faq_html(svc["faq"])}
    </section>
    <section class="container section" id="contact-form">
      <h2 class="section-title-bar">הצעת מחיר ל{esc(svc["h1"])}</h2>
{contact_form(service=svc["service_name"])}
    </section>
  </main>
{footer_block()}
{sticky_bar()}
  <script type="application/ld+json">
{breadcrumb_schema(bc_schema)}
  </script>
  <script type="application/ld+json">
{service_schema(svc["service_name"], svc["description"], path)}
  </script>
  <script type="application/ld+json">
{faq_schema(svc["faq"])}
  </script>
  <script src="contact-form.js" defer></script>
</body>
</html>
"""


def render_areas_page(regions: list) -> str:
    title = f"כל הערים והאזורים | {BRAND}"
    description = (
        "HD הרחקת יונים — שירות ב-74 ערים בכל הארץ: גוש דאן, השרון, ירושלים, הצפון והדרום. "
        "דוקרנים, רשתות, פס חשמלי והגנה לפאנלים. אחריות 5 שנים."
    )
    path = "/areas.html"
    bc_html = [("דף הבית", "index.html"), ("כל הערים והאזורים", "areas.html")]
    bc_schema = [("דף הבית", "/"), ("כל הערים והאזורים", path)]
    sections = []
    for region in regions:
        links = "\n".join(
            f'            <a href="{c["file"]}">{esc(c["name"])}</a>'
            for c in region["cities"]
        )
        sections.append(
            f"""    <section class="container section region-block">
      <h2 class="section-title-bar">{esc(region["name"])}</h2>
      <nav class="city-links" aria-label="{esc(region["name"])}">
{links}
      </nav>
    </section>"""
        )

    return f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
{head_block(title, description, path)}
</head>
<body class="has-sticky-bar">
  <a href="#main-content" class="skip-link">דלג לתוכן הראשי</a>
  <header class="hero page-hero">
    <div class="container">
{site_header()}
      <div class="page-intro">
      {breadcrumbs(bc_html)}
        <h1>כל הערים והאזורים</h1>
        <p class="subtitle">HD הרחקת יונים — 74 ערים בכל הארץ. בחרו את העיר שלכם לפרטים והצעת מחיר.</p>
      </div>
    </div>
  </header>
  <main id="main-content">
{chr(10).join(sections)}
    <section class="container section">
      <p class="section-subtitle"><a class="button secondary" href="index.html#contact-form">הצעת מחיר לכל הארץ</a></p>
    </section>
  </main>
{footer_block()}
{sticky_bar()}
  <script type="application/ld+json">
{breadcrumb_schema(bc_schema)}
  </script>
  <script src="contact-form.js" defer></script>
</body>
</html>
"""


def write_sitemap(urls: list[tuple[str, str]]) -> None:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path, priority in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{DOMAIN}{path}</loc>")
        lines.append(f"    <lastmod>{LASTMOD}</lastmod>")
        lines.append("    <changefreq>weekly</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    (BASE / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    data = json.loads((BASE / "cities.json").read_text(encoding="utf-8"))
    regions = data["regions"]
    city_count = 0
    urls: list[tuple[str, str]] = [
        ("/", "1.0"),
        ("/areas.html", "0.9"),
    ]

    for svc in SERVICE_PAGES:
        html = render_service_page(svc)
        (BASE / svc["file"]).write_text(html, encoding="utf-8")
        urls.append((svc["slug"], "0.9"))

    for region in regions:
        cities = region["cities"]
        region_id = region["id"]
        region_name = region["name"]
        for city in cities:
            html = render_city_page(city, region_name, region_id, cities)
            (BASE / city["file"]).write_text(html, encoding="utf-8")
            urls.append((f"/{city['file']}", "0.8"))
            city_count += 1

    (BASE / "areas.html").write_text(render_areas_page(regions), encoding="utf-8")
    write_sitemap(urls)
    print(f"Generated {city_count} city pages, {len(SERVICE_PAGES)} service pages, areas.html, sitemap.xml")


if __name__ == "__main__":
    main()
