# script enanles holberton user to login n access files without error

# thus increaee hard files limits for holberton user
exec { 'hard-files-limit-increase-for-holberton':
  command => "sed -i '/^holberton hard/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}

# thus increase soft files limits for holberton
exec { 'soft-files-limit-increase-for-holberton':
  command => "sed -i '/^holberton soft/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}
