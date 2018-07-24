<?php
    function insertHealMagi() 
    {
        include "../Tools/sourcelinks.php";

        $spreadsheet_data = grabCSVData($linkHealMagi);

        insertMagiDB($spreadsheet_data, "Heal");

        return true;
    }
?>