param(
[string]$ProductName
)

if ([string]::IsNullOrWhiteSpace($ProductName)) {
Write-Host ""
Write-Host "❌ ProductName is required."
Write-Host ""
exit
}

$basePath = "C:\ProjectsAOC\FlowOpsAI\products"
$productPath = Join-Path $basePath $ProductName

$folders = @(
"01-master-guide",
"02-prompt-vault",
"03-quickstart-system",
"04-workflow-playbooks",
"05-assets",
"06-export"

'''
"02-prompt-vault\01-excel-reporting",
"02-prompt-vault\02-technical-documentation",
"02-prompt-vault\03-troubleshooting-it",
"02-prompt-vault\04-project-management",
"02-prompt-vault\05-business-productivity"
'''

)

foreach ($folder in $folders) {

'''
$fullPath = Join-Path $productPath $folder

if (!(Test-Path $fullPath)) {
    New-Item `
    -Path $fullPath `
    -ItemType Directory | Out-Null

    Write-Host "✅ Created:"
    Write-Host $fullPath
}
'''

}

$readmePath = Join-Path $productPath "README.md"

$readme = @"

# $ProductName

Premium AI productivity system.

## Structure

### 01-master-guide

Premium PDF guide.

### 02-prompt-vault

Copy-paste prompt system.

### 03-quickstart-system

Fast onboarding.

### 04-workflow-playbooks

Practical AI workflows.

### 05-assets

Branding, covers, visuals.

### 06-export

Final packaged files.
"@

$readme | Out-File -FilePath $readmePath -Encoding utf8

Write-Host ""
Write-Host "🚀 Product scaffold completed."
Write-Host ""
Write-Host "Location:"
Write-Host $productPath