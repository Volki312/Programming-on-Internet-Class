-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 16, 2020 at 06:53 PM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `vj_5`
--

-- --------------------------------------------------------

--
-- Table structure for table `collections`
--

CREATE TABLE `collections` (
  `collection_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `collections`
--

INSERT INTO `collections` (`collection_id`, `name`) VALUES
(2, 'test'),
(3, 'temp'),
(5, 'testytest');

-- --------------------------------------------------------

--
-- Table structure for table `images`
--

CREATE TABLE `images` (
  `image_id` int(11) NOT NULL,
  `path` varchar(255) NOT NULL,
  `counter` int(11) NOT NULL,
  `created` timestamp NOT NULL DEFAULT current_timestamp(),
  `last` timestamp NOT NULL DEFAULT current_timestamp(),
  `collection_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `images`
--

INSERT INTO `images` (`image_id`, `path`, `counter`, `created`, `last`, `collection_id`) VALUES
(9, 'test/logo192.png', 24, '2020-01-14 14:56:01', '2020-01-16 14:37:21', 2),
(11, 'temp/logo192.png', 0, '2020-01-14 15:06:57', '2020-01-14 15:06:57', 3),
(12, 'testytest/logo512.png', 0, '2020-01-14 15:07:20', '2020-01-14 15:07:20', 5),
(13, 'test/logo192.png', 0, '2020-01-14 15:08:56', '2020-01-14 15:08:56', 2);

-- --------------------------------------------------------

--
-- Table structure for table `sessions`
--

CREATE TABLE `sessions` (
  `session_id` int(11) NOT NULL,
  `data` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sessions`
--

INSERT INTO `sessions` (`session_id`, `data`) VALUES
(1, '{\"user_id\": 2}'),
(8, '{\"user_id\": 7}'),
(9, '{\"user_id\": 7}'),
(12, '{\"user_id\": 10}'),
(13, '{\"user_id\": 7}'),
(14, '{\"user_id\": 10}'),
(15, '{\"user_id\": 7}'),
(17, '{\"user_id\": 7}'),
(18, '{\"user_id\": 10}'),
(19, '{\"user_id\": 7}'),
(20, '{\"user_id\": 7}'),
(21, '{\"user_id\": 10}');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `role` enum('admin','user','') NOT NULL,
  `username` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `email`, `password`, `role`, `username`) VALUES
(7, 'Josip312@hotmail.com', '$2b$12$VaIv/E1Z5XzHO5WeXnr3TeTk4GoOLsIw/X5m6QYq.u281DUfgRsqe', 'user', 'Josip'),
(8, 'josip.volarevic4@gmail.com', '$2b$12$xyT4zIT0ywIwTisi4Yr30ule5YQz/HrRKIdvlpvfUF37RnmWd8AeC', 'user', 'Test'),
(10, 'jv46250@oss.unist.hr', '$2b$12$TTy88ZEkvatRzQWKziUyfOKaFZ6/tVMNbyOkclon6SpPCW2xQM3iG', 'admin', 'Josip1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `collections`
--
ALTER TABLE `collections`
  ADD PRIMARY KEY (`collection_id`);

--
-- Indexes for table `images`
--
ALTER TABLE `images`
  ADD PRIMARY KEY (`image_id`),
  ADD KEY `collection_id` (`collection_id`);

--
-- Indexes for table `sessions`
--
ALTER TABLE `sessions`
  ADD PRIMARY KEY (`session_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `collections`
--
ALTER TABLE `collections`
  MODIFY `collection_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `images`
--
ALTER TABLE `images`
  MODIFY `image_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `sessions`
--
ALTER TABLE `sessions`
  MODIFY `session_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `images`
--
ALTER TABLE `images`
  ADD CONSTRAINT `images_ibfk_1` FOREIGN KEY (`collection_id`) REFERENCES `collections` (`collection_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
