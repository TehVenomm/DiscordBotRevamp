<?php
    include "../Tools/sourcelinks.php";
    include "../Tools/genericFunctions.php";
    include "../Tools/conexao.php";  

    $spreadsheet_data = grabCSVData($linkArmour);

    $skip2rowscounter  		= 0; 
    $errorCounter      		= 0; 
	$armorQueryArray 		= [];
	$idBehemothArray 		= [];
	$idBehemothArmorArray 	= [];


	$sql = "SELECT idBehemoth, Name FROM behemothtable";
	try
	{
		$setupQuery = $conex -> query($sql);

	} catch (Exception $setupQuery) 
	{
		echo 'Caught exception: ',  $setupQuery->getMessage(), "</br>";
	}
	foreach($setupQuery as $x)
	{
		$idBehemothArray[$x['Name']] = $x["idBehemoth"];
	}
	
	
	$sql = "SELECT IdBehemoth_ArmourTable FROM armourtable";
	try
	{
		$setupQuery = $conex -> query($sql);

	} catch (Exception $setupQuery) 
	{
		echo 'Caught exception: ',  $setupQuery->getMessage(), "</br>";
	}
	foreach($setupQuery as $x)
	{
		$idBehemothArmorArray[] = $x["IdBehemoth_ArmourTable"];
	}


    foreach($spreadsheet_data as $rowcount)
    {
        if($skip2rowscounter > 1)
        {
            $behemothNameCSV    = $rowcount[0];
            $defElementCSV      = $rowcount[1];

            $hpHelmetCSV        = $rowcount[4];
            $eDefHelmetCSV      = $rowcount[5];

            $pDefChestCSV       = $rowcount[7];
            $eDefChestCSV       = $rowcount[8];

            $hpGlovesCSV        = $rowcount[10];
            $pDefGlovesCSV      = $rowcount[11];
            $eDefGlovesCSV      = $rowcount[12];
            $pAtkGlovesCSV      = $rowcount[13];

            $hpLegsCSV          = $rowcount[15];
            $pDefLegsCSV        = $rowcount[16];
            $eDefLegsCSV        = $rowcount[17];
            $pAtkLegsCSV        = $rowcount[18];

            $abilityCSV         = str_replace("'", "\'", $rowcount[20]);
            $obsCSV             = str_replace("'", "\'", filterNotObs($rowcount[21]));

			if (!empty($abilityCSV))
			{
				if(isset($idBehemothArray[$behemothNameCSV]))
				{
					$idBehemothQuery = $idBehemothArray[$behemothNameCSV];
					if(!in_array($idBehemothQuery, $idBehemothArmorArray)){
						$armorQueryArray[] = " ( '".$defElementCSV."', '".$hpHelmetCSV."', 0, '".$eDefHelmetCSV."', 0, '".$abilityCSV."', '".$obsCSV."', 1, ".$idBehemothQuery." ) ";
						$armorQueryArray[] = " ( '".$defElementCSV."', 0, '".$pDefChestCSV."', '".$eDefChestCSV."', 0, '".$abilityCSV."', '".$obsCSV."', 2, ".$idBehemothQuery." ) ";
						$armorQueryArray[] = " ( '".$defElementCSV."', '".$hpGlovesCSV."', '".$pDefGlovesCSV."', '".$eDefGlovesCSV."', '".$pAtkGlovesCSV."', '".$abilityCSV."', '".$obsCSV."', 3, ".$idBehemothQuery." ) ";
						$armorQueryArray[] = " ( '".$defElementCSV."', '".$hpLegsCSV."', '".$pDefLegsCSV."', '".$eDefLegsCSV."', '".$pAtkLegsCSV."', '".$abilityCSV."', '".$obsCSV."', 4, ".$idBehemothQuery." ) ";
					} else {
						$errorCounter++;
						echo "behemoth ->".$behemothNameCSV."<- already has armour pieces registered<br>";
					}
				} else 
				{
					$errorCounter++;
					echo "behemoth ->".$behemothNameCSV."<- not found thus registering failed.<br>";
				}
			}
			
        }

        $skip2rowscounter++;

    }
	// this thing can be made into a genericFunction, its gonna be applied like 4x over the source code so shorten this bitch
	
	$sql = "INSERT INTO `armourtable` (`DefElement`, `HpValue`, `PhysDef`, `ElemDef`, `PhysAttack`, `Ability`, `Obs`, `IdArmourtype_ArmourTable`, `IdBehemoth_ArmourTable`) VALUES ";
	$i = 0;
		
	if (is_array($armorQueryArray)) {
		foreach ($armorQueryArray as $row){
			if( !next( $armorQueryArray ) ) {
				$sql .= $row."; ";
			} else {
				$sql .= $row.", ";
			}
		}
	} elseif (!empty($armorQueryArray)){
		$sql .= $armorQueryArray."; ";
	}
	
	if (!empty($armorQueryArray)){	
		try
		{
			$insertArmourQuery = $conex -> query($sql);
		} 
		catch (Exception $insertArmourQuery) 
		{
			echo 'Caught exception: ',  $insertArmourQuery->getMessage(), "</br>";
			$conex = NULL;
			return false;
		}
	} else {
		echo "Nothing to insert.";
		return false;
	}

	$conex = NULL;
	
    if ($errorCounter == 0)
        echo "Success.</br>";
    else   
        echo $errorCounter."Error.<b>Make sure you run the weapons first</b>";

?>

<a href="../../index.php">
    <input type="button" value="Finish">
</a>