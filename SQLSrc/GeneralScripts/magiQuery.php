<?php
    include "../Tools/genericFunctions.php";

    if(isset($_POST['submit']))
    {
        $name            = '';
        $type            = '';
        $description     = '';
        $cooldown        = '';

        $queryInput = $_POST['query'];
        $queryInput = filterInput($queryInput);

        include "../Tools/conexao.php";

        $sql = "SELECT magitable.name, Description, magitypelist.Name as Type, Cooldown FROM magitable
            INNER JOIN magitypelist ON magitypelist.IdMagiType = magitable.IdMagiType_MagiTable
            WHERE magitable.Name LIKE ?";

        $query  =   $conex -> prepare($sql);
        $query  ->  execute(array('%'.$queryInput.'%'));
        
        $qty = $query -> rowCount();

        if ($qty > 0)
        {
            foreach ($query as $x)
            {
                $name            = $x['name'];
                $type            = $x['Description'];
                $description     = $x['Type'];
                $cooldown        = $x['Cooldown'];
                echo $name." - ".$type." - ".$description." - ".$cooldown."<br>-----------<br>";
            }
        }
         else 
        {
            echo "nothing found! searched: ".$queryInput;

            
        }
    }

?>

<form action="" method="POST">
<input type="text" name="query">
<input type="submit" name="submit" value="enviar">
</form>