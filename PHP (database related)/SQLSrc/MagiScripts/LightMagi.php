<?php
    function insertLightMagi() 
    {
        include "../Tools/sourcelinks.php";

        $spreadsheet_data = grabCSVData($linkLightMagi);

        insertMagiDB($spreadsheet_data, "Light");
        
        return true;
    }
?>