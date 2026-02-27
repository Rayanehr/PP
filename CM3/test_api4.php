<?php
require_once 'config/config.php';
require_once 'services/StudentService.php';
// Appel du service
$students = StudentService::getAllStudents();
echo "<h1>Liste des étudiants</h1>";
foreach ($students as $student) {
    echo $student['prenom'] . "-" . $student['age'] . "ans<br>" ; 
 }