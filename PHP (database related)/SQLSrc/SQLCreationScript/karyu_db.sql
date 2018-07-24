-- phpMyAdmin SQL Dump
-- version 4.8.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 24-Jul-2018 às 02:40
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
-- Database: `karyu_db`
--
CREATE DATABASE IF NOT EXISTS `karyu_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `karyu_db`;

-- --------------------------------------------------------

--
-- Estrutura da tabela `armourtable`
--

CREATE TABLE `armourtable` (
  `Idarmour` int(11) NOT NULL,
  `DefElement` text COLLATE utf8_unicode_ci NOT NULL,
  `HpValue` text COLLATE utf8_unicode_ci NOT NULL,
  `PhysDef` text COLLATE utf8_unicode_ci NOT NULL,
  `ElemDef` text COLLATE utf8_unicode_ci NOT NULL,
  `PhysAttack` text COLLATE utf8_unicode_ci NOT NULL,
  `Ability` text COLLATE utf8_unicode_ci NOT NULL,
  `Obs` text COLLATE utf8_unicode_ci NOT NULL,
  `IdArmourtype_ArmourTable` int(11) NOT NULL,
  `IdBehemoth_ArmourTable` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `armourtypelist`
--

CREATE TABLE `armourtypelist` (
  `IdArmourTypeList` int(11) NOT NULL,
  `Name` text COLLATE utf8_unicode_ci NOT NULL
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
  `Name` text COLLATE utf8_unicode_ci NOT NULL,
  `Element` text COLLATE utf8_unicode_ci NOT NULL,
  `IdWeapon_BehemothTable` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `magitable`
--

CREATE TABLE `magitable` (
  `IdMagi` int(11) NOT NULL,
  `Name` text COLLATE utf8_unicode_ci NOT NULL,
  `Cooldown` int(11) NOT NULL,
  `Description` text COLLATE utf8_unicode_ci NOT NULL,
  `Obs` text COLLATE utf8_unicode_ci NOT NULL,
  `IdMagiType_MagiTable` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `magitypelist`
--

CREATE TABLE `magitypelist` (
  `IdMagiType` int(11) NOT NULL,
  `Name` text COLLATE utf8_unicode_ci NOT NULL
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
-- Estrutura da tabela `ratingstable`
--

CREATE TABLE `ratingstable` (
  `IdRating` int(11) NOT NULL,
  `DraPro` text COLLATE utf8_unicode_ci NOT NULL,
  `Global` text COLLATE utf8_unicode_ci NOT NULL,
  `Japan` text COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `weapontable`
--

CREATE TABLE `weapontable` (
  `IdWeapon` int(11) NOT NULL,
  `Type` text COLLATE utf8_unicode_ci NOT NULL,
  `Tier` text COLLATE utf8_unicode_ci NOT NULL,
  `Element` text COLLATE utf8_unicode_ci NOT NULL,
  `PysAttack` text COLLATE utf8_unicode_ci NOT NULL,
  `ElemAttack` text COLLATE utf8_unicode_ci NOT NULL,
  `Ability` text COLLATE utf8_unicode_ci NOT NULL,
  `Obs` text COLLATE utf8_unicode_ci NOT NULL
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
-- Indexes for table `ratingstable`
--
ALTER TABLE `ratingstable`
  ADD PRIMARY KEY (`IdRating`);

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
  MODIFY `IdArmourTypeList` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `behemothtable`
--
ALTER TABLE `behemothtable`
  MODIFY `IdBehemoth` int(11) NOT NULL AUTO_INCREMENT;

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
-- AUTO_INCREMENT for table `ratingstable`
--
ALTER TABLE `ratingstable`
  MODIFY `IdRating` int(11) NOT NULL AUTO_INCREMENT;

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
