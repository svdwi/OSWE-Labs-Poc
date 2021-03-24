#!/bin/bash

check_ports () {
   string="8009 8010 3306"
for value in $string ;do echo -n ` nc -vz 127.0.0.1  $value  ` ; done

}


clean_logs(){
	
echo "[+] Clean up Logs files and Database   ... "
` sudo rm -rf data/mysql/* sessions/* logs/*   `
}


stop_docker_container(){
	
echo "[+] stop all Container mysql & phpadmin & webserver "
string=`sudo docker ps -aq  `
for value in $string; do echo  `sudo docker rm -f  $value ` ; done


}


build_and_run(){

sudo service mysql stop &> /dev/null

if ! docker --version  &> /dev/null
then 
	echo " docker Not found !! "
	exit
fi 

if ! docker-compose -v  &> /dev/null
then
    echo " docker-compose Not Found !! "
    exit
else

sudo docker-compose	build    
sudo docker-compose up   


fi

	
	
}




case "$1" in
        ports)
            check_ports
            ;;
         
        clean)
            clean_logs
            ;;
         
        stop)
            stop_docker_container
            ;;
        run)
            build_and_run
            ;;
           
         
        *)
			echo "Usage: $0 [OPTION]"
			echo " "
			echo " run             build & compose up"
			echo " clean           clean logs files "
			echo " stop            stop docker container"
			echo " ports           check ports |apache|phpmyadmin|mysql"
		echo " " 
            
            exit 1
 
esac


