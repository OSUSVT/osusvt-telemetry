Hey,

Here is the VM. I haven't seen any bugs yet...
​
 [Telemetry VM.zip](https://docs.google.com/a/onid.oregonstate.edu/file/d/0B-H3fZ3A_WMqX1J4djhzeTVyLWs/edit?usp=drive_web)
​
---

root password: `OSUSVT`

user account:
```
username: solar
password: Phenix
```

---

I humbly recommend changing the amount of ram and number of cores to the maximum you feel comfortable with. 
Load it into vmware, boot it up, ssh as root, then run:

Replace 0.0.0.0 with the IP or Hostname of the solarcar and follow Instructions, OSUSVT is our usual root password, press enter for all of the secure_setup prompts. Some parts will be very slow.

```
cd /var/www/html/telemetry && git pull origin master
bash /var/www/html/telemetry/config-files/resetdatabase.bash 0.0.0.0
service httpd restart
```

---

If your curious about how the server is setup visit [the github documentation](https://github.com/OSUSVT/osusvt-telemetry/blob/master/config-files/README.md).

---

The following commands stop the Slave IO Thread and Restart it, this might be useful if the car computer has been restarted or they have gotten out of sync.

```
mysql -uroot -pOSUSVT -e "STOP SLAVE IO_THREAD; START SLAVE IO_THREAD;" solarcar #Where OSUSVT is root password for Telemetry Box
```

---

I forgot to give solar sudo, but I don't think that it needs it...
If so do `visudo` then add a line that looks like so

```
solar    ALL=(ALL)    NOPASSWD: ALL
```
