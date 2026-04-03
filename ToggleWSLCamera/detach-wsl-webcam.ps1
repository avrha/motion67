$deviceName = "1080P Pro Stream"

$lines = usbipd list
$match = $lines | Where-Object { $_ -match [regex]::Escape($deviceName) } | Select-Object -First 1

if (-not $match) {
    Write-Host "Device '$deviceName' not found."
    exit 1
}

$parts = $match -split '\s{2,}'
$busid = $parts[0].Trim()

if (-not ($busid -match '^[0-9-]+$')) {
    Write-Host "Invalid BUSID parsed: $busid"
    exit 1
}

Write-Host "Detaching '$deviceName' (BUSID: $busid) from WSL..."
usbipd detach --busid $busid

if ($LASTEXITCODE -eq 0) {
    Write-Host "Camera returned to Windows."
} else {
    Write-Host "Failed to detach camera."
}

usbipd list


