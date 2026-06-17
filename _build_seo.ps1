# SEO page generator
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Web
$Base = $PSScriptRoot
$Utf8 = [System.Text.UTF8Encoding]::new($false)
function Write-Utf8([string]$Path, [string]$Content) { [System.IO.File]::WriteAllText($Path, $Content, $Utf8) }
function Esc([string]$t) { [System.Web.HttpUtility]::HtmlEncode($t) }
$PyText = [System.IO.File]::ReadAllText((Join-Path $Base 'generate_seo.py'), $Utf8)
$DOMAIN = ([regex]::Match($PyText, 'DOMAIN = "([^"]+)"')).Groups[1].Value
$BRAND = ([regex]::Match($PyText, 'BRAND = "([^"]+)"')).Groups[1].Value
$PHONE_DISPLAY = ([regex]::Match($PyText, 'PHONE_DISPLAY = "([^"]+)"')).Groups[1].Value
$PHONE_TEL = ([regex]::Match($PyText, 'PHONE_TEL = "([^"]+)"')).Groups[1].Value
$EMAIL = ([regex]::Match($PyText, 'EMAIL = "([^"]+)"')).Groups[1].Value
$OG_IMAGE = "$DOMAIN/images/og-default.svg"
$LASTMOD = (Get-Date).ToString('yyyy-MM-dd')

function Get-PyString([string]$block, [string]$key) {
  $m = [regex]::Match($block, '"' + [regex]::Escape($key) + '":\s*"((?:\\.|[^"\\])*)"')
  if (-not $m.Success) { throw "Missing key $key" }
  return ($m.Groups[1].Value -replace '\\"','"')
}
function Get-PyStringList([string]$block, [string]$key) {
  $m = [regex]::Match($block, '"' + [regex]::Escape($key) + '":\s*\[(.*?)\]', 'Singleline')
  if (-not $m.Success) { return @() }
  $list = New-Object System.Collections.Generic.List[string]
  foreach ($pm in [regex]::Matches($m.Groups[1].Value, '"((?:\\.|[^"\\])*)"')) {
    $list.Add(($pm.Groups[1].Value -replace '\\"','"'))
  }
  return $list.ToArray()
}
function Get-PyTupleList([string]$block, [string]$key) {
  $m = [regex]::Match($block, '"' + [regex]::Escape($key) + '":\s*\[(.*?)\]\s*,\s*"image_alt"', 'Singleline')
  if (-not $m.Success) { $m = [regex]::Match($block, '"' + [regex]::Escape($key) + '":\s*\[(.*?)\]\s*,\s*"links"', 'Singleline') }
  if (-not $m.Success) { return @() }
  $pairs = New-Object System.Collections.Generic.List[object]
  foreach ($tm in [regex]::Matches($m.Groups[1].Value, '\("((?:\\.|[^"\\])*)",\s*"((?:\\.|[^"\\])*)"\)')) {
    $pairs.Add(@(($tm.Groups[1].Value -replace '\\"','"'), ($tm.Groups[2].Value -replace '\\"','"')))
  }
  return $pairs.ToArray()
}
function Get-RegionBlurb([string]$id) {
  $pattern = '"' + [regex]::Escape($id) + '":\s*\((.*?)\r?\n\s*\),'
  $m = [regex]::Match($PyText, $pattern, 'Singleline')
  if (-not $m.Success) { return '' }
  $sb = New-Object System.Text.StringBuilder
  foreach ($pm in [regex]::Matches($m.Groups[1].Value, '"((?:\\.|[^"\\])*)"')) {
    [void]$sb.Append(($pm.Groups[1].Value -replace '\\"','"'))
  }
  return $sb.ToString()
}
$REGION_BLURBS = @{ gush-dan = (Get-RegionBlurb 'gush-dan'); sharon = (Get-RegionBlurb 'sharon'); jerusalem = (Get-RegionBlurb 'jerusalem'); north = (Get-RegionBlurb 'north'); south = (Get-RegionBlurb 'south') }
function Get-ServicePages() {
  $files = @('pigeon-spikes.html','bird-netting.html','electric-bird-deterrent.html','solar-panels-protection.html')
  $pages = @()
  foreach ($f in $files) {
    $pattern = '\{\s*"file":\s*"' + [regex]::Escape($f) + '"'
    $start = [regex]::Match($PyText, $pattern).Index
    if ($start -lt 0) { throw "Service block not found: $f" }
    $depth = 0
    for ($i = $start; $i -lt $PyText.Length; $i++) {
      $ch = $PyText[$i]
      if ($ch -eq '{') { $depth++ } elseif ($ch -eq '}') { $depth--; if ($depth -eq 0) { break } }
    }
    $block = $PyText.Substring($start, $i - $start + 1)
    $pages += [pscustomobject]@{ file = (Get-PyString $block 'file'); slug = (Get-PyString $block 'slug'); h1 = (Get-PyString $block 'h1'); title = (Get-PyString $block 'title'); description = (Get-PyString $block 'description'); subtitle = (Get-PyString $block 'subtitle'); service_name = (Get-PyString $block 'service_name'); content = (Get-PyStringList $block 'content'); h2 = (Get-PyString $block 'h2'); process = (Get-PyStringList $block 'process'); faq = (Get-PyTupleList $block 'faq'); image_alt = (Get-PyString $block 'image_alt'); links = (Get-PyTupleList $block 'links') }
  }
  return $pages
}
function Head-Block($title, $description, $canonicalPath, $ogType = 'website') {
  $url = "$DOMAIN$canonicalPath"
  "  <meta charset=`"UTF-8`">`n  <meta name=`"viewport`" content=`"width=device-width, initial-scale=1.0`">`n  <title>$(Esc $title)</title>`n  <meta name=`"description`" content=`"$(Esc $description)`">`n  <meta name=`"robots`" content=`"index, follow`">`n  <meta name=`"theme-color`" content=`"#1d4f8f`">`n  <link rel=`"canonical`" href=`"$url`">`n  <link rel=`"icon`" href=`"favicon.svg`" type=`"image/svg+xml`">`n  <link rel=`"apple-touch-icon`" href=`"images/og-default.svg`">`n  <meta property=`"og:type`" content=`"$ogType`">`n  <meta property=`"og:title`" content=`"$(Esc $title)`">`n  <meta property=`"og:description`" content=`"$(Esc $description)`">`n  <meta property=`"og:url`" content=`"$url`">`n  <meta property=`"og:image`" content=`"$OG_IMAGE`">`n  <meta property=`"og:locale`" content=`"he_IL`">`n  <meta property=`"og:site_name`" content=`"$(Esc $BRAND)`">`n  <link rel=`"preconnect`" href=`"https://fonts.googleapis.com`">`n  <link rel=`"preconnect`" href=`"https://fonts.gstatic.com`" crossorigin>`n  <link href=`"https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600;700;800&display=swap`" rel=`"stylesheet`">`n  <link rel=`"stylesheet`" href=`"styles.css`">"
}
function Site-Header() {
  $nav = [regex]::Match($PyText, 'nav_extra or """<ul>([\s\S]*?)</ul>"""').Groups[1].Value
  "      <div class=`"site-header`">`n        <a href=`"index.html`" class=`"logo`">$BRAND</a>`n        <nav class=`"site-nav`" aria-label=`"ניווט ראשי`">`n          <ul>$nav</ul>`n        </nav>`n        <a class=`"header-cta`" href=`"tel:$PHONE_TEL`">$PHONE_DISPLAY</a>`n      </div>"
}
function Breadcrumbs($items) {
  $parts = @('<nav class="breadcrumbs" aria-label="מיקום בעמוד">')
  for ($i = 0; $i -lt $items.Count; $i++) {
    $label = $items[$i][0]; $href = $items[$i][1]
    if ($i -eq $items.Count - 1) { $parts += "<span aria-current=`"page`">$(Esc $label)</span>" }
    else { $parts += "<a href=`"$href`">$(Esc $label)</a>"; $parts += '<span class="bc-sep" aria-hidden="true">›</span>' }
  }
  $parts += '</nav>'
  $parts -join "`n      "
}
function Json-Ld($obj) { ($obj | ConvertTo-Json -Depth 12 -Compress) }
function Breadcrumb-Schema($items) {
  $elements = @(); $pos = 1
  foreach ($it in $items) { $elements += @{ '@type'='ListItem'; position=$pos; name=$it[0]; item=($(if ($it[1].StartsWith('/')) { "$DOMAIN$($it[1])" } else { $it[1] })) }; $pos++ }
  Json-Ld @{ '@context'='https://schema.org'; '@type'='BreadcrumbList'; itemListElement=$elements }
}
function LocalBusiness-Schema($city, $description) {
  Json-Ld @{ '@context'='https://schema.org'; '@type'='LocalBusiness'; name=$BRAND; description=$description; telephone='+972528805053'; email=$EMAIL; url="$DOMAIN/"; image=$OG_IMAGE; priceRange='$$'; address=@{ '@type'='PostalAddress'; addressCountry='IL' }; areaServed=@{ '@type'='City'; name=$city }; openingHoursSpecification=@{ '@type'='OpeningHoursSpecification'; dayOfWeek=@('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday'); opens='08:00'; closes='20:00' } }
}
function Service-Schema($name, $description, $urlPath) {
  Json-Ld @{ '@context'='https://schema.org'; '@type'='Service'; name=$name; description=$description; provider=@{ '@type'='LocalBusiness'; name=$BRAND; telephone='+972528805053'; url="$DOMAIN/" }; areaServed=@{ '@type'='Country'; name='Israel' }; url="$DOMAIN$urlPath" }
}
function Faq-Schema($questions) {
  $entities = @(); foreach ($qa in $questions) { $entities += @{ '@type'='Question'; name=$qa[0]; acceptedAnswer=@{ '@type'='Answer'; text=$qa[1] } } }
  Json-Ld @{ '@context'='https://schema.org'; '@type'='FAQPage'; mainEntity=$entities }
}
function Faq-Html($questions) {
  $items = ($questions | ForEach-Object { "        <div class=`"faq-item`"><dt>$(Esc $_[0])</dt><dd>$(Esc $_[1])</dd></div>" }) -join "`n"
  "      <h2 class=`"section-title-bar`">שאלות נפוצות</h2>`n      <dl class=`"faq-list`">`n$items`n      </dl>"
}
function Sticky-Bar() {
  $m = [regex]::Match($PyText, 'def sticky_bar\(\)[\s\S]*?return f"""([\s\S]*?)"""')
  if ($m.Success) { return ($m.Groups[1].Value -replace '\{PHONE_TEL\}', $PHONE_TEL) }
  ''
}
function Footer-Block() {
  $m = [regex]::Match($PyText, 'def footer_block\(\)[\s\S]*?return f"""([\s\S]*?)"""')
  if ($m.Success) { return ($m.Groups[1].Value -replace '\{BRAND\}', $BRAND -replace '\{PHONE_TEL\}', $PHONE_TEL -replace '\{PHONE_DISPLAY\}', $PHONE_DISPLAY) }
  ''
}
function Contact-Form([string]$city = '', [string]$service = '') {
  $m = [regex]::Match($PyText, 'def contact_form\([\s\S]*?return f"""([\s\S]*?)"""')
  $tpl = $m.Groups[1].Value
  $tpl = $tpl -replace '\{esc\(city\)\}', (Esc $city) -replace '\{city_val\}', (Esc $city) -replace '\{esc\(service\)\}', (Esc $service)
  if ($service) {
    $tpl = [regex]::Replace($tpl, '\{service_field\}', "<input type=`"hidden`" name=`"service`" value=`"$(Esc $service)`">")
  } else {
    $sf = [regex]::Match($PyText, 'else """([\s\S]*?)"""', [System.Text.RegularExpressions.RegexOptions]::None)
    $tpl = [regex]::Replace($tpl, '\{service_field\}', $sf.Groups[1].Value)
  }
  $tpl
}