<?PHP

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

    function insertMagiDB($CSVData, $MagiTypeString)
    {
        include "conexao.php";

        $CSVRowCounter = 0;

        foreach($CSVData as $rowcount)
        {
            if($CSVRowCounter > 1)
            {
                if ($MagiTypeString == "Passive")
                {
                    $MagiNameCSV        = removeSpecialChars($rowcount[0]);
                    $MagiCDCSV          = "0";
                    $MagiDescCSV        = $rowcount[4];
                    $MagiObsCSV         = "";
                }
                else
                {
                    $MagiNameCSV        = removeSpecialChars($rowcount[0]);
                    $MagiCDCSV          = $rowcount[1];
                    $MagiDescCSV        = $rowcount[5];
                    $MagiObsCSV         = $rowcount[6];
                }

                $idMagiType = getMagiTypeId($MagiTypeString);

                if (!empty($MagiDescCSV))
                {
                    if(!nameExistsInDB($MagiNameCSV))
                    {
                        insertMagiInDB($MagiNameCSV, $MagiCDCSV, $MagiDescCSV, $MagiObsCSV, $idMagiType);
                    } 
                    else 
                    {
                        echo "Magi ->".$MagiNameCSV."<- Already registered, thus skipped.<br>";
                    }
                }
            }

            $CSVRowCounter++;

        }

        $conex = NULL;
    }

    function getMagiTypeId($string){
        include "conexao.php";

        $sql                = "SELECT idMagiType FROM magitypelist WHERE magitypelist.Name = ?";
        $query      = $conex -> prepare($sql);

        try
        {
            $query -> execute(array($string));
        } 
        catch (Exception $query) 
        {
            echo 'Caught exception: ',  $query->getMessage(), "</br>";
        }
        foreach($query as $x)
        {
            $ObtainedID = $x["idMagiType"];
        }

        $conex = NULL;

        return $ObtainedID;
    }

    function nameExistsInDB($nameString){
        include "conexao.php";

        $sql           = "SELECT idMagi FROM magitable WHERE magitable.Name = ?";
        $existsQuery   = $conex -> prepare($sql);

        try
        {
            $existsQuery -> execute(array($nameString));
        } 
        catch (Exception $existsQuery) 
        {
            echo 'Caught exception: ',  $existsQuery->getMessage(), "</br>";
        }
        foreach($existsQuery as $x)
        {
            $nameString = $x["idMagi"];
        }

        $qty = 0;
        $qty = $existsQuery->rowCount();

        $conex = NULL;

        if ($qty > 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

    function insertMagiInDB($Name, $cooldown, $description, $observation, $idType)
    {
        $sql             = "INSERT INTO `magitable` VALUES ('', ?, ?, ?, ?, ?)";
        $insertMagiQuery = $conex -> prepare($sql);

        try
        {
            $insertMagiQuery -> execute(array($Name, $cooldown, $description, $observation, $idType));
        } 
        catch (Exception $insertMagiQuery) 
        {
            echo 'Caught exception: ',  $insertMagiQuery->getMessage(), "</br>";
            return false;
        }
        return true;
    }
?>