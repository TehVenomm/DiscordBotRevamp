<?php
    function insertPassiveMagi() {
        include "../Tools/sourcelinks.php";
        include "../Tools/conexao.php";
        if(!ini_set('default_socket_timeout', 15)) echo "<!-- unable to change socket timeout -->";

        if (($handle = fopen($linkPassiveMagi, "r")) !== FALSE) {
            while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
                $spreadsheet_data[] = $data;
            }
            fclose($handle);
        }
        else
            die("Problem reading csv");
        
        $skip2rowscounter = 0;

        foreach($spreadsheet_data as $rowcount){
            if($skip2rowscounter > 1){
                $MagiNameCSV        = $rowcount[0];
                $MagiCDCSV          = "0";
                $MagiDescCSV        = $rowcount[4];
                $MagiObsCSV         = "";
                $MagiTypeString     = "Passive";
                

                $sql = "SELECT idMagiType FROM magitypelist
                        WHERE magitypelist.Name = ?";
                $magiTypeQuery = $conex -> prepare($sql);
                try
                {
                    $magiTypeQuery -> execute(array($MagiTypeString));
                } 
                catch (Exception $magiTypeQuery) 
                {
                    echo 'Caught exception: ',  $magiTypeQuery->getMessage(), "</br>";
                }
                foreach($magiTypeQuery as $x)
                {
                    $idMagiType = $x["idMagiType"];
                }

                //verifies if the magi exists already
                $sql = "SELECT idMagi FROM magitable
                WHERE magitable.Name = ?";
                $magiExistsQuery = $conex -> prepare($sql);
                try
                {
                    $magiExistsQuery -> execute(array($MagiNameCSV));
                } 
                catch (Exception $magiExistsQuery) 
                {
                    echo 'Caught exception: ',  $magiExistsQuery->getMessage(), "</br>";
                }
                foreach($magiExistsQuery as $x)
                {
                    $idMagiExists = $x["idMagi"];
                }
                $qty = 0;
                $qty = $magiExistsQuery->rowCount();

                if (!empty($MagiDescCSV))
                {
                    if($qty == 0)
                    {
                        $sql = "INSERT INTO `magitable`
                                VALUES ('', ?, ?, ?, ?, ?)"; //DARK
                        $passiveMagiQuery = $conex -> prepare($sql);
                        try
                        {
                            $passiveMagiQuery -> execute(array($MagiNameCSV, $MagiCDCSV, $MagiDescCSV, $MagiObsCSV, $idMagiType));
                        } 
                        catch (Exception $passiveMagiQuery) 
                        {
                            echo 'Caught exception: ',  $passiveMagiQuery->getMessage(), "</br>";
                        }

                    } 
                    else 
                    {
                        echo "Magi ->".$MagiNameCSV."<- Already registered, thus skipped.<br>";
                    }
                }

            }
            $skip2rowscounter++;
        }
        $conex = NULL;
        return true;
    }
?>