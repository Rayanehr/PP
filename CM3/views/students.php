<!DOCTYPE html>
<html lang="fr"> 
<head> 
    <meta charset="UTF-8"> 
    <title> Liste des etudiants </title> 
    <link rel="stylesheet" href = "assets/style.css"> 
</head>
<body>
    <h1> Liste des etudiants </h1> 
<ul> 
<?php foreach ($students as $student) : ?> 
    <li> 
        <?= $student['name'] ?> (<?= $student['age'] ?> ans ) 
    </li>
<?php endforeach; ?> 
</ul>
</body>
</html>
