$basePromptPath = "C:\ProjectsAOC\FlowOpsAI\prompts"

$productPath = "C:\ProjectsAOC\FlowOpsAI\products\workday-acceleration-system\02-prompt-vault"

$mapping = @{
"excel-reporting" = "01-excel-reporting"
"technical-documentation" = "02-technical-documentation"
"troubleshooting-it" = "03-troubleshooting-it"
"project-management" = "04-project-management"
"business-productivity" = "05-business-productivity"
}

foreach ($sourceFolder in $mapping.Keys) {

'''
$sourcePath = Join-Path $basePromptPath $sourceFolder
$targetPath = Join-Path $productPath $mapping[$sourceFolder]

if (Test-Path $sourcePath) {

    Copy-Item `
    -Path "$sourcePath\*" `
    -Destination $targetPath `
    -Recurse `
    -Force

    Write-Host "✅ Copied:"
    Write-Host $sourceFolder
}
'''

}

Write-Host ""
Write-Host "🚀 Prompt Vault Build Completed."