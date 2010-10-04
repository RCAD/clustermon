; Script to launch a logoff script with admin privilidges to take out a user from the cluster
if ((stringLeft(@ComputerName, 3)) == "SGI") then
	Local $_UserName = "HPCadmin"
	Local $_Password = "" ;CHANGE WHEN READY
	Local $_Domain = "SCHOLASTIC"
	Local $_unrestricted = "cmd.exe /c powershell set-executionpolicy unrestricted"
	Local $_remote = "cmd.exe /c powershell set-executionpolicy remotesigned"
	Local $_CancelJobs = "cmd.exe /c powershell.exe -file C:\Ringling\hpc-job-cancel-logoff.ps1 >> C:\Ringling\SGI_logout.log -append"
	Local $_RemoveUser = "cmd.exe /c net group HPC-Users-"&@ComputerName&"NODE1 /delete "&@UserName&" /domain"
	RunAsWait($_UserName, $_Domain, $_Password, 2, $_unrestricted)
	RunAsWait($_UserName, $_Domain, $_Password, 2, $_CancelJobs)
	RunAsWait($_UserName, $_Domain, $_Password, 2, $_remote)
	RunAsWait($_UserName, $_Domain, $_Password, 2, $_RemoveUser)
endif

