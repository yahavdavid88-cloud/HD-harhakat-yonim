$ErrorActionPreference = "Stop"
$path = Join-Path $PSScriptRoot "cities.json"
$c = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)

$ashdod = -join @([char]0x05D0,[char]0x05E9,[char]0x05D3,[char]0x05D5,[char]0x05D3)
$kiryatGat = -join @([char]0x05E7,[char]0x05E8,[char]0x05D9,[char]0x05D9,[char]0x05EA,' ',[char]0x05D2,[char]0x05EA)
$eilat = -join @([char]0x05D0,[char]0x05D9,[char]0x05DC,[char]0x05EA)
$kiryatMalakhi = -join @([char]0x05E7,[char]0x05E8,[char]0x05D9,[char]0x05D9,[char]0x05EA,' ',[char]0x05DE,[char]0x05DC,[char]0x05D0,[char]0x05DB,[char]0x05D9)
$bet = [char]0x05D1

$badAshdod = -join @([char]0x05D0,[char]0x05E9,'dod')
$badGat = -join @([char]0x05E7,[char]0x05E8,[char]0x05D9,[char]0x05D9,[char]0x05EA,' ',[char]0x05D2,'at')
$badEilat = -join @([char]0x05D0,[char]0x05D9,[char]0x05DC,'at')
$badMalakhi = -join @([char]0x05E7,[char]0x05E8,[char]0x05D9,[char]0x05D9,[char]0x05EA,' ',[char]0x05DE,'alakhi')

$c = $c.Replace($badAshdod, $ashdod)
$c = $c.Replace($bet + $badAshdod, $bet + $ashdod)
$c = $c.Replace($badGat, $kiryatGat)
$c = $c.Replace($bet + $badGat, $bet + $kiryatGat)
$c = $c.Replace($badEilat, $eilat)
$c = $c.Replace($bet + $badEilat, $bet + $eilat)
$c = $c.Replace($badMalakhi, $kiryatMalakhi)
$c = $c.Replace($bet + $badMalakhi, $bet + $kiryatMalakhi)

[System.IO.File]::WriteAllText($path, $c, [System.Text.UTF8Encoding]::new($false))
Write-Host "Fixed remaining city names"
