<?php
    function insertHybridMagi() 
    {
        include "../Tools/sourcelinks.php";

        $spreadsheet_data = grabCSVData($linkHybridMagi);

        insertMagiDB($spreadsheet_data, "Hybrid");

        return true;
    }
?>