<?php
    function insertFireMagi() 
    {
        include "../Tools/sourcelinks.php";

        $spreadsheet_data = grabCSVData($linkFireMagi);

        insertMagiDB($spreadsheet_data, "Fire");
        
        return true;
    }
?>