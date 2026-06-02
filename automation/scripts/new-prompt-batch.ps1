param(
    [string]$Category
)

$basePath = "C:\ProjectsAOC\FlowOpsAI\prompts"
$targetFolder = Join-Path $basePath $Category

if (!(Test-Path $targetFolder)) {
    New-Item -Path $targetFolder -ItemType Directory | Out-Null
    Write-Host "✅ Folder created:"
    Write-Host $targetFolder
}

$prompts = @(
    @{ File="21-incident-troubleshooting-framework"; Title="Incident Troubleshooting Framework" },
    @{ File="22-api-error-diagnostic-assistant"; Title="API Error Diagnostic Assistant" },
    @{ File="23-authentication-failure-analyzer"; Title="Authentication Failure Analyzer" },
    @{ File="24-log-analysis-assistant"; Title="Log Analysis Assistant" },
    @{ File="25-environment-comparison-analyzer"; Title="Environment Comparison Analyzer" },
    @{ File="26-production-issue-rca-assistant"; Title="Production Issue RCA Assistant" },
    @{ File="27-configuration-validation-assistant"; Title="Configuration Validation Assistant" },
    @{ File="28-dependency-failure-diagnostic"; Title="Dependency Failure Diagnostic" },
    @{ File="29-technical-escalation-builder"; Title="Technical Escalation Builder" },
    @{ File="30-smart-troubleshooting-playbook"; Title="Smart Troubleshooting Playbook" }
)

foreach ($prompt in $prompts) {

    $filePath = Join-Path $targetFolder "$($prompt.File).md"

    $template = @"
# $($prompt.Title)

## Business Scenario
Describe a real business troubleshooting scenario.

## Use Case
Describe when to use this prompt.

## Prompt
You are an expert troubleshooting specialist.

Help me diagnose the following issue.

Problem:
[Describe the issue]

Symptoms:
[List symptoms]

Environment:
[Production / Test / QA / Development]

Recent changes:
[What changed?]

Requirements:
- Identify probable causes.
- Suggest troubleshooting steps.
- Prioritize likely failures.
- Recommend validation methods.
- Suggest mitigation actions.

## Example Input
Add a real troubleshooting example.

## Expected Output
A structured diagnosis with recommended next steps.

## Pro Tip
Provide timestamps, logs, errors, and recent changes for better diagnosis.
"@

    $template | Out-File -FilePath $filePath -Encoding utf8

    Write-Host "✅ Created $($prompt.File)"
}

Write-Host ""
Write-Host "🚀 Batch generation completed."