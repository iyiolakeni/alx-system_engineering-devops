# Define the class for Nginx installation and configuration
class nginx_config {
  package { 'nginx':
    ensure => 'installed',
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
  }

  # Create an Nginx configuration file
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => template('nginx_config/nginx.conf.erb'),
    notify  => Service['nginx'],
  }

  # Ensure Nginx is listening on port 80
  file { '/etc/nginx/sites-available/default':
    ensure  => present,
    require => Package['nginx'],
  }

  # Create the Hello World HTML file
  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello World!',
    require => Package['nginx'],
  }

  # Create a symbolic link to enable the site
  file { '/etc/nginx/sites-enabled/default':
    ensure  => link,
    target  => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
  }

  # Define the 301 redirect location
  nginx::resource::location { 'redirect_me':
    ensure       => present,
    location     => '/redirect_me',
    return       => '301',
    return_value => 'https://www.example.com/new_location',
    require      => Package['nginx'],
  }
}

# Apply the Nginx configuration class
include nginx_config
