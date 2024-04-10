-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--

-- Author   :Prajwal Kedari
-- github   :@prajwalkedari
-- repo    :prajwalkedari/scholarsync
-- license :MIT
--
-- Database: `scholarsync`
--
CREATE DATABASE scholarsync;
use scholarsync;
-- Table structure for table `noteUpdate`


CREATE TABLE `noteupdate` (
  `NoteId` int(5) NOT NULL,
  `Subject` varchar(10) NOT NULL,
  `sem` varchar(10) NOT NULL,
  `Branch` varchar(20) NOT NULL,
  `Ref` varchar(20) NOT NULL,
  `DescNote` tinytext NOT NULL,
  `Path` tinytext NOT NULL,
  `Student_id` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Table structure for table `student`


CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `uname` varchar(10) NOT NULL,
  `psk` varchar(20) NOT NULL,
  `branch` varchar(20) NOT NULL,
  `year` int(2) NOT NULL,
  `rollno` int(10) NOT NULL,
  `email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

ALTER TABLE `noteupdate`
  ADD PRIMARY KEY (`NoteId`),
  ADD KEY `Student_id` (`Student_id`);


ALTER TABLE `noteupdate`
  ADD CONSTRAINT `noteupdate_ibfk_1` FOREIGN KEY (`Student_id`) REFERENCES `student` (`id`);
COMMIT;
