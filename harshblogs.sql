-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 24, 2021 at 12:02 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `harshblogs`
--

-- --------------------------------------------------------

--
-- Table structure for table `blogsdata`
--

CREATE TABLE `blogsdata` (
  `sno` int(11) NOT NULL,
  `title` text NOT NULL,
  `subtitle` text NOT NULL,
  `slug` varchar(25) NOT NULL,
  `content` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `img` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `blogsdata`
--

INSERT INTO `blogsdata` (`sno`, `title`, `subtitle`, `slug`, `content`, `date`, `img`) VALUES
(0, '', '', '', '', '2021-06-05 18:34:40', ''),
(1, 'Being a special child', 'Myths and facts', 'Myths and facts', 'Standing out in a class of 50 students to solve the trickiest math problems of having magical talents in arts and music or anything of admiration are some traits defined by the society of a special child.\r\n\r\nBut what really makes a child special', '2021-06-24 14:31:49', ''),
(2, 'Family and Career', 'Importance and Priority', 'Importance and Priority', 'Well our family is what has actually made us this capable to pursue a career from our parents to our elders we were guided to pursue a career then what happens that somehow when we are actually passionate about making our career strive in the early stages of adulthood there comes this unsaid rift between us and family.', '2021-06-24 14:47:23', ''),
(3, 'Expense Manager App', 'manage your day to day expenses', 'manage your day to day ex', 'It is an app built to manage your day-to-day expenses by keeping a track of your expenses and notifying you about the expenditure and the due bills and the manages the in and out of money.', '2021-06-24 15:16:08', '');

-- --------------------------------------------------------

--
-- Table structure for table `contactsdata`
--

CREATE TABLE `contactsdata` (
  `sno` int(11) NOT NULL,
  `name` text NOT NULL,
  `email` varchar(40) NOT NULL,
  `phno` varchar(256) NOT NULL,
  `message` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contactsdata`
--

INSERT INTO `contactsdata` (`sno`, `name`, `email`, `phno`, `message`) VALUES
(1, 'Harsh', 'harsh@gmail.com', '9999999999', 'Hi this is dummy check text'),


--
-- Indexes for dumped tables
--

--
-- Indexes for table `blogsdata`
--
ALTER TABLE `blogsdata`
  ADD PRIMARY KEY (`sno`);

--
-- Indexes for table `contactsdata`
--
ALTER TABLE `contactsdata`
  ADD PRIMARY KEY (`sno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blogsdata`
--
ALTER TABLE `blogsdata`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `contactsdata`
--
ALTER TABLE `contactsdata`
  MODIFY `sno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
