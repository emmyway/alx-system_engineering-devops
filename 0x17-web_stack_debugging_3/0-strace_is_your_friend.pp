# fixes phpp extension to php in wp-settings.php

exec{'fixing-wordpress':
	command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
	path => '/usr/local/bin/:/bin/'
}
