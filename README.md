
#  OSWE -LABS 

Dockerized labs For Web Expert (OSWE) certification. Preparation for coming AWAE Training ... 
 
 
## Available labs for the OSWE 

 1. **ATutor** is an Open Source Web-based Learning Content Management
    System. [Wikipedia](https://en.wikipedia.org/wiki/ATutor)
 2. **DNN** is a web content management system and web application framework based on **Microsoft .NET**

 - ATutor Authentication Bypass and RCE (2.2.1) CVE-2016-2555
 - ATutor LMS Type Juggling Vulnerability (<=2.2.1) CVE-?
 - DotNetNuke Cookie Deserialization RCE (<9.1.1) CVE-2017-9822



## Instructions
You must follow the following steps:
For Atutor : 
 ```
$ ./run_lab.sh
```
-   Run : Run Docker file ( build & compose up)
-   Clean : Clear all Logs File
-   Stop : Stop all docker container
-   Ports : Check Ports Of lab for any error

For  DotNetNuke-DNN
 ```
$ cd DotNetNuke-DNN/dnn-platform-version
```
 Compile compose file (docker-compose.yml) with Docker Compose in Powershell or Bash (WSL) console:
 ```
$ docker-compose up
```



