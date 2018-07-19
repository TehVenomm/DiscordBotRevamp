<?php
    include "sourcelinks.php";
    if(!ini_set('default_socket_timeout', 15)) echo "<!-- unable to change socket timeout -->";

    if (($handle = fopen($linkWeapon, "r")) !== FALSE) {
        while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
            $spreadsheet_data[] = $data;
        }
        fclose($handle);
    }
    else
        die("Problem reading csv");

    include "conexao.php";  
    $skiphadercounter = 0;  
    foreach($spreadsheet_data as $rowcount){
        if($skiphadercounter > 1){
            $behemothName   = $rowcount[0];
            $typeCSV        = $rowcount[1];
            $elementCSV     = $rowcount[2];
            $tierCSV        = $rowcount[3];

            $pAttackCSV     = $rowcount[6];
            $eAttackCSV     = $rowcount[7];

            $abilityCSV     = $rowcount[11];
            $obsCSV         = $rowcount[12];
            if (!empty($abilityCSV)){
                $sql = "INSERT INTO `weapontable`
                        VALUES ('', ?, ?, ?, ?, ?, ?, ?);
                        ";
                $weaponQuery = $conex -> prepare($sql);
                try{
                    $weaponQuery -> execute(array($typeCSV, $tierCSV, $elementCSV, $pAttackCSV, $eAttackCSV, $abilityCSV, $obsCSV));

                } catch (Exception $weaponQuery) {
                    echo 'Caught exception: ',  $weaponQuery->getMessage(), "</br>";
                }

                $lastWeaponId = $conex->lastInsertId(); 
                

                $sql = "INSERT IGNORE INTO `behemothtable` 
                        VALUES ('', ?, ?, ?)";
                $weaponQuery = $conex -> prepare($sql);
                try{
                    $weaponQuery -> execute(array($behemothName, $elementCSV, $lastWeaponId));
                } catch (Exception $weaponQuery) {
                    echo 'Caught exception: ',  $weaponQuery->getMessage(), "</br>";
                }
            }
        }
        $skiphadercounter++;
    }
    echo "Succ-ess!</br>";
    
?>
<a href="linkArmourStash.php">
    <input type="button" value="Step 2. (Store Armour)">
</a>