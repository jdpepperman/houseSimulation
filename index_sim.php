<?php
	header("Refresh:1");
	$myfilename = "output.txt";
	if(file_exists($myfilename))
	{
		echo nl2br(file_get_contents($myfilename));
	}
?>
