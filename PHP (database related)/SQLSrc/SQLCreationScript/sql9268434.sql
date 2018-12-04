-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 28-Jul-2018 às 08:09
-- Versão do servidor: 10.1.34-MariaDB
-- PHP Version: 7.2.7

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
  `IdWeapon_BehemothTable` int(11) NOT NULL
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
(2, 'Felnarog', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/a/a4/SS_Felna.png?version=b28e1b21d7300c1229fdeef644acb146'),
(3, 'Reaper', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/d/d1/SS_Reaper.png?version=5f4df3d3f1a032b9b6b29a410c0eda5a'),
(4, 'Ovidius', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/9/96/SS_Ovid.png?version=f8fea5056a90915d421bce67b03152a7'),
(5, 'Akra', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/a/a8/SS_Akra.png?version=4490ed6f703971e33bb9b438cd76578e'),
(6, 'Mephitus', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/4/49/SS_Mephitus.png?version=dc7091fc5cd42be4462a1bbe5c8d8da2'),
(7, 'Yggdra', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/8/87/Yggdragis.png?version=4b5e877dad08114c2efac2c4e6bcaa0e'),
(8, 'Pandemon', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/8/8b/Pandemon.png?version=6b004dde87fd86e1e69645a1909e530c'),
(9, 'Amarok', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/9/97/Amarok.png?version=de165a5c1a9619c18e78f52a22dfefcd'),
(10, 'Houran', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/6/68/Houran.png?version=c93f57e08a7c4c4661e8ba121ac374ae'),
(11, 'Galdon', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/2/29/Galdon.png?version=b893fa5df12bff2bb83ffe82bdc61466'),
(12, 'Empiris', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/0/0e/Emphi.png?version=c56ccfa66d8a5c2d9e7b1b622235fcc1'),
(13, 'Abaia', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/7/7b/Abaia.png?version=3c541cc498b05f1f2ae1b821c2e24023'),
(14, 'Mudigger', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/0/0c/Mudigger.png?version=a3ba3b2c859f1ac2cd25b858ad873c9e'),
(15, 'Wicked Blossom King', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/d/dd/Wbk.png?version=b9842dbaf234b927b92cfd6e08db7990'),
(16, 'Thundering Blossom King', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/7/7a/Tbk.png?version=20eeeaa1335d76def5c563ec77d8c1be'),
(17, 'Morphose', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/4/45/Vemerphose.png?version=e19dd6f22d24633922578ff79ee10509'),
(18, 'Infina', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/2/2b/Infina.png?version=7543c3b51551193e7bac521720347079'),
(19, 'Aragami', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/2/2f/Aragami.png?version=953b776f75de2461c2e89b974d7f01a3'),
(20, 'Khong', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/9/9f/Khongtransparenticon.png?version=8012fad0a71ce8b95933fb44a42f9413'),
(21, 'Ciel', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/8/87/Ciel.png?version=85509747353981822c1981b196d62ed2'),
(22, 'Necroth', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/2/27/Necroth.png?version=e22f0e9e6bd651a8dd05b58df10a9a8f'),
(23, 'Ayame', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/4/4f/Ayame.png?version=fc5f51f53da7667e8fc4482539fd306b'),
(24, 'Yurami', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/0/0a/Yurami.png?version=67c844becf6ebc79359b90cb4ef1b95c'),
(25, 'Zylant', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/a/a2/Zylant.png?version=fb69af2ff29c78d3a3ed343e8c58b4e7'),
(26, 'Magna', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/6/6d/Magna.png?version=69d26d3428e11df54f0ef5e32ff4fe17'),
(27, 'Tzaran', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/8/8e/Tzaran.png?version=691218eb623de79eced0059f482f8781'),
(28, 'Thalmus', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/0/0b/Thalmus.png?version=690815f7d04a6647f2c4e573290b49bf'),
(29, 'Lich', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/8/86/Lich.png?version=4c8623c4ea1703a6b333602a2ca8e12c'),
(30, 'Fantail', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/b/b6/Fantail.png?version=9048dd58a966432177e4214652930356'),
(31, 'Mercurius', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/6/6d/Mercurius.png?version=0fa805b6cdadab9c4eeb6760926858de'),
(32, 'Anubis', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/2/26/Anubis.png?version=d2a629a89b4984c9131c60b2f8977f88'),
(33, 'Azdaja', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/3/38/Azdaja.png?version=1d772d5c92b5e5d4b9aa4eb9366df39d'),
(34, 'Gorynych', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/5/52/Gorynych.png?version=8af243caa2721a3669664ce2fd9cf91b'),
(35, 'Golden Ovidium ★', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/9/96/SS_Ovid.png?version=f8fea5056a90915d421bce67b03152a7'),
(36, 'Trumpa', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/9/9b/Gumbatransparenticon.png?version=241d67a9800fa65300a0b1b31f3d9a09'),
(37, 'Carniva', 'https://d1u5p3l4wpay3k.cloudfront.net/dragonproject_gamepedia_en/f/f1/Carnivatransparenticon.png?version=1662f853111d662667a0b36e8d9fd87a'),
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
  `Cooldown` varchar(50) NOT NULL,
  `HealAmount` varchar(50) NOT NULL,
  `Description` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `Obs` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `IdMagiType_MagiTable` int(11) NOT NULL
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
  ADD CONSTRAINT `armourtable_ibfk_1` FOREIGN KEY (`IdArmourtype_ArmourTable`) REFERENCES `armourtypelist` (`idArmourTypeList`) ON DELETE CASCADE ON UPDATE CASCADE,
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