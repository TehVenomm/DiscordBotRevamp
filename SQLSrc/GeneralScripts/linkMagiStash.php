<?php
    include "../Tools/genericFunctions.php";
    include "../MagiScripts/FireMagi.php";
    include "../MagiScripts/WaterMagi.php";
    include "../MagiScripts/EarthMagi.php";
    include "../MagiScripts/LightningMagi.php";
    include "../MagiScripts/LightMagi.php";
    include "../MagiScripts/DarkMagi.php";
    include "../MagiScripts/HybridMagi.php";
    include "../MagiScripts/SupportMagi.php";
    include "../MagiScripts/HealMagi.php";
    include "../MagiScripts/PassiveMagi.php";

    if (!insertFireMagi())
        echo "Error in fire magi";

    if (!insertWaterMagi())
        echo "Error in Water magi";

    if (!insertEarthMagi())
        echo "Error in earth magi";

    if (!insertLightningMagi())
        echo "Error in lightning magi";

    if (!insertLightMagi())
        echo "Error in light magi";

    if (!insertDarkMagi())
        echo "Error in dark magi";

    if (!insertHybridMagi())
        echo "Error in hybrid magi";

    if (!insertSupportMagi())
        echo "Error in support magi";

    if (!insertHealMagi())
        echo "Error in heal magi";

    if (!insertPassiveMagi())
        echo "Error in passive magi";
    
?>

<a href="../../index.php">
    <input type="button" value="gz ur done">
</a>