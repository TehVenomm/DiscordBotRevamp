<?php	
	try
	{
		if (!headers_sent()) 
		{
			header('Content-Type: text/html; charset=utf-8');
		}
		$conex = new PDO("mysql:host=85.10.205.173:3306;dbname=karyu_db;charset=utf8","*****","****");
		$conex ->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		$conex -> query("SET NAMES 'utf8'");
		$conex -> query("SET CHARACTER SET 'utf8'");
		set_time_limit(0);
	}
	catch(PDOexception $e)
	{
		echo $e->getMessage();
	}
?>