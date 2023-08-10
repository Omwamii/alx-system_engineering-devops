# fix typo causing server error in settings file

exec { 'fix_typo':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path    => ['/bin','/usr/bin']
}
