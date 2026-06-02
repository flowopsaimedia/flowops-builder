$basePath = "C:\ProjectsAOC\FlowOpsAI\products\workday-acceleration-system\01-master-guide"

$documents = @{

"00-cover.md" = @"

# FlowOps AI

# Workday Acceleration System

## 50 Practical AI Systems to Save Time, Improve Reporting, and Work Smarter

### Hybrid Productivity Edition

Practical AI systems for professionals, technical teams, managers, and modern businesses.

---

Created by FlowOps AI

flowopsai.io
"@

"01-introduction.md" = @"

# Introduction

Welcome to the **FlowOps AI — Workday Acceleration System**.

This is not a collection of random prompts.

This is a practical productivity system designed to help professionals, technical teams, managers, consultants, and modern businesses work smarter using artificial intelligence.

Most people approach AI incorrectly.

They ask vague questions, receive inconsistent answers, and conclude that AI is unreliable.

The problem is rarely the technology.

The problem is usually the system.

This guide was created to solve that.

Inside this system, you will find 50 practical AI workflows designed to help you:

* Save time on repetitive work
* Improve reporting and analysis
* Create better documentation
* Troubleshoot problems faster
* Improve project execution
* Communicate more professionally
* Build smarter workflows using AI

Rather than focusing on theory, this system prioritizes execution.

Every module is practical.

Every prompt is actionable.

Every recommendation is designed to improve real-world productivity.

## Who Is This For?

This system is especially valuable for:

* Professionals
* Project managers
* Technical teams
* Business analysts
* IT specialists
* Consultants
* Founders
* Operations teams
* Productivity-focused professionals

## How To Get The Best Results

Artificial intelligence becomes dramatically more powerful when context improves.

For best results:

1. Be specific.
2. Add business or technical context.
3. Include examples when possible.
4. Explain your desired outcome.
5. Iterate and improve outputs.

Think of AI as a highly capable collaborator.

The quality of the result often depends on the quality of the instructions.

The goal of this system is simple:

> Help you save time and work smarter.

Let's begin.
"@

"02-how-to-use-ai-effectively.md" = @"

# How To Use AI Effectively

Most people use artificial intelligence inefficiently.

They ask vague questions and expect highly precise answers.

Professional results require professional inputs.

## The FlowOps AI Framework

### 1. Add Context

Always explain your situation.

Bad:
'Help me write an email.'

Better:
'Help me write an executive email to a customer regarding implementation delays.'

### 2. Be Specific

Specific requests generate better outputs.

### 3. Add Examples

Examples dramatically improve quality.

### 4. Define Your Goal

Explain the expected result.

### 5. Iterate

AI works best through refinement.

## Pro Recommendation

Treat AI as a highly capable collaborator rather than a magic button.
"@

}

foreach ($doc in $documents.Keys) {

'''
$filePath = Join-Path $basePath $doc

$documents[$doc] | Out-File `
-FilePath $filePath `
-Encoding utf8

Write-Host "✅ Generated:"
Write-Host $doc
'''

}

Write-Host ""
Write-Host "🚀 Master Guide generation completed."
