#This code creates a manifest that kills a process named killmenow

exec { 'kill_killmenow_process':
  command     => 'pkill killmenow',
  path        => '/bin:/usr/bin',
  onlyif      => 'pgrep killmenow',
  refreshonly => true,
}
