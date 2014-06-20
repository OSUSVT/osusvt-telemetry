#!/usr/bin/env bash
USER=svtremote
PASSWORD=Phenix
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" &&
echo $DIR

if [ $# -eq 0 ] ; then
	echo "USAGE ./$0 hostname" &&
	exit
fi 

HOST=$1

service mysqld stop
rm -rf /var/lib/mysql/* &&
service mysqld start &&
/usr/bin/mysql_secure_installation &&
service mysqld restart &&
touch mysql.sql &&
rm mysql.sql &&
echo "mysqldump -u $USER -p$PASSWORD -h$HOST --extended-insert --all-databases --add-drop-database --disable-keys --flush-privileges --quick --routines --triggers > mysql.sql" &&
mysqldump -u$USER -p$PASSWORD -h $HOST --extended-insert --all-databases --add-drop-database --disable-keys --flush-privileges --quick --routines --triggers > mysql.sql &&
read -s -p "Pleas Enter the Local Root Password you Just Created: " root &&
cat mysql.sql | mysql -uroot -p$root &&
echo "Remote Database Imported..." &&
grep -o 'CHANGE MASTER TO MASTER_LOG_FILE='\''.*'\'', MASTER_LOG_POS=.*;$' mysql.sql | mysql -uroot -p$root &&
echo "CHANGE MASTER TO MASTER_HOST='$HOST', MASTER_USER='$USER', MASTER_PASSWORD='$PASSWORD'; START SLAVE;" | mysql -uroot -p$root &&
rm mysql.sql &&
echo "Setup Complete... Verify by running SHOW SLAVE STATUS; in a mysql prompt" ||
echo "Setup Failed..."

