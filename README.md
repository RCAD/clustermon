For immediate purposes:
	
	- getting users in a specific sgi where "sgi10node1" is a variable head node 
	(can be done from anywhere. no credentials needed)
		net group hpc-users-sgi10node1 /domain
		
	- adding or deleting users from a given sgi headnode where "sgi10node1" is a ghead node variable and "test" is a variable user
	(has to be done with admin credentials and an admin shell, preferable from the domain controller)
		net group hpc-users-sgi10node1 /add test /domain
		net group hpc-users-sgi10node1 /delete test /domain
		
	- checking for current jobs running onan sgi where "sgi10node1" is a variable head node
	(needs to be done from a powershell cmd window, preferably an hpc powershell cmd window)
		add-pssnapin microsoft.hpc
			(needed is done from a normal powershell cmd window)
		 get-hpcjob -scheduler sgi10node1
			(can add the parameter "-owner test" where "test" is a user to retrieve jobs by a user)
			
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
			
Application Build Draft

	Information Needed (functional requirements):
		- # of jobs running on a cluster
		- users connected to a cluster
			- check for it to be 0 or 1 in case of the sgi's
		- check for job owner/user connected correlation
		
	Optional (non functional requirements):
		- nice gui
		- Ability to write a comprehensive report to a file
			- able to choose what cluster(s) to write the report on
			- able to browse where to print the report
		- Ability to provide credentials at startup
		
	Maybe available on application:
		- Ability to cancel jobs
		- Ability to add/remove users
		
	Using:
		- python
			-main drive program
		- ps1 files 
			-for powershell scrips when necessary
		- AutoIt Compiled executables
			- for commands run using credentials provided
			- credetntials feeded through command line
		- Tmp folder access
			- command and script output retireval when not possible to output to python main directly
