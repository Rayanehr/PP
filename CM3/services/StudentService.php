<?php 
class StudentService
{ 
    public static function getAllStudents() 
    { 
        $url = API_BASE_URL . '/students' ; 
        $response = file_get_contents($url) ; 

        return json_decode($response, true) ; 
    }
     public static function get_student_by_id($id) 
    { 
        $url = API_BASE_URL . '/students/' . $id ; 
        $response = file_get_contents($url) ; 

        return json_decode($response, true) ; 
    }
}