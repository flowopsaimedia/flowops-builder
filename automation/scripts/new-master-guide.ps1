$basePath = "C:\ProjectsAOC\FlowOpsAI\products\workday-acceleration-system\01-master-guide"

$files = @(
"00-cover.md",
"01-introduction.md",
"02-how-to-use-ai-effectively.md",
"03-excel-reporting.md",
"04-technical-documentation.md",
"05-troubleshooting-it.md",
"06-project-management.md",
"07-business-productivity.md",
"08-best-practices.md",
"09-next-steps.md"
)

foreach ($file in $files) {

'''
$filePath = Join-Path $basePath $file

if (!(Test-Path $filePath)) {

    New-Item -Path $filePath -ItemType File | Out-Null

    Write-Host "✅ Created:"
    Write-Host $file
}
'''

}

Write-Host ""
Write-Host "🚀 Master Guide scaffold completed."