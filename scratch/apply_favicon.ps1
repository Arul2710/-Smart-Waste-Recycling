$old = '<link rel="icon" href="assets/icons/recycle.svg" type="image/svg+xml">'
$new = "<link rel=`"icon`" href=`"assets/icons/favicon.ico`" sizes=`"any`">`n    <link rel=`"icon`" href=`"assets/icons/favicon.png`" type=`"image/png`">`n    <link rel=`"apple-touch-icon`" href=`"assets/icons/apple-touch-icon.png`">"

$enc = New-Object System.Text.UTF8Encoding($false)
$results = @()

foreach ($f in Get-ChildItem -Path . -Filter *.html) {
    $text = [System.IO.File]::ReadAllText($f.FullName, $enc)
    $count = ([regex]::Matches($text, [regex]::Escape($old))).Count
    if ($count -eq 0) {
        $results += [pscustomobject]@{ File = $f.Name; Replaced = 0; Status = 'no icon tag found' }
        continue
    }
    $text = $text.Replace($old, $new)
    [System.IO.File]::WriteAllText($f.FullName, $text, $enc)
    $results += [pscustomobject]@{ File = $f.Name; Replaced = $count; Status = 'ok' }
}

$results | Sort-Object File | Format-Table -AutoSize
"total pages updated: " + ($results | Where-Object { $_.Status -eq 'ok' }).Count
"total replacements: " + ($results | Measure-Object -Property Replaced -Sum).Sum
