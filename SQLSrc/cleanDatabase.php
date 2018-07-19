<?PHP
    include "conexao.php";
    $sql = "DELETE FROM armourtable;
            ALTER TABLE armourtable AUTO_INCREMENT = 1;
            DELETE FROM behemothtable;
            ALTER TABLE behemothtable AUTO_INCREMENT = 1;
            DELETE FROM magitable;
            ALTER TABLE magitable AUTO_INCREMENT = 1;
            DELETE FROM ratingstable;
            ALTER TABLE ratingstable AUTO_INCREMENT = 1;
            DELETE FROM weapontable;
            ALTER TABLE weapontable AUTO_INCREMENT = 1;";
    $cleanDB = $conex -> prepare($sql);
    try{
        $cleanDB -> execute();

    } catch (Exception $cleanDB) {
        echo 'Caught exception: ',  $cleanDB->getMessage(), "</br>";
    }
    echo "all cleaned out bub move along";
?>  
<a href="linkWeaponStash.php">
    <input type="button" value="Step 2. (weapons and behemoths)">
</a>