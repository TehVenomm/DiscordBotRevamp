<?php
	include "../Tools/genericFunctions.php";
    include "../Tools/sourcelinks.php";
	
	$nameList = magiInDBList();
	$typeList = getMagiTypes();
	
	$enormousQueryBuilder = [];
	
	foreach ($link as $key=>$value){
		$spreadsheet_data = grabCSVData($value);
		
		$results = generateMagiInsertDB($spreadsheet_data, $key, $nameList, $typeList);
        $enormousQueryBuilder = array_merge($results, $enormousQueryBuilder);
	}
	
	insertMagiInDB($enormousQueryBuilder);
?>

<a href="../../index.php">
    <input type="button" value="Finish">
</a>