<?php
require_once 'config/config.php';
require_once 'services/StudentService.php';
// recuperation des données 
$students = StudentService::getAllStudents();
//Affichage
require_once 'views/students.php' ; 