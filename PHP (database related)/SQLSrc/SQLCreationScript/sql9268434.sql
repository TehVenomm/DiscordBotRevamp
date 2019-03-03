-- phpMyAdmin SQL Dump
-- version 4.8.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 03-Jan-2019 às 12:37
-- Versão do servidor: 10.1.31-MariaDB
-- PHP Version: 7.0.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sql9268434`
--
CREATE DATABASE IF NOT EXISTS `sql9268434` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `sql9268434`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `armourtable`
--

CREATE TABLE `armourtable` (
  `Idarmour` int(11) NOT NULL,
  `DefElement` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `HpValue` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `PhysDef` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `ElemDef` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `PhysAttack` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Ability` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `Obs` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `IdArmourtype_ArmourTable` int(11) NOT NULL,
  `IdBehemoth_ArmourTable` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `armourtypelist`
--

CREATE TABLE `armourtypelist` (
  `IdArmourTypeList` int(11) NOT NULL,
  `Name` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `armourtypelist`
--

INSERT INTO `armourtypelist` (`IdArmourTypeList`, `Name`) VALUES
(1, 'Helmet'),
(2, 'Chest'),
(3, 'Gloves'),
(4, 'Legs');

-- --------------------------------------------------------

--
-- Estrutura da tabela `behemothtable`
--

CREATE TABLE `behemothtable` (
  `IdBehemoth` int(11) NOT NULL,
  `Name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `Element` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `IdWeapon_BehemothTable` int(11) NOT NULL,
  `name_clean` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `icontable`
--

CREATE TABLE `icontable` (
  `idIcon` int(11) NOT NULL,
  `behemothName` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `imageLink` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `icontable`
--

INSERT INTO `icontable` (`idIcon`, `behemothName`, `imageLink`) VALUES
(1, 'Genman', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/7/75/SS_Gigantor.png?version=c96abf8efbfdd65d6070aea4508dca4e'),
(2, 'Felnarog', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/a/a4/SS_Felna.png?version=0bf26453758cdf3686c5a971d4f3eaf1'),
(3, 'Reaper', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/d/d1/SS_Reaper.png?version=5dcceb4bf19d7cf240867ab50f1060c3'),
(4, 'Ovidius', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/9/96/SS_Ovid.png?version=6f8febccd337dbed56c8bea23aaa190b'),
(5, 'Akra', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/a/a8/SS_Akra.png?version=62aacba0779232045571c38ec4b52c38'),
(6, 'Mephitus', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/4/49/SS_Mephitus.png?version=7991d1a686ab40e039f52eb96fdf5f88'),
(7, 'Yggdra', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/8/87/Yggdragis.png?version=b521155b969dc9bdf6ee24ac1c413554'),
(8, 'Pandemon', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/8/8b/Pandemon.png?version=0ba8c57263f0492e77fdca1c028c42f0'),
(9, 'Amarok', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/9/97/Amarok.png?version=67290633cbac6ac0ba1026191b4858bf'),
(10, 'Houran', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/6/68/Houran.png?version=5c4d94359edec813bcd018bcde020bfb'),
(11, 'Galdon', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/2/29/Galdon.png?version=c9c5a22df1abd96c640cd5e7f3b60f43'),
(12, 'Empiris', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/0/0e/Emphi.png?version=cc3e6e762b97f3dc8fab53d414e2a82d'),
(13, 'Abaia', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/7/7b/Abaia.png?version=07f6e9c9ec4a385be9b79d5f9bb4311d'),
(14, 'Mudigger', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/0/0c/Mudigger.png?version=614d4b1d8927e179c18dc8f880bb66ed'),
(15, 'Wicked Blossom King', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/d/dd/Wbk.png?version=704c11724af760ea0e55c91611143e98'),
(16, 'Thundering Blossom King', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/7/7a/Tbk.png?version=d666133068d60b45f94f4dbce938c04e'),
(17, 'Morphose', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/4/45/Vemerphose.png?version=f0574e2112fed2614144a9c7fab47112'),
(18, 'Infina', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/2/2b/Infina.png?version=e231070da83ea12129973a6d44324a5a'),
(19, 'Aragami', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/2/2f/Aragami.png?version=3e4ee2fe44710ae12dd16533fb84e768'),
(20, 'Khong', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/9/9f/Khongtransparenticon.png?version=94a4bc074a31aa7942f5616dadf5efcc'),
(21, 'Ciel', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/8/87/Ciel.png?version=fe504a48fe61c72725a2b8630cf28ef6'),
(22, 'Necroth', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/2/27/Necroth.png?version=6ffc0d35e2abc19016b6cff7cd23a992'),
(23, 'Ayame', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/4/4f/Ayame.png?version=d1849b8ca832786a6495437b3e755f4a'),
(24, 'Yurami', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/0/0a/Yurami.png?version=296d675201594c22f1e0d305e21af78f'),
(25, 'Zylant', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/a/a2/Zylant.png?version=7d168134af72488e57fa9fb3daea811b'),
(26, 'Magna', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/6/6d/Magna.png?version=5085f13a47b247ae68599565ea716a77'),
(27, 'Tzaran', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/8/8e/Tzaran.png?version=4bf121e4c9e17f87d7d6c17ae7d22721'),
(28, 'Thalmus', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/0/0b/Thalmus.png?version=a0a0eac6b57b372807d06eb4b5906550'),
(29, 'Lich', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/8/86/Lich.png?version=b5b3f64ec72328202ad2098df0d21d8a'),
(30, 'Fantail', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/b/b6/Fantail.png?version=21ab6e747e7daefac94d35324225618d'),
(31, 'Mercurius', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/6/6d/Mercurius.png?version=12e5cc273f5759d6f2b9dc778942fbe5'),
(32, 'Anubis', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/2/26/Anubis.png?version=8160ec3f1b108403e214da7476db0d5b'),
(33, 'Azdaja', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/5/52/Gorynych.png?version=c09b4a28d0b874e8196d7751c6b40b9d'),
(34, 'Gorynych', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/5/52/Gorynych.png?version=c09b4a28d0b874e8196d7751c6b40b9d'),
(35, 'Golden Ovidium ★', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/9/96/SS_Ovid.png?version=6f8febccd337dbed56c8bea23aaa190b'),
(36, 'Trumpa', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/9/9b/Gumbatransparenticon.png?version=7577a88446022058251fb09531a5ed1d'),
(37, 'Carniva', 'https://gamepedia.cursecdn.com/dragonproject_gamepedia_en/f/f1/Carnivatransparenticon.png?version=1a89661cc8c80b68274bda042d179442'),
(38, 'DefaultMonster', 'https://cdn.discordapp.com/attachments/456208112790142977/471391941008031784/Main_page_monsters_background.png'),
(39, 'DefaultWeapon', 'https://cdn.discordapp.com/attachments/456208112790142977/471391945667641355/Main_page_weapons_background.png'),
(40, 'DefaultArmor', 'https://media.discordapp.net/attachments/456208112790142977/471391948192612354/Main_page_armor_background.png'),
(41, 'DefaultMagi', 'https://media.discordapp.net/attachments/456208112790142977/472631537289134080/Main_page_magi_background.png'),
(42, 'DefaultMagi', 'https://media.discordapp.net/attachments/456208112790142977/472631537289134080/Main_page_magi_background.png');

-- --------------------------------------------------------

--
-- Estrutura da tabela `magitable`
--

CREATE TABLE `magitable` (
  `IdMagi` int(11) NOT NULL,
  `Name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `Cooldown` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `HealAmount` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `Description` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `Obs` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `IdMagiType_MagiTable` int(11) NOT NULL,
  `name_clean` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `magitypelist`
--

CREATE TABLE `magitypelist` (
  `IdMagiType` int(11) NOT NULL,
  `Name` varchar(50) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Extraindo dados da tabela `magitypelist`
--

INSERT INTO `magitypelist` (`IdMagiType`, `Name`) VALUES
(1, 'Fire'),
(2, 'Water'),
(3, 'Earth'),
(4, 'Lightning'),
(5, 'Light'),
(6, 'Dark'),
(7, 'Hybrid'),
(8, 'Support'),
(9, 'Heal'),
(10, 'Passive');

-- --------------------------------------------------------

--
-- Estrutura da tabela `weapontable`
--

CREATE TABLE `weapontable` (
  `IdWeapon` int(11) NOT NULL,
  `Type` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `Tier` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `Element` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `PhysAttack` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `ElemAttack` varchar(20) COLLATE utf8_unicode_ci NOT NULL,
  `Ability` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `Obs` varchar(500) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `armourtable`
--
ALTER TABLE `armourtable`
  ADD PRIMARY KEY (`Idarmour`),
  ADD KEY `armourtable_ibfk_1` (`IdArmourtype_ArmourTable`),
  ADD KEY `armourtable_ibfk_2` (`IdBehemoth_ArmourTable`);

--
-- Indexes for table `armourtypelist`
--
ALTER TABLE `armourtypelist`
  ADD PRIMARY KEY (`IdArmourTypeList`);

--
-- Indexes for table `behemothtable`
--
ALTER TABLE `behemothtable`
  ADD PRIMARY KEY (`IdBehemoth`),
  ADD KEY `behemothtable_ibfk_2` (`IdWeapon_BehemothTable`);

--
-- Indexes for table `icontable`
--
ALTER TABLE `icontable`
  ADD PRIMARY KEY (`idIcon`);

--
-- Indexes for table `magitable`
--
ALTER TABLE `magitable`
  ADD PRIMARY KEY (`IdMagi`),
  ADD KEY `magitable_ibfk_1` (`IdMagiType_MagiTable`);

--
-- Indexes for table `magitypelist`
--
ALTER TABLE `magitypelist`
  ADD PRIMARY KEY (`IdMagiType`);

--
-- Indexes for table `weapontable`
--
ALTER TABLE `weapontable`
  ADD PRIMARY KEY (`IdWeapon`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `armourtable`
--
ALTER TABLE `armourtable`
  MODIFY `Idarmour` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `armourtypelist`
--
ALTER TABLE `armourtypelist`
  MODIFY `IdArmourTypeList` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `behemothtable`
--
ALTER TABLE `behemothtable`
  MODIFY `IdBehemoth` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `icontable`
--
ALTER TABLE `icontable`
  MODIFY `idIcon` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `magitable`
--
ALTER TABLE `magitable`
  MODIFY `IdMagi` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `magitypelist`
--
ALTER TABLE `magitypelist`
  MODIFY `IdMagiType` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `weapontable`
--
ALTER TABLE `weapontable`
  MODIFY `IdWeapon` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Limitadores para a tabela `armourtable`
--
ALTER TABLE `armourtable`
  ADD CONSTRAINT `armourtable_ibfk_1` FOREIGN KEY (`IdArmourtype_ArmourTable`) REFERENCES `armourtypelist` (`IdArmourTypeList`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `armourtable_ibfk_2` FOREIGN KEY (`IdBehemoth_ArmourTable`) REFERENCES `behemothtable` (`IdBehemoth`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `behemothtable`
--
ALTER TABLE `behemothtable`
  ADD CONSTRAINT `behemothtable_ibfk_2` FOREIGN KEY (`IdWeapon_BehemothTable`) REFERENCES `weapontable` (`IdWeapon`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Limitadores para a tabela `magitable`
--
ALTER TABLE `magitable`
  ADD CONSTRAINT `magitable_ibfk_1` FOREIGN KEY (`IdMagiType_MagiTable`) REFERENCES `magitypelist` (`IdMagiType`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
