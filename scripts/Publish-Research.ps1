param(
    [Parameter(Mandatory)][string]$ResearchRepo,
    [Parameter(Mandatory)][string]$SiteRepo
)
$ErrorActionPreference = 'Stop'
function Invoke-Git([string]$RepoPath, [string[]]$Arguments) {
    & git -C $RepoPath @Arguments
    if ($LASTEXITCODE -ne 0) { throw 'Git command failed.' }
}
$sourcePath = (Resolve-Path -LiteralPath $ResearchRepo).Path
$sitePath = (Resolve-Path -LiteralPath $SiteRepo).Path
if (!(Test-Path -LiteralPath (Join-Path $sourcePath 'site/index.html'))) { throw 'Render the library first.' }
$remote = & git -C $sitePath remote get-url origin
if ($LASTEXITCODE -ne 0 -or $remote -notmatch 'github.com[:/]larsklanderpe/agents-phone(?:\.git)?$') { throw 'Site repository does not match the configured domain owner.' }
$dirty = & git -C $sitePath status --porcelain
if ($dirty) { throw 'Use a clean site checkout.' }
Invoke-Git $sitePath @('fetch','origin','--prune')
$branch = 'feat/research-publication-' + (Get-Date -Format 'yyyyMMdd-HHmmss')
Invoke-Git $sitePath @('switch','-c',$branch,'origin/main')
$targetPath = Join-Path $sitePath 'research-documents-pe'
New-Item -ItemType Directory -Path $targetPath -Force | Out-Null
Copy-Item -Path (Join-Path $sourcePath 'site/*') -Destination $targetPath -Recurse -Force
Invoke-Git $sitePath @('add','research-documents-pe')
& git -C $sitePath diff --cached --quiet
if ($LASTEXITCODE -eq 0) { Write-Output 'Published files already match. No PR needed.'; exit 0 }
if ($LASTEXITCODE -ne 1) { throw 'Unable to inspect staged changes.' }
Invoke-Git $sitePath @('commit','-m','docs(research): publish source-linked research guides')
Invoke-Git $sitePath @('push','-u','origin',$branch)
$bodyPath = Join-Path $sourcePath '.publication-pr-body.txt'
@'
Publish the rendered research library under /research-documents-pe/ on the existing domain site.

Source: larsklanderpe/research-documents-pe. Existing domain and pages remain in place.
Validation: renderer completed; generated content and local navigation checked.
'@ | Set-Content -LiteralPath $bodyPath -Encoding utf8
& gh pr create --repo larsklanderpe/agents-phone --head $branch --base main --title 'Publish research document library' --body-file $bodyPath
if ($LASTEXITCODE -ne 0) { throw 'PR creation failed; the pushed branch is available for recovery.' }
Write-Output 'Publication awaits merge under the active approval rules.'
