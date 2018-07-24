<?php	
	try
	{
		if (!headers_sent()) 
		{
			header('Content-Type: text/html; charset=utf-8');
		}
		$conex = new PDO("mysql:host=localhost;dbname=karyu_db;charset=utf8","root","");
		$conex ->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
		$conex -> query("SET NAMES 'utf8'");
		$conex -> query("SET CHARACTER SET 'utf8'");
	}
	catch(PDOexception $e)
	{
		echo $e->getMessage();
	}
?>