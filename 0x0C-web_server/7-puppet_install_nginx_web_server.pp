# setting up a new ubuntu server with Nginx

exec { 'system update':
	command	=> /usr/bin/apt-get update',
}

package { 'nginx':
	ensure	=> 'installed',
	require	=> Exec['system update']
}

file { '/var/www/html/index.html':
	content		=> 'Hello World!'
}

exec { 'redirect_me':
	command		=> 'sed -i "24i\	rewrite ^/redirect_me https://wwww.youtube.com;" /etc/nginx/sites-available/default',
	provider	=> 'shell'
}

service { 'nginx':
	ensure		=> running,
	require		=> Package['nginx']
}
