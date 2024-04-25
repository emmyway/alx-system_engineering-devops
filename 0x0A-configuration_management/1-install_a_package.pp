# puppet manifest uses pip3 to install flask in a system
package { 'flask':
	ensure		=> '2.1.0',
	provider	=> 'pip3',
}
