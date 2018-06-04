-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: 04 Jun 2018 pada 11.29
-- Versi Server: 10.1.21-MariaDB
-- PHP Version: 7.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `project_management`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `audit_trail`
--

CREATE TABLE `audit_trail` (
  `AuditTrail_ID` varchar(10) NOT NULL,
  `Audit_Activity` varchar(50) NOT NULL,
  `Audit_Field` varchar(20) NOT NULL,
  `Audit_Before` varchar(50) NOT NULL,
  `Audit_After` varchar(50) NOT NULL,
  `Audit_Date` date NOT NULL,
  `Audit_Time` time NOT NULL,
  `Audit_User` varchar(7) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `city`
--

CREATE TABLE `city` (
  `city_code` varchar(20) NOT NULL DEFAULT '0',
  `city_name` varchar(50) NOT NULL,
  `province_id` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `city`
--

INSERT INTO `city` (`city_code`, `city_name`, `province_id`) VALUES
('CITY00001', 'Kabupaten Simeulue', 'PROV00001'),
('CITY00002', 'Kabupaten Aceh Singkil', 'PROV00001'),
('CITY00003', 'Kabupaten Aceh Selatan', 'PROV00001'),
('CITY00004', 'Kabupaten Aceh Tenggara', 'PROV00001'),
('CITY00005', 'Kabupaten Aceh Timur', 'PROV00001'),
('CITY00006', 'Kabupaten Aceh Tengah', 'PROV00001'),
('CITY00007', 'Kabupaten Aceh Barat', 'PROV00001'),
('CITY00008', 'Kabupaten Aceh Besar', 'PROV00001'),
('CITY00009', 'Kabupaten Pidie', 'PROV00001'),
('CITY00010', 'Kabupaten Bireuen', 'PROV00001'),
('CITY00011', 'Kabupaten Aceh Utara', 'PROV00001'),
('CITY00012', 'Kabupaten Aceh Barat Daya', 'PROV00001'),
('CITY00013', 'Kabupaten Gayo Lues', 'PROV00001'),
('CITY00014', 'Kabupaten Aceh Tamiang', 'PROV00001'),
('CITY00015', 'Kabupaten Nagan Raya', 'PROV00001'),
('CITY00016', 'Kabupaten Aceh Jaya', 'PROV00001'),
('CITY00017', 'Kabupaten Bener Meriah', 'PROV00001'),
('CITY00018', 'Kabupaten Pidie Jaya', 'PROV00001'),
('CITY00019', 'Kota Banda Aceh', 'PROV00001'),
('CITY00020', 'Kota Sabang', 'PROV00001'),
('CITY00021', 'Kota Langsa', 'PROV00001'),
('CITY00022', 'Kota Lhokseumawe', 'PROV00001'),
('CITY00023', 'Kota Subulussalam', 'PROV00001'),
('CITY00024', 'Kabupaten nias	', 'PROV00002'),
('CITY00025', 'Kabupaten mandailing natal	', 'PROV00002'),
('CITY00026', 'Kabupaten tapanuli Selatan	', 'PROV00002'),
('CITY00027', 'Kabupaten tapanuli Tengah	', 'PROV00002'),
('CITY00028', 'Kabupaten tapanuli Utara	', 'PROV00002'),
('CITY00029', 'Kabupaten toba samosir	', 'PROV00002'),
('CITY00030', 'Kabupaten labuhan batu	', 'PROV00002'),
('CITY00031', 'Kabupaten asahan	', 'PROV00002'),
('CITY00032', 'Kabupaten simalungun	', 'PROV00002'),
('CITY00033', 'Kabupaten dairi	', 'PROV00002'),
('CITY00034', 'Kabupaten karo	', 'PROV00002'),
('CITY00035', 'Kabupaten deli serdang	', 'PROV00002'),
('CITY00036', 'Kabupaten langkat	', 'PROV00002'),
('CITY00037', 'Kabupaten nias Selatan	', 'PROV00002'),
('CITY00038', 'Kabupaten humbang hasundutan	', 'PROV00002'),
('CITY00039', 'Kabupaten pakpak bharat	', 'PROV00002'),
('CITY00040', 'Kabupaten samosir	', 'PROV00002'),
('CITY00041', 'Kabupaten serdang bedagai	', 'PROV00002'),
('CITY00042', 'Kabupaten batu bara	', 'PROV00002'),
('CITY00043', 'Kabupaten padang lawas Utara	', 'PROV00002'),
('CITY00044', 'Kabupaten padang lawas	', 'PROV00002'),
('CITY00045', 'Kabupaten labuhan batu Selatan	', 'PROV00002'),
('CITY00046', 'Kabupaten labuhan batu Utara	', 'PROV00002'),
('CITY00047', 'Kabupaten nias Utara	', 'PROV00002'),
('CITY00048', 'Kabupaten nias Barat	', 'PROV00002'),
('CITY00049', 'Kota sibolga	', 'PROV00002'),
('CITY00050', 'Kota tanjung balai	', 'PROV00002'),
('CITY00051', 'Kota pematang siantar	', 'PROV00002'),
('CITY00052', 'Kota tebing tinggi	', 'PROV00002'),
('CITY00053', 'Kota medan	', 'PROV00002'),
('CITY00054', 'Kota binjai	', 'PROV00002'),
('CITY00055', 'Kota padangsidimpuan	', 'PROV00002'),
('CITY00056', 'Kota gunungsitoli	', 'PROV00002'),
('CITY00057', 'Kabupaten kepulauan mentawai	', 'PROV00003'),
('CITY00058', 'Kabupaten pesisir Selatan	', 'PROV00003'),
('CITY00059', 'Kabupaten solok	', 'PROV00003'),
('CITY00060', 'Kabupaten sijunjung	', 'PROV00003'),
('CITY00061', 'Kabupaten tanah datar	', 'PROV00003'),
('CITY00062', 'Kabupaten padang pariaman	', 'PROV00003'),
('CITY00063', 'Kabupaten agam	', 'PROV00003'),
('CITY00064', 'Kabupaten lima puluh Kota	', 'PROV00003'),
('CITY00065', 'Kabupaten pasaman	', 'PROV00003'),
('CITY00066', 'Kabupaten solok Selatan	', 'PROV00003'),
('CITY00067', 'Kabupaten dharmasraya	', 'PROV00003'),
('CITY00068', 'Kabupaten pasaman Barat	', 'PROV00003'),
('CITY00069', 'Kota padang	', 'PROV00003'),
('CITY00070', 'Kota solok	', 'PROV00003'),
('CITY00071', 'Kota sawah lunto	', 'PROV00003'),
('CITY00072', 'Kota padang panjang	', 'PROV00003'),
('CITY00073', 'Kota bukittinggi	', 'PROV00003'),
('CITY00074', 'Kota payakumbuh	', 'PROV00003'),
('CITY00075', 'Kota pariaman	', 'PROV00003'),
('CITY00076', 'Kabupaten kuantan singingi	', 'PROV00004'),
('CITY00077', 'Kabupaten indragiri hulu	', 'PROV00004'),
('CITY00078', 'Kabupaten indragiri hilir	', 'PROV00004'),
('CITY00079', 'Kabupaten pelalawan	', 'PROV00004'),
('CITY00080', 'Kabupaten siak	', 'PROV00004'),
('CITY00081', 'Kabupaten kampar	', 'PROV00004'),
('CITY00082', 'Kabupaten rokan hulu	', 'PROV00004'),
('CITY00083', 'Kabupaten bengkalis	', 'PROV00004'),
('CITY00084', 'Kabupaten rokan hilir	', 'PROV00004'),
('CITY00085', 'Kabupaten kepulauan meranti	', 'PROV00004'),
('CITY00086', 'Kota pekanbaru	', 'PROV00004'),
('CITY00087', 'Kota dumai	', 'PROV00004'),
('CITY00088', 'Kabupaten kerinci	', 'PROV00005'),
('CITY00089', 'Kabupaten merangin	', 'PROV00005'),
('CITY00090', 'Kabupaten sarolangun	', 'PROV00005'),
('CITY00091', 'Kabupaten batang hari	', 'PROV00005'),
('CITY00092', 'Kabupaten muaro jambi	', 'PROV00005'),
('CITY00093', 'Kabupaten tanjung jabung Timur	', 'PROV00005'),
('CITY00094', 'Kabupaten tanjung jabung Barat	', 'PROV00005'),
('CITY00095', 'Kabupaten tebo	', 'PROV00005'),
('CITY00096', 'Kabupaten bungo	', 'PROV00005'),
('CITY00097', 'Kota Jambi	', 'PROV00005'),
('CITY00098', 'Kota sungai penuh	', 'PROV00005'),
('CITY00099', 'Kabupaten ogan komering ulu	', 'PROV00006'),
('CITY00100', 'Kabupaten ogan komering ilir	', 'PROV00006'),
('CITY00101', 'Kabupaten muara enim	', 'PROV00006'),
('CITY00102', 'Kabupaten lahat	', 'PROV00006'),
('CITY00103', 'Kabupaten musi rawas	', 'PROV00006'),
('CITY00104', 'Kabupaten musi banyuasin	', 'PROV00006'),
('CITY00105', 'Kabupaten banyu asin	', 'PROV00006'),
('CITY00106', 'Kabupaten ogan komering ulu Selatan	', 'PROV00006'),
('CITY00107', 'Kabupaten ogan komering ulu Timur	', 'PROV00006'),
('CITY00108', 'Kabupaten ogan ilir	', 'PROV00006'),
('CITY00109', 'Kabupaten empat lawang	', 'PROV00006'),
('CITY00110', 'Kabupaten penukal abab lematang ilir	', 'PROV00006'),
('CITY00111', 'Kabupaten musi rawas Utara	', 'PROV00006'),
('CITY00112', 'Kota palembang	', 'PROV00006'),
('CITY00113', 'Kota prabumulih	', 'PROV00006'),
('CITY00114', 'Kota pagar alam	', 'PROV00006'),
('CITY00115', 'Kota lubuklinggau	', 'PROV00006'),
('CITY00116', 'Kabupaten Bengkulu Selatan	', 'PROV00007'),
('CITY00117', 'Kabupaten rejang lebong	', 'PROV00007'),
('CITY00118', 'Kabupaten Bengkulu Utara	', 'PROV00007'),
('CITY00119', 'Kabupaten kaur	', 'PROV00007'),
('CITY00120', 'Kabupaten seluma	', 'PROV00007'),
('CITY00121', 'Kabupaten mukomuko	', 'PROV00007'),
('CITY00122', 'Kabupaten lebong	', 'PROV00007'),
('CITY00123', 'Kabupaten kepahiang	', 'PROV00007'),
('CITY00124', 'Kabupaten Bengkulu Tengah	', 'PROV00007'),
('CITY00125', 'Kota Bengkulu	', 'PROV00007'),
('CITY00126', 'Kabupaten Lampung Barat	', 'PROV00007'),
('CITY00127', 'Kabupaten tanggamus	', 'PROV00008'),
('CITY00128', 'Kabupaten Lampung Selatan	', 'PROV00008'),
('CITY00129', 'Kabupaten Lampung Timur	', 'PROV00008'),
('CITY00130', 'Kabupaten Lampung Tengah	', 'PROV00008'),
('CITY00131', 'Kabupaten Lampung Utara	', 'PROV00008'),
('CITY00132', 'Kabupaten way kanan	', 'PROV00008'),
('CITY00133', 'Kabupaten tulangbawang	', 'PROV00008'),
('CITY00134', 'Kabupaten pesawaran	', 'PROV00008'),
('CITY00135', 'Kabupaten pringsewu	', 'PROV00008'),
('CITY00136', 'Kabupaten mesuji	', 'PROV00008'),
('CITY00137', 'Kabupaten tulang bawang Barat	', 'PROV00008'),
('CITY00138', 'Kabupaten pesisir Barat	', 'PROV00008'),
('CITY00139', 'Kota bandar Lampung	', 'PROV00008'),
('CITY00140', 'Kota metro	', 'PROV00008'),
('CITY00141', 'Kabupaten bangka	', 'PROV00009'),
('CITY00142', 'Kabupaten Belitung	', 'PROV00009'),
('CITY00143', 'Kabupaten bangka Barat	', 'PROV00009'),
('CITY00144', 'Kabupaten bangka Tengah	', 'PROV00009'),
('CITY00145', 'Kabupaten bangka Selatan	', 'PROV00009'),
('CITY00146', 'Kabupaten Belitung Timur	', 'PROV00009'),
('CITY00147', 'Kota pangkal pinang	', 'PROV00009'),
('CITY00148', 'Kabupaten karimun	', 'PROV00010'),
('CITY00149', 'Kabupaten bintan	', 'PROV00010'),
('CITY00150', 'Kabupaten natuna	', 'PROV00010'),
('CITY00151', 'Kabupaten lingga	', 'PROV00010'),
('CITY00152', 'Kabupaten kepulauan anambas	', 'PROV00010'),
('CITY00153', 'Kota b a t a m	', 'PROV00010'),
('CITY00154', 'Kota tanjung pinang	', 'PROV00010'),
('CITY00155', 'Kabupaten kepulauan seribu	', 'PROV00033'),
('CITY00156', 'Kota Jakarta Selatan	', 'PROV00033'),
('CITY00157', 'Kota Jakarta Timur	', 'PROV00033'),
('CITY00158', 'Kota Jakarta pusat	', 'PROV00033'),
('CITY00159', 'Kota Jakarta Barat	', 'PROV00033'),
('CITY00160', 'Kota Jakarta Utara	', 'PROV00033'),
('CITY00161', 'Kabupaten bogor	', 'PROV00011'),
('CITY00162', 'Kabupaten sukabumi	', 'PROV00011'),
('CITY00163', 'Kabupaten cianjur	', 'PROV00011'),
('CITY00164', 'Kabupaten bandung	', 'PROV00011'),
('CITY00165', 'Kabupaten garut	', 'PROV00011'),
('CITY00166', 'Kabupaten tasikmalaya	', 'PROV00011'),
('CITY00167', 'Kabupaten ciamis	', 'PROV00011'),
('CITY00168', 'Kabupaten kuningan	', 'PROV00011'),
('CITY00169', 'Kabupaten cirebon	', 'PROV00011'),
('CITY00170', 'Kabupaten majalengka	', 'PROV00011'),
('CITY00171', 'Kabupaten sumedang	', 'PROV00011'),
('CITY00172', 'Kabupaten indramayu	', 'PROV00011'),
('CITY00173', 'Kabupaten subang	', 'PROV00011'),
('CITY00174', 'Kabupaten purwakarta	', 'PROV00011'),
('CITY00175', 'Kabupaten karawang	', 'PROV00011'),
('CITY00176', 'Kabupaten bekasi	', 'PROV00011'),
('CITY00177', 'Kabupaten bandung Barat	', 'PROV00011'),
('CITY00178', 'Kabupaten pangandaran	', 'PROV00011'),
('CITY00179', 'Kota bogor	', 'PROV00011'),
('CITY00180', 'Kota sukabumi	', 'PROV00011'),
('CITY00181', 'Kota bandung	', 'PROV00011'),
('CITY00182', 'Kota cirebon	', 'PROV00011'),
('CITY00183', 'Kota bekasi	', 'PROV00011'),
('CITY00184', 'Kota depok	', 'PROV00011'),
('CITY00185', 'Kota cimahi	', 'PROV00011'),
('CITY00186', 'Kota tasikmalaya	', 'PROV00011'),
('CITY00187', 'Kota banjar	', 'PROV00011'),
('CITY00188', 'Kabupaten cilacap	', 'PROV00012'),
('CITY00189', 'Kabupaten banyumas	', 'PROV00012'),
('CITY00190', 'Kabupaten purBalingga	', 'PROV00012'),
('CITY00191', 'Kabupaten banjarnegara	', 'PROV00012'),
('CITY00192', 'Kabupaten kebumen	', 'PROV00012'),
('CITY00193', 'Kabupaten purworejo	', 'PROV00012'),
('CITY00194', 'Kabupaten wonosobo	', 'PROV00012'),
('CITY00195', 'Kabupaten magelang	', 'PROV00012'),
('CITY00196', 'Kabupaten boyolali	', 'PROV00012'),
('CITY00197', 'Kabupaten klaten	', 'PROV00012'),
('CITY00198', 'Kabupaten sukoharjo	', 'PROV00012'),
('CITY00199', 'Kabupaten wonogiri	', 'PROV00012'),
('CITY00200', 'Kabupaten karanganyar	', 'PROV00012'),
('CITY00201', 'Kabupaten sragen	', 'PROV00012'),
('CITY00202', 'Kabupaten grobogan	', 'PROV00012'),
('CITY00203', 'Kabupaten blora	', 'PROV00012'),
('CITY00204', 'Kabupaten rembang	', 'PROV00012'),
('CITY00205', 'Kabupaten pati	', 'PROV00012'),
('CITY00206', 'Kabupaten kudus	', 'PROV00012'),
('CITY00207', 'Kabupaten jepara	', 'PROV00012'),
('CITY00208', 'Kabupaten demak	', 'PROV00012'),
('CITY00209', 'Kabupaten semarang	', 'PROV00012'),
('CITY00210', 'Kabupaten temanggung	', 'PROV00012'),
('CITY00211', 'Kabupaten kendal	', 'PROV00012'),
('CITY00212', 'Kabupaten batang	', 'PROV00012'),
('CITY00213', 'Kabupaten pekalongan	', 'PROV00012'),
('CITY00214', 'Kabupaten pemalang	', 'PROV00012'),
('CITY00215', 'Kabupaten tegal	', 'PROV00012'),
('CITY00216', 'Kabupaten brebes	', 'PROV00012'),
('CITY00217', 'Kota magelang	', 'PROV00012'),
('CITY00218', 'Kota surakarta	', 'PROV00012'),
('CITY00219', 'Kota salatiga	', 'PROV00012'),
('CITY00220', 'Kota semarang	', 'PROV00012'),
('CITY00221', 'Kota pekalongan	', 'PROV00012'),
('CITY00222', 'Kota tegal	', 'PROV00012'),
('CITY00223', 'Kabupaten kulon progo	', 'PROV00034'),
('CITY00224', 'Kabupaten bantul	', 'PROV00034'),
('CITY00225', 'Kabupaten gunung kidul	', 'PROV00034'),
('CITY00226', 'Kabupaten sleman	', 'PROV00034'),
('CITY00227', 'Kota Yogyakarta	', 'PROV00034'),
('CITY00228', 'Kabupaten pacitan	', 'PROV00013'),
('CITY00229', 'Kabupaten ponorogo	', 'PROV00013'),
('CITY00230', 'Kabupaten trenggalek	', 'PROV00013'),
('CITY00231', 'Kabupaten tulungagung	', 'PROV00013'),
('CITY00232', 'Kabupaten blitar	', 'PROV00013'),
('CITY00233', 'Kabupaten kediri	', 'PROV00013'),
('CITY00234', 'Kabupaten malang	', 'PROV00013'),
('CITY00235', 'Kabupaten lumajang	', 'PROV00013'),
('CITY00236', 'Kabupaten jember	', 'PROV00013'),
('CITY00237', 'Kabupaten banyuwangi	', 'PROV00013'),
('CITY00238', 'Kabupaten bondowoso	', 'PROV00013'),
('CITY00239', 'Kabupaten situbondo	', 'PROV00013'),
('CITY00240', 'Kabupaten probolinggo	', 'PROV00013'),
('CITY00241', 'Kabupaten pasuruan	', 'PROV00013'),
('CITY00242', 'Kabupaten sidoarjo	', 'PROV00013'),
('CITY00243', 'Kabupaten mojokerto	', 'PROV00013'),
('CITY00244', 'Kabupaten jombang	', 'PROV00013'),
('CITY00245', 'Kabupaten nganjuk	', 'PROV00013'),
('CITY00246', 'Kabupaten madiun	', 'PROV00013'),
('CITY00247', 'Kabupaten magetan	', 'PROV00013'),
('CITY00248', 'Kabupaten ngawi	', 'PROV00013'),
('CITY00249', 'Kabupaten bojonegoro	', 'PROV00013'),
('CITY00250', 'Kabupaten tuban	', 'PROV00013'),
('CITY00251', 'Kabupaten lamongan	', 'PROV00013'),
('CITY00252', 'Kabupaten gresik	', 'PROV00013'),
('CITY00253', 'Kabupaten bangkalan	', 'PROV00013'),
('CITY00254', 'Kabupaten sampang	', 'PROV00013'),
('CITY00255', 'Kabupaten pamekasan	', 'PROV00013'),
('CITY00256', 'Kabupaten sumenep	', 'PROV00013'),
('CITY00257', 'Kota kediri	', 'PROV00013'),
('CITY00258', 'Kota blitar	', 'PROV00013'),
('CITY00259', 'Kota malang	', 'PROV00013'),
('CITY00260', 'Kota probolinggo	', 'PROV00013'),
('CITY00261', 'Kota pasuruan	', 'PROV00013'),
('CITY00262', 'Kota mojokerto	', 'PROV00013'),
('CITY00263', 'Kota madiun	', 'PROV00013'),
('CITY00264', 'Kota surabaya	', 'PROV00013'),
('CITY00265', 'Kota batu	', 'PROV00013'),
('CITY00266', 'Kabupaten pandeglang	', 'PROV00014'),
('CITY00267', 'Kabupaten lebak	', 'PROV00014'),
('CITY00268', 'Kabupaten tangerang	', 'PROV00014'),
('CITY00269', 'Kabupaten serang	', 'PROV00014'),
('CITY00270', 'Kota tangerang	', 'PROV00014'),
('CITY00271', 'Kota cilegon	', 'PROV00014'),
('CITY00272', 'Kota serang	', 'PROV00014'),
('CITY00273', 'Kota tangerang Selatan	', 'PROV00014'),
('CITY00274', 'Kabupaten jembrana	', 'PROV00015'),
('CITY00275', 'Kabupaten tabanan	', 'PROV00015'),
('CITY00276', 'Kabupaten badung	', 'PROV00015'),
('CITY00277', 'Kabupaten gianyar	', 'PROV00015'),
('CITY00278', 'Kabupaten klungkung	', 'PROV00015'),
('CITY00279', 'Kabupaten bangli	', 'PROV00015'),
('CITY00280', 'Kabupaten karang asem	', 'PROV00015'),
('CITY00281', 'Kabupaten buleleng	', 'PROV00015'),
('CITY00282', 'Kota denpasar	', 'PROV00015'),
('CITY00283', 'Kabupaten lombok Barat	', 'PROV00016'),
('CITY00284', 'Kabupaten lombok Tengah	', 'PROV00016'),
('CITY00285', 'Kabupaten lombok Timur	', 'PROV00016'),
('CITY00286', 'Kabupaten sumbawa	', 'PROV00016'),
('CITY00287', 'Kabupaten dompu	', 'PROV00016'),
('CITY00288', 'Kabupaten bima	', 'PROV00016'),
('CITY00289', 'Kabupaten sumbawa Barat	', 'PROV00016'),
('CITY00290', 'Kabupaten lombok Utara	', 'PROV00016'),
('CITY00291', 'Kota mataram	', 'PROV00016'),
('CITY00292', 'Kota bima	', 'PROV00016'),
('CITY00293', 'Kabupaten sumba Barat	', 'PROV00017'),
('CITY00294', 'Kabupaten sumba Timur	', 'PROV00017'),
('CITY00295', 'Kabupaten kupang	', 'PROV00017'),
('CITY00296', 'Kabupaten timor Tengah Selatan	', 'PROV00017'),
('CITY00297', 'Kabupaten timor Tengah Utara	', 'PROV00017'),
('CITY00298', 'Kabupaten belu	', 'PROV00017'),
('CITY00299', 'Kabupaten alor	', 'PROV00017'),
('CITY00300', 'Kabupaten lembata	', 'PROV00017'),
('CITY00301', 'Kabupaten flores Timur	', 'PROV00017'),
('CITY00302', 'Kabupaten sikka	', 'PROV00017'),
('CITY00303', 'Kabupaten ende	', 'PROV00017'),
('CITY00304', 'Kabupaten ngada	', 'PROV00017'),
('CITY00305', 'Kabupaten manggarai	', 'PROV00017'),
('CITY00306', 'Kabupaten rote ndao	', 'PROV00017'),
('CITY00307', 'Kabupaten manggarai Barat	', 'PROV00017'),
('CITY00308', 'Kabupaten sumba Tengah	', 'PROV00017'),
('CITY00309', 'Kabupaten sumba Barat daya	', 'PROV00017'),
('CITY00310', 'Kabupaten nagekeo	', 'PROV00017'),
('CITY00311', 'Kabupaten manggarai Timur	', 'PROV00017'),
('CITY00312', 'Kabupaten sabu raijua	', 'PROV00017'),
('CITY00313', 'Kabupaten malaka	', 'PROV00017'),
('CITY00314', 'Kota kupang	', 'PROV00017'),
('CITY00315', 'Kabupaten sambas	', 'PROV00018'),
('CITY00316', 'Kabupaten bengkayang	', 'PROV00018'),
('CITY00317', 'Kabupaten landak	', 'PROV00018'),
('CITY00318', 'Kabupaten mempawah	', 'PROV00018'),
('CITY00319', 'Kabupaten sanggau	', 'PROV00018'),
('CITY00320', 'Kabupaten ketapang	', 'PROV00018'),
('CITY00321', 'Kabupaten sintang	', 'PROV00018'),
('CITY00322', 'Kabupaten kapuas hulu	', 'PROV00018'),
('CITY00323', 'Kabupaten sekadau	', 'PROV00018'),
('CITY00324', 'Kabupaten melawi	', 'PROV00018'),
('CITY00325', 'Kabupaten kayong Utara	', 'PROV00018'),
('CITY00326', 'Kabupaten kubu raya	', 'PROV00018'),
('CITY00327', 'Kota pontianak	', 'PROV00018'),
('CITY00328', 'Kota singkawang	', 'PROV00018'),
('CITY00329', 'Kabupaten Kotawaringin Barat	', 'PROV00019'),
('CITY00330', 'Kabupaten Kotawaringin Timur	', 'PROV00019'),
('CITY00331', 'Kabupaten kapuas	', 'PROV00019'),
('CITY00332', 'Kabupaten barito Selatan	', 'PROV00019'),
('CITY00333', 'Kabupaten barito Utara	', 'PROV00019'),
('CITY00334', 'Kabupaten sukamara	', 'PROV00019'),
('CITY00335', 'Kabupaten lamandau	', 'PROV00019'),
('CITY00336', 'Kabupaten seruyan	', 'PROV00019'),
('CITY00337', 'Kabupaten katingan	', 'PROV00019'),
('CITY00338', 'Kabupaten pulang pisau	', 'PROV00019'),
('CITY00339', 'Kabupaten gunung mas	', 'PROV00019'),
('CITY00340', 'Kabupaten barito Timur	', 'PROV00019'),
('CITY00341', 'Kabupaten murung raya	', 'PROV00019'),
('CITY00342', 'Kota palangka raya	', 'PROV00019'),
('CITY00343', 'Kabupaten tanah laut	', 'PROV00020'),
('CITY00344', 'Kabupaten Kota baru	', 'PROV00020'),
('CITY00345', 'Kabupaten banjar	', 'PROV00020'),
('CITY00346', 'Kabupaten barito kuala	', 'PROV00020'),
('CITY00347', 'Kabupaten tapin	', 'PROV00020'),
('CITY00348', 'Kabupaten hulu sungai Selatan	', 'PROV00020'),
('CITY00349', 'Kabupaten hulu sungai Tengah	', 'PROV00020'),
('CITY00350', 'Kabupaten hulu sungai Utara	', 'PROV00020'),
('CITY00351', 'Kabupaten tabalong	', 'PROV00020'),
('CITY00352', 'Kabupaten tanah bumbu	', 'PROV00020'),
('CITY00353', 'Kabupaten balangan	', 'PROV00020'),
('CITY00354', 'Kota banjarmasin	', 'PROV00020'),
('CITY00355', 'Kota banjar baru	', 'PROV00020'),
('CITY00356', 'Kabupaten paser	', 'PROV00021'),
('CITY00357', 'Kabupaten kutai Barat	', 'PROV00021'),
('CITY00358', 'Kabupaten kutai kartanegara	', 'PROV00021'),
('CITY00359', 'Kabupaten kutai Timur	', 'PROV00021'),
('CITY00360', 'Kabupaten berau	', 'PROV00021'),
('CITY00361', 'Kabupaten penajam paser Utara	', 'PROV00021'),
('CITY00362', 'Kabupaten mahakam hulu	', 'PROV00021'),
('CITY00363', 'Kota Balikpapan	', 'PROV00021'),
('CITY00364', 'Kota samarinda	', 'PROV00021'),
('CITY00365', 'Kota bontang	', 'PROV00021'),
('CITY00366', 'Kabupaten malinau	', 'PROV00022'),
('CITY00367', 'Kabupaten bulungan	', 'PROV00022'),
('CITY00368', 'Kabupaten tana tidung	', 'PROV00022'),
('CITY00369', 'Kabupaten nunukan	', 'PROV00022'),
('CITY00370', 'Kota tarakan	', 'PROV00022'),
('CITY00371', 'Kabupaten bolaang mongondow	', 'PROV00023'),
('CITY00372', 'Kabupaten minahasa	', 'PROV00023'),
('CITY00373', 'Kabupaten kepulauan sangihe	', 'PROV00023'),
('CITY00374', 'Kabupaten kepulauan talaud	', 'PROV00023'),
('CITY00375', 'Kabupaten minahasa Selatan	', 'PROV00023'),
('CITY00376', 'Kabupaten minahasa Utara	', 'PROV00023'),
('CITY00377', 'Kabupaten bolaang mongondow Utara	', 'PROV00023'),
('CITY00378', 'Kabupaten siau tagulandang biaro	', 'PROV00023'),
('CITY00379', 'Kabupaten minahasa Tenggara	', 'PROV00023'),
('CITY00380', 'Kabupaten bolaang mongondow Selatan	', 'PROV00023'),
('CITY00381', 'Kabupaten bolaang mongondow Timur	', 'PROV00023'),
('CITY00382', 'Kota manado	', 'PROV00023'),
('CITY00383', 'Kota bitung	', 'PROV00023'),
('CITY00384', 'Kota tomohon	', 'PROV00023'),
('CITY00385', 'Kota Kotamobagu	', 'PROV00023'),
('CITY00386', 'Kabupaten banggai kepulauan	', 'PROV00024'),
('CITY00387', 'Kabupaten banggai	', 'PROV00024'),
('CITY00388', 'Kabupaten morowali	', 'PROV00024'),
('CITY00389', 'Kabupaten poso	', 'PROV00024'),
('CITY00390', 'Kabupaten donggala	', 'PROV00024'),
('CITY00391', 'Kabupaten toli-toli	', 'PROV00024'),
('CITY00392', 'Kabupaten buol	', 'PROV00024'),
('CITY00393', 'Kabupaten parigi moutong	', 'PROV00024'),
('CITY00394', 'Kabupaten tojo una-una	', 'PROV00024'),
('CITY00395', 'Kabupaten sigi	', 'PROV00024'),
('CITY00396', 'Kabupaten banggai laut	', 'PROV00024'),
('CITY00397', 'Kabupaten morowali Utara	', 'PROV00024'),
('CITY00398', 'Kota palu	', 'PROV00024'),
('CITY00399', 'Kabupaten kepulauan selayar	', 'PROV00025'),
('CITY00400', 'Kabupaten bulukumba	', 'PROV00025'),
('CITY00401', 'Kabupaten bantaeng	', 'PROV00025'),
('CITY00402', 'Kabupaten jeneponto	', 'PROV00025'),
('CITY00403', 'Kabupaten takalar	', 'PROV00025'),
('CITY00404', 'Kabupaten gowa	', 'PROV00025'),
('CITY00405', 'Kabupaten sinjai	', 'PROV00025'),
('CITY00406', 'Kabupaten maros	', 'PROV00025'),
('CITY00407', 'Kabupaten pangkajene dan kepulauan	', 'PROV00025'),
('CITY00408', 'Kabupaten barru	', 'PROV00025'),
('CITY00409', 'Kabupaten bone	', 'PROV00025'),
('CITY00410', 'Kabupaten soppeng	', 'PROV00025'),
('CITY00411', 'Kabupaten wajo	', 'PROV00025'),
('CITY00412', 'Kabupaten sidenreng rappang	', 'PROV00025'),
('CITY00413', 'Kabupaten pinrang	', 'PROV00025'),
('CITY00414', 'Kabupaten enrekang	', 'PROV00025'),
('CITY00415', 'Kabupaten luwu	', 'PROV00025'),
('CITY00416', 'Kabupaten tana toraja	', 'PROV00025'),
('CITY00417', 'Kabupaten luwu Utara	', 'PROV00025'),
('CITY00418', 'Kabupaten luwu Timur	', 'PROV00025'),
('CITY00419', 'Kabupaten toraja Utara	', 'PROV00025'),
('CITY00420', 'Kota makassar	', 'PROV00025'),
('CITY00421', 'Kota parepare	', 'PROV00025'),
('CITY00422', 'Kota palopo	', 'PROV00025'),
('CITY00423', 'Kabupaten buton	', 'PROV00026'),
('CITY00424', 'Kabupaten muna	', 'PROV00026'),
('CITY00425', 'Kabupaten konawe	', 'PROV00026'),
('CITY00426', 'Kabupaten kolaka	', 'PROV00026'),
('CITY00427', 'Kabupaten konawe Selatan	', 'PROV00026'),
('CITY00428', 'Kabupaten bombana	', 'PROV00026'),
('CITY00429', 'Kabupaten wakatobi	', 'PROV00026'),
('CITY00430', 'Kabupaten kolaka Utara	', 'PROV00026'),
('CITY00431', 'Kabupaten buton Utara	', 'PROV00026'),
('CITY00432', 'Kabupaten konawe Utara	', 'PROV00026'),
('CITY00433', 'Kabupaten kolaka Timur	', 'PROV00026'),
('CITY00434', 'Kabupaten konawe kepulauan	', 'PROV00026'),
('CITY00435', 'Kabupaten muna Barat	', 'PROV00026'),
('CITY00436', 'Kabupaten buton Tengah	', 'PROV00026'),
('CITY00437', 'Kabupaten buton Selatan	', 'PROV00026'),
('CITY00438', 'Kota kendari	', 'PROV00026'),
('CITY00439', 'Kota baubau	', 'PROV00026'),
('CITY00440', 'Kabupaten boalemo	', 'PROV00027'),
('CITY00441', 'Kabupaten Gorontalo	', 'PROV00027'),
('CITY00442', 'Kabupaten pohuwato	', 'PROV00027'),
('CITY00443', 'Kabupaten bone bolango	', 'PROV00027'),
('CITY00444', 'Kabupaten Gorontalo Utara	', 'PROV00027'),
('CITY00445', 'Kota Gorontalo	', 'PROV00027'),
('CITY00446', 'Kabupaten majene	', 'PROV00028'),
('CITY00447', 'Kabupaten polewali mandar	', 'PROV00028'),
('CITY00448', 'Kabupaten mamasa	', 'PROV00028'),
('CITY00449', 'Kabupaten mamuju	', 'PROV00028'),
('CITY00450', 'Kabupaten mamuju Utara	', 'PROV00028'),
('CITY00451', 'Kabupaten mamuju Tengah	', 'PROV00028'),
('CITY00452', 'Kabupaten Maluku Tenggara Barat	', 'PROV00029'),
('CITY00453', 'Kabupaten Maluku Tenggara	', 'PROV00029'),
('CITY00454', 'Kabupaten Maluku Tengah	', 'PROV00029'),
('CITY00455', 'Kabupaten buru	', 'PROV00029'),
('CITY00456', 'Kabupaten kepulauan aru	', 'PROV00029'),
('CITY00457', 'Kabupaten seram bagian Barat	', 'PROV00029'),
('CITY00458', 'Kabupaten seram bagian Timur	', 'PROV00029'),
('CITY00459', 'Kabupaten Maluku Barat daya	', 'PROV00029'),
('CITY00460', 'Kabupaten buru Selatan	', 'PROV00029'),
('CITY00461', 'Kota ambon	', 'PROV00029'),
('CITY00462', 'Kota tual	', 'PROV00029'),
('CITY00463', 'Kabupaten halmahera Barat	', 'PROV00030'),
('CITY00464', 'Kabupaten halmahera Tengah	', 'PROV00030'),
('CITY00465', 'Kabupaten kepulauan sula	', 'PROV00030'),
('CITY00466', 'Kabupaten halmahera Selatan	', 'PROV00030'),
('CITY00467', 'Kabupaten halmahera Utara	', 'PROV00030'),
('CITY00468', 'Kabupaten halmahera Timur	', 'PROV00030'),
('CITY00469', 'Kabupaten pulau morotai	', 'PROV00030'),
('CITY00470', 'Kabupaten pulau taliabu	', 'PROV00030'),
('CITY00471', 'Kota ternate	', 'PROV00030'),
('CITY00472', 'Kota tidore kepulauan	', 'PROV00030'),
('CITY00473', 'Kabupaten fakfak	', 'PROV00031'),
('CITY00474', 'Kabupaten kaimana	', 'PROV00031'),
('CITY00475', 'Kabupaten teluk wondama	', 'PROV00031'),
('CITY00476', 'Kabupaten teluk bintuni	', 'PROV00031'),
('CITY00477', 'Kabupaten manokwari	', 'PROV00031'),
('CITY00478', 'Kabupaten sorong Selatan	', 'PROV00031'),
('CITY00479', 'Kabupaten sorong	', 'PROV00031'),
('CITY00480', 'Kabupaten raja ampat	', 'PROV00031'),
('CITY00481', 'Kabupaten tambrauw	', 'PROV00031'),
('CITY00482', 'Kabupaten maybrat	', 'PROV00031'),
('CITY00483', 'Kabupaten manokwari Selatan	', 'PROV00031'),
('CITY00484', 'Kabupaten pegunungan arfak	', 'PROV00031'),
('CITY00485', 'Kota sorong	', 'PROV00031'),
('CITY00486', 'Kabupaten merauke	', 'PROV00032'),
('CITY00487', 'Kabupaten jayawijaya	', 'PROV00032'),
('CITY00488', 'Kabupaten jayapura	', 'PROV00032'),
('CITY00489', 'Kabupaten nabire	', 'PROV00032'),
('CITY00490', 'Kabupaten kepulauan yapen	', 'PROV00032'),
('CITY00491', 'Kabupaten biak numfor	', 'PROV00032'),
('CITY00492', 'Kabupaten paniai	', 'PROV00032'),
('CITY00493', 'Kabupaten puncak jaya	', 'PROV00032'),
('CITY00494', 'Kabupaten mimika	', 'PROV00032'),
('CITY00495', 'Kabupaten boven digoel	', 'PROV00032'),
('CITY00496', 'Kabupaten mappi	', 'PROV00032'),
('CITY00497', 'Kabupaten asmat	', 'PROV00032'),
('CITY00498', 'Kabupaten yahukimo	', 'PROV00032'),
('CITY00499', 'Kabupaten pegunungan bintang	', 'PROV00032'),
('CITY00500', 'Kabupaten tolikara	', 'PROV00032'),
('CITY00501', 'Kabupaten sarmi	', 'PROV00032'),
('CITY00502', 'Kabupaten keerom	', 'PROV00032'),
('CITY00503', 'Kabupaten waropen	', 'PROV00032'),
('CITY00504', 'Kabupaten supiori	', 'PROV00032'),
('CITY00505', 'Kabupaten mamberamo raya	', 'PROV00032'),
('CITY00506', 'Kabupaten nduga	', 'PROV00032'),
('CITY00507', 'Kabupaten lanny jaya	', 'PROV00032'),
('CITY00508', 'Kabupaten mamberamo Tengah	', 'PROV00032'),
('CITY00509', 'Kabupaten yalimo	', 'PROV00032'),
('CITY00510', 'Kabupaten puncak	', 'PROV00032'),
('CITY00511', 'Kabupaten dogiyai	', 'PROV00032'),
('CITY00512', 'Kabupaten intan jaya	', 'PROV00032'),
('CITY00513', 'Kabupaten deiyai	', 'PROV00032'),
('CITY00514', 'Kota jayapura	', 'PROV00032');

--
-- Trigger `city`
--
DELIMITER $$
CREATE TRIGGER `tg_city` BEFORE INSERT ON `city` FOR EACH ROW begin
 declare x int;
 declare y int;
 declare name_tab varchar(5);
 set y := (select seq_lastno from sequence where seq_table = 'city');
 set name_tab := (select table_code from sequence where seq_table = 'city');
 update sequence set seq_lastno =  y+1 where seq_table = 'city';
 set x := (select seq_lastno from sequence where seq_table = 'city');
 set new.city_code = concat(name_tab, LPAD(x, 5, '0'));
 end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `client`
--

CREATE TABLE `client` (
  `client_id` varchar(20) NOT NULL DEFAULT '0',
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` varchar(255) NOT NULL,
  `city_code` varchar(20) DEFAULT NULL,
  `pic_name` varchar(50) NOT NULL,
  `pic_number` varchar(15) NOT NULL,
  `pic_email` varchar(50) NOT NULL,
  `created_by` varchar(20) NOT NULL DEFAULT 'system',
  `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modify_by` varchar(20) NOT NULL DEFAULT 'system',
  `modify_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` enum('added','deleted') NOT NULL DEFAULT 'added',
  `client_code` varchar(4) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `client`
--

INSERT INTO `client` (`client_id`, `name`, `email`, `address`, `city_code`, `pic_name`, `pic_number`, `pic_email`, `created_by`, `created_date`, `modify_by`, `modify_date`, `status`, `client_code`) VALUES
('CLNT00001', 'Bank DKI Syariah', 'care@bankdki.co.id', 'Jl. Batu Tulis No. 1 Jakarta', 'CITY00158', 'Irma', '085312345432', 'irma@bankdki.co.id', 'system', '2018-05-25 10:31:00', 'system', '2018-05-25 10:31:00', 'added', 'DKIS'),
('CLNT00002', 'BPD Riau Syariah', 'care@bpdriau.co.id', 'Jl. Pusat Riau', 'CITY00378', 'Nanang', '081254320987', 'nanang@bpdriau.co.id', 'system', '2018-05-25 10:33:07', 'system', '2018-05-25 10:33:07', 'added', 'BRUS');

--
-- Trigger `client`
--
DELIMITER $$
CREATE TRIGGER `tg_client` BEFORE INSERT ON `client` FOR EACH ROW begin
 declare x int;
 declare y int;
 declare name_tab varchar(5);
 set y := (select seq_lastno from sequence where seq_table = 'client');
 set name_tab := (select table_code from sequence where seq_table = 'client');
 update sequence set seq_lastno =  y+1 where seq_table = 'client';
 set x := (select seq_lastno from sequence where seq_table = 'client');
 set new.client_id = concat(name_tab, LPAD(x, 5, '0'));
 end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `department`
--

CREATE TABLE `department` (
  `department_id` varchar(20) NOT NULL DEFAULT '0',
  `department_name` varchar(50) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_by` varchar(10) NOT NULL DEFAULT 'system',
  `modify_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modify_by` varchar(10) NOT NULL DEFAULT 'system',
  `status` enum('added','deleted') DEFAULT 'added'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `department`
--

INSERT INTO `department` (`department_id`, `department_name`, `description`, `created_date`, `created_by`, `modify_date`, `modify_by`, `status`) VALUES
('DEPT00002', 'Marketing01', 'testing', '2018-05-20 22:53:18', 'system', '2018-05-20 22:53:18', 'system', 'added'),
('DEPT00003', 'IT', NULL, '2018-05-20 22:53:29', 'system', '2018-05-20 22:53:29', 'system', 'added'),
('DEPT00004', 'Finance', NULL, '2018-05-21 10:49:16', 'system', '2018-05-21 10:49:16', 'system', 'added'),
('DEPT00005', 'General Affair', NULL, '2018-05-21 10:49:49', 'system', '2018-05-21 10:49:49', 'system', 'added'),
('DEPT00006', 'Contact Center', NULL, '2018-05-21 12:55:57', 'system', '2018-05-21 12:55:57', 'system', 'added'),
('DEPT00007', 'Telesales', NULL, '2018-05-21 12:57:10', 'system', '2018-05-21 12:57:10', 'system', 'added'),
('DEPT00008', 'Testing', NULL, '2018-05-21 13:00:13', 'system', '2018-05-21 13:00:13', 'system', 'deleted'),
('DEPT00009', 'Departement testing', 'Departement testing saja', '2018-05-28 17:30:12', 'system', '2018-05-28 17:30:12', 'system', 'added');

--
-- Trigger `department`
--
DELIMITER $$
CREATE TRIGGER `tg_department` BEFORE INSERT ON `department` FOR EACH ROW begin
declare x int;
declare y int;
set y := (select seq_lastno from sequence where seq_table = 'department');
update sequence set seq_lastno =  y+1 where seq_table = 'department';
set x := (select seq_lastno from sequence where seq_table = 'department');
set new.department_id = concat('DEPT', LPAD(x, 5, '0'));
end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `division`
--

CREATE TABLE `division` (
  `division_id` varchar(20) NOT NULL DEFAULT '0',
  `department_id` varchar(20) NOT NULL,
  `division_name` varchar(50) NOT NULL,
  `description` varchar(100) DEFAULT NULL,
  `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_by` varchar(10) NOT NULL DEFAULT 'system',
  `modify_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modify_by` varchar(10) NOT NULL DEFAULT 'system',
  `status` enum('added','deleted') NOT NULL DEFAULT 'added'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `division`
--

INSERT INTO `division` (`division_id`, `department_id`, `division_name`, `description`, `created_date`, `created_by`, `modify_date`, `modify_by`, `status`) VALUES
('DIVS00001', 'DEPT00003', 'Product Manager 01', 'testing aja', '2018-05-21 15:57:31', 'system', '2018-05-21 15:57:31', 'system', 'added'),
('DIVS00002', 'DEPT00004', 'Accounting testing', 'Accounting Division', '2018-05-31 13:31:55', 'system', '2018-05-31 13:31:55', 'system', 'deleted');

--
-- Trigger `division`
--
DELIMITER $$
CREATE TRIGGER `tg_division` BEFORE INSERT ON `division` FOR EACH ROW begin
 declare x int;
 declare y int;
 declare name_tab varchar(5);
 set y := (select seq_lastno from sequence where seq_table = 'division');
 set name_tab := (select table_code from sequence where seq_table = 'division');
 update sequence set seq_lastno =  y+1 where seq_table = 'division';
 set x := (select seq_lastno from sequence where seq_table = 'division');
 set new.division_id = concat(name_tab, LPAD(x, 5, '0'));
 end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `document`
--

CREATE TABLE `document` (
  `Document_No` varchar(20) NOT NULL,
  `Document_Name` varchar(50) NOT NULL,
  `Document_Desc` varchar(100) NOT NULL,
  `Document_URL` varchar(100) NOT NULL,
  `Document_Status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `employees`
--

CREATE TABLE `employees` (
  `employee_id` varchar(20) NOT NULL DEFAULT '0',
  `NIK` varchar(10) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `firstname` varchar(100) DEFAULT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `gender` enum('Male','Female') NOT NULL,
  `address` text,
  `city_code` varchar(20) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `division_id` varchar(20) DEFAULT NULL,
  `empTitle_id` varchar(20) DEFAULT NULL,
  `join_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_by` varchar(20) NOT NULL DEFAULT 'system',
  `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modify_by` varchar(20) NOT NULL DEFAULT 'system',
  `modify_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` enum('added','deleted') NOT NULL DEFAULT 'added'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `employees`
--

INSERT INTO `employees` (`employee_id`, `NIK`, `email`, `password`, `firstname`, `lastname`, `birthday`, `gender`, `address`, `city_code`, `phone`, `division_id`, `empTitle_id`, `join_date`, `created_by`, `created_date`, `modify_by`, `modify_date`, `status`) VALUES
('EMPY00021', '201905001', '14linggar@gmail.com', 'password123', 'Linggar', 'Dedi Kurniawan', '0000-00-00', 'Male', 'Karawaci Tangerang Banten', 'CITY00270', '085280034936', 'DIVS00001', 'EMTL00001', '2018-05-24 16:15:24', 'system', '2018-05-24 16:15:24', 'system', '2018-05-24 16:15:24', 'added'),
('EMPY00022', '201905002', 'simulfa@gmail.com', 'password123', 'Siti', 'Maria Ulfa', '2018-05-24', 'Female', 'Harapan Kita', 'CITY00270', '085280034936', 'DIVS00001', 'EMTL00002', '2018-05-24 16:18:10', 'system', '2018-05-24 16:18:10', 'system', '2018-05-24 16:18:10', 'added'),
('EMPY00023', '201905003', 'akbar.wijayanto@gmail.com', 'password123', 'Akbar', 'Wijayanto', '0000-00-00', 'Male', 'Karawaci Cibodasari Tangerang Banten', 'CITY00270', '085280034936', 'DIVS00001', 'EMTL00003', '2018-05-24 16:18:10', 'system', '2018-05-28 11:41:43', 'system', '2018-05-28 11:41:43', 'added');

--
-- Trigger `employees`
--
DELIMITER $$
CREATE TRIGGER `tg_employees` BEFORE INSERT ON `employees` FOR EACH ROW begin
 declare x int;
 declare y int;
 declare name_tab varchar(5);
 set y := (select seq_lastno from sequence where seq_table = 'employees');
 set name_tab := (select table_code from sequence where seq_table = 'employees');
 update sequence set seq_lastno =  y+1 where seq_table = 'employees';
 set x := (select seq_lastno from sequence where seq_table = 'employees');
 set new.employee_id = concat(name_tab, LPAD(x, 5, '0'));
 end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `emptitle`
--

CREATE TABLE `emptitle` (
  `empTitle_id` varchar(20) NOT NULL DEFAULT '0',
  `title_name` varchar(50) NOT NULL,
  `description` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `emptitle`
--

INSERT INTO `emptitle` (`empTitle_id`, `title_name`, `description`) VALUES
('EMTL00001', 'Department Head', 'Department Head Title'),
('EMTL00002', 'Manager', 'manager Title'),
('EMTL00003', 'Project Manajer', 'Project Manager'),
('EMTL00004', 'Leader', 'Leader Title'),
('EMTL00005', 'Staff', 'Staff Title');

--
-- Trigger `emptitle`
--
DELIMITER $$
CREATE TRIGGER `tg_empTitle` BEFORE INSERT ON `emptitle` FOR EACH ROW begin
 declare x int;
 declare y int;
 declare name_tab varchar(5);
 set y := (select seq_lastno from sequence where seq_table = 'empTitle');
 set name_tab := (select table_code from sequence where seq_table = 'empTitle');
 update sequence set seq_lastno =  y+1 where seq_table = 'empTitle';
 set x := (select seq_lastno from sequence where seq_table = 'empTitle');
 set new.empTitle_id = concat(name_tab, LPAD(x, 5, '0'));
 end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `job`
--

CREATE TABLE `job` (
  `Job_ID` char(2) NOT NULL,
  `Job_Name` varchar(30) NOT NULL,
  `Job_Desc` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Trigger `job`
--
DELIMITER $$
CREATE TRIGGER `tg_job` BEFORE INSERT ON `job` FOR EACH ROW begin
 declare x int;
 declare y int;
 declare name_tab varchar(5);
 set y := (select seq_lastno from sequence where seq_table = 'job');
 set name_tab := (select table_code from sequence where seq_table = 'job');
 update sequence set seq_lastno =  y+1 where seq_table = 'job';
 set x := (select seq_lastno from sequence where seq_table = 'job');
 set new.Job_ID = concat(name_tab, LPAD(x, 5, '0'));
 end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `notification`
--

CREATE TABLE `notification` (
  `Notif_ID` varchar(12) NOT NULL,
  `employee_id` varchar(20) NOT NULL,
  `Notif_Name` varchar(20) NOT NULL,
  `Notif_Desc` varchar(100) NOT NULL,
  `Notif_Date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `project`
--

CREATE TABLE `project` (
  `project_id` varchar(20) NOT NULL DEFAULT '0',
  `client_id` varchar(20) NOT NULL,
  `name` varchar(150) NOT NULL,
  `mandays` int(10) NOT NULL,
  `startDate` date NOT NULL,
  `endDate` date NOT NULL,
  `status_id` varchar(20) NOT NULL DEFAULT 'PRST00001',
  `created_by` varchar(20) NOT NULL DEFAULT 'system',
  `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modify_by` varchar(20) NOT NULL DEFAULT 'system',
  `modify_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` enum('added','deleted') NOT NULL DEFAULT 'added',
  `pid` varchar(13) NOT NULL,
  `priority` enum('High','Medium','Low') NOT NULL,
  `employee_id` varchar(20) NOT NULL,
  `description` text,
  `doc_project` varchar(100) NOT NULL,
  `doc_size` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `project`
--

INSERT INTO `project` (`project_id`, `client_id`, `name`, `mandays`, `startDate`, `endDate`, `status_id`, `created_by`, `created_date`, `modify_by`, `modify_date`, `status`, `pid`, `priority`, `employee_id`, `description`, `doc_project`, `doc_size`) VALUES
('PRJT00001', 'CLNT00001', 'Penambahan Fitur e-channel Core Banking', 10, '2018-09-18', '0000-00-00', 'PRST00001', 'system', '2018-05-31 11:06:19', 'system', '2018-05-31 11:06:19', 'added', '7DKIS20180001', 'Medium', 'EMPY00023', 'Penambahan Fitur e-channel Core Banking', '7DKIS20180001_NEW_PROJECT.pdf', '321895'),
('PRJT00002', 'CLNT00002', 'Penambahan Fitur e-channel Internet Banking', 10, '0000-00-00', '0000-00-00', 'PRST00001', 'system', '2018-05-31 11:14:58', 'system', '2018-05-31 11:14:58', 'added', '7BRUS20180001', 'Medium', 'EMPY00023', '<p>Penambahan Fitur e-channel Internet Banking<br></p>', '7BRUS20180001_NEW_PROJECT.pdf', '321895'),
('PRJT00003', 'CLNT00002', 'Penambahan Fitur e-channel Internet Banking', 10, '0000-00-00', '0000-00-00', 'PRST00001', 'system', '2018-05-31 11:16:09', 'system', '2018-05-31 11:16:09', 'added', '7BRUS20180001', 'Medium', 'EMPY00023', '<p>Penambahan Fitur e-channel Internet Banking<br></p>', '7BRUS20180001_NEW_PROJECT.pdf', '321895'),
('PRJT00004', 'CLNT00001', 'ATM Bersama', 10, '2018-06-01', '2018-06-02', 'PRST00001', 'system', '2018-05-31 11:48:00', 'system', '2018-05-31 11:48:00', 'added', '7DKIS20180002', 'Medium', 'EMPY00023', '<p>ATM Bersama<br></p>', '7DKIS20180002_NEW_PROJECT.pdf', '321895'),
('PRJT00005', 'CLNT00001', 'ATM Loading', 10, '2018-06-01', '2018-06-06', 'PRST00001', 'system', '2018-05-31 12:04:27', 'system', '2018-05-31 12:04:27', 'added', '7DKIS20180003', 'Medium', 'EMPY00023', '<p>ATM Loading<br></p>', '7DKIS20180003_NEW_PROJECT.pdf', '321895'),
('PRJT00006', 'CLNT00001', 'Teller ATM Error', 10, '2018-06-01', '2018-06-02', 'PRST00001', 'system', '2018-05-31 12:06:55', 'system', '2018-05-31 12:06:55', 'added', '7DKIS20180004', 'Medium', 'EMPY00023', '<p>Teller ATM Error<br></p>', '7DKIS20180004_NEW_PROJECT.pdf', '321895'),
('PRJT00007', 'CLNT00001', 'Proses Migrasi Core', 10, '2018-06-21', '2018-06-29', 'PRST00001', 'system', '2018-05-31 12:08:41', 'system', '2018-05-31 12:08:41', 'added', '7DKIS20180005', 'Medium', 'EMPY00023', '<p>Proses Migrasi Core<br></p>', '7DKIS20180005_NEW_PROJECT.pdf', '321895'),
('PRJT00008', 'CLNT00001', 'project testing', 10, '2018-06-09', '2018-06-30', 'PRST00001', 'system', '2018-05-31 12:10:14', 'system', '2018-05-31 12:10:14', 'added', '7DKIS20180006', 'Medium', 'EMPY00023', '<p>project testing<br></p>', '7DKIS20180006_NEW_PROJECT.pdf', '321895'),
('PRJT00009', 'CLNT00001', 'Project testing02', 10, '2018-06-01', '2018-07-26', 'PRST00001', 'system', '2018-05-31 12:12:58', 'system', '2018-05-31 12:12:58', 'added', '7DKIS20180007', 'Medium', 'EMPY00023', '<p>Project testing02<br></p>', '7DKIS20180007_NEW_PROJECT.pdf', '321895'),
('PRJT00010', 'CLNT00001', 'Project testing 001', 10, '2018-06-01', '2018-06-16', 'PRST00001', 'system', '2018-05-31 12:15:56', 'system', '2018-05-31 12:15:56', 'added', '7DKIS20180008', 'Medium', 'EMPY00023', '<p>Project testing 001<br></p>', '7DKIS20180008_NEW_PROJECT.pdf', '321895'),
('PRJT00011', 'CLNT00001', 'Penambahan Fitur Mobile Banking', 10, '2018-06-01', '2018-06-30', 'PRST00001', 'system', '2018-05-31 13:13:01', 'system', '2018-05-31 13:13:01', 'added', '7DKIS20180009', 'Medium', 'EMPY00023', '<p>Penambahan Fitur Mobile Banking<br></p>', '7DKIS20180009_NEW_PROJECT.pdf', '321895'),
('PRJT00012', 'CLNT00002', 'Core Banking back end', 10, '2018-06-01', '2018-06-08', 'PRST00001', 'system', '2018-05-31 13:14:59', 'system', '2018-05-31 13:14:59', 'added', '7BRUS20180003', 'Medium', 'EMPY00023', '<p>Core Banking back end<br></p>', '7BRUS20180003_NEW_PROJECT.pdf', '321895'),
('PRJT00013', 'CLNT00002', 'Creating End of day', 3, '2018-06-01', '2018-06-05', 'PRST00001', 'system', '2018-05-31 13:17:08', 'system', '2018-05-31 13:17:08', 'added', '7BRUS20180004', 'Medium', 'EMPY00023', '<p>Creating End of day<br></p>', '7BRUS20180004_NEW_PROJECT.pdf', '321895'),
('PRJT00014', 'CLNT00002', 'Add mobile apps', 10, '2018-06-08', '2018-07-06', 'PRST00001', 'system', '2018-05-31 13:18:37', 'system', '2018-05-31 13:18:37', 'added', '7BRUS20180005', 'Medium', 'EMPY00023', '<p>Add mobile apps<br></p>', '7BRUS20180005_NEW_PROJECT.pdf', '321895'),
('PRJT00015', 'CLNT00002', 'test', 10, '2018-06-07', '2018-06-09', 'PRST00001', 'system', '2018-05-31 13:20:56', 'system', '2018-05-31 13:20:56', 'added', '7BRUS20180006', 'Medium', 'EMPY00023', '<p>test</p>', '7BRUS20180006_NEW_PROJECT.pdf', '321895'),
('PRJT00016', 'CLNT00002', 'test01', 10, '2018-06-01', '2018-06-05', 'PRST00001', 'system', '2018-05-31 13:23:08', 'system', '2018-05-31 13:23:08', 'added', '7BRUS20180007', 'Medium', 'EMPY00023', 'test01', '7BRUS20180007_NEW_PROJECT.pdf', '321895');

--
-- Trigger `project`
--
DELIMITER $$
CREATE TRIGGER `tg_project` BEFORE INSERT ON `project` FOR EACH ROW begin
 declare x int;
 declare y int;
 declare name_tab varchar(5);
 set y := (select seq_lastno from sequence where seq_table = 'project');
 set name_tab := (select table_code from sequence where seq_table = 'project');
 update sequence set seq_lastno =  y+1 where seq_table = 'project';
 set x := (select seq_lastno from sequence where seq_table = 'project');
 set new.project_id = concat(name_tab, LPAD(x, 5, '0'));
 end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `project_status`
--

CREATE TABLE `project_status` (
  `status_id` varchar(20) NOT NULL DEFAULT '0',
  `status_name` varchar(100) NOT NULL,
  `status_desc` text,
  `created_by` varchar(20) NOT NULL DEFAULT 'system',
  `created_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modify_by` varchar(20) NOT NULL DEFAULT 'system',
  `modify_date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `status` enum('added','deleted') NOT NULL DEFAULT 'added'
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `project_status`
--

INSERT INTO `project_status` (`status_id`, `status_name`, `status_desc`, `created_by`, `created_date`, `modify_by`, `modify_date`, `status`) VALUES
('PRST00001', 'New', 'Add New Project', 'system', '2018-05-28 11:05:16', 'system', '2018-05-28 11:05:16', 'added'),
('PRST00002', 'Approve', 'Project Approve', 'system', '2018-05-28 11:05:16', 'system', '2018-05-28 11:05:16', 'added'),
('PRST00003', 'Reject', 'Project Reject', 'system', '2018-05-28 11:05:16', 'system', '2018-05-28 11:05:16', 'added'),
('PRST00004', 'Project Kick Off', 'Project Kick Off', 'system', '2018-05-28 11:05:16', 'system', '2018-05-28 11:05:16', 'added'),
('PRST00005', 'Project Design', 'Project Design', 'system', '2018-05-28 11:05:16', 'system', '2018-05-28 11:05:16', 'added'),
('PRST00006', 'Project Development', 'Project Development', 'system', '2018-05-28 11:05:16', 'system', '2018-05-28 11:05:16', 'added'),
('PRST00007', 'Project Closing ', 'Project Closing', 'system', '2018-05-28 11:05:16', 'system', '2018-05-28 11:05:16', 'added'),
('PRST00008', 'Maintenance', 'Maintenance Process', 'system', '2018-05-31 11:55:40', 'system', '2018-05-31 11:55:40', 'added'),
('PRST00009', 'Maintenance Close', 'Maintenance Close', 'system', '2018-05-31 11:55:40', 'system', '2018-05-31 11:55:40', 'added');

--
-- Trigger `project_status`
--
DELIMITER $$
CREATE TRIGGER `tg_project_status` BEFORE INSERT ON `project_status` FOR EACH ROW begin
 declare x int;
 declare y int;
 declare name_tab varchar(5);
 set y := (select seq_lastno from sequence where seq_table = 'project_status');
 set name_tab := (select table_code from sequence where seq_table = 'project_status');
 update sequence set seq_lastno =  y+1 where seq_table = 'project_status';
 set x := (select seq_lastno from sequence where seq_table = 'project_status');
 set new.status_id = concat(name_tab, LPAD(x, 5, '0'));
 end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `province`
--

CREATE TABLE `province` (
  `province_id` varchar(20) NOT NULL DEFAULT '0',
  `province_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `province`
--

INSERT INTO `province` (`province_id`, `province_name`) VALUES
('PROV00001', 'Aceh'),
('PROV00002', 'Sumatera Utara'),
('PROV00003', 'Sumatera Barat'),
('PROV00004', 'Riau'),
('PROV00005', 'Jambi'),
('PROV00006', 'Sumatera Selatan'),
('PROV00007', 'Bengkulu'),
('PROV00008', 'Lampung'),
('PROV00009', 'Kepulauan Bangka Belitung'),
('PROV00010', 'Kepulauan Riau'),
('PROV00011', 'Jawa Barat'),
('PROV00012', 'Jawa Tengah'),
('PROV00013', 'Jawa Timur'),
('PROV00014', 'Banten'),
('PROV00015', 'Bali'),
('PROV00016', 'Nusa Tenggara Barat'),
('PROV00017', 'Nusa Tenggara Timur'),
('PROV00018', 'Kalimantan Barat'),
('PROV00019', 'Kalimantan Tengah'),
('PROV00020', 'Kalimantan Selatan'),
('PROV00021', 'Kalimantan Timur'),
('PROV00022', 'Kalimantan Utara'),
('PROV00023', 'Sulawesi Utara'),
('PROV00024', 'Sulawesi Tengah'),
('PROV00025', 'Sulawesi Selatan'),
('PROV00026', 'Sulawesi Tenggara'),
('PROV00027', 'Gorontalo'),
('PROV00028', 'Sulawesi Barat'),
('PROV00029', 'Maluku'),
('PROV00030', 'Maluku Utara'),
('PROV00031', 'Papua Barat'),
('PROV00032', 'Papua'),
('PROV00033', 'Daerah Khusus Ibukota Jakarta'),
('PROV00034', 'Daerah Istimewa Yogyakarta');

--
-- Trigger `province`
--
DELIMITER $$
CREATE TRIGGER `tg_province` BEFORE INSERT ON `province` FOR EACH ROW begin
 declare x int;
 declare y int;
 declare name_tab varchar(5);
 set y := (select seq_lastno from sequence where seq_table = 'province');
 set name_tab := (select table_code from sequence where seq_table = 'province');
 update sequence set seq_lastno =  y+1 where seq_table = 'province';
 set x := (select seq_lastno from sequence where seq_table = 'province');
 set new.province_id = concat(name_tab, LPAD(x, 5, '0'));
 end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Struktur dari tabel `sequence`
--

CREATE TABLE `sequence` (
  `no` int(11) NOT NULL,
  `seq_table` varchar(20) NOT NULL,
  `seq_lastno` int(11) NOT NULL,
  `table_code` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `sequence`
--

INSERT INTO `sequence` (`no`, `seq_table`, `seq_lastno`, `table_code`) VALUES
(1, 'audit_trail', 0, NULL),
(2, 'client', 2, 'CLNT'),
(3, 'document', 0, NULL),
(4, 'employees', 23, 'EMPY'),
(5, 'prl', 0, NULL),
(6, 'project', 16, 'PRJT'),
(7, 'task', 0, NULL),
(8, 'team_project', 0, NULL),
(9, 'department', 9, 'DEPT'),
(10, 'division', 2, 'DIVS'),
(16, 'empTitle', 5, 'EMTL'),
(17, 'job', 0, 'JOBS'),
(18, 'school_level', 8, 'SCHL'),
(19, 'province', 34, 'PROV'),
(20, 'city', 514, 'CITY'),
(21, 'testing', 2, 'TEST'),
(22, 'project_status', 9, 'PRST'),
(23, 'notification', 0, 'NOTF');

-- --------------------------------------------------------

--
-- Struktur dari tabel `status`
--

CREATE TABLE `status` (
  `Status_ID` char(1) NOT NULL,
  `Status_Name` varchar(20) NOT NULL,
  `Status_Desc` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `task`
--

CREATE TABLE `task` (
  `Task_ID` varchar(12) NOT NULL,
  `Project_ID` varchar(12) NOT NULL,
  `status_id` varchar(20) NOT NULL,
  `TeamProject_ID` varchar(12) NOT NULL,
  `Task_StartDate` date NOT NULL,
  `Task_EndDate` date NOT NULL,
  `Task_Target` date NOT NULL,
  `Task_Name` varchar(20) NOT NULL,
  `Task_Status` char(1) NOT NULL,
  `Task_Document_No` varchar(20) NOT NULL,
  `Task_Notes` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Struktur dari tabel `team_project`
--

CREATE TABLE `team_project` (
  `TeamProject_ID` varchar(12) NOT NULL,
  `employee_id` varchar(20) NOT NULL,
  `project_id` varchar(20) NOT NULL,
  `Job_ID` char(2) NOT NULL,
  `Task_ID` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Stand-in structure for view `v_client_detail`
-- (Lihat di bawah untuk tampilan aktual)
--
CREATE TABLE `v_client_detail` (
`client_id` varchar(20)
,`name` varchar(50)
,`email` varchar(50)
,`address` varchar(255)
,`city_code` varchar(20)
,`city_name` varchar(50)
,`pic_name` varchar(50)
,`pic_number` varchar(15)
,`pic_email` varchar(50)
,`client_code` varchar(4)
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `v_division_detail`
-- (Lihat di bawah untuk tampilan aktual)
--
CREATE TABLE `v_division_detail` (
`division_id` varchar(20)
,`division_name` varchar(50)
,`department_id` varchar(20)
,`department_name` varchar(50)
,`description` varchar(100)
,`status` enum('added','deleted')
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `v_employees_detail`
-- (Lihat di bawah untuk tampilan aktual)
--
CREATE TABLE `v_employees_detail` (
);

-- --------------------------------------------------------

--
-- Stand-in structure for view `v_project_detail`
-- (Lihat di bawah untuk tampilan aktual)
--
CREATE TABLE `v_project_detail` (
`project_id` varchar(20)
,`client_id` varchar(20)
,`client_name` varchar(50)
,`project_name` varchar(150)
,`mandays` int(10)
,`startDate` varchar(10)
,`endDate` varchar(10)
,`status_id` varchar(20)
,`status_name` varchar(100)
,`created_date` datetime
,`pid` varchar(13)
,`project_manager` varchar(20)
,`nik` varchar(10)
,`email` varchar(100)
,`firstname` varchar(100)
,`lastname` varchar(255)
,`description` text
,`doc_project` varchar(100)
,`doc_size` varchar(100)
,`priority` enum('High','Medium','Low')
);

-- --------------------------------------------------------

--
-- Struktur untuk view `v_client_detail`
--
DROP TABLE IF EXISTS `v_client_detail`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_client_detail`  AS  select `cl`.`client_id` AS `client_id`,`cl`.`name` AS `name`,`cl`.`email` AS `email`,`cl`.`address` AS `address`,`ci`.`city_code` AS `city_code`,`ci`.`city_name` AS `city_name`,`cl`.`pic_name` AS `pic_name`,`cl`.`pic_number` AS `pic_number`,`cl`.`pic_email` AS `pic_email`,`cl`.`client_code` AS `client_code` from (`client` `cl` left join `city` `ci` on((`cl`.`city_code` = `ci`.`city_code`))) ;

-- --------------------------------------------------------

--
-- Struktur untuk view `v_division_detail`
--
DROP TABLE IF EXISTS `v_division_detail`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_division_detail`  AS  select `dv`.`division_id` AS `division_id`,`dv`.`division_name` AS `division_name`,`dept`.`department_id` AS `department_id`,`dept`.`department_name` AS `department_name`,`dv`.`description` AS `description`,`dv`.`status` AS `status` from (`division` `dv` left join `department` `dept` on((`dv`.`department_id` = `dept`.`department_id`))) ;

-- --------------------------------------------------------

--
-- Struktur untuk view `v_employees_detail`
--
DROP TABLE IF EXISTS `v_employees_detail`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_employees_detail`  AS  select left(`emp`.`firstname`,1) AS `Initial`,`emp`.`employee_id` AS `employee_id`,`emp`.`NIK` AS `NIK`,`emp`.`email` AS `email`,`emp`.`password` AS `password`,`emp`.`firstname` AS `firstname`,`emp`.`lastname` AS `lastname`,`emp`.`birthday` AS `birthday`,`emp`.`gender` AS `gender`,`emp`.`address` AS `address`,`ci`.`city_name` AS `city_name`,`emp`.`pincode` AS `pincode`,`emp`.`phone` AS `phone`,`divs`.`division_name` AS `division_name`,`ti`.`title_name` AS `title_name`,`emp`.`join_date` AS `join_date`,`sc`.`school` AS `school`,`emp`.`institusi_name` AS `institusi_name`,`emp`.`start_school` AS `start_school`,`emp`.`completed_school` AS `completed_school`,`emp`.`degree` AS `degree`,`emp`.`grade` AS `grade`,`emp`.`experience_comp` AS `experience_comp`,`emp`.`experience_location` AS `experience_location`,`emp`.`experience_position` AS `experience_position`,`emp`.`experience_report` AS `experience_report`,`emp`.`experience_start` AS `experience_start`,`emp`.`experience_completed` AS `experience_completed`,`emp`.`status` AS `status` from ((((`employees` `emp` left join `city` `ci` on((`emp`.`city_code` = `ci`.`city_code`))) left join `division` `divs` on((`emp`.`division_id` = `divs`.`division_id`))) left join `emptitle` `ti` on((`emp`.`empTitle_id` = `ti`.`empTitle_id`))) left join `school_level` `sc` on((`emp`.`schoollevel_id` = `sc`.`schoollevel_id`))) ;

-- --------------------------------------------------------

--
-- Struktur untuk view `v_project_detail`
--
DROP TABLE IF EXISTS `v_project_detail`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `v_project_detail`  AS  select `pro`.`project_id` AS `project_id`,`pro`.`client_id` AS `client_id`,`cli`.`name` AS `client_name`,`pro`.`name` AS `project_name`,`pro`.`mandays` AS `mandays`,date_format(`pro`.`startDate`,'%d-%m-%Y') AS `startDate`,date_format(`pro`.`endDate`,'%d-%m-%Y') AS `endDate`,`pro`.`status_id` AS `status_id`,`stat`.`status_name` AS `status_name`,`pro`.`created_date` AS `created_date`,`pro`.`pid` AS `pid`,`pro`.`employee_id` AS `project_manager`,`emp`.`NIK` AS `nik`,`emp`.`email` AS `email`,`emp`.`firstname` AS `firstname`,`emp`.`lastname` AS `lastname`,`pro`.`description` AS `description`,`pro`.`doc_project` AS `doc_project`,`pro`.`doc_size` AS `doc_size`,`pro`.`priority` AS `priority` from (((`project` `pro` left join `client` `cli` on((`pro`.`client_id` = `cli`.`client_id`))) left join `project_status` `stat` on((`pro`.`status_id` = `stat`.`status_id`))) left join `employees` `emp` on((`pro`.`employee_id` = `emp`.`employee_id`))) ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `city`
--
ALTER TABLE `city`
  ADD PRIMARY KEY (`city_code`),
  ADD KEY `province_id` (`province_id`);

--
-- Indexes for table `client`
--
ALTER TABLE `client`
  ADD PRIMARY KEY (`client_id`),
  ADD KEY `city_code` (`city_code`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`department_id`);

--
-- Indexes for table `division`
--
ALTER TABLE `division`
  ADD PRIMARY KEY (`division_id`);

--
-- Indexes for table `document`
--
ALTER TABLE `document`
  ADD PRIMARY KEY (`Document_No`);

--
-- Indexes for table `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`employee_id`),
  ADD KEY `city_code` (`city_code`),
  ADD KEY `division_id` (`division_id`),
  ADD KEY `empTitle_id` (`empTitle_id`);

--
-- Indexes for table `emptitle`
--
ALTER TABLE `emptitle`
  ADD PRIMARY KEY (`empTitle_id`);

--
-- Indexes for table `job`
--
ALTER TABLE `job`
  ADD PRIMARY KEY (`Job_ID`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`Notif_ID`),
  ADD KEY `FKNotificati823642` (`employee_id`);

--
-- Indexes for table `project`
--
ALTER TABLE `project`
  ADD PRIMARY KEY (`project_id`),
  ADD KEY `client_id` (`client_id`),
  ADD KEY `status_id` (`status_id`),
  ADD KEY `employee_id` (`employee_id`);

--
-- Indexes for table `project_status`
--
ALTER TABLE `project_status`
  ADD PRIMARY KEY (`status_id`);

--
-- Indexes for table `province`
--
ALTER TABLE `province`
  ADD PRIMARY KEY (`province_id`);

--
-- Indexes for table `sequence`
--
ALTER TABLE `sequence`
  ADD PRIMARY KEY (`no`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`Status_ID`);

--
-- Indexes for table `task`
--
ALTER TABLE `task`
  ADD PRIMARY KEY (`Task_ID`),
  ADD KEY `FKTask857121` (`Task_Status`),
  ADD KEY `FKTask390397` (`Task_Document_No`),
  ADD KEY `FKTask885393` (`status_id`);

--
-- Indexes for table `team_project`
--
ALTER TABLE `team_project`
  ADD PRIMARY KEY (`TeamProject_ID`),
  ADD KEY `FKTeam_proje214919` (`employee_id`),
  ADD KEY `FKTeam_proje153194` (`project_id`),
  ADD KEY `FKTeam_proje756887` (`Job_ID`),
  ADD KEY `FKTeam_proje910071` (`Task_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `sequence`
--
ALTER TABLE `sequence`
  MODIFY `no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `city`
--
ALTER TABLE `city`
  ADD CONSTRAINT `city_ibfk_1` FOREIGN KEY (`province_id`) REFERENCES `province` (`province_id`);

--
-- Ketidakleluasaan untuk tabel `client`
--
ALTER TABLE `client`
  ADD CONSTRAINT `client_ibfk_1` FOREIGN KEY (`city_code`) REFERENCES `city` (`city_code`);

--
-- Ketidakleluasaan untuk tabel `employees`
--
ALTER TABLE `employees`
  ADD CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`city_code`) REFERENCES `city` (`city_code`),
  ADD CONSTRAINT `employees_ibfk_2` FOREIGN KEY (`division_id`) REFERENCES `division` (`division_id`),
  ADD CONSTRAINT `employees_ibfk_3` FOREIGN KEY (`empTitle_id`) REFERENCES `emptitle` (`empTitle_id`);

--
-- Ketidakleluasaan untuk tabel `notification`
--
ALTER TABLE `notification`
  ADD CONSTRAINT `notification_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`);

--
-- Ketidakleluasaan untuk tabel `project`
--
ALTER TABLE `project`
  ADD CONSTRAINT `project_ibfk_1` FOREIGN KEY (`client_id`) REFERENCES `client` (`client_id`),
  ADD CONSTRAINT `project_ibfk_2` FOREIGN KEY (`status_id`) REFERENCES `project_status` (`status_id`),
  ADD CONSTRAINT `project_ibfk_3` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`);

--
-- Ketidakleluasaan untuk tabel `task`
--
ALTER TABLE `task`
  ADD CONSTRAINT `FKTask390397` FOREIGN KEY (`Task_Document_No`) REFERENCES `document` (`Document_No`),
  ADD CONSTRAINT `FKTask857121` FOREIGN KEY (`Task_Status`) REFERENCES `status` (`Status_ID`),
  ADD CONSTRAINT `task_ibfk_1` FOREIGN KEY (`status_id`) REFERENCES `project_status` (`status_id`);

--
-- Ketidakleluasaan untuk tabel `team_project`
--
ALTER TABLE `team_project`
  ADD CONSTRAINT `FKTeam_proje756887` FOREIGN KEY (`Job_ID`) REFERENCES `job` (`Job_ID`),
  ADD CONSTRAINT `FKTeam_proje910071` FOREIGN KEY (`Task_ID`) REFERENCES `task` (`Task_ID`),
  ADD CONSTRAINT `team_project_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`),
  ADD CONSTRAINT `team_project_ibfk_2` FOREIGN KEY (`project_id`) REFERENCES `project` (`project_id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
