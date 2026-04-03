Start-Process wsl.exe -ArgumentList '-d Ubuntu-24.04' -WindowStyle Hidden

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

Write-Host "Attaching '$deviceName' on BUSID $busid"
usbipd attach --wsl --busid $busid
usbipd list

