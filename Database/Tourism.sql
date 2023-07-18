-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 18, 2023 at 08:21 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `trs`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_details`
--

CREATE TABLE `customer_details` (
  `customer_id` int(11) NOT NULL,
  `customer_username` varchar(100) DEFAULT NULL,
  `customer_name` varchar(30) DEFAULT NULL,
  `email` varchar(200) DEFAULT NULL,
  `mobileno` bigint(10) DEFAULT NULL,
  `customer_password` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_details`
--

INSERT INTO `customer_details` (`customer_id`, `customer_username`, `customer_name`, `email`, `mobileno`, `customer_password`) VALUES
(1, 'akash11', 'akash kalloli', 'akash11@gmail.com', 9595009501, 'akash11');

-- --------------------------------------------------------

--
-- Table structure for table `customer_query`
--

CREATE TABLE `customer_query` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `customer_name` varchar(20) NOT NULL,
  `customer_email` varchar(60) NOT NULL,
  `customer_number` varchar(11) NOT NULL,
  `customer_message` varchar(100) NOT NULL,
  `employee_reply` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('h6oz202flt7b88gedohcsfdxsgxr6hrv', 'eyJ1c2VybmFtZSI6ImFrYXNoMTEiLCJhZG1pbl91c2VybmFtZSI6InNhbmtldEAzMyJ9:1qKNct:Y2ZVM9_N7YaqOdglgV6VqFGWAG05cFrF99BWWXG2X8Y', '2023-07-28 18:34:47.661723');

-- --------------------------------------------------------

--
-- Table structure for table `hotel_booking`
--

CREATE TABLE `hotel_booking` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `customer_name` varchar(40) NOT NULL,
  `customer_email` varchar(40) NOT NULL,
  `customer_number` varchar(11) NOT NULL,
  `room_booked` varchar(3) NOT NULL,
  `no_of_people` varchar(3) NOT NULL,
  `hotel_checkin` date NOT NULL,
  `hotel_checkout` date NOT NULL,
  `date_booked` date NOT NULL,
  `hotel_status` int(11) NOT NULL COMMENT '0 = Approve\r\n1 = Initialise\r\n2 = Denied\r\n'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hotel_booking`
--

INSERT INTO `hotel_booking` (`id`, `customer_id`, `customer_name`, `customer_email`, `customer_number`, `room_booked`, `no_of_people`, `hotel_checkin`, `hotel_checkout`, `date_booked`, `hotel_status`) VALUES
(4, 1, 'SURAJ PANDURANG GIRI', 'surajgiri974@gmail.com', '8308149964', '1', '1', '2023-07-14', '2023-07-15', '2023-07-14', 0);

-- --------------------------------------------------------

--
-- Table structure for table `payment`
--

CREATE TABLE `payment` (
  `id` int(11) NOT NULL,
  `paid_date` date DEFAULT NULL,
  `paid_amount` float DEFAULT NULL,
  `paid_status` int(2) DEFAULT NULL,
  `paid_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payment`
--

INSERT INTO `payment` (`id`, `paid_date`, `paid_amount`, `paid_status`, `paid_by`) VALUES
(4, '2023-07-15', 30000, 0, 1),
(6, '2023-07-15', 30000, 0, 1),
(7, '2023-07-15', 30000, 0, 1),
(8, '2023-07-15', 30000, 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `tourism_plan`
--

CREATE TABLE `tourism_plan` (
  `plan_id` int(3) NOT NULL,
  `plan_name` varchar(40) DEFAULT NULL,
  `plan_details` varchar(200) DEFAULT NULL,
  `plan_duration` varchar(100) DEFAULT NULL,
  `plan_amount` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tourism_plan`
--

INSERT INTO `tourism_plan` (`plan_id`, `plan_name`, `plan_details`, `plan_duration`, `plan_amount`) VALUES
(103, 'Kedarnath', 'Nice Temple', '7', 30000),
(104, 'Kashmir', 'Mountains', '7', 60000);

-- --------------------------------------------------------

--
-- Table structure for table `tour_registration`
--

CREATE TABLE `tour_registration` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `customer_name` varchar(30) NOT NULL,
  `customer_email` varchar(60) NOT NULL,
  `customer_phone` varchar(12) NOT NULL,
  `customer_address` varchar(100) NOT NULL,
  `customer_gender` varchar(8) NOT NULL,
  `customer_country` varchar(20) NOT NULL,
  `customer_state` varchar(20) NOT NULL,
  `customer_passport` varchar(10) NOT NULL,
  `customer_selected_package` int(3) NOT NULL,
  `trip_startdate` date NOT NULL,
  `trip_enddate` date NOT NULL,
  `trip_amt` float NOT NULL,
  `customer_payment` float NOT NULL,
  `trip_status` int(1) NOT NULL COMMENT '0 = "Initialise"\r\n1 = "Ongoing"\r\n2 = "Completed"\r\n3 = "Cancelled"\r\n'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tour_registration`
--

INSERT INTO `tour_registration` (`id`, `customer_id`, `customer_name`, `customer_email`, `customer_phone`, `customer_address`, `customer_gender`, `customer_country`, `customer_state`, `customer_passport`, `customer_selected_package`, `trip_startdate`, `trip_enddate`, `trip_amt`, `customer_payment`, `trip_status`) VALUES
(1, 1, 'Akash', 'akash@gmail.com', '8308139963', 'Pune', 'Male', 'India', 'Maharashtra', 'jdagh2dabs', 103, '2023-07-14', '2023-07-23', 30000, 2000, 2),
(9, 1, 'SURAJ GIRI', 'surajgiri974@gmail.com', '08308149964', 'Sr. No. 26 1 Laxmibai Nandgude colony near mahadev nivas vishal nagar pimple nilakh pune', 'Male', 'India', 'Maharashtra', 'msdgkadgka', 103, '2022-07-20', '2000-10-01', 30000, 0, 2);

-- --------------------------------------------------------

--
-- Table structure for table `trs_employee`
--

CREATE TABLE `trs_employee` (
  `emp_id` int(10) NOT NULL,
  `emp_name` varchar(50) NOT NULL,
  `emp_address` varchar(100) NOT NULL,
  `emp_dob` date NOT NULL,
  `emp_email` varchar(200) NOT NULL,
  `emp_mobno` bigint(11) NOT NULL,
  `emp_sal` float NOT NULL,
  `emp_type` int(1) NOT NULL COMMENT '0 = Administrator\r\n1 = Employee',
  `emp_username` varchar(100) NOT NULL,
  `emp_password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `trs_employee`
--

INSERT INTO `trs_employee` (`emp_id`, `emp_name`, `emp_address`, `emp_dob`, `emp_email`, `emp_mobno`, `emp_sal`, `emp_type`, `emp_username`, `emp_password`) VALUES
(1, 'sanket', 'kolhapur', '0000-00-00', 'sanket@gmail.com', 9860854417, 10000, 0, 'sanket@33', 'sanket@33');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_registration`
--

CREATE TABLE `vehicle_registration` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) NOT NULL,
  `customer_name` varchar(50) NOT NULL,
  `customer_license` varchar(16) NOT NULL,
  `customer_email` varchar(60) NOT NULL,
  `customer_phone` varchar(11) NOT NULL,
  `customer_pickup` date NOT NULL,
  `customer_drop` date NOT NULL,
  `vehicle_type` varchar(20) NOT NULL,
  `city` varchar(15) NOT NULL,
  `amount` float NOT NULL,
  `vehicle_status` int(11) NOT NULL COMMENT '0 = Approve\r\n1 = Initialise\r\n2 = Denied'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vehicle_registration`
--

INSERT INTO `vehicle_registration` (`id`, `customer_id`, `customer_name`, `customer_license`, `customer_email`, `customer_phone`, `customer_pickup`, `customer_drop`, `vehicle_type`, `city`, `amount`, `vehicle_status`) VALUES
(2, 1, 'Suraj', 'MH14Ksdkjgadkgk2', 'surajgiri974@gmail.com', '8308149964', '2023-01-01', '2023-01-02', 'Two Wheeler', 'PCMC', 640, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer_details`
--
ALTER TABLE `customer_details`
  ADD PRIMARY KEY (`customer_id`),
  ADD UNIQUE KEY `customer_username` (`customer_username`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `mobileno` (`mobileno`);

--
-- Indexes for table `customer_query`
--
ALTER TABLE `customer_query`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `hotel_booking`
--
ALTER TABLE `hotel_booking`
  ADD PRIMARY KEY (`id`),
  ADD KEY `customer_id` (`customer_id`);

--
-- Indexes for table `payment`
--
ALTER TABLE `payment`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tourism_plan`
--
ALTER TABLE `tourism_plan`
  ADD PRIMARY KEY (`plan_id`);

--
-- Indexes for table `tour_registration`
--
ALTER TABLE `tour_registration`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `customer_passport` (`customer_passport`),
  ADD KEY `customer_id` (`customer_id`),
  ADD KEY `customer_selected_package` (`customer_selected_package`);

--
-- Indexes for table `trs_employee`
--
ALTER TABLE `trs_employee`
  ADD PRIMARY KEY (`emp_id`);

--
-- Indexes for table `vehicle_registration`
--
ALTER TABLE `vehicle_registration`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `customer_license` (`customer_license`),
  ADD KEY `customer_id` (`customer_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer_details`
--
ALTER TABLE `customer_details`
  MODIFY `customer_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `customer_query`
--
ALTER TABLE `customer_query`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `hotel_booking`
--
ALTER TABLE `hotel_booking`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `payment`
--
ALTER TABLE `payment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `tourism_plan`
--
ALTER TABLE `tourism_plan`
  MODIFY `plan_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=105;

--
-- AUTO_INCREMENT for table `tour_registration`
--
ALTER TABLE `tour_registration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `trs_employee`
--
ALTER TABLE `trs_employee`
  MODIFY `emp_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `vehicle_registration`
--
ALTER TABLE `vehicle_registration`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `customer_query`
--
ALTER TABLE `customer_query`
  ADD CONSTRAINT `customer_query_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer_details` (`customer_id`);

--
-- Constraints for table `hotel_booking`
--
ALTER TABLE `hotel_booking`
  ADD CONSTRAINT `hotel_booking_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer_details` (`customer_id`);

--
-- Constraints for table `payment`
--
ALTER TABLE `payment`
  ADD CONSTRAINT `payment_ibfk_1` FOREIGN KEY (`paid_by`) REFERENCES `customer_details` (`customer_id`);

--
-- Constraints for table `tour_registration`
--
ALTER TABLE `tour_registration`
  ADD CONSTRAINT `tour_registration_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer_details` (`customer_id`),
  ADD CONSTRAINT `tour_registration_ibfk_2` FOREIGN KEY (`customer_selected_package`) REFERENCES `tourism_plan` (`plan_id`);

--
-- Constraints for table `vehicle_registration`
--
ALTER TABLE `vehicle_registration`
  ADD CONSTRAINT `vehicle_registration_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customer_details` (`customer_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
