<?php
    function insertPassiveMagi() 
    {
        include "../Tools/sourcelinks.php";

        $spreadsheet_data = grabCSVData($linkPassiveMagi);

        insertMagiDB($spreadsheet_data, "Passive");
        
        return true;
    }
?>