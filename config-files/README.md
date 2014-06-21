Steps to build Telemetry Server
===============================

Assuming a Complete and Updated CentOS 6.5 Setup (Minimal install will work)
Assume root for all commands

##Install Nessasary Packages

```
curl http://mirror.us.leaseweb.net/epel/6/i386/epel-release-6-8.noarch.rpm #Check for new release
yum localinstall epel-release-6-8.noarch.rpm
yum install python-devel python-virtualenv python python-pip vim httpd httpd-devel git mod_ssl wget unzip zip mod_wsgi gcc
```

##Install MySQL

Find the file from here http://dev.mysql.com/downloads/repo/

```
wget http://dev.mysql.com/get/mysql-community-release-el6-5.noarch.rpm
yum localinstall mysql-community-release-el6-5.noarch.rpm
yum install mysql-community-server mysql-community-devel
````

##Configure Networking
Not sure how much of this is nessasary

```
iptables -I INPUT -p tcp --dport 80 -j ACCEPT

# OpenVPN
iptables -A INPUT -i eth0 -m state --state NEW -p udp --dport 1194 -j ACCEPT

# Allow TUN interface connections to OpenVPN server
iptables -A INPUT -i tun+ -j ACCEPT

# Allow TUN interface connections to be forwarded through other interfaces
iptables -A FORWARD -i tun+ -j ACCEPT
iptables -A FORWARD -i tun+ -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -o tun+ -m state --state RELATED,ESTABLISHED -j ACCEPT

# NAT the VPN client traffic to the internet
iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE

service iptables save
```

###Enable Port Forwarding

```
sed -i 's/^net.ipv4.ip_forward =.*/net.ipv4.ip_forward = 1/' /etc/sysctl.conf
sysctl -p
```

##Turn stuff on and turn off SELinux

```
chkconfig httpd on
chkconfig sshd on
chkconfig mysqld on
sed -i 's/^SELINUX=.*/SELINUX=disabled/' /etc/sysconfig/selinux
```

##Get the Repo

```
cd /var/www/html/
git clone https://github.com/OSUSVT/osusvt-telemetry.git
mv osusvt-telemetry telemetry
cd telemetry/config-files/
bash setup.bash
```

##Setup our user

```
useradd solar
passwd solar
sed -i 's/^User .*/User solar/' /etc/httpd/conf/httpd.conf
sed -i 's/^Group .*/Group solar/' /etc/httpd/conf/httpd.conf
chmod 755 /var/www/html/telemetry/
chown solar:solar /var/www/html/telemetry/
```

##Set up our Python Virtualenv

```
cd /var/www/html/telemetry/
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```

##Reboot

```
reboot
```

##Start MySQL Replication
Where 0.0.0.0 is the IP or Hostname of the solarcar
Follow Instructions, `OSUSVT` is our usual root password, press enter for all of the secure_setup prompts. Some parts will be very slow.

```
bash /var/www/html/telemetry/config-files/resetdatabase.bash 0.0.0.0
service httpd restart
```

