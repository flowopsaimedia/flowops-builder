param(
    [string]$Category,
    [string]$Module
)

$basePath = "C:\ProjectsAOC\FlowOpsAI\prompts"
$targetFolder = Join-Path $basePath $Category

if (!(Test-Path $targetFolder)) {
    New-Item -Path $targetFolder -ItemType Directory | Out-Null
    Write-Host "✅ Folder created:"
    Write-Host $targetFolder
}

$modules = @{

    "project-management" = @(
        @{ File="31-project-scope-builder"; Title="Project Scope Builder" },
        @{ File="32-project-timeline-generator"; Title="Project Timeline Generator" },
        @{ File="33-risk-assessment-assistant"; Title="Risk Assessment Assistant" },
        @{ File="34-stakeholder-communication-builder"; Title="Stakeholder Communication Builder" },
        @{ File="35-project-status-report-generator"; Title="Project Status Report Generator" },
        @{ File="36-implementation-roadmap-builder"; Title="Implementation Roadmap Builder" },
        @{ File="37-meeting-action-tracker"; Title="Meeting Action Tracker" },
        @{ File="38-task-prioritization-assistant"; Title="Task Prioritization Assistant" },
        @{ File="39-project-blocker-analyzer"; Title="Project Blocker Analyzer" },
        @{ File="40-executive-project-summary-generator"; Title="Executive Project Summary Generator" }
    )

}

if (!$modules.ContainsKey($Module)) {
    Write-Host "❌ Module not found"
    exit
}

foreach ($prompt in $modules[$Module]) {

    $filePath = Join-Path $targetFolder "$($prompt.File).md"

$template = @"
# $($prompt.Title)

## Business Scenario
Describe a real business scenario.

## Use Case
Describe when to use this prompt.

## Prompt
You are an expert business and project management specialist.

Help me solve the following scenario.

Context:
[Describe situation]

Objective:
[Goal]

Constraints:
[List constraints]

Requirements:
- Recommend practical actions.
- Prioritize business value.
- Structure recommendations clearly.
- Identify risks and dependencies.
- Suggest best practices.

## Example Input
Add a real-world example.

## Expected Output
A professional and actionable result.

## Pro Tip
Provide business context and desired outcome for better results.
"@

    $template | Out-File -FilePath $filePath -Encoding utf8

    Write-Host "✅ Created $($prompt.File)"
}

Write-Host ""
Write-Host "🚀 Batch generation completed."