Docker configuration for Apache, PHP 7.4, MySQL 8 and phpmyadmin.

1. Create sessions folder.
2. Create data/mysq folder.
3. Create logs/mysql folder.
4. Run: docker-compose build
5. Run: docker-compose up


phpmyadmin username / password: root / password


Config logs mysql :

sudo docker exec a258924db900 chmod 0750 /var/log/mysql
sudo docker exec a258924db900 chmod 0775 /var/log
sudo docker exec a258924db900  chmod 0755 /var
sudo docker exec a258924db900  chmod 777 /var/log/mysql/error.log
sudo docker exec a258924db900 chmod 0444   /etc/mysql/mysql.conf.d/*
sudo docker exec a258924db900 touch  /var/log/mysql/slow.log
sudo docker exec a258924db900 chmod 666   /var/log/mysql/slow.log
sudo docker cp ~/Desktop/mysqld.cnf 34b2913dd61a:/etc/mysql/mysql.conf.d/mysqld.cnf
sudo docker restart a258924db900 

