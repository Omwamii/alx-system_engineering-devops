# puppet to configure web server with Puppet
exec { 'install nginx':
	command  => "apt-get update && apt-get install -y nginx"
}
exec { 'configure port':
	command  =>  "ufw allow 'Nginx HTTP'"
}

file { 'index.html':
	path  => '/var/www/html/index.html',
	content  => 'Hello World',
}

exec { 'Restart nginx':
	command  => 'service nginx restart'
}
