# Powershell script for cancellign a job on user logoff from an SGI

# imports the hpc commands 
Add-PSSnapIn Microsoft.HPC

# gets the current user logging off in "domain\username" format
$owner = [Security.Principal.WindowsIdentity]::GetCurrent().Name

# gets the name of the local cluster
$cluster = $env:computername + "NODE1"

#writes to log file
write-host "Attempting to cancel jobs for $owner"
 
# launches the command to cancel any and all jobs by the current user on the current cluster
foreach ($job in (get-hpcjob -owner $owner -scheduler $cluster)){$job.cancel()}
