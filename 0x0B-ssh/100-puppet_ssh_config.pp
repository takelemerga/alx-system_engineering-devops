# setup a client SSH configuration file so that we can connect to server without password

exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
path    => '/bin/'
}
