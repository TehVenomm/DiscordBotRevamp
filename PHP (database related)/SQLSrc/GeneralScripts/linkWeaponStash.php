<?php
    include "../Tools/sourcelinks.php";
    include "../Tools/genericFunctions.php";
    include "../Tools/conexao.php";  

    $spreadsheet_data = grabCSVData($linkWeapon);

    weaponBehemothProcedure($spreadsheet_data);
    
    echo "Succ-ess!</br>";
    
?>
<a href="linkArmourStash.php">
    <input type="button" value="Step 2. (Store Armour)">
</a>