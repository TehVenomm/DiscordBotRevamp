<?php
    include "../Tools/sourcelinks.php";
    include "../Tools/genericFunctions.php";
    include "../Tools/conexao.php";  

    $spreadsheet_data = grabCSVData($linkArmour);

    $skip2rowscounter  = 0; 
    $errorCounter      = 0; 

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

            $abilityCSV         = $rowcount[20];
            $obsCSV             = $rowcount[21];

            //get existing behemoth's id
            $sql = "SELECT idBehemoth FROM behemothtable WHERE behemothtable.Name = ?";
            $behemothQuery = $conex -> prepare($sql);

            try
            {
                $behemothQuery -> execute(array($behemothNameCSV));

            } catch (Exception $behemothQuery) 
            {
                echo 'Caught exception: ',  $behemothQuery->getMessage(), "</br>";
            }
            foreach($behemothQuery as $x)
            {
                $idBehemothQuery = $x["idBehemoth"];
            }

            $qty = $behemothQuery->rowCount();

            if (!empty($abilityCSV))
            {
                if($qty != 0)
                {
                    $sql = "INSERT INTO `armourtable` VALUES ('', ?, ?, 0, ?, 0, ?, ?, 1, ?)"; //HELMET
                    $armoryHelmet = $conex -> prepare($sql);
                    try
                    {
                        $armoryHelmet -> execute(array($defElementCSV, $hpHelmetCSV, $eDefHelmetCSV, $abilityCSV, $obsCSV, $idBehemothQuery));
                    } catch (Exception $armoryHelmet) 
                    {
                        echo 'Caught exception: ',  $armoryHelmet->getMessage(), "</br>";
                    }

                    $sql = "INSERT INTO `armourtable` VALUES ('', ?, 0, ?, ?, 0, ?, ?, 2, ?)"; //CHEST
                    $armoryChest = $conex -> prepare($sql);
                    try
                    {
                        $armoryChest -> execute(array($defElementCSV, $pDefChestCSV, $eDefChestCSV, $abilityCSV, $obsCSV, $idBehemothQuery));
                    } catch (Exception $armoryChest) {
                        echo 'Caught exception: ',  $armoryChest->getMessage(), "</br>";
                    }

                    $sql = "INSERT INTO `armourtable` VALUES ('', ?, ?, ?, ?, ?, ?, ?, 3, ?)"; //GLOVES
                    $armoryGloves = $conex -> prepare($sql);
                    try{
                        $armoryGloves -> execute(array($defElementCSV, $hpGlovesCSV, $pDefGlovesCSV, $eDefGlovesCSV, $pAtkGlovesCSV, $abilityCSV, $obsCSV, $idBehemothQuery));
                    } catch (Exception $armoryGloves) {
                        echo 'Caught exception: ',  $armoryGloves->getMessage(), "</br>";
                    }

                    $sql = "INSERT INTO `armourtable` VALUES ('', ?, ?, ?, ?, ?, ?, ?, 4, ?)"; //LEGS
                    $armoryLegs = $conex -> prepare($sql);
                    try{
                        $armoryLegs -> execute(array($defElementCSV, $hpLegsCSV, $pDefLegsCSV, $eDefLegsCSV, $pAtkLegsCSV, $abilityCSV, $obsCSV, $idBehemothQuery));
                    } catch (Exception $armoryLegs) {
                        echo 'Caught exception: ',  $armoryLegs->getMessage(), "</br>";
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
    if ($errorCounter == 0)
        echo "Success.</br>";
    else   
        echo $errorCounter."Error.<b>Make sure you run the weapons first</b>";

?>

<a href="../../index.php">
    <input type="button" value="gz ur done">
</a>