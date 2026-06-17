$Base = $PSScriptRoot
$fixes = @{
    ([string][char]0x05D3 + "an") = -join @([char]0x05D3,[char]0x05D0,[char]0x05DF)
    ("בק" + "adima") = -join @([char]0x05D1,[char]0x05E7,[char]0x05D3,[char]0x05D9,[char]0x05DE,[char]0x05D4)
    ([string][char]0x05E9 + "mesh") = -join @([char]0x05E9,[char]0x05DE,[char]0x05E9)
    ("מבשר" + "et") = -join @([char]0x05DE,[char]0x05D1,[char]0x05E9,[char]0x05E8,[char]0x05EA)
    ([string][char]0x05D2 + "ivat") = -join @([char]0x05D2,[char]0x05D1,[char]0x05E2,[char]0x05EA)
    (" ע" + "ilit") = " " + (-join @([char]0x05E2,[char]0x05DC,[char]0x05D9,[char]0x05EA))
    ("מודיע" + "in") = -join @([char]0x05DE,[char]0x05D5,[char]0x05D3,[char]0x05D9,[char]0x05E2,[char]0x05D9,[char]0x05DF)
    ([string][char]0x05E2 + "כo") = -join @([char]0x05E2,[char]0x05DB,[char]0x05D5)
    ("טיר" + "at הכ" + "armel") = (-join @([char]0x05D8,[char]0x05D9,[char]0x05E8,[char]0x05EA)) + " " + (-join @([char]0x05D4,[char]0x05DB,[char]0x05E8,[char]0x05DE,[char]0x05DC))
    ([string][char]0x05D9 + "okneam") = -join @([char]0x05D9,[char]0x05D5,[char]0x05E7,[char]0x05E0,[char]0x05E2,[char]0x05DD)
    ("כרמ" + "iel") = -join @([char]0x05DB,[char]0x05E8,[char]0x05DE,[char]0x05D9,[char]0x05D0,[char]0x05DC)
    ("מעל" + "ot") = -join @([char]0x05DE,[char]0x05E2,[char]0x05DC,[char]0x05D5,[char]0x05EA)
    (" פ" + "ina") = " " + (-join @([char]0x05E4,[char]0x05D9,[char]0x05E0,[char]0x05D4))
    (" ש" + "mona") = " " + (-join @([char]0x05E9,[char]0x05DE,[char]0x05D5,[char]0x05E0,[char]0x05D4))
    ("מגד" + "al הע" + "emek") = (-join @([char]0x05DE,[char]0x05D2,[char]0x05D3,[char]0x05DC)) + " " + (-join @([char]0x05D4,[char]0x05E2,[char]0x05DE,[char]0x05E7))
    ("אשק" + "elon") = -join @([char]0x05D0,[char]0x05E9,[char]0x05E7,[char]0x05DC,[char]0x05D5,[char]0x05DF)
    ("אשד" + "od") = -join @([char]0x05D0,[char]0x05E9,[char]0x05D3,[char]0x05D5,[char]0x05D3)
    (" ג" + "at") = " " + (-join @([char]0x05D2,[char]0x05EA))
    ("איל" + "at") = -join @([char]0x05D0,[char]0x05D9,[char]0x05DC,[char]0x05EA)
    ("דימ" + "ona") = -join @([char]0x05D3,[char]0x05D9,[char]0x05DE,[char]0x05D5,[char]0x05E0,[char]0x05D4)
    ("ער" + "ad") = -join @([char]0x05E2,[char]0x05E8,[char]0x05D3)
    ("ש" + "derot") = -join @([char]0x05E9,[char]0x05D3,[char]0x05E8,[char]0x05D5,[char]0x05EA)
    ("א" + "ofakim") = -join @([char]0x05D0,[char]0x05D5,[char]0x05E4,[char]0x05E7,[char]0x05D9,[char]0x05DD)
    ("נתיב" + "ot") = -join @([char]0x05E0,[char]0x05EA,[char]0x05D9,[char]0x05D1,[char]0x05D5,[char]0x05EA)
    (" מ" + "alakhi") = " " + (-join @([char]0x05DE,[char]0x05DC,[char]0x05D0,[char]0x05DB,[char]0x05D9))
    ("ע" + "omer") = -join @([char]0x05E2,[char]0x05DE,[char]0x05E8)
    ("ש" + "oham") = -join @([char]0x05E9,[char]0x05D5,[char]0x05D4,[char]0x05DD)
    (" ד" + "agan") = " " + (-join @([char]0x05D3,[char]0x05D2,[char]0x05DF))
    ("פרד" + "es ח" + "anna") = (-join @([char]0x05E4,[char]0x05E8,[char]0x05D3,[char]0x05E1)) + " " + (-join @([char]0x05D7,[char]0x05E0,[char]0x05D4))
}
$count = 0
Get-ChildItem (Join-Path $Base "*.html") | ForEach-Object {
    $t = [System.IO.File]::ReadAllText($_.FullName, [System.Text.UTF8Encoding]::new($false))
    $orig = $t
    foreach ($k in $fixes.Keys) { $t = $t.Replace($k, $fixes[$k]) }
    if ($t -ne $orig) {
        [System.IO.File]::WriteAllText($_.FullName, $t, [System.Text.UTF8Encoding]::new($false))
        $count++
    }
}
Write-Host "Fixed $count html files"
