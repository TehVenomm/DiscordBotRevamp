<?php
    function insertWaterMagi() 
    {
        include "../Tools/sourcelinks.php";

        $spreadsheet_data = grabCSVData($linkWaterMagi);

        insertMagiDB($spreadsheet_data, "Water");
        
        return true;
    }
?>