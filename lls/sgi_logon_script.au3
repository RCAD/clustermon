; Script to launch a logon script with admin privilidges to add a user to the cluster
if ((stringLeft(@ComputerName, 3)) == "SGI") then
	Local $_UserName = "HPCadmin"
	Local $_Password = "" ;CHANGE WHEN READY
	Local $_Domain = "SCHOLASTIC"
	Local $_AddUser = "cmd.exe /c net group HPC-Users-"&@ComputerName&"NODE1 /add "&@UserName&" /domain"
	RunAsWait($_UserName, $_Domain, $_Password, 2, $_AddUser)
endif
