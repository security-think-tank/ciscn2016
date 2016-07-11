???<?php
       require_once  '../connect.php';
       checkLogined();
       if($_FILES){
       $upfile=$_FILES["file"]["name"];
       $fileTypes=array(
              'jpg',  'png','gif','zip','rar','txt'
       );
 
       function  getFileExt($file_name)
       {
         while($dot = strpos($file_name, "."))
          {
                $file_name =  substr($file_name, $dot+1);
          }
         return $file_name;
       }
       $test1=  strtolower(getFileExt($upfile));
       if(!in_array($test1,  $fileTypes))
       //?¡ê???£¤???????¡À????
       {
              echo  "<font color='red'>???¨¨???????  ?-¡è?¡À?????????????</font>";
              exit();
       }
       else{
       $nfile=md5(rand(10,1000).time()).".".$test1;
       move_uploaded_file($_FILES["file"]["tmp_name"],  "../file123asdp/" . $nfile);
       echo  "ok!<a  href=../file123asdp/".$nfile.">$nfile</a>";
       }
       }
?>
 
<!doctype html>
<html>
<head>
       <meta  charset="UTF-8">
       <title>Document</title>
       <link  href="css/admin.css" rel="stylesheet"  type="text/css"/>
</head>
<body>
       <div>
              <h2>???????????¡é</h2>
       </div>
       <div>
              <div>
                     <ul>
                            <li><a  href="admininfile.php?name=add">???????????  </a></li>
                            <li><a  href="admininfile.php?name=manage">???????????  </a></li>
                            <li><a  href="admininfile.php?name=upload">?????  ??????</a></li>
                     </ul>
              </div>
              <div>
                     <div>
                            <h3>?????  ??????</h3>
                      
                            <form  action="" method="post"  enctype="multipart/form-data">
<label  for="file">Filename:</label>
<input type="file"  name="file" id="file" /> 
<br />
<input type="submit"  name="submit" value="Submit" />
</form>
                     </div>
              </div>
       </div>
</body>
</html>
