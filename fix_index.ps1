$path = Join-Path $PSScriptRoot "index.html"
$c = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)
$ashdod = -join @([char]0x05D0,[char]0x05E9,[char]0x05D3,[char]0x05D5,[char]0x05D3)
$ashkelon = -join @([char]0x05D0,[char]0x05E9,[char]0x05E7,[char]0x05DC,[char]0x05D5,[char]0x05DF)
$eilat = -join @([char]0x05D0,[char]0x05D9,[char]0x05DC,[char]0x05EA)
$kiryatGat = -join @([char]0x05E7,[char]0x05E8,[char]0x05D9,[char]0x05D9,[char]0x05EA,' ',[char]0x05D2,[char]0x05EA)
$c = $c.Replace(-join @([char]0x05D0,[char]0x05E9,'dod'), $ashdod)
$c = $c.Replace(-join @([char]0x05D0,[char]0x05E9,'kelon'), $ashkelon)
$c = $c.Replace(-join @([char]0x05D0,[char]0x05D9,[char]0x05DC,'at'), $eilat)
$c = $c.Replace(-join @([char]0x05E7,[char]0x05E8,[char]0x05D9,[char]0x05D9,[char]0x05EA,' ',[char]0x05D2,'at'), $kiryatGat)
[System.IO.File]::WriteAllText($path, $c, [System.Text.UTF8Encoding]::new($false))
Write-Host "Fixed index.html"
