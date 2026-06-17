from pathlib import Path
base = Path('.')
renames = {
    'images/pigeon.svg': 'images/pigeon-removal.svg',
    'images/net.svg': 'images/bird-netting.svg',
    'images/inspection.svg': 'images/inspection-solar.svg'
}
for old, new in renames.items():
    oldp = base / old
    newp = base / new
    if oldp.exists() and not newp.exists():
        oldp.rename(newp)

domain = 'https://hd-harakat-yunim.co.il'

index = '''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>HD הרחקת יונים | שירותי הרחקת יונים מקצועיים בכל הארץ</title>
  <meta name="description" content="HD הרחקת יונים מספקת שירותי הרחקת יונים מקצועיים, רשת נגד יונים, דוקרנים, פס חשמלי והגנה לפאנלים סולאריים. 18 שנות ניסיון, שירות הומאני ואחריות מלאה.">
  <link rel="canonical" href="/">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="website">
  <meta property="og:title" content="HD הרחקת יונים | שירותי הרחקת יונים מקצועיים בכל הארץ">
  <meta property="og:description" content="שירות HD הרחקת יונים בכל הארץ עם רשתות נגד יונים, דוקרנים, פס חשמל והגנה לפאנלים סולאריים. טלפון, וואטסאפ ואחריות מלאה.">
  <meta property="og:url" content="''' + domain + '''/">
  <meta property="og:image" content="''' + domain + '''/images/pigeon-removal.svg">
  <meta property="og:site_name" content="HD הרחקת יונים">
  <meta property="og:locale" content="he_IL">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="hero">
    <div class="container">
      <div class="site-header">
        <div class="logo">HD הרחקת יונים</div>
        <nav class="site-nav" aria-label="תפריט ראשי">
          <ul>
            <li><a href="/">בית</a></li>
            <li><a href="#services">שירותים</a></li>
            <li><a href="#cities">אזורים</a></li>
            <li><a href="#contact">צור קשר</a></li>
          </ul>
        </nav>
      </div>
      <div class="page-intro">
        <p class="eyebrow">שירותי הרחקת יונים בכל הארץ</p>
        <h1>HD הרחקת יונים - פתרונות מקצועיים להרחבת יונים</h1>
        <p class="subtitle">18 שנות ניסיון בשירותים הומאניים, רשתות נגד יונים, דוקרנים, פס חשמלי והגנה לפאנלים סולאריים. שירות מהיר לכל הארץ עם אחריות מלאה.</p>
        <div class="hero-buttons">
          <a class="button primary" href="tel:+972537770944">התקשר עכשיו</a>
          <a class="button secondary" href="https://wa.me/972537770944?text=%D7%A9%D7%9C%D7%95%D7%9D%20HD%20%D7%94%D7%A8%D7%97%D7%A7%D7%AA%20%D7%99%D7%95%D7%A0%D7%99%D7%9D">וואטסאפ</a>
        </div>
        <p class="hero-note">פעיל כל השבוע חוץ משבת | רישיון עבודה בגובה, סנפלינג ומנוף | חומרים עמידים לשמש ולחלודה</p>
      </div>
    </div>
  </header>

  <main>
    <section class="container section services" id="services">
      <h2>שירותים מקצועיים בתחום הרחקת היונים</h2>
      <div class="cards">
        <article class="card">
          <h3>הרחקת יונים מקצועית</h3>
          <p>HD הרחקת יונים מבצעת הרחקת יונים לכל סוגי המבנים, עם טיפול נקי ללא פגיעה ושימוש בשיטות הומאניות.</p>
          <a class="card-link" href="pigeon-removal.html">לפרטים על הרחקת יונים</a>
        </article>
        <article class="card">
          <h3>רשת נגד יונים</h3>
          <p>התקנת רשתות נגד יונים עמידות UV שמונעות כניסה מרקיעות ומהמרפסות בצורה בטוחה ויעילה.</p>
          <a class="card-link" href="bird-netting.html">לפרטים על רשתות נגד יונים</a>
        </article>
        <article class="card">
          <h3>דוקרנים נגד יונים</h3>
          <p>התקנת דוקרני נירוסטה מקצועיים על קירות, אדנים ופלטפורמות כדי להרחיק יונים ללא נזק.</p>
          <a class="card-link" href="pigeon-spikes.html">לפרטים על דוקרנים נגד יונים</a>
        </article>
        <article class="card">
          <h3>הגנה לפאנלים סולאריים</h3>
          <p>הגנה מתקדמת לפאנלים סולאריים מפני יונים ולכלוך, כולל התקנה מקצועית על גגות ומתקנים פתוחים.</p>
          <a class="card-link" href="solar-panels-protection.html">לפרטים על הגנה לפאנלים סולאריים</a>
        </article>
        <article class="card">
          <h3>פס חשמלי נגד יונים</h3>
          <p>פתרון פס חשמלי נגד יונים לכניסה לגרמי מדרגות, מרפסות וגגות, שמבטיח סביבה ללא יונים.</p>
          <a class="card-link" href="electric-bird-deterrent.html">לפרטים על פס חשמלי נגד יונים</a>
        </article>
      </div>
    </section>

    <section class="container section why-us">
      <div class="content">
        <h2>למה לבחור ב-HD הרחקת יונים?</h2>
        <ul>
          <li>18 שנות ניסיון בהרחקת יונים ושירותי מניעה מקצועיים.</li>
          <li>פתרונות הומאניים ללא פגיעה בבעלי החיים.</li>
          <li>אחריות מלאה ללקוחות פרטיים, וועד בית וחברות אחזקה.</li>
          <li>חומרים עמידים לשמש, UV ולחלודה לשנים רבות.</li>
          <li>רישיון עבודה בגובה, סנפלינג ומנוף לכל אתגר.</li>
        </ul>
      </div>
      <div class="image-box">
        <img src="images/pigeon-removal.svg" alt="טיפול הרחקת יונים מקצועי" loading="lazy">
      </div>
    </section>

    <section class="container section cities" id="cities">
      <h2>שירותי הרחקת יונים בערים מרכזיות</h2>
      <div class="cards">
        <article class="card"><h3>הרחקת יונים תל אביב</h3><p>טיפול מהיר בתל אביב עם פתרונות מקומיים לרשתות ודוקרנים.</p><a class="card-link" href="tel-aviv.html">לפרטים</a></article>
        <article class="card"><h3>הרחקת יונים רמת גן</h3><p>הגנה מקצועית על בתים פרטיים, דירות ומשרדים ברמת גן.</p><a class="card-link" href="ramet-gan.html">לפרטים</a></article>
        <article class="card"><h3>הרחקת יונים גבעתיים</h3><p>פתרונות מותאמים לרשתות ומניעת יונים בגבעתיים.</p><a class="card-link" href="givatayim.html">לפרטים</a></article>
        <article class="card"><h3>הרחקת יונים ראשון לציון</h3><p>שירות אמין ומקצועי באזור ראשון לציון עם אחריות מלאה.</p><a class="card-link" href="rishon-lezion.html">לפרטים</a></article>
        <article class="card"><h3>הרחקת יונים פתח תקווה</h3><p>טיפול יסודי בפתח תקווה הכולל ניקיונות והתקנת מערכות הגנה.</p><a class="card-link" href="petah-tikva.html">לפרטים</a></article>
        <article class="card"><h3>הרחקת יונים חולון</h3><p>התקנת רשתות וחומרים עמידים עבור נדל"ן וחברות אחזקה בחולון.</p><a class="card-link" href="holon.html">לפרטים</a></article>
        <article class="card"><h3>הרחקת יונים בת ים</h3><p>טיפול מקצועי בת ים עם דגש על גגות ומרפסות פתוחות.</p><a class="card-link" href="bat-yam.html">לפרטים</a></article>
      </div>
    </section>

    <section class="container section gallery">
      <h2>דוגמאות עבודה והגנה מקצועית</h2>
      <div class="gallery-grid">
        <article class="gallery-card">
          <img src="images/pigeon-removal.svg" alt="התקנת פתרון הרחקת יונים" loading="lazy">
          <p>הרחקת יונים וניקיון אזורי קינון</p>
        </article>
        <article class="gallery-card">
          <img src="images/bird-netting.svg" alt="התקנת רשת נגד יונים" loading="lazy">
          <p>התקנת רשת נגד יונים לעסקים ולבתים</p>
        </article>
        <article class="gallery-card">
          <img src="images/inspection-solar.svg" alt="בדיקת הגנה לפאנלים סולאריים" loading="lazy">
          <p>הגנה לפאנלים סולאריים מפני יונים ולכלוך</p>
        </article>
      </div>
    </section>

    <section class="container section testimonials">
      <h2>לקוחות מרוצים</h2>
      <div class="testimonial-grid">
        <article class="testimonial">
          <p>"שירות מהיר, אדיב ומקצועי. התקינו רשת על המרפסת שלנו בבן גוריון ופשוט שקט היום."</p>
          <span>– נועה, תל אביב</span>
        </article>
        <article class="testimonial">
          <p>"הבעל מקצוע הגיע בזמן, הסביר את הפתרון והתקין דוקרנים איכותיים. ממליץ בחום."</p>
          <span>– דני, פתח תקווה</span>
        </article>
      </div>
    </section>

    <section class="container section faq">
      <h2>שאלות נפוצות על הרחקת יונים</h2>
      <dl>
        <dt>כמה זמן לוקח טיפול בהרחקת יונים?</dt>
        <dd>הטיפול בדרך כלל מתבצע ביום אחד. התקנת רשתות או דוקרנים יכולה לקחת בין מספר שעות ליום אחד, בהתאם לגודל והמורכבות.</dd>
        <dt>האם השירות פוגע ביונים?</dt>
        <dd>לא. אנו עובדים עם שיטות הומאניות שמרחיקות את היונים ללא פגיעה ומאפשרות סביבה נקייה ובטוחה.</dd>
        <dt>מהי האחריות שאתם נותנים?</dt>
        <dd>אנו מעניקים אחריות מלאה למשך 5 שנים על מערכות ההגנה והחומרים הניתנים להתקנה.</dd>
      </dl>
    </section>

    <section class="container section contact" id="contact">
      <h2>צרו קשר עם HD הרחקת יונים</h2>
      <p>התקשרו עכשיו או שלחו הודעת וואטסאפ כדי לקבל ייעוץ ולתאם שירות בכל הארץ.</p>
      <div class="contact-cards">
        <article class="contact-card">
          <h3>טלפון</h3>
          <a href="tel:+972537770944">+972 53-777-0944</a>
        </article>
        <article class="contact-card">
          <h3>וואטסאפ</h3>
          <a href="https://wa.me/972537770944?text=%D7%A9%D7%9C%D7%95%D7%9D%20HD%20%D7%94%D7%A8%D7%97%D7%A7%D7%AA%20%D7%99%D7%95%D7%A0%D7%99%D7%9D">שלח הודעת וואטסאפ</a>
        </article>
        <article class="contact-card">
          <h3>אימייל</h3>
          <a href="mailto:h_devid@walla.com">h_devid@walla.com</a>
        </article>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container">
      <p>HD הרחקת יונים | שירות אמין בכל הארץ | רישיון עבודה בגובה | אחריות 5 שנים</p>
    </div>
  </footer>

  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "LocalBusiness",
        "name": "HD הרחקת יונים",
        "description": "שירותים מקצועיים להרחבת יונים, רשתות נגד יונים, דוקרנים, פס חשמלי והגנה לפאנלים סולאריים.",
        "url": "''' + domain + '''/",
        "telephone": "+972537770944",
        "email": "h_devid@walla.com",
        "address": {
          "@type": "PostalAddress",
          "addressCountry": "IL"
        },
        "areaServed": {
          "@type": "Country",
          "name": "Israel"
        },
        "openingHoursSpecification": {
          "@type": "OpeningHoursSpecification",
          "dayOfWeek": ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"],
          "opens": "08:00",
          "closes": "18:00"
        },
        "keywords": "הרחקת יונים, רשת נגד יונים, דוקרנים נגד יונים, פס חשמלי נגד יונים, הגנה לפאנלים סולאריים"
      },
      {
        "@type": "Service",
        "serviceType": "הרחקת יונים",
        "provider": {
          "@type": "LocalBusiness",
          "name": "HD הרחקת יונים"
        },
        "areaServed": "Israel",
        "description": "שירותי הרחקת יונים מקצועיים לכל הארץ, כולל גגות, מרפסות, בתים פרטיים ומוסדות."
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {
            "@type": "Question",
            "name": "כמה זמן לוקח טיפול בהרחקת יונים?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "הטיפול בדרך כלל מתבצע ביום אחד. התקנת רשתות או דוקרנים יכולה לקחת בין מספר שעות ליום אחד."
            }
          },
          {
            "@type": "Question",
            "name": "האם השירות פוגע ביונים?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "לא. השירות נעשה בשיטות הומאניות שמרחיקות את היונים ללא פגיעה ומקנות סביבה נקייה ובטוחה."
            }
          },
          {
            "@type": "Question",
            "name": "מה כוללת האחריות?",
            "acceptedAnswer": {
              "@type": "Answer",
              "text": "האחריות כוללת תיקון ושדרוג מערכות ההגנה למשך 5 שנים, כולל רשתות, דוקרנים ופסי חשמל."
            }
          }
        ]
      }
    ]
  }
  </script>
</body>
</html>
'''

service_pages = {
    'pigeon-removal.html': {
        'title': 'הסרת יונים מקצועית | HD הרחקת יונים',
        'description': 'הסרת יונים מקצועית של HD הרחקת יונים לכל סוגי הגגות, מרפסות ובניינים. פתרונות הומאניים ללא פגיעה ואחריות מלאה.',
        'h1': 'הסרת יונים מקצועית',
        'content': 'HD הרחקת יונים מבצעת הרחקת יונים מקצועית ברחבי הארץ, עם ניסיון של 18 שנים. אנו מציעים טיפול נקי, בדיקה מלאה של נקודות כניסה והתקנה של פתרונות מניעה מתקדמים. הטיפול מתאים לגגות, בתים פרטיים, מוסדות ועסקים.',
        'faq': [
            ('איך מתבצעת הסרת יונים?', 'הסרת היונים מתבצעת באמצעות ניקוי אזורי קינון, התקנת פתרונות מניעה והרחבת צפייה כך שהיונים לא יחזרו. הכל בשיטות הומאניות.'),
            ('האם יש אחריות על הטיפול?', 'כן. אנו נותנים אחריות מלאה למשך 5 שנים על מערכת ההגנה ועל ההתקנה.'),
            ('האם השירות מתאים למרפסת?', 'בוודאי. אנו עוסקים גם בהרחקת יונים במרפסות ודירות גבוהות עם רשתות ודוקרנים מותאמים.'),
        ],
        'links': [
            ('bird-netting.html', 'רשת נגד יונים'),
            ('pigeon-spikes.html', 'דוקרנים נגד יונים'),
            ('electric-bird-deterrent.html', 'פס חשמלי נגד יונים'),
        ],
        'image': 'images/pigeon-removal.svg',
        'image_alt': 'הסרת יונים מקצועית'
    },
    'bird-netting.html': {
        'title': 'רשת נגד יונים | HD הרחקת יונים',
        'description': 'התקנת רשת נגד יונים עמידה לשמש ולחלודה. פתרון בטיחותי לכל מרפסת, גג ובניין.',
        'h1': 'רשת נגד יונים מקצועית',
        'content': 'התקנת רשת נגד יונים היא פתרון מעשי ועמיד שנועד להרחיק יונים מאזורים פתוחים. HD הרחקת יונים משתמשת ברשתות איכותיות העמידות UV וחלודה, עם תכנון מותאם לכל מבנה כדי לשמור על מראה אסתטי ובטיחות מרבית.',
        'faq': [
            ('למה חשוב להתקין רשת נגד יונים?', 'רשת נגד יונים מונעת כניסה של יונים למרפסות, גגות וחללים פתוחים ומפחיתה נזק וניקיון תכוף.'),
            ('האם הרשת מתאימה לפאנלים סולאריים?', 'כן. ניתן להתאים רשת סביב פאנלים סולאריים ולמנוע חיכוך ולכלוך על המערכת.'),
            ('כמה זמן החומר מחזיק?', 'הרשתות שלנו עמידות UV ולחלודה, ולכן נשארות לאורך שנים בתנאי חוץ קשים.'),
        ],
        'links': [
            ('pigeon-removal.html', 'הסרת יונים'),
            ('solar-panels-protection.html', 'הגנה לפאנלים סולאריים'),
        ],
        'image': 'images/bird-netting.svg',
        'image_alt': 'רשת נגד יונים'
    },
    'pigeon-spikes.html': {
        'title': 'דוקרנים נגד יונים | HD הרחקת יונים',
        'description': 'דוקרנים נגד יונים מנירוסטה עם התקנה מקצועית על אדנים וקירות. פתרון יעיל ומאושר לשמירה על המקום.',
        'h1': 'דוקרנים נגד יונים מנירוסטה',
        'content': 'דוקרנים נגד יונים הם פתרון יעיל להרחיק יונים מאזורים מוגדרים. HD הרחקת יונים משתמשת בדוקרני נירוסטה איכותיים שמותקנים בצורה דיסקרטית ומקצועית. זה מתאים במיוחד לאדנים, גגות וקירות שבהם היונים נוחתים.',
        'faq': [
            ('האם הדוקרנים פוגעים ביונים?', 'הדוקרנים לא פוגעים ביונים; הם מונעים ישיבה ונוחתים בצורה עדינה ובטוחה.'),
            ('האם זה מתאים לעסקים ומוסדות?', 'כן. דוקרני נירוסטה מותקנים גם בבניינים ציבוריים, בתי עסק ומוסדות כדי למנוע נזק וניקיון מתמשך.'),
            ('האם יש אחריות על התקנה?', 'כן, כולל אחריות מלאה על ההתקנה והחומר הנבחר למשך 5 שנים.'),
        ],
        'links': [
            ('pigeon-removal.html', 'הסרת יונים'),
            ('bird-netting.html', 'רשת נגד יונים'),
        ],
        'image': 'images/bird-netting.svg',
        'image_alt': 'דוקרנים נגד יונים'
    },
    'solar-panels-protection.html': {
        'title': 'הגנה לפאנלים סולאריים | HD הרחקת יונים',
        'description': 'הגנה מקצועית לפאנלים סולאריים מפני יונים ולכלוך, עם התקנה מותאמת לגגות ולמערכות סולאריות.',
        'h1': 'הגנה לפאנלים סולאריים נגד יונים',
        'content': 'הגנה לפאנלים סולאריים חשובה למניעת יונים ולשמירה על ייצור אנרגיה יעיל. HD הרחקת יונים מציעה פתרונות מותאמים עם רשתות ובקרות מיקום כדי למנוע רקבון ולכלוך על הפאנלים.',
        'faq': [
            ('למה צריך הגנה על פאנלים סולאריים?', 'יונים עלולים לזהם ולפגוע ביעילות הפאנלים. הגנה נכונה שומרת על תקינות וייצור אנרגיה גבוה.'),
            ('איזה פתרון מתאים לפאנלים?', 'אנו ממליצים על רשתות והגנות ייעודיות שמותקנות סביב הפאנלים בלי לפגוע באוורור.'),
            ('האם ניתן להגן גם על גגות תעשייתיים?', 'כן. אנו מספקים פתרונות גם לגגות תעשייתיים ולחוות סולאריות.'),
        ],
        'links': [
            ('bird-netting.html', 'רשת נגד יונים'),
            ('electric-bird-deterrent.html', 'פס חשמלי נגד יונים'),
        ],
        'image': 'images/inspection-solar.svg',
        'image_alt': 'הגנה לפאנלים סולאריים'
    },
    'electric-bird-deterrent.html': {
        'title': 'פס חשמלי נגד יונים | HD הרחקת יונים',
        'description': 'פס חשמלי נגד יונים להתקנה על אדנים, מרפסות וגגות. פתרון בטיחותי שמרחיק יונים בלי לפגוע בהם.',
        'h1': 'פס חשמלי נגד יונים',
        'content': 'התקנת פס חשמלי נגד יונים היא פתרון אפקטיבי ונקי לשמירה על מרפסות, אדנים וגגות. HD הרחקת יונים מספקת התקנה מקצועית עם חומרים עמידים, פתרון מתאים גם לעסקים וחברות אחזקה.',
        'faq': [
            ('האם הפס החשמלי בטוח?', 'הפס החשמלי נועד להרתיע ולא לפגוע והוא מותקן בצורה בטיחותית ומבוקרת.'),
            ('האם מתאים לבתים פרטיים?', 'כן, זהו פתרון שאינו מסיח את הדעת ומתאים במיוחד למרפסות וכניסות.'),
            ('האם צריך תחזוקה?', 'תחזוקה קלה מבוצעת אחת לכמה חודשים כדי לשמור על פעולה תקינה ואפקטיבית.'),
        ],
        'links': [
            ('pigeon-removal.html', 'הסרת יונים'),
            ('solar-panels-protection.html', 'הגנה לפאנלים סולאריים'),
        ],
        'image': 'images/bird-netting.svg',
        'image_alt': 'פס חשמלי נגד יונים'
    }
}

city_pages = {
    'tel-aviv.html': {
        'title': 'הרחקת יונים תל אביב | HD הרחקת יונים',
        'description': 'שירות הרחקת יונים מקצועי בתל אביב. פתרונות רשתות, דוקרנים, פס חשמלי והגנה לפאנלים סולאריים. שירות מהיר עם אחריות.',
        'h1': 'הרחקת יונים בתל אביב',
        'intro': 'HD הרחקת יונים מספקת שירותי הרחקת יונים בתל אביב, עם פתרונות מותאמים לכל דירה, גג ומרפסת. שירות מהיר אמין ואיכותי.',
        'faq': [
            ('האם אתם מספקים שירות בכל תל אביב?', 'כן. מרמת החייל ועד יפו, אנו מספקים שירות הרחקת יונים ודוקרנים בכל השכונות.'),
            ('האם יש אפשרות לתשלום בכרטיס?', 'ניתן לתאם תשלום בכרטיס או מזומן לפי ההעדפה שלך.'),
            ('כמה זמן לוקח להגיע?', 'בזמן העומס אנחנו מגיעים בדרך כלל בתוך 24-48 שעות בהתאם לבקשה.'),
        ],
        'city_text': 'בתל אביב אנחנו נותנים דגש על פתרונות שמותאמים לבניינים רבי קומות ולמרפסות צפופות. השירות כולל בדיקה מקדימה, ניקוי מקומות קינון והתקנה של מערכת מניעה שתמנע חזרה של יונים.'
    },
    'ramet-gan.html': {
        'title': 'הרחקת יונים רמת גן | HD הרחקת יונים',
        'description': 'שירותי הרחקת יונים ברמת גן לכל בתים פרטיים ומוסדות. רשתות, דוקרנים ופסים חשמליים עם אחריות מלאה.',
        'h1': 'הרחקת יונים ברמת גן',
        'intro': 'ברמת גן אנו מספקים פתרונות מקיפים להרחקת יונים כולל התקנת רשתות וניקוי מקצועי של גגות ומרפסות.',
        'faq': [
            ('האם אתם מגיעים גם לוועדי בתים?', 'כן. אנו מספקים הטבות לועד בית וחברות אחזקה ברמת גן.'),
            ('האם העבודה מתאימה לגגות ישנים?', 'אנו מבצעים בדיקה לפני התקנה וממליצים על הפתרון המתאים לכל מבנה.'),
            ('האם השירות כולל אחריות?', 'כן. אחריות מלאה ל-5 שנים ניתנת לכל התקנה ושירות.'),
        ],
        'city_text': 'ברמת גן אנו מתמודדים עם מבנים ישנים וחדשים כאחד. הפתרונות שלנו כוללים רשתות נגד יונים, דוקרנים בפינות ומערכות חשמליות להתמודדות עם יונים חוזרים.'
    },
    'givatayim.html': {
        'title': 'הרחקת יונים גבעתיים | HD הרחקת יונים',
        'description': 'הגנה מקצועית מפני יונים בגבעתיים. שירותים מותאמים למרפסות, גגות ובניינים.',
        'h1': 'הרחקת יונים בגבעתיים',
        'intro': 'גבעתיים מקבלת פתרון איכותי והרחקת יונים מקצועית. אנו מבצעים התקנת רשתות, דוקרנים וניקויים באופן מותאם למבני העיר.',
        'faq': [
            ('מה הבחירה הנכונה לדירות בגבעתיים?', 'בדירה בגבעתיים מומלץ לשלב רשת נגד יונים עם דוקרנים באזורים פתוחים כדי למנוע חזרה.'),
            ('האם יש שירות לעסקים?', 'כן. אנו מטפלים גם במשרדים, חנויות ובנייני משרדים בעיר.'),
            ('כמה זמן החומר מחזיק?', 'חומרי הרשת והדוקרנים עמידים לשמש ולחלודה ומחזיקים מספר שנים.'),
        ],
        'city_text': 'העבודה בגבעתיים מתמקדת במניעת ישיבה של יונים על אדנים ומרפסות. אנו מספקים פתרון מקצועי עם חומרים איכותיים ושירות ידידותי ללקוח.'
    },
    'rishon-lezion.html': {
        'title': 'הרחקת יונים ראשון לציון | HD הרחקת יונים',
        'description': 'שירות הרחקת יונים בראשון לציון לדירות, עסקים ובניינים. התקנת רשתות ודוקרנים עם מקצועיות וניסיון.',
        'h1': 'הרחקת יונים בראשון לציון',
        'intro': 'בראשון לציון אנו מעניקים שירותי הרחקת יונים לכל המבנים בעיר. הטיפול כולל בדיקה, ניקוי והתקנה של פתרונות מניעת יונים עם אחריות.',
        'faq': [
            ('האם אתם עוברים גם לפריפריה של ראשון לציון?', 'כן. אנו נותנים שירות גם בשכונות הצפון והדרום של ראשון לציון.'),
            ('האם יכולים לטפל בפאנלים סולאריים?', 'כן. אנו מספקים פתרונות הגנה לפאנלים סולאריים בראשון לציון.'),
            ('האם יש הוכחה לניסיון שלכם?', 'כן. יש לנו ניסיון של 18 שנים בעבודה מקצועית בכל הארץ.'),
        ],
        'city_text': 'ראשון לציון מקבלת פתרונות מותאמים הן למבני מגורים והן לעסקים. אנו עובדים בצורה נקייה ומהירה כדי להקטין את הפרעה לשגרה.'
    },
    'petah-tikva.html': {
        'title': 'הרחקת יונים פתח תקווה | HD הרחקת יונים',
        'description': 'שירות הרחקת יונים בפתח תקווה, כולל רשתות, דוקרנים ופסי חשמל לכל סוגי המבנים.',
        'h1': 'הרחקת יונים בפתח תקווה',
        'intro': 'פתח תקווה זקוקה לפתרונות הרחקת יונים מקצועיים. אנו מספקים פתרונות ברמת איכות גבוהה לשמירה על מרפסות, גגות ושטחים פתוחים.',
        'faq': [
            ('האם אתם מגיעים גם למפעלים בפתח תקווה?', 'כן. אנו מטפלים גם במתקנים תעשייתיים ובחברות אחזקה באזור.'),
            ('האם יש פתרון לפס חשמלי?', 'כן. פס חשמלי נגד יונים הוא פתרון יעיל למקומות שבהם אין אפשרות לרשת.'),
            ('האם השירות מספק טיפול לניקיון אחריו?', 'כן. ניתן לכלול ניקיון מקצועי של אזורי קינון כחלק מהשירות.'),
        ],
        'city_text': 'בפתח תקווה אנו דואגים להתקנה מדויקת עם חומרים עמידים. השירות מתאים לבתים פרטיים, בניינים ומקומות עבודה.'
    },
    'holon.html': {
        'title': 'הרחקת יונים חולון | HD הרחקת יונים',
        'description': 'הגנת חולון מפני יונים עם רשתות, דוקרנים ופס חשמלי. שירות אמין לעסקים ולבתים פרטיים.',
        'h1': 'הרחקת יונים בחולון',
        'intro': 'חולון מקבלת שירות HD הרחקת יונים עם פתרונות מותאמים למרחב העירוני. התקנה בטיחותית של רשתות ודוקרנים בכל סוגי המבנים.',
        'faq': [
            ('האם העבודה מתאימה גם לבנייני מגורים בחולון?', 'כן. אנו מספקים פתרונות לבנייני מגורים, מוסדות ועסקים בחולון.'),
            ('כיצד אתם מטפלים בעונת החורף?', 'בהתאם למזג האוויר אנו מתקינים חומרים עמידים ומוודאים סגירה טובה של הרשתות.'),
            ('האם יש אחריות לניצול?', 'בוודאי. אחריות מלאה ל-5 שנים כלולה בכל ההתקנות.'),
        ],
        'city_text': 'בחולון אנו מספקים פתרונות שקטים ואסתטיים למרפסות, גגות וחללים פתוחים, עם דגש על שירות מהיר ולא מזיק.'
    },
    'bat-yam.html': {
        'title': 'הרחקת יונים בת ים | HD הרחקת יונים',
        'description': 'הסרת יונים מקצועית בת ים לכל גגות, מרפסות ופאנלים סולאריים. שירות מהיר ואחריות מלאה.',
        'h1': 'הרחקת יונים בבת ים',
        'intro': 'בת ים מקבלת שירות הרחקת יונים מקצועי ומקיף. אנו מטפלים גם בגגות ובפאנלים סולאריים, עם דגש על סביבת מגורים בטוחה ונקייה.',
        'faq': [
            ('האם יש לכם פתרון לחשמל ולמים בבת ים?', 'החומרים שלנו עמידים ללחות ולמליחות, ומתאימים לעבודה בחוף ובהרים קרובים.'),
            ('האם השירות מתאים לבניינים צמודי ים?', 'כן. אנו מבצעים בדיקה מקיפה ובוחרים פתרון מותאם לכל בניין.'),
            ('כיצד ניתן להזמין שירות?', 'ניתן להתקשר או לשלוח וואטסאפ למספר +972537770944 ולקבל תיאום מהיר.'),
        ],
        'city_text': 'בבת ים אנו נותנים מענה מהיר לגגות ולמרפסות עם פתרונות מניעה מקצועיים ועמידים בשמש ובמליחות.'
    }
}

page_template = '''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="/{filename}">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{full_url}">
  <meta property="og:image" content="{image_url}">
  <meta property="og:site_name" content="HD הרחקת יונים">
  <meta property="og:locale" content="he_IL">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="hero page-hero">
    <div class="container">
      <div class="site-header">
        <div class="logo">HD הרחקת יונים</div>
        <nav class="site-nav" aria-label="תפריט ראשי">
          <ul>
            <li><a href="/">בית</a></li>
            <li><a href="pigeon-removal.html">שירותים</a></li>
            <li><a href="#contact">צור קשר</a></li>
          </ul>
        </nav>
      </div>
      <div class="page-intro">
        <p class="eyebrow">שירות מקצועי בכל הארץ</p>
        <h1>{h1}</h1>
        <p class="subtitle">{content}</p>
        <div class="hero-buttons">
          <a class="button primary" href="tel:+972537770944">התקשר עכשיו</a>
          <a class="button secondary" href="https://wa.me/972537770944?text=%D7%A9%D7%9C%D7%95%D7%9D%20HD%20%D7%94%D7%A8%D7%97%D7%A7%D7%AA%20%D7%99%D7%95%D7%A0%D7%99%D7%9D">וואטסאפ</a>
        </div>
        <p class="hero-note">אחריות 5 שנים | חומרים עמידים לשמש ולחלודה | עבודות גובה וסנפלינג</p>
      </div>
    </div>
  </header>
  <main>
    <section class="container section page-content">
      <h2>מה כוללת {h1}</h2>
      <div class="page-grid">
        <div>
          <p>{content}</p>
          <p>הצוות שלנו משתמש בחומרים איכותיים ומותאמים לכל מבנה וכן בהתקנות בטיחות עם אחריות. את הפתרון אנו בוחרים לפי סוג המקום: גג, מרפסת, בית פרטי, מוסד או עסק.</p>
        </div>
        <div class="image-box page-image">
          <img src="{image}" alt="{image_alt}" loading="lazy">
        </div>
      </div>
      <div class="related-links">
        <h3>קישורים נוספים</h3>
        <ul>
          {link_items}
        </ul>
      </div>
    </section>
    <section class="container section faq">
      <h2>שאלות נפוצות</h2>
      <dl>
        {faq_items}
      </dl>
    </section>
    <section class="container section contact" id="contact">
      <h2>צרו קשר</h2>
      <p>לפרטים והצעת מחיר מהירה, התקשרו או שלחו הודעת וואטסאפ.</p>
      <div class="contact-cards">
        <article class="contact-card">
          <h3>טלפון</h3>
          <a href="tel:+972537770944">+972 53-777-0944</a>
        </article>
        <article class="contact-card">
          <h3>וואטסאפ</h3>
          <a href="https://wa.me/972537770944?text=%D7%A9%D7%9C%D7%95%D7%9D%20HD%20%D7%94%D7%A8%D7%97%D7%A7%D7%AA%20%D7%99%D7%95%D7%A0%D7%99%D7%9D">שלח הודעת וואטסאפ</a>
        </article>
        <article class="contact-card">
          <h3>אימייל</h3>
          <a href="mailto:h_devid@walla.com">h_devid@walla.com</a>
        </article>
      </div>
    </section>
  </main>
  <footer class="footer">
    <div class="container">
      <p>HD הרחקת יונים | שירות מקצועי בכל הארץ | רישיון עבודה בגובה | אחריות 5 שנים</p>
    </div>
  </footer>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "LocalBusiness",
        "name": "HD הרחקת יונים",
        "description": "שירותים מקצועיים להרחבת יונים, רשתות נגד יונים, דוקרנים, פס חשמלי והגנה לפאנלים סולאריים.",
        "url": "''' + domain + '''/",
        "telephone": "+972537770944",
        "email": "h_devid@walla.com",
        "address": {"@type": "PostalAddress", "addressCountry": "IL"},
        "areaServed": {"@type": "Country", "name": "Israel"},
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification","dayOfWeek": ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"],"opens": "08:00","closes": "18:00"}
      },
      {
        "@type": "Service",
        "serviceType": "{service_type}",
        "provider": {"@type": "LocalBusiness", "name": "HD הרחקת יונים"},
        "areaServed": "Israel",
        "description": "{description}"
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "בית", "item": "''' + domain + '''/"},
          {"@type": "ListItem", "position": 2, "name": "{h1}", "item": "{full_url}"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {faq_json}
        ]
      }
    ]
  }
  </script>
</body>
</html>
'''

city_template = '''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="/{filename}">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{full_url}">
  <meta property="og:image" content="''' + domain + '''/images/pigeon-removal.svg">
  <meta property="og:site_name" content="HD הרחקת יונים">
  <meta property="og:locale" content="he_IL">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <header class="hero page-hero">
    <div class="container">
      <div class="site-header">
        <div class="logo">HD הרחקת יונים</div>
        <nav class="site-nav" aria-label="תפריט ראשי">
          <ul>
            <li><a href="/">בית</a></li>
            <li><a href="pigeon-removal.html">שירותים</a></li>
            <li><a href="#contact">צור קשר</a></li>
          </ul>
        </nav>
      </div>
      <div class="page-intro">
        <p class="eyebrow">שירותי הרחקת יונים ב{city_name}</p>
        <h1>{h1}</h1>
        <p class="subtitle">{intro}</p>
        <div class="hero-buttons">
          <a class="button primary" href="tel:+972537770944">התקשר עכשיו</a>
          <a class="button secondary" href="https://wa.me/972537770944?text=%D7%A9%D7%9C%D7%95%D7%9D%20HD%20%D7%94%D7%A8%D7%97%D7%A7%D7%AA%20%D7%99%D7%95%D7%A0%D7%99%D7%9D">וואטסאפ</a>
        </div>
        <p class="hero-note">שירות מהיר באזור {city_name} | פתרונות הגנה לדירות, גגות ועסקים</p>
      </div>
    </div>
  </header>
  <main>
    <section class="container section page-content">
      <h2>הפתרון שלנו ל{city_name}</h2>
      <div class="page-grid">
        <div>
          <p>{city_text}</p>
          <p>אנו מספקים פתרונות מותאמים אישית, כולל התקנת רשתות, דוקרנים, פס חשמלי והגנה לפאנלים סולאריים בכל העיר.</p>
        </div>
        <div class="image-box page-image">
          <img src="images/pigeon-removal.svg" alt="שירות הרחקת יונים ב{city_name}" loading="lazy">
        </div>
      </div>
      <div class="related-links">
        <h3>שירותים רלוונטיים</h3>
        <ul>
          <li><a href="pigeon-removal.html">הסרת יונים</a></li>
          <li><a href="bird-netting.html">רשת נגד יונים</a></li>
          <li><a href="pigeon-spikes.html">דוקרנים נגד יונים</a></li>
        </ul>
      </div>
    </section>
    <section class="container section faq">
      <h2>שאלות נפוצות ב{city_name}</h2>
      <dl>
        {faq_items}
      </dl>
    </section>
    <section class="container section contact" id="contact">
      <h2>צרו קשר עכשיו</h2>
      <p>התקשרו או שלחו הודעת וואטסאפ ל-+972 53-777-0944 כדי לתאם שירות מהיר ב{city_name}.</p>
      <div class="contact-cards">
        <article class="contact-card">
          <h3>טלפון</h3>
          <a href="tel:+972537770944">+972 53-777-0944</a>
        </article>
        <article class="contact-card">
          <h3>וואטסאפ</h3>
          <a href="https://wa.me/972537770944?text=%D7%A9%D7%9C%D7%95%D7%9D%20%E2%80%93%20%D7%90%D7%96%D7%95%D7%A8%20%D7%99%D7%95%D7%A0%D7%99%D7%9D%20%D7%91{city_name}">שלח הודעת וואטסאפ</a>
        </article>
        <article class="contact-card">
          <h3>אימייל</h3>
          <a href="mailto:h_devid@walla.com">h_devid@walla.com</a>
        </article>
      </div>
    </section>
  </main>
  <footer class="footer">
    <div class="container">
      <p>HD הרחקת יונים | שירות מקצועי בכל הארץ | רישיון עבודה בגובה | אחריות 5 שנים</p>
    </div>
  </footer>
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@graph": [
      {
        "@type": "LocalBusiness",
        "name": "HD הרחקת יונים",
        "description": "שירותים מקצועיים להרחבת יונים, רשתות נגד יונים, דוקרנים, פס חשמלי והגנה לפאנלים סולאריים.",
        "url": "''' + domain + '''/",
        "telephone": "+972537770944",
        "email": "h_devid@walla.com",
        "address": {"@type": "PostalAddress", "addressCountry": "IL"},
        "areaServed": {"@type": "Country", "name": "Israel"},
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification","dayOfWeek": ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"],"opens": "08:00","closes": "18:00"}
      },
      {
        "@type": "BreadcrumbList",
        "itemListElement": [
          {"@type": "ListItem", "position": 1, "name": "בית", "item": "''' + domain + '''/"},
          {"@type": "ListItem", "position": 2, "name": "{h1}", "item": "{full_url}"}
        ]
      },
      {
        "@type": "FAQPage",
        "mainEntity": [
          {faq_json}
        ]
      }
    ]
  }
  </script>
</body>
</html>
'''

for filename, data in service_pages.items():
    faq_items = ''.join([f'<dt>{q}</dt>\n        <dd>{a}</dd>\n        ' for q, a in data['faq']])
    faq_json = ',\n          '.join([f'{{"@type": "Question", "name": "{q}", "acceptedAnswer": {{"@type": "Answer", "text": "{a}"}}}}' for q, a in data['faq']])
    link_items = ''.join([f'<li><a href="{url}">{label}</a></li>\n          ' for url, label in data['links']])
    page_html = page_template.format(
        title=data['title'],
        description=data['description'],
        filename=filename,
        full_url=domain + '/' + filename,
        h1=data['h1'],
        content=data['content'],
        image=data['image'],
        image_alt=data['image_alt'],
        image_url=domain + '/' + data['image'],
        link_items=link_items,
        faq_items=faq_items,
        faq_json=faq_json,
        service_type=data['h1'],
    )
    (base / filename).write_text(page_html, encoding='utf-8')

for filename, data in city_pages.items():
    faq_items = ''.join([f'<dt>{q}</dt>\n        <dd>{a}</dd>\n        ' for q, a in data['faq']])
    faq_json = ',\n          '.join([f'{{"@type": "Question", "name": "{q}", "acceptedAnswer": {{"@type": "Answer", "text": "{a}"}}}}' for q, a in data['faq']])
    page_html = city_template.format(
        title=data['title'],
        description=data['description'],
        filename=filename,
        full_url=domain + '/' + filename,
        h1=data['h1'],
        intro=data['intro'],
        city_name=data['h1'].replace('הרחקת יונים ', ''),
        city_text=data['city_text'],
        faq_items=faq_items,
        faq_json=faq_json,
    )
    (base / filename).write_text(page_html, encoding='utf-8')

(base / 'index.html').write_text(index, encoding='utf-8')
robots = 'User-agent: *\nAllow: /\nSitemap: ' + domain + '/sitemap.xml\n'
(base / 'robots.txt').write_text(robots, encoding='utf-8')

sitemap_urls = [
    '/',
    '/pigeon-removal.html',
    '/bird-netting.html',
    '/pigeon-spikes.html',
    '/solar-panels-protection.html',
    '/electric-bird-deterrent.html',
    '/tel-aviv.html',
    '/ramet-gan.html',
    '/givatayim.html',
    '/rishon-lezion.html',
    '/petah-tikva.html',
    '/holon.html',
    '/bat-yam.html'
]
xml = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for path in sitemap_urls:
    xml.append('  <url>')
    xml.append('    <loc>' + domain + path + '</loc>')
    xml.append('    <changefreq>weekly</changefreq>')
    xml.append('    <priority>0.8</priority>')
    xml.append('  </url>')
xml.append('</urlset>')
(base / 'sitemap.xml').write_text('\n'.join(xml), encoding='utf-8')
print('files created and index updated')
