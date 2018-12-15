<?php	
	try
	{
		if (!headers_sent()) 
		{
			header('Content-Type: text/html; charset=utf-8');
		}
		$conex = new PDO("mysql:host=hostname;dbname=database_name;charset=utf8","databaseusername","databasepassword", array(PDO::MYSQL_ATTR_INIT_COMMAND => "SET NAMES 'utf8'"));
		$conex ->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		$conex -> query("SET NAMES 'utf8'");
		$conex -> query("SET CHARACTER SET 'utf8'");
		set_time_limit(900);
	}
	catch(PDOexception $e)
	{
		echo $e->getMessage();
	}
?>