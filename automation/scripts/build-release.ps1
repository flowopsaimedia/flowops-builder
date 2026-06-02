$projectRoot = 'C:\ProjectsAOC\FlowOpsAI'

$productName = 'workday-acceleration-system'

$productPath = Join-Path $projectRoot 'products'
$productPath = Join-Path $productPath $productName

$exportPath = Join-Path $productPath '06-export'

$releaseFolder = Join-Path $exportPath 'release-v1'

if (!(Test-Path $releaseFolder)) {
New-Item -Path $releaseFolder -ItemType Directory | Out-Null
}

$foldersToCopy = @(
'01-master-guide',
'02-prompt-vault',
'03-quickstart-system',
'04-workflow-playbooks',
'05-assets'
)

foreach ($folder in $foldersToCopy) {

$source = Join-Path $productPath $folder
$destination = Join-Path $releaseFolder $folder

if (Test-Path $source) {

    Copy-Item -Path $source -Destination $destination -Recurse -Force

    Write-Host 'Copied:'
    Write-Host $folder
}


}

Write-Host ''
Write-Host 'Release package ready.'