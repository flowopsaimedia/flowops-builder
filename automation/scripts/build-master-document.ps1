$projectRoot = 'C:\ProjectsAOC\FlowOpsAI'

$productName = 'workday-acceleration-system'

$guidePath = Join-Path $projectRoot 'products'
$guidePath = Join-Path $guidePath $productName
$guidePath = Join-Path $guidePath '01-master-guide'

$outputFile = Join-Path $guidePath 'MASTER-GUIDE.md'

$files = @(
'00-cover.md',
'01-introduction.md',
'02-how-to-use-ai-effectively.md',
'03-excel-reporting.md',
'04-technical-documentation.md',
'05-troubleshooting-it.md',
'06-project-management.md',
'07-business-productivity.md',
'08-best-practices.md',
'09-next-steps.md'
)

$compiledContent = @()

foreach ($file in $files) {


$filePath = Join-Path $guidePath $file

if (Test-Path $filePath) {

    Write-Host 'Reading:'
    Write-Host $file

    $content = Get-Content -Path $filePath

    $compiledContent += $content
    $compiledContent += ''
    $compiledContent += '---'
    $compiledContent += ''
}


}

Set-Content -Path $outputFile -Value $compiledContent -Encoding UTF8

Write-Host ''
Write-Host 'MASTER-GUIDE.md generated successfully.'