$projectRoot = 'C:\ProjectsAOC\FlowOpsAI'

$productName = 'workday-acceleration-system'

$productPath = Join-Path $projectRoot 'products'
$productPath = Join-Path $productPath $productName

$guidePath = Join-Path $productPath '01-master-guide'

$masterGuide = Join-Path $guidePath 'MASTER-GUIDE.md'

$styledGuide = Join-Path $guidePath 'MASTER-GUIDE-STYLED.md'

if (!(Test-Path $masterGuide)) {
Write-Host 'MASTER-GUIDE.md not found.'
exit
}

Write-Host 'Applying FlowOps visual styling...'

$content = Get-Content -Path $masterGuide -Raw -Encoding UTF8

$content = $content.Replace(
'# Excel & Reporting',
'# <span class=''hero hero-analytics''>Excel & Reporting</span>'
)

$content = $content.Replace(
'# Technical Documentation',
'# <span class=''hero hero-documentation''>Technical Documentation</span>'
)

$content = $content.Replace(
'# Troubleshooting & IT Analysis',
'# <span class=''hero hero-troubleshooting''>Troubleshooting & IT Analysis</span>'
)

$content = $content.Replace(
'# Project Management',
'# <span class=''hero hero-workflow''>Project Management</span>'
)

$content = $content.Replace(
'# Business Productivity',
'# <span class=''hero hero-productivity''>Business Productivity</span>'
)

$content = $content.Replace(
'# Best Practices',
'# <span class=''hero hero-bestpractices''>Best Practices</span>'
)

$content = $content.Replace(
'# Next Steps',
'# <span class=''hero hero-roadmap''>Next Steps</span>'
)

Set-Content -Path $styledGuide -Value $content -Encoding UTF8

Write-Host ''
Write-Host 'Styled guide generated successfully.'
Write-Host $styledGuide
