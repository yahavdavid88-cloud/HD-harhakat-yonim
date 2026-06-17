$ErrorActionPreference = "Stop"
$path = Join-Path $PSScriptRoot "cities.json"
$c = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)

$replacements = @{
    '"name": "גush דan והמרכז"' = '"name": "גוש דאן והמרכז"'
    'בזיכרון יעakov' = 'בזיכרון יעakov'
    '"name": "פרdס חanna"' = '"name": "פרdס חanna"'
    'בפרdס חanna' = 'בפרdס חanna'
    '"name": "בית שmesh"' = '"name": "בית שmesh"'
    'בבית שmesh' = 'בבית שmesh'
    '"name": "כרמiel"' = '"name": "כרמיאל"'
    'בכרמiel' = 'בכרמיאל'
    '"name": "קריית שmona"' = '"name": "קריית שmona"'
    'בקריית שmona' = 'בקריית שmona'
    '"name": "אשkelon"' = '"name": "אשקלון"'
    'באשkelon' = 'באשקלון'
    '"name": "אשdod"' = '"name": "אשדוד"'
    'באשdod' = 'באשדוד'
    '"name": "קריית גat"' = '"name": "קריית גat"'
    'בקריית גat' = 'בקריית גat'
    '"name": "אילat"' = '"name": "אילat"'
    'באילat' = 'באילat'
    '"name": "קריית מalakhi"' = '"name": "קריית מalakhi"'
    'בקריית מalakhi' = 'בקריית מalakhi'
}

# Build correct strings from Unicode code points
$pardesHanna = -join @([char]0x05E4,[char]0x05E8,[char]0x05D3,[char]0x05E1,' ',[char]0x05D7,[char]0x05E0,[char]0x05D4)
$beitShemesh = -join @([char]0x05D1,[char]0x05D9,[char]0x05EA,' ',[char]0x05E9,[char]0x05DE,[char]0x05E9)
$karmiel = -join @([char]0x05DB,[char]0x05E8,[char]0x05DE,[char]0x05D9,[char]0x05D0,[char]0x05DC)
$kiryatShmona = -join @([char]0x05E7,[char]0x05E8,[char]0x05D9,[char]0x05D9,[char]0x05EA,' ',[char]0x05E9,[char]0x05DE,[char]0x05D5,[char]0x05E0,[char]0x05D4)
$ashkelon = -join @([char]0x05D0,[char]0x05E9,[char]0x05E7,[char]0x05DC,[char]0x05D5,[char]0x05DF)
$ashdod = -join @([char]0x05D0,[char]0x05E9,[char]0x05D3,[char]0x05D5,[char]0x05D3)
$kiryatGat = -join @([char]0x05E7,[char]0x05E8,[char]0x05D9,[char]0x05D9,[char]0x05EA,' ',[char]0x05D2,[char]0x05EA)
$eilat = -join @([char]0x05D0,[char]0x05D9,[char]0x05DC,[char]0x05EA)
$kiryatMalakhi = -join @([char]0x05E7,[char]0x05E8,[char]0x05D9,[char]0x05D9,[char]0x05EA,' ',[char]0x05DE,[char]0x05DC,[char]0x05D0,[char]0x05DB,[char]0x05D9)
$gushDan = -join @([char]0x05D2,[char]0x05D5,[char]0x05E9,' ',[char]0x05D3,[char]0x05D0,[char]0x05DF,' ',[char]0x05D5,[char]0x05D4,[char]0x05DE,[char]0x05E8,[char]0x05DB,[char]0x05D6)
$yaakov = -join @([char]0x05D9,[char]0x05E2,[char]0x05E7,[char]0x05D5,[char]0x05D1)

$map = @(
    @('פרdס חanna', $pardesHanna),
    @('בפרdס חanna', "ב$pardesHanna"),
    @('בית שmesh', $beitShemesh),
    @('בבית שmesh', "ב$beitShemesh"),
    @('כרמiel', $karmiel),
    @('בכרמiel', "ב$karmiel"),
    @('קריית שmona', $kiryatShmona),
    @('בקריית שmona', "ב$kiryatShmona"),
    @('אשkelon', $ashkelon),
    @('באשkelon', "ב$ashkelon"),
    @('אשdod', $ashdod),
    @('באשdod', "ב$ashdod"),
    @('קריית גat', $kiryatGat),
    @('בקריית גat', "ב$kiryatGat"),
    @('אילat', $eilat),
    @('באילat', "ב$eilat"),
    @('קריית מalakhi', $kiryatMalakhi),
    @('בקריית מalakhi', "ב$kiryatMalakhi"),
    @('גush דan והמרכז', $gushDan),
    @('יעakov', $yaakov)
)

foreach ($pair in $map) {
    $c = $c.Replace($pair[0], $pair[1])
}

[System.IO.File]::WriteAllText($path, $c, [System.Text.UTF8Encoding]::new($false))
Write-Host "Fixed $($map.Count) patterns in cities.json"
