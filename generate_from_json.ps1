$ErrorActionPreference = "Stop"
$Base = $PSScriptRoot
$Domain = "https://hd-harakat-yunim.co.il"
$data = Get-Content (Join-Path $Base "cities.json") -Raw -Encoding UTF8 | ConvertFrom-Json

$dot = [char]0x00B7
$H = @{
    brand = "HD " + (-join @([char]0x05D4,[char]0x05E8,[char]0x05D7,[char]0x05E7,[char]0x05EA,[char]0x0020,[char]0x05D9,[char]0x05D5,[char]0x05E0,[char]0x05D9,[char]0x05DD))
    services = -join @([char]0x05E9,[char]0x05D9,[char]0x05E8,[char]0x05D5,[char]0x05EA,[char]0x05D9,[char]0x05DD)
    areas = -join @([char]0x05D0,[char]0x05D6,[char]0x05D5,[char]0x05E8,[char]0x05D9,[char]0x05DD)
    harakat = -join @([char]0x05D4,[char]0x05E8,[char]0x05D7,[char]0x05E7,[char]0x05EA,[char]0x0020,[char]0x05D9,[char]0x05D5,[char]0x05E0,[char]0x05D9,[char]0x05DD)
    harakatBe = -join @([char]0x05D4,[char]0x05E8,[char]0x05D7,[char]0x05E7,[char]0x05EA,[char]0x0020,[char]0x05D9,[char]0x05D5,[char]0x05E0,[char]0x05D9,[char]0x05DD,[char]0x0020,[char]0x05D1)
    call = -join @([char]0x05D4,[char]0x05EA,[char]0x05E7,[char]0x05E9,[char]0x05E8,[char]0x0020,[char]0x05E2,[char]0x05DB,[char]0x05E9,[char]0x05D9,[char]0x05D5)
    quote = -join @([char]0x05D4,[char]0x05E6,[char]0x05E2,[char]0x05EA,[char]0x0020,[char]0x05DE,[char]0x05D7,[char]0x05D9,[char]0x05E8)
    spikes = -join @([char]0x05D3,[char]0x05D5,[char]0x05E7,[char]0x05E8,[char]0x05E0,[char]0x05D9,[char]0x0020,[char]0x05D9,[char]0x05D5,[char]0x05E0,[char]0x05D9,[char]0x05DD)
    nets = -join @([char]0x05E8,[char]0x05E9,[char]0x05EA,[char]0x05D5,[char]0x05EA,[char]0x0020,[char]0x05D9,[char]0x05D5,[char]0x05E0,[char]0x05D9,[char]0x05DD)
    allAreas = -join @([char]0x05DB,[char]0x05DC,[char]0x0020,[char]0x05D4,[char]0x05D0,[char]0x05D6,[char]0x05D5,[char]0x05E8,[char]0x05D9,[char]0x05DD)
    name = -join @([char]0x05E9,[char]0x05DD)
    phone = -join @([char]0x05D8,[char]0x05DC,[char]0x05E4,[char]0x05D5,[char]0x05DF)
    city = -join @([char]0x05E2,[char]0x05D9,[char]0x05E8)
    details = -join @([char]0x05E4,[char]0x05E8,[char]0x05D8,[char]0x05D9,[char]0x05DD)
    whatsapp = -join @([char]0x05D5,[char]0x05D5,[char]0x05D0,[char]0x05D8,[char]0x05E1,[char]0x05D0,[char]0x05E4)
    home = -join @([char]0x05E2,[char]0x05DE,[char]0x05D5,[char]0x05D3,[char]0x0020,[char]0x05E8,[char]0x05D0,[char]0x05E9,[char]0x05D9)
    photo = -join @([char]0x05EA,[char]0x05DE,[char]0x05D5,[char]0x05E0,[char]0x05D4)
    areasTitle = -join @([char]0x05DB,[char]0x05DC,[char]0x0020,[char]0x05D4,[char]0x05E2,[char]0x05E8,[char]0x05D9,[char]0x05DD,[char]0x0020,[char]0x05D5,[char]0x05D4,[char]0x05D0,[char]0x05D6,[char]0x05D5,[char]0x05E8,[char]0x05D9,[char]0x05DD)
    areasDesc = -join @([char]0x05D4,[char]0x05E8,[char]0x05E9,[char]0x05D9,[char]0x05DE,[char]0x05D4,[char]0x0020,[char]0x05DE,[char]0x05DC,[char]0x05D0,[char]0x05D4,[char]0x0020,[char]0x05E9,[char]0x05DC,[char]0x0020,[char]0x05DB,[char]0x05DC,[char]0x0020,[char]0x05D4,[char]0x05E2,[char]0x05E8,[char]0x05D9,[char]0x05DD,[char]0x0020,[char]0x05D5,[char]0x05D4,[char]0x05D0,[char]0x05D6,[char]0x05D5,[char]0x05E8,[char]0x05D9,[char]0x05DD,[char]0x0020,[char]0x05E9,[char]0x05D1,[char]0x05D4,[char]0x05DD,[char]0x0020,[char]0x05D0,[char]0x05E0,[char]0x05D5,[char]0x002E)
}

function Get-CityPage($file, $city, $region, $text) {
    $title = "$($H.harakatBe)$city | $($H.brand)"
    $esc = $city.Replace('"','&quot;')
    $mid = "$region $dot $city"
@"
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>$title</title>
  <meta name="description" content="$text">
  <link rel="canonical" href="$Domain/$file">
  <meta name="robots" content="index, follow">
  <link rel="stylesheet" href="styles.css">
</head>
<body class="has-sticky-bar">
  <header class="hero page-hero"><div class="container"><div class="site-header"><a href="index.html" class="logo">$($H.brand)</a><nav class="site-nav"><ul><li><a href="index.html#services">$($H.services)</a></li><li><a href="areas.html">$($H.areas)</a></li></ul></nav><a class="header-cta" href="tel:0528805053">052-880-5053</a></div><div class="page-intro"><p class="eyebrow">$mid</p><h1>$($H.harakatBe)$city</h1><p class="subtitle">$text</p><div class="hero-buttons"><a class="button primary" href="tel:0528805053">$($H.call)</a><a class="button secondary" href="index.html#contact-form">$($H.quote)</a></div></div></div></header>
  <main><section class="container section"><div class="page-content-grid"><div><p>$text</p><p><a href="pigeon-spikes.html">$($H.spikes)</a> $dot <a href="bird-netting.html">$($H.nets)</a> $dot <a href="areas.html">$($H.allAreas)</a></p></div><div class="media-placeholder"><span>$($H.photo): $city</span></div></div></section><section class="container section" id="contact-form"><div class="contact-form-section"><form class="lead-form" novalidate><div><label for="name">$($H.name)</label><input id="name" name="name" required></div><div><label for="phone">$($H.phone)</label><input id="phone" name="phone" type="tel" required></div><div><label for="city">$($H.city)</label><input id="city" name="city" value="$esc"></div><div><label for="message">$($H.details)</label><textarea id="message" name="message"></textarea></div><button type="submit" class="button whatsapp form-submit">$($H.whatsapp)</button></form></div></section></main>
  <footer class="footer"><div class="container"><p><a href="index.html">$($H.home)</a> $dot <a href="areas.html">$($H.areas)</a></p></div></footer>
  <div class="sticky-bar"><a href="tel:0528805053" class="sbtn sbtn-call">$($H.call)</a><a href="#contact-form" class="sbtn sbtn-quote">$($H.quote)</a><a href="#" class="sbtn sbtn-wa wa-direct">$($H.whatsapp)</a></div>
  <script src="contact-form.js" defer></script>
</body>
</html>
"@
}

$count = 0
$urls = @("/", "/areas.html", "/pigeon-spikes.html", "/bird-netting.html", "/electric-bird-deterrent.html", "/solar-panels-protection.html")
$areasParts = @()
$areasParts += @"
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>$($H.areasTitle) | $($H.brand)</title>
  <meta name="description" content="$($H.areasDesc)">
  <link rel="canonical" href="$Domain/areas.html">
  <link rel="stylesheet" href="styles.css">
</head>
<body class="has-sticky-bar">
  <header class="hero page-hero">
    <div class="container">
      <div class="site-header">
        <a href="index.html" class="logo">$($H.brand)</a>
        <nav class="site-nav"><ul><li><a href="index.html#services">$($H.services)</a></li><li><a href="areas.html">$($H.areas)</a></li></ul></nav>
        <a class="header-cta" href="tel:0528805053">052-880-5053</a>
      </div>
      <div class="page-intro">
        <h1>$($H.areasTitle)</h1>
        <p class="subtitle"><a href="index.html">$($H.home)</a></p>
      </div>
    </div>
  </header>
  <main>
"@

foreach ($region in $data.regions) {
    $areasParts += "<section class=`"container section region-block`"><h2 class=`"section-title-bar`">$($region.name)</h2><nav class=`"city-links`">"
    foreach ($c in $region.cities) {
        $html = Get-CityPage $c.file $c.name $region.name $c.text
        [System.IO.File]::WriteAllText((Join-Path $Base $c.file), $html, [System.Text.UTF8Encoding]::new($false))
        $urls += "/$($c.file)"
        $areasParts += "<a href=`"$($c.file)`">$($c.name)</a>"
        $count++
    }
    $areasParts += "</nav></section>"
}

$areasParts += @"
  </main>
  <footer class="footer"><div class="container"><p><a href="index.html">$($H.home)</a> $dot <a href="areas.html">$($H.areas)</a></p></div></footer>
  <div class="sticky-bar"><a href="tel:0528805053" class="sbtn sbtn-call">$($H.call)</a><a href="#contact-form" class="sbtn sbtn-quote">$($H.quote)</a><a href="#" class="sbtn sbtn-wa wa-direct">$($H.whatsapp)</a></div>
  <script src="contact-form.js" defer></script>
</body>
</html>
"@

[System.IO.File]::WriteAllText((Join-Path $Base "areas.html"), ($areasParts -join "`n"), [System.Text.UTF8Encoding]::new($false))

$sitemap = @('<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
foreach ($u in $urls) { $sitemap += "  <url><loc>$Domain$u</loc><changefreq>weekly</changefreq></url>" }
$sitemap += '</urlset>'
[System.IO.File]::WriteAllText((Join-Path $Base "sitemap.xml"), ($sitemap -join "`n"), [System.Text.UTF8Encoding]::new($false))
Write-Host "Generated $count city pages + areas.html + sitemap.xml"
