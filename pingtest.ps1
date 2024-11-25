# Define the device to ping
$device = "ENTER DEVICE NAME OR IP"  # Replace with the IP address or hostname of your target device

# Send a single ping request
$pingResult = Test-Connection -ComputerName $device -Count 1 -Quiet

# Check the result and output the status
if ($pingResult) {
    Write-Output "On"
} else {
    Write-Output "Off"
}
