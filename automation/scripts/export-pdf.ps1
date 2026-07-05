$projectRoot = 'C:\ProjectsAOC\FlowOpsAI'

$productName = 'workday-acceleration-system'

$productPath = Join-Path $projectRoot 'products'
$productPath = Join-Path $productPath $productName

$guidePath = Join-Path $productPath '01-master-guide'

$assetsPath = Join-Path $productPath '05-assets'
$stylesPath = Join-Path $assetsPath 'styles'

$styledGuide = Join-Path $guidePath 'MASTER-GUIDE-STYLED.md'

$htmlTemplate = Join-Path $stylesPath 'flowops-template.html'
$cssFile = Join-Path $stylesPath 'flowops-premium.css'

$htmlOutput = Join-Path $productPath '06-export\MASTER-GUIDE.html'

$pdfOutput = Join-Path $productPath '06-export\FlowOpsAI-Workday-Acceleration-System.pdf'

$wkhtmltopdf = 'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

if (!(Test-Path $styledGuide)) {
    Write-Host 'MASTER-GUIDE-STYLED.md not found.'
    exit
}

if (!(Test-Path $wkhtmltopdf)) {
    Write-Host 'wkhtmltopdf not found.'
    exit
}

Write-Host 'Generating premium HTML...'

pandoc `
$styledGuide `
-f markdown `
-t html5 `
--standalone `
--css $cssFile `
--template $htmlTemplate `
-o $htmlOutput

if (!(Test-Path $htmlOutput)) {
    Write-Host 'HTML generation failed.'
    exit
}

$htmlOutputFixed = $htmlOutput.Replace('\', '/')
$htmlUri = 'file:///' + $htmlOutputFixed

Write-Host 'Generating premium PDF...'

& $wkhtmltopdf --enable-local-file-access --encoding utf-8 --page-size A4 --margin-top 30 --margin-bottom 25 --margin-left 25 --margin-right 20 --disable-smart-shrinking $htmlUri $pdfOutput

Write-Host ''
Write-Host 'Premium PDF exported successfully.'
Write-Host $pdfOutput