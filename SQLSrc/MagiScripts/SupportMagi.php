<?php
    function insertSupportMagi() 
    {
        include "../Tools/sourcelinks.php";

        $spreadsheet_data = grabCSVData($linkSupportMagi);

        insertMagiDB($spreadsheet_data, "Support");
        
        return true;
    }
?>