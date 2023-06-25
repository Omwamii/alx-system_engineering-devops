# puppet to setup configuration
file {'/home/omwami/.ssh/config':
	ensure   => present,
	content  => "Host 206724-web-01\n
		HostName 54.84.24.93\n
		User     ubuntu\n
		IdentityFile       ~/.ssh/school\n
		PreferredAuthentications publickey\n
		PasswordAuthentication no\n"
}
