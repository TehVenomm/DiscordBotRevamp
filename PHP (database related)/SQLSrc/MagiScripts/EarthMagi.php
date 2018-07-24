<?php
    function insertEarthMagi() 
    {
        include "../Tools/sourcelinks.php";
        
        $spreadsheet_data = grabCSVData($linkEarthMagi);

        insertMagiDB($spreadsheet_data, "Earth");
        
        return true;
    }
?>