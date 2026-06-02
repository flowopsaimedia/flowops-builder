$basePath = 'C:\ProjectsAOC\FlowOpsAI\products\workday-acceleration-system\01-master-guide'

function Write-MarkdownFile {
param (
[string]$FileName,
[string[]]$Content
)


$filePath = Join-Path $basePath $FileName

Set-Content -Path $filePath -Value $Content -Encoding UTF8

Write-Host 'Generated:'
Write-Host $FileName

}


Write-MarkdownFile -FileName '00-cover.md' -Content @(
'# FlowOps AI',
'',
'# Workday Acceleration System',
'',
'## 50 Practical AI Systems to Save Time, Improve Reporting, and Work Smarter',
'',
'### Hybrid Productivity Edition',
'',
'Practical AI systems for professionals, technical teams, managers, and modern businesses.',
'',
'---',
'',
'Created by FlowOps AI',
'',
'flowopsai.io'
)

Write-MarkdownFile -FileName '01-introduction.md' -Content @(
'# Introduction',
'',
'Welcome to the **FlowOps AI — Workday Acceleration System**.',
'',
'This is not a collection of random prompts.',
'',
'This is a practical productivity system designed to help professionals, technical teams, managers, consultants, and modern businesses work smarter using artificial intelligence.',
'',
'Most people approach AI incorrectly.',
'',
'They ask vague questions, receive inconsistent answers, and conclude that AI is unreliable.',
'',
'The problem is rarely the technology.',
'',
'The problem is usually the system.',
'',
'This guide was created to solve that.',
'',
'Inside this system, you will find 50 practical AI workflows designed to help you:',
'',
'- Save time on repetitive work',
'- Improve reporting and analysis',
'- Create better documentation',
'- Troubleshoot problems faster',
'- Improve project execution',
'- Communicate more professionally',
'- Build smarter workflows using AI',
'',
'Rather than focusing on theory, this system prioritizes execution.',
'',
'Every module is practical.',
'Every prompt is actionable.',
'Every recommendation is designed to improve real-world productivity.',
'',
'## Who Is This For?',
'',
'- Professionals',
'- Project managers',
'- Technical teams',
'- Business analysts',
'- IT specialists',
'- Consultants',
'- Founders',
'- Operations teams',
'- Productivity-focused professionals'
)

Write-MarkdownFile -FileName '02-how-to-use-ai-effectively.md' -Content @(
'# How To Use AI Effectively',
'',
'Most people use artificial intelligence inefficiently.',
'',
'Professional results require professional inputs.',
'',
'## The FlowOps AI Framework',
'',
'### 1. Add Context',
'Always explain your situation.',
'',
'### 2. Be Specific',
'Specific requests generate better outputs.',
'',
'### 3. Add Examples',
'Examples dramatically improve quality.',
'',
'### 4. Define Your Goal',
'Explain the expected result.',
'',
'### 5. Iterate',
'AI works best through refinement.',
'',
'## Pro Recommendation',
'',
'Treat AI as a highly capable collaborator rather than a magic button.'
)

Write-MarkdownFile -FileName '03-excel-reporting.md' -Content @(
'# Excel & Reporting',
'',
'Artificial intelligence can dramatically improve Excel productivity.',
'',
'This module helps you:',
'',
'- Create formulas faster',
'- Clean messy datasets',
'- Build dashboards',
'- Generate KPI reports',
'- Analyze trends',
'- Create executive summaries'
)

Write-MarkdownFile -FileName '04-technical-documentation.md' -Content @(
'# Technical Documentation',
'',
'Technical documentation often consumes unnecessary time.',
'',
'This module helps professionals:',
'',
'- Create procedures',
'- Write implementation plans',
'- Build RCA documents',
'- Document integrations',
'- Create technical summaries'
)

Write-MarkdownFile -FileName '05-troubleshooting-it.md' -Content @(
'# Troubleshooting & IT Analysis',
'',
'Troubleshooting becomes dramatically faster when structured correctly.',
'',
'This module helps you:',
'',
'- Diagnose incidents',
'- Analyze logs',
'- Identify patterns',
'- Validate environments',
'- Build escalations'
)

Write-MarkdownFile -FileName '06-project-management.md' -Content @(
'# Project Management',
'',
'Project execution improves significantly when supported by structured AI workflows.',
'',
'This module helps you:',
'',
'- Define scope',
'- Build timelines',
'- Prioritize risks',
'- Communicate with stakeholders',
'- Generate executive updates'
)

Write-MarkdownFile -FileName '07-business-productivity.md' -Content @(
'# Business Productivity',
'',
'Artificial intelligence can dramatically improve professional productivity.',
'',
'This module helps you:',
'',
'- Write better emails',
'- Summarize meetings',
'- Improve decisions',
'- Optimize workflows',
'- Create better communication'
)

Write-MarkdownFile -FileName '08-best-practices.md' -Content @(
'# Best Practices',
'',
'To maximize AI performance:',
'',
'1. Be specific.',
'2. Add context.',
'3. Provide examples.',
'4. Iterate.',
'5. Think like a professional.',
'',
'The best outputs come from clear thinking.'
)

Write-MarkdownFile -FileName '09-next-steps.md' -Content @(
'# Next Steps',
'',
'You now have access to the FlowOps AI — Workday Acceleration System.',
'',
'Recommended actions:',
'',
'1. Start with your biggest productivity pain point.',
'2. Test prompts immediately.',
'3. Customize outputs.',
'4. Save successful workflows.',
'5. Build repeatable systems.',
'',
'Work smarter.'
)

Write-Host ''
Write-Host 'Master Guide generation completed.'