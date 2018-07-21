<?php
    function insertLightningMagi() 
    {
        include "../Tools/sourcelinks.php";

        $spreadsheet_data = grabCSVData($linkLightningMagi);

        insertMagiDB($spreadsheet_data, "Lightning");
        
        return true;
    }
?>