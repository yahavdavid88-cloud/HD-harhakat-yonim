$ErrorActionPreference="Stop"; Add-Type -AssemblyName System.Web; $Base=$PSScriptRoot; $U8=[Text.UTF8Encoding]::new($false); function WFile($p,$c){[IO.File]::WriteAllText($p,$c,$U8)}; function Esc($t){[Web.HttpUtility]::HtmlEncode([string]$t)}
$Py=[IO.File]::ReadAllText((Join-Path $Base "generate_seo.py"),$U8)
$DOMAIN=[regex]::Match($Py,'DOMAIN = "([^"]+)"').Groups[1].Value
$BRAND=[regex]::Match($Py,'BRAND = "([^"]+)"').Groups[1].Value
$PHONE_DISPLAY=[regex]::Match($Py,'PHONE_DISPLAY = "([^"]+)"').Groups[1].Value
$PHONE_TEL=[regex]::Match($Py,'PHONE_TEL = "([^"]+)"').Groups[1].Value
$EMAIL=[regex]::Match($Py,'EMAIL = "([^"]+)"').Groups[1].Value
$OG_IMAGE="$DOMAIN/images/og-default.svg"
$LASTMOD=(Get-Date).ToString("yyyy-MM-dd")
function Head($title,$desc,$path){$u="$DOMAIN$path";"  <meta charset=`"UTF-8`">`n  <meta name=`"viewport`" content=`"width=device-width, initial-scale=1.0`">`n  <title>$(Esc $title)</title>`n  <meta name=`"description`" content=`"$(Esc $desc)`">`n  <meta name=`"robots`" content=`"index, follow`">`n  <meta name=`"theme-color`" content=`"#1d4f8f`">`n  <link rel=`"canonical`" href=`"$u`">`n  <link rel=`"icon`" href=`"favicon.svg`" type=`"image/svg+xml`">`n  <link rel=`"apple-touch-icon`" href=`"images/og-default.svg`">`n  <meta property=`"og:type`" content=`"website`">`n  <meta property=`"og:title`" content=`"$(Esc $title)`">`n  <meta property=`"og:description`" content=`"$(Esc $desc)`">`n  <meta property=`"og:url`" content=`"$u`">`n  <meta property=`"og:image`" content=`"$OG_IMAGE`">`n  <meta property=`"og:locale`" content=`"he_IL`">`n  <meta property=`"og:site_name`" content=`"$(Esc $BRAND)`">`n  <link rel=`"preconnect`" href=`"https://fonts.googleapis.com`">`n  <link rel=`"preconnect`" href=`"https://fonts.gstatic.com`" crossorigin>`n  <link href=`"https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;600;700;800&display=swap`" rel=`"stylesheet`">`n  <link rel=`"stylesheet`" href=`"styles.css`">"}
function SiteHeader(){ $nav=[regex]::Match($Py,'nav_extra or """<ul>([\s\S]*?)</ul>"""').Groups[1].Value; $al=[regex]::Match($Py,'site-nav" aria-label="([^"]+)"').Groups[1].Value; "      <div class=`"site-header`">`n        <a href=`"index.html`" class=`"logo`">$BRAND</a>`n        <nav class=`"site-nav`" aria-label=`"$al`">`n          <ul>$nav</ul>`n        </nav>`n        <a class=`"header-cta`" href=`"tel:$PHONE_TEL`">$PHONE_DISPLAY</a>`n      </div>" }
function Breadcrumbs($items){$al=[regex]::Match($Py,'class="breadcrumbs" aria-label="([^"]+)"').Groups[1].Value;$sep=[char]0x203A;$p=@("<nav class=`"breadcrumbs`" aria-label=`"$al`">");for($i=0;$i -lt $items.Count;$i++){if($i -gt 0){$p+="<span class=`"bc-sep`" aria-hidden=`"true`">$sep</span>"};if($i -eq $items.Count-1){$p+="<span aria-current=`"page`">$(Esc $items[$i][0])</span>"}else{$p+="<a href=`"$($items[$i][1])`">$(Esc $items[$i][0])</a>"}};$p+='</nav>'; $p -join "`n      "}
function JL($o){$o|ConvertTo-Json -Depth 12 -Compress}
function BcSchema($items){$el=@();$pos=1;foreach($it in $items){$el+=@{ '@type'='ListItem';position=$pos;name=$it[0];item=$(if($it[1].StartsWith('/')){"$DOMAIN$($it[1])"}else{$it[1]})};$pos++}; JL @{ '@context'='https://schema.org';'@type'='BreadcrumbList';itemListElement=$el}}
function LbSchema($city,$desc){JL @{ '@context'='https://schema.org';'@type'='LocalBusiness';name=$BRAND;description=$desc;telephone='+972528805053';email=$EMAIL;url="$DOMAIN/";image=$OG_IMAGE;priceRange='$$';address=@{ '@type'='PostalAddress';addressCountry='IL'};areaServed=@{ '@type'='City';name=$city};openingHoursSpecification=@{ '@type'='OpeningHoursSpecification';dayOfWeek=@('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday');opens='08:00';closes='20:00'}}}
function SvcSchema($n,$d,$p){JL @{ '@context'='https://schema.org';'@type'='Service';name=$n;description=$d;provider=@{ '@type'='LocalBusiness';name=$BRAND;telephone='+972528805053';url="$DOMAIN/"};areaServed=@{ '@type'='Country';name='Israel'};url="$DOMAIN$p"}}
function FaqSchema($qa){$e=@();foreach($q in $qa){$e+=@{ '@type'='Question';name=$q[0];acceptedAnswer=@{ '@type'='Answer';text=$q[1]}}}; JL @{ '@context'='https://schema.org';'@type'='FAQPage';mainEntity=$e}}
function FaqHtml($qa){$t=[regex]::Match($Py,'class="section-title-bar">([^<]+)</h2>\s*\n\s*<dl class="faq-list"').Groups[1].Value;$it=($qa|%{ "        <div class=`"faq-item`"><dt>$(Esc $_[0])</dt><dd>$(Esc $_[1])</dd></div>"})-join "`n";"      <h2 class=`"section-title-bar`">$t</h2>`n      <dl class=`"faq-list`">`n$it`n      </dl>"}
function Sticky(){([regex]::Match($Py,'def sticky_bar\(\) -> str:\s*return f"""([\s\S]*?)"""').Groups[1].Value)-replace '\{PHONE_TEL\}',$PHONE_TEL}
function Footer(){([regex]::Match($Py,'def footer_block\(\) -> str:\s*return f"""([\s\S]*?)"""').Groups[1].Value)-replace '\{BRAND\}',$BRAND -replace '\{PHONE_TEL\}',$PHONE_TEL -replace '\{PHONE_DISPLAY\}',$PHONE_DISPLAY}
function ContactForm($city,$service){$tpl=([regex]::Match($Py,'def contact_form\([\s\S]*?return f"""([\s\S]*?)"""').Groups[1].Value);$tpl=$tpl-replace '\{esc\(city\)\}',(Esc $city)-replace '\{city_val\}',(Esc $city);if($service){$sf="<input type=`"hidden`" name=`"service`" value=`"$(Esc $service)`">"}else{$sf=[regex]::Match($Py,'else """([\s\S]*?)"""').Groups[1].Value}; $tpl-replace '\{service_field\}',$sf-replace '\{esc\(service\)\}',(Esc $service)}
function PyCat($inner){$sb=New-Object Text.StringBuilder;foreach($pm in [regex]::Matches($inner,'"(?:\\.|[^"\\])*"')){[void]$sb.Append(($pm.Value.Trim('"')-replace '\\"','"'))};$sb.ToString()}
function GetBlurb($id){$m=[regex]::Match($Py,'"'+[regex]::Escape($id)+'":\s*\((.*?)\r?\n\s*\),','Singleline'); if($m.Success){PyCat $m.Groups[1].Value}else{''}}
$BLURBS=@{}; foreach($id in @('gush-dan','sharon','jerusalem','north','south')){$BLURBS[$id]=GetBlurb $id}
function CityMeta($city,$text){$b=$text.Trim();$s=[regex]::Match($Py,'if len\(base\) < 120:\s*base \+= f"([^"]+)"').Groups[1].Value;$s=$s-replace '\{city\}',$city;if($b.Length -lt 120){$b+=$s};if($b.Length -gt 160){$t=$b.Substring(0,157);$sp=$t.LastIndexOf(' ');if($sp -gt 80){$t=$t.Substring(0,$sp)};$b=$t+[char]0x2026};$b}
function CityFaq($name){$blk=[regex]::Match($Py,'def render_city_page[\s\S]*?faq = \[([\s\S]*?)\]\s*\n\s*bc_html').Groups[1].Value;$o=@();foreach($tm in [regex]::Matches($blk,'\(f?"((?:\\.|[^"\\])*)",\s*"((?:\\.|[^"\\])*)"\)')){$o+=,@(($tm.Groups[1].Value-replace '\\"','"'-replace '\{name\}',$name),($tm.Groups[2].Value-replace '\\"','"'))};$o}
function Nearby($cities,$cur){$links=@();foreach($c in $cities){if($c.file-eq $cur){continue};$links+="<a href=`"$($c.file)`">$(Esc $c.name)</a>";if($links.Count-ge 5){break}};if(-not $links.Count){return ''};$h=[regex]::Match($Py,"nearby_cities_html[\s\S]*?return \(\s*'([^']+)'").Groups[1].Value;"      <h3>$h</h3>`n      <nav class=`"city-links`" aria-label=`"$h`">`n        $($links-join "`n        ")`n      </nav>"}
$cityTpl=[regex]::Match($Py,'def render_city_page[\s\S]*?return f"""([\s\S]*?)"""').Groups[1].Value
$svcTpl=[regex]::Match($Py,'def render_service_page[\s\S]*?return f"""([\s\S]*?)"""').Groups[1].Value
$areasTpl=[regex]::Match($Py,'def render_areas_page[\s\S]*?return f"""([\s\S]*?)"""').Groups[1].Value
function RenderCity($city,$rn,$rid,$rc){
  $name=$city.name;$file=$city.file;$text=$city.text;$path="/$file"
  $titleTpl=[regex]::Match($Py,'title = f"((?:\\.|[^"\\])*)"').Groups[1].Value
  $title=$titleTpl.Replace('{name}',$name).Replace('{BRAND}',$BRAND)
  $desc=CityMeta $name $text;$rb=$BLURBS[$rid];$faq=CityFaq $name;$near=Nearby $rc $file
  $bch=@(@([regex]::Match($Py,'bc_html = \[\("([^"]+)"').Groups[1].Value,'index.html'),@([regex]::Match($Py,', \("([^"]+)", "areas.html"\)').Groups[1].Value,'areas.html'),@($name,$file))
  $bcs=@(@($bch[0][0],'/'),@($bch[1][0],'/areas.html'),@($name,$path))
  $h=$cityTpl
  $h=$h.Replace('{head_block(title, description, path)}',(Head $title $desc $path))
  $h=$h.Replace('{site_header()}',(SiteHeader))
  $h=$h.Replace('{breadcrumbs(bc_html)}',(Breadcrumbs $bch))
  $h=$h.Replace('{esc(region_name)}',(Esc $rn)).Replace('{esc(name)}',(Esc $name)).Replace('{esc(text)}',(Esc $text)).Replace('{esc(region_blurb)}',(Esc $rb))
  $h=$h.Replace('{PHONE_TEL}',$PHONE_TEL).Replace('{PHONE_DISPLAY}',$PHONE_DISPLAY).Replace('{BRAND}',$BRAND)
  $h=$h.Replace('{nearby}',$near).Replace('{faq_html(faq)}',(FaqHtml $faq)).Replace('{contact_form(city=name)}',(ContactForm $name ''))
  $h=$h.Replace('{footer_block()}',(Footer)).Replace('{sticky_bar()}',(Sticky))
  $h=$h.Replace('{breadcrumb_schema(bc_schema)}',(BcSchema $bcs)).Replace('{local_business_schema(name, description)}',(LbSchema $name $desc)).Replace('{faq_schema(faq)}',(FaqSchema $faq))
  $h
}
function GetPyStr($b,$k){$m=[regex]::Match($b,'"'+[regex]::Escape($k)+'":\s*"((?:\\.|[^"\\])*)"');($m.Groups[1].Value-replace '\\"','"')}
function GetPyList($b,$k){$m=[regex]::Match($b,'"'+[regex]::Escape($k)+'":\s*\[(.*?)\]','Singleline');$a=@();foreach($pm in [regex]::Matches($m.Groups[1].Value,'"((?:\\.|[^"\\])*)"')){$a+=($pm.Groups[1].Value-replace '\\"','"')};$a}
function GetPyPairs($b,$k){$m=[regex]::Match($b,'"'+[regex]::Escape($k)+'":\s*\[(.*?)\]\s*,\s*"image_alt"','Singleline');$p=@();foreach($tm in [regex]::Matches($m.Groups[1].Value,'\("((?:\\.|[^"\\])*)",\s*"((?:\\.|[^"\\])*)"\)')){$p+=,@(($tm.Groups[1].Value-replace '\\"','"'),($tm.Groups[2].Value-replace '\\"','"'))};$p}
function GetSvc($f){$st=[regex]::Match($Py,'\{\s*"file":\s*"'+[regex]::Escape($f)+'"').Index;$d=0;for($i=$st;$i -lt $Py.Length;$i++){if($Py[$i]-eq '{'){$d++}elseif($Py[$i]-eq '}'){$d--;if($d-eq 0){break}}};$b=$Py.Substring($st,$i-$st+1);[pscustomobject]@{file=$f;slug=GetPyStr $b 'slug';h1=GetPyStr $b 'h1';title=GetPyStr $b 'title';description=GetPyStr $b 'description';subtitle=GetPyStr $b 'subtitle';service_name=GetPyStr $b 'service_name';content=(GetPyList $b 'content');h2=GetPyStr $b 'h2';process=(GetPyList $b 'process');faq=(GetPyPairs $b 'faq');image_alt=GetPyStr $b 'image_alt';links=(GetPyPairs $b 'links')}}
function RenderSvc($svc){
  $path=$svc.slug
  $bch=@(@([regex]::Match($Py,'bc_html = \[\("([^"]+)"').Groups[1].Value,'index.html'),@('שירותים','index.html#services'),@($svc.h1,$svc.file))
  $bcs=@(@($bch[0][0],'/'),@('שירותים','/#services'),@($svc.h1,$path))
  $lh=($svc.links|%{ "<a href=`"$($_[0])`">$(Esc $_[1])</a>"})-join ' · '
  $ph=($svc.process|%{ "            <li>$(Esc $_)</li>"})-join "`n"
  $ch=($svc.content|%{ "<p>$(Esc $_)</p>"})-join "`n          "
  $h=$svcTpl
  $h=$h.Replace('{head_block(svc["title"], svc["description"], path)}',(Head $svc.title $svc.description $path))
  $h=$h.Replace('{site_header()}',(SiteHeader)).Replace('{breadcrumbs(bc_html)}',(Breadcrumbs $bch))
  $h=$h.Replace('{esc(svc["h1"])}',(Esc $svc.h1)).Replace('{esc(svc["subtitle"])}',(Esc $svc.subtitle)).Replace('{esc(svc["h2"])}',(Esc $svc.h2))
  $h=$h.Replace('{content_html}',$ch).Replace('{process_html}',$ph).Replace('{links_html}',$lh).Replace('{esc(svc["image_alt"])}',(Esc $svc.image_alt))
  $h=$h.Replace('{faq_html(svc["faq"])}',(FaqHtml $svc.faq)).Replace('{contact_form(service=svc["service_name"])}',(ContactForm '' $svc.service_name))
  $h=$h.Replace('{footer_block()}',(Footer)).Replace('{sticky_bar()}',(Sticky))
  $h=$h.Replace('{breadcrumb_schema(bc_schema)}',(BcSchema $bcs)).Replace('{service_schema(svc["service_name"], svc["description"], path)}',(SvcSchema $svc.service_name $svc.description $path))
  $h=$h.Replace('{faq_schema(svc["faq"])}',(FaqSchema $svc.faq)).Replace('{PHONE_TEL}',$PHONE_TEL)
  $h
}
function RenderAreas($regions){
  $title=([regex]::Match($Py,'def render_areas_page[\s\S]*?title = f"([^"]+)"').Groups[1].Value).Replace('{BRAND}',$BRAND)
  $desc=([regex]::Match($Py,'def render_areas_page[\s\S]*?description = \(\s*"([^"]+)"').Groups[1].Value)
  $secs=@(); foreach($r in $regions){$ln=($r.cities|%{ "            <a href=`"$($_.file)`">$(Esc $_.name)</a>"})-join "`n";$secs+="    <section class=`"container section region-block`">`n      <h2 class=`"section-title-bar`">$(Esc $r.name)</h2>`n      <nav class=`"city-links`" aria-label=`"$(Esc $r.name)`">`n$ln`n      </nav>`n    </section>"}
  $h=$areasTpl
  $h=$h.Replace('{head_block(title, description, path)}',(Head $title $desc '/areas.html'))
  $h=$h.Replace('{site_header()}',(SiteHeader)).Replace('{breadcrumbs(bc_html)}',(Breadcrumbs @(@([regex]::Match($Py,'bc_html = \[\("([^"]+)"').Groups[1].Value,'index.html'),@('כל האזורים והערים','areas.html'))))
  $h=$h.Replace('{chr(10).join(sections)}',($secs-join "`n")).Replace('{footer_block()}',(Footer)).Replace('{sticky_bar()}',(Sticky))
  $h=$h.Replace('{breadcrumb_schema(bc_schema)}',(BcSchema @(@([regex]::Match($Py,'bc_html = \[\("([^"]+)"').Groups[1].Value,'/'),@('כל האזורים והערים','/areas.html')))).Replace('{BRAND}',$BRAND)
  $h
}
$data=Get-Content (Join-Path $Base 'cities.json') -Raw -Encoding UTF8|ConvertFrom-Json
$cityCount=0;$urls=@(@('/','1.0'),@('/areas.html','0.9'))
foreach($f in @('pigeon-spikes.html','bird-netting.html','electric-bird-deterrent.html','solar-panels-protection.html')){$svc=GetSvc $f;WFile (Join-Path $Base $f)(RenderSvc $svc);$urls+=,@($svc.slug,'0.9')}
foreach($region in $data.regions){foreach($city in $region.cities){WFile (Join-Path $Base $city.file)(RenderCity $city $region.name $region.id $region.cities);$urls+=,@("/$($city.file)",'0.8');$cityCount++}}
WFile (Join-Path $Base 'areas.html')(RenderAreas $data.regions)
$xml=@('<?xml version="1.0" encoding="UTF-8"?>','<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'); foreach($u in $urls){$xml+="  <url>";$xml+="    <loc>$DOMAIN$($u[0])</loc>";$xml+="    <lastmod>$LASTMOD</lastmod>";$xml+="    <changefreq>weekly</changefreq>";$xml+="    <priority>$($u[1])</priority>";$xml+="  </url>"}; $xml+='</urlset>'; WFile (Join-Path $Base 'sitemap.xml') (($xml-join "`n")+"`n")
$total=$cityCount+4+2
Write-Output "Generated $cityCount city pages, 4 service pages, areas.html, sitemap.xml (total $total files)"
