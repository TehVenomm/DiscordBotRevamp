<?php
    if(isset($_POST['submit'])){
        $name            = '';
        $type            = '';
        $description     = '';
        $cooldown        = '';

        $queryInput = $_POST['query'];
        $queryInput = htmlspecialchars($queryInput);
        include "../Tools/conexao.php";
        $sql = "SELECT magitable.name, Description, magitypelist.Name as Type, Cooldown FROM magitable
        INNER JOIN magitypelist ON magitypelist.IdMagiType = magitable.IdMagiType_MagiTable
        WHERE magitable.Name LIKE '%$queryInput%'";
        $query = $conex -> prepare($sql);
        $query -> execute();
        
        $qty = $query -> rowCount();
        if ($qty == 1){
            foreach ($query as $x){
                $name            = $x['name'];
                $type            = $x['Description'];
                $description     = $x['Type'];
                $cooldown        = $x['Cooldown'];
                
            }
        } else {
            echo "nothing found!";
        }
        echo $name." - ".$type." - ".$description." - ".$cooldown;
    }

?>

<form action="" method="POST">
<input type="text" name="query">
<input type="submit" name="submit" value="enviar">
</form>