# configure to increase limit of nginx server can handle
# that is the 'ULIMIT'
exec { 'fix-on-nginx':
  # change the ULIMIT value
  command => '/bin/sed/ -i "s/15/4096/" /etc/default/nginx',
  path    => 'usr/local/bin/:/bin/',
}

# restart nginx
exec { 'nginx-restart':
  # restart nginx
  command => '/etc/init.d/nginx restart',
  # init.d specific script path
  path    => '/etc/init.d/',
}
