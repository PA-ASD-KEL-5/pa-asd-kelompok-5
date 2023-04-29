-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 29 Apr 2023 pada 12.58
-- Versi server: 10.4.27-MariaDB
-- Versi PHP: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `contact`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `nomor_telepon`
--

CREATE TABLE `nomor_telepon` (
  `nama` varchar(40) NOT NULL,
  `nomor` varchar(13) NOT NULL,
  `email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `nomor_telepon`
--

INSERT INTO `nomor_telepon` (`nama`, `nomor`, `email`) VALUES
('dgfhghj', '0989765433', 'tia@gmail.com'),
('lkjfgsf', '234567', 'tia@gmail.com'),
('wertyuyiuo', '567898', 'tia@gmail.com'),
('sanrina', '666', 'sagita@gmail.com'),
('tia', '222', 'sagita@gmail.com'),
('bayu', '111111111', 'anu'),
('arya', '2222222222222', 'anu'),
('doni', '3333333', 'anu'),
('mboh', '66666', 'anu');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `email` varchar(40) NOT NULL,
  `password` varchar(20) NOT NULL,
  `no_telepon` varchar(13) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`email`, `password`, `no_telepon`) VALUES
('novi@gmail.com', 'novi', '085821658572'),
('tia@gmail.com', 'tia', '0881026814105'),
('sagita@gmail.com', '12', '081313348205'),
('wahyu', 'wahyu', '1111111111'),
('sari', 'sari', '44444444444'),
('anu', 'anu', '5555555');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
