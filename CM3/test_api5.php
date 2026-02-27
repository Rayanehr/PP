<?php
require_once 'config/config.php';
require_once 'services/StudentService.php';
// recuperation des données 
$students = StudentService::getAllStudents();
$student = StudentService::get_student_by_id(1);

//Affichage
require_once 'views/students.php' ; 

require_once 'views/student.php' ; 