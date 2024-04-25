#!/usr/bin/env bash
# a puppet script to make changes to configuration file
file { '.ssh/config'
	ensure	=> file
	content	=> "
Host *
	IdentityFile ~/.ssh/school
	PasswordAuthentication no
",
}
