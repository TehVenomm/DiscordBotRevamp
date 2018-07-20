<?php
    
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
        echo "shit in fire magi";

    if (!insertWaterMagi())
        echo "shit in Water magi";

    if (!insertEarthMagi())
        echo "shit in earth magi";

    if (!insertLightningMagi())
        echo "shit in lightning magi";

    if (!insertLightMagi())
        echo "shit in light magi";

    if (!insertDarkMagi())
        echo "shit in dark magi";

    if (!insertHybridMagi())
        echo "shit in hybrid magi";

    if (!insertSupportMagi())
        echo "shit in support magi";

    if (!insertHealMagi())
        echo "shit in heal magi";

    if (!insertPassiveMagi())
        echo "shit in passive magi";

    
?>
<a href="../../index.php">
    <input type="button" value="gz ur done">
</a>