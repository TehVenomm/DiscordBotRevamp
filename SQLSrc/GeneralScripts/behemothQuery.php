<?php
if(isset($_POST['submit'])){
    $name           = '';
    $element        = '';
    $wepType        = '';
    $wepTier        = '';
    $wepAbility     = '';
    $armourAbility  = '';

    $queryInput = $_POST['query'];
  
    include "../Tools/conexao.php";
    $sql = "SELECT behemoth.Name, behemoth.Element, weapontable.Type, weapontable.Tier, weapontable.Ability as wepAbility, armourtable.Ability as armourAbility FROM behemothtable as behemoth
    LEFT JOIN weapontable ON weapontable.IdWeapon = behemoth.IdWeapon_BehemothTable
    LEFT JOIN armourtable ON armourtable.IdBehemoth_ArmourTable = behemoth.IdBehemoth
    WHERE behemoth.name LIKE '%$queryInput%' GROUP BY behemoth.Name";
    $query = $conex -> prepare($sql);
    try{
        $query -> execute();
    } catch (Exception $behemothQuery) {
        echo 'Caught exception: ',  $query->getMessage(), "</br>";
    }
    $qty = $query -> rowCount();
    if ($qty == 1){
        foreach ($query as $x){
            $name = $x['Name'];
            $element = $x['Element'];
            $wepType = $x['Type'];
            $wepTier = $x['Tier'];
            $wepAbility = $x['wepAbility'];
            $armourAbility = $x['armourAbility'];
            
        }
    } else {
        echo "nothing found!";
    }
    echo $name." - ".$element." - ".$wepType." - ".$wepTier." - ".$wepAbility." - ".$armourAbility;
}

?>

<form action="" method="POST">
<input type="text" name="query">
<input type="submit" name="submit" value="enviar">
</form>