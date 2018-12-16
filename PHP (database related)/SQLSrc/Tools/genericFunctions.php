<?PHP
    //tools
    function removeSpecialChars($stringInput)
    {
        $charsToRemove = array("'", "’");
        $fixedString = str_replace($charsToRemove, "", $stringInput);
        return $fixedString;
    }

    function filterInput($stringInput)
    {
        $fixedString = preg_replace('/[^0-9a-zA-Z\s★()]/',"",$stringInput);
        return $fixedString;
    }

    function filterNotObs($stringInput)
    {
        if (strpos($stringInput, '❈') !== false) {
            return $stringInput;
        } 
        else
        {
            return "";
        }
    }
    function grabCSVData($linkString)
    {
        if(!ini_set('default_socket_timeout', 15)) echo "<!-- unable to change socket timeout -->";

        if (($handle = fopen($linkString, "r")) !== FALSE) 
        {
            while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) 
            {
                $obtained_data[] = $data;
            }
            fclose($handle);
        }
        else
        {
            die("Problem reading csv");
        }
        return $obtained_data;
    }
    //specific functions
    function generateMagiInsertDB($CSVData, $MagiTypeString, $nameExistsArray, $magiTypeList)
    {
        $CSVRowCounter = 0;
		
		$builderArray = [];

        foreach($CSVData as $rowcount)
        {

            if($CSVRowCounter > 1)
            {
                $MagiHealCSV        = "";
                if ($MagiTypeString == "Passive")
                {
                    $MagiNameCSV        = removeSpecialChars($rowcount[0]);
                    $MagiCDCSV          = "0";
                    $MagiDescCSV        = str_replace("'", "\'", $rowcount[4]);
                    $MagiobsString      = "";
                }
                else if ($MagiTypeString == "Heal")
                {
                    $MagiNameCSV        = removeSpecialChars($rowcount[0]);
                    $MagiCDCSV          = str_replace("'", "\'", $rowcount[1]);
                    $MagiHealCSV        = str_replace("'", "\'", $rowcount[2]);
                    $MagiDescCSV        = str_replace("'", "\'", $rowcount[6]);
                    $MagiobsString      = str_replace("'", "\'", filterNotObs($rowcount[7]));
                    
                } 
                else
                {
                    $MagiNameCSV        = removeSpecialChars($rowcount[0]);
                    $MagiCDCSV          = str_replace("'", "\'", $rowcount[1]);
                    $MagiDescCSV        = str_replace("'", "\'", $rowcount[5]);
                    $MagiobsString      = str_replace("'", "\'", filterNotObs($rowcount[6]));
                    
                }

                $idMagiType = $magiTypeList[$MagiTypeString];

                if (!empty($MagiDescCSV))
                {
                    if(!in_array($MagiNameCSV, $nameExistsArray))
                    {
						$builderArray[] = "( '".$MagiNameCSV."', '".$MagiCDCSV."', '".$MagiHealCSV."', '".$MagiDescCSV."', '".$MagiobsString."', ".$idMagiType." )";
						
                    } 
                    else 
                    {
                        echo "Magi ->".$MagiNameCSV."<- Already registered, thus skipped.<br>";
                    }
                }
            }

            $CSVRowCounter++;

        }
	
		return $builderArray;
    }

    function weaponBehemothProcedure($spreadsheet_data){
        $skipHeaderCounter = 0;  

        foreach($spreadsheet_data as $rowcount)
        {
            if($skipHeaderCounter > 1)
            {
                $behemothName   = $rowcount[0];
                $typeCSV        = $rowcount[1];
                $elementCSV     = $rowcount[2];
                $tierCSV        = $rowcount[3];

                $pAttackCSV     = $rowcount[6];
                $eAttackCSV     = $rowcount[7];

                $abilityCSV     = $rowcount[11];
                $obsCSV         = filterNotObs($rowcount[12]);
                
                if (!empty($abilityCSV))
                {
                    $lastWeaponId = insertWeaponInDB($typeCSV, $tierCSV, $elementCSV, $pAttackCSV, $eAttackCSV, $abilityCSV, $obsCSV);
                    insertBehemothInDB($behemothName, $elementCSV, $lastWeaponId);
                }
            }
            $skipHeaderCounter++;
        }
    }

    //specific database functions
    function getMagiTypes(){ //returns an array of Name => Id for each magi type
        include "conexao.php";

        $sql = "SELECT idMagiType, Name FROM magitypelist";
        
        try
        {
            $magiTypeQuery = $conex->query($sql);
        } 
        catch (Exception $magiTypeQuery) 
        {
            echo 'Caught exception: ',  $magiTypeQuery->getMessage(), "</br>";
        }
        foreach($magiTypeQuery as $x)
        {
            $result[$x["Name"]] = $x["idMagiType"];
        }

        $conex = NULL;
        return $result;
    }

    function magiInDBList(){
        include "conexao.php";

        $sql           = "SELECT Name FROM magitable";
        $existsQuery   = $conex -> prepare($sql);
		$nameStringArray = [];

        try
        {
            $existsQuery->execute();
        } 
        catch (Exception $existsQuery) 
        {
            echo 'Caught exception: ',  $existsQuery->getMessage(), "</br>";
        }
		
        foreach($existsQuery as $x)
        {
            $nameStringArray[] = $x["Name"];
        }

        $conex = NULL;
		return $nameStringArray;
    }

    function insertMagiInDB($magiArray)
    {
        include "conexao.php";

        $sql             = "INSERT INTO `magitable` (`Name`, `Cooldown`, `HealAmount`, `Description`, `Obs`, `IdMagiType_MagiTable`) VALUES ";
		$i = 0;
		
		if (is_array($magiArray)) {
			foreach ($magiArray as $row){
				if( !next( $magiArray ) ) {
					$sql .= $row."; ";
				} else {
					$sql .= $row.", ";
				}
			}
		} elseif (!empty($magiArray)){
			$sql .= $magiArray."; ";
		}
		
		if (!empty($magiArray)){	
			try
			{
				$insertMagiQuery = $conex -> query($sql);
			} 
			catch (Exception $insertMagiQuery) 
			{
				echo 'Caught exception: ',  $insertMagiQuery->getMessage(), "</br>";
				$conex = NULL;
				return false;
			}
		} else {
			echo "Nothing to insert.";
			return false;
		}

        $conex = NULL;
    }

    function insertWeaponInDB($typeString, $tierString, $elementString, $pAttackString, $eAttackString, $abilityString, $obsString)
    {
        include "conexao.php";

        $sql = "INSERT INTO `weapontable` VALUES ('', ?, ?, ?, ?, ?, ?, ?)";
        $insertWeaponQuery = $conex -> prepare($sql);

        try
        {
            $insertWeaponQuery -> execute(array($typeString, $tierString, $elementString, $pAttackString, $eAttackString, $abilityString, $obsString));
        } 
        catch (Exception $insertWeaponQuery) 
        {
            echo 'Caught exception: ',  $insertWeaponQuery->getMessage(), "</br>";
        }

        $lastWeaponId = $conex->lastInsertId(); 
        $conex = NULL;
        return $lastWeaponId;
    }

    function insertBehemothInDB($nameString, $elementString, $weaponID)
    {
        include "conexao.php";
        
        $sql = "INSERT IGNORE INTO `behemothtable` VALUES ('', ?, ?, ?)";
        $weaponQuery = $conex -> prepare($sql);

        try
        {
            $weaponQuery -> execute(array($nameString, $elementString, $weaponID));
        } 
        catch (Exception $weaponQuery)
        {
            echo 'Caught exception: ',  $weaponQuery->getMessage(), "</br>";
        }

        return true;
    }
?>