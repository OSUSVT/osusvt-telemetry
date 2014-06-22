#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )" &&
echo $DIR

rm -f /etc/httpd/conf.d/telemetry.conf &&
touch /etc/httpd/conf.d/telemetry.conf &&
cat $DIR/telemetry.conf >> /etc/httpd/conf.d/telemetry.conf &&
echo "telemetry.conf Coppied to /etc/httpd/conf.d/telemetry.conf"

rm -f /etc/httpd/conf.d/welcome.conf

rm -f /etc/my.cnf &&
touch /etc/my.cnf &&
cat $DIR/my.cnf >> /etc/my.cnf &&
echo "my.cnf Coppied to /etc/my.cnf"
