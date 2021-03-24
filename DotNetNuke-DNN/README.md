# DotNetNuke LAB 
Just a lab  for the DotNetNuke Cookie Deserialization RCE (<9.1.1) CVE-2017-9822

## Instructions
You must follow the following steps:
1. Install Docker containers in your Windows SO (Windows Server 2016 or Windows 10 Fall Creators Update) (follow official steps https://docs.docker.com/docker-for-windows/install/)
2. Clone this repository.
3. Change to folder of the DNN version you want to run.
 ```
$ cd DNN-Dockerized/dnn-platform-version
```
4. Compile compose file (docker-compose.yml) with Docker Compose in Powershell or Bash (WSL) console:
 ```
$ docker-compose up
```
6. Open your browser at http://localhost and enjoy!
