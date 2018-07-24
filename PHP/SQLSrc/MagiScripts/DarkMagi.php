<?php
    function insertDarkMagi() 
    {
        include "../Tools/sourcelinks.php";

        $spreadsheet_data = grabCSVData($linkDarkMagi);

        insertMagiDB($spreadsheet_data, "Dark");
        
        return true;
    }
?>