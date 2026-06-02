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

    "business-productivity" = @(
        @{ File="41-executive-email-writer"; Title="Executive Email Writer" },
        @{ File="42-meeting-notes-to-action-plan"; Title="Meeting Notes to Action Plan" },
        @{ File="43-business-decision-assistant"; Title="Business Decision Assistant" },
        @{ File="44-smart-research-summarizer"; Title="Smart Research Summarizer" },
        @{ File="45-professional-proposal-generator"; Title="Professional Proposal Generator" },
        @{ File="46-weekly-productivity-planner"; Title="Weekly Productivity Planner" },
        @{ File="47-client-communication-assistant"; Title="Client Communication Assistant" },
        @{ File="48-business-process-optimizer"; Title="Business Process Optimizer" },
        @{ File="49-ai-workflow-designer"; Title="AI Workflow Designer" },
        @{ File="50-professional-document-improver"; Title="Professional Document Improver" }
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