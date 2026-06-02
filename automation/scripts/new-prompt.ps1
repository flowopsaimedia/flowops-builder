param(
[string]$Category,
[string]$FileName,
[string]$PromptTitle,
[string]$UseCase = "Describe when to use this prompt."
)

$basePath = "C:\ProjectsAOC\FlowOpsAI\prompts"
$targetFolder = Join-Path $basePath $Category

if (!(Test-Path $targetFolder)) {
Write-Host ""
Write-Host "❌ Category folder not found: $Category"
exit
}

$filePath = Join-Path $targetFolder "$FileName.md"

$template = @"

# $PromptTitle

## Use Case

$UseCase

## Prompt

You are an expert specialist.

Help me with the following scenario.

Context:
[Describe your situation]

Requirements:
[List requirements]

## Expected Output

A professional and actionable result.

## Pro Tip

Add context and examples to get better results.
"@

$template | Out-File -FilePath $filePath -Encoding utf8

Write-Host ""
Write-Host "✅ Prompt created successfully:"
Write-Host $filePath
Write-Host ""