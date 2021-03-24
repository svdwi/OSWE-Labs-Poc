
sudo docker exec $1 rm -rf /var/lib/mysql/ib_logfile0
sudo docker exec $1 rm -rf /var/lib/mysql/ib_logfile1
sudo docker exec $1 chmod 0750 /var/log/mysql
sudo docker exec $1 chmod 0775 /var/log
sudo docker exec $1  chmod 0755 /var
sudo docker exec $1  touch /var/log/mysql/error.log
sudo docker exec $1  chmod 0644 /var/log/mysql/error.log
sudo docker exec $1 touch  /var/log/mysql/slow.log
sudo docker exec $1 chmod 0644   /var/log/mysql/slow.log
sudo docker exec $1 chmod 0444   /etc/mysql/mysql.conf.d/mysqld.cnf
sudo docker cp ~/Desktop/mysqld.cnf $1:/etc/mysql/mysql.conf.d/mysqld.cnf
sudo docker exec $1 chmod 0444   /etc/mysql/mysql.conf.d/mysqld.cnf
sudo docker restart $1 
