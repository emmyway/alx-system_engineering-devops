# a manifest that kills killmenow process
exec { 'kill_killmenow_process':
	command	=> '/usr/bin/pkill killmemow',
}
