<?php
// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve the form data
    $username = $_POST["Username"];
    $firstname = $_POST["firstname"];
    $lastname = $_POST["lastname"];
    $course = $_POST["course"];
    $subject = $_POST["subject"];

    // Connect to the MySQL database
    $servername = "localhost"; // Change this if your server is on a different host
    $username_db = "root"; // Change this to your MySQL username
    $password_db = ""; // Change this to your MySQL password
    $dbname = "feedback"; // Change this to your database name

    $conn = new mysqli("localhost", "root", "", "feedback");

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Prepare and execute the SQL query to insert the data into the 'feedback' table
    $sql = "INSERT INTO users (username, firstname, lastname, course, subject) 
            VALUES ('$username', '$firstname', '$lastname', '$course', '$subject')";

    if ($conn->query($sql) === TRUE) {
        echo '<script>alert("Feedback submitted successfully!");</script>';
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    // Close the database connection
    $conn->close();
}
?>
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {font-family: Arial, Helvetica, sans-serif;}
* {box-sizing: border-box;}
form {border: 3px solid #f1f1f1; width: 700px;margin: 0 auto;}

input[type=text], select, textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  margin-top: 6px;
  margin-bottom: 16px;
  resize: vertical;
}

input[type=submit] {
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

input[type=submit]:hover {
  background-color: #45a049;
}

.container {
  border-radius: 5px;
  background-color: #f2f2f2;
  padding: 20px;
}
.button{
  background-color: #04AA6D;
  color: white;
  padding: 12px 20px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>
</head>
<body>

<h3>Feedback Form</h3>

<div class="container">
  <form method="post" action="feedback.php">
    <label for="Username">Username</label><br>
    <input type="text" id="fname" name="Username" placeholder="Enter your email...."><br>
    <label for="fname">First Name</label>
    <input type="text" id="fname" name="firstname" placeholder="Your name..">

    <label for="lname">Last Name</label>
    <input type="text" id="lname" name="lastname" placeholder="Your last name..">

    <label for="course">Course</label>
    <select id="course" name="course">
      <option value="Python">Python</option>
      <option value="Java">Java</option>
      <option value="C">C</option>
      <option value="R">R</option>
      <option value="Matlab">Matlab</option>
      <option value="Html">Html</option>
      <option value="Css">Css</option>
    </select>

    <label for="subject">Subject</label>
    <textarea id="subject" name="subject" placeholder="Write something.." style="height:200px"></textarea>

    <input type="submit" value="Submit">
  </form>
  <form action="elearning.html">
        <input type="submit" value="Back To Home">
  </form>
</div>

</body>
</html>
