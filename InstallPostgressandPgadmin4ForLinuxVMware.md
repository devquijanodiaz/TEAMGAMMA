# !/bin/bash
# installing postgress on your VMware Centos 8
dnf install postgresql-server

# checking your postgres version
postgres -V

# Initializing database in '/var/lib/pgsql/data'
# initializing, logs are in /var/lib/pgsql/initddb_postgresql.log
sudo postgresql-setup --initdb --unit postgresql

# starting the postgresql service
sudo systemctl start postgresql

# enabliing postgresql service and creating a symlink PATH of the spostgresql ervice
sudo systemctl enable postgresql

# checking that status of the postgres service
sudo systemctl status postgresql

# finding the file postgresql.conf in the system
sudo find / -name postgresql.conf

# going into the .conf file and editing listen_addresses = 'localhost' to   listen listen_addresses = '0.0.0.0' 
sudo vi /var/lib/pgsql/data/postgresql.conf

# restarting postgresql service
sudo systemctl restart postgresql

# checking the status of the postgresql service
sudo systemctl status postgresql

# going into the postgresql server
sudo -u postgres psql

# exit/quit out of the server
\q

# searching for the .conf file in the system
sudo find /-name pg_hba.conf
# gooing into the .conf file to edit it
# at the end of the file go to the TYPE (local) line and change the METHOD peer to password
sudo vi /var/lib/pgsql/data/pg_hba.conf

# restart the service
sudo systemctl start postgresql

# log back into the server
sudo -u postgres psql

# looking for the .log file and then vi into it to edit
sudo find / -name postgresql-*.log


# PGADMIN INSTALLATION
# Add EPEL repository using our guide below.
sudo dnf -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

# enable PowerTools repository as it contain the packages we’ll need
sudo dnf config-manager --set-enabled PowerTools

# You need to add PostgreSQL RPM repository, which should have been done while installing PostgreSQL
sudo dnf -y install https://download.postgresql.org/pub/repos/yum/reporpms/EL-8-x86_64/pgdg-redhat-repo-latest.noarch.rpm

# Then install the pgAdmin package:
sudo dnf -qy module disable postgresql
sudo dnf install pgadmin4

# Start and enable httpd
sudo systemctl start httpd && sudo systemctl enable httpd

# check status of httpd service
systemctl status httpd

# Rename pgAdmin Apache configuration sample:
sudo cp /etc/httpd/conf.d/pgadmin4.conf.sample /etc/httpd/conf.d/pgadmin4.conf


# Confirm configuration syntax to prevent any errors and restart httpd service.
sudo httpd -t
Syntax OK
sudo systemctl restart httpd

# Create pgAdmin data directories
sudo mkdir -p /var/lib/pgadmin4/ /var/log/pgadmin4/

# Edit config_local.py
sudo vi /usr/lib/python3.6/site-packages/pgadmin4-web/config_distro.py

# Run the following command to create the configuration database:
sudo dnf -y install python3-bcrypt python3-pynacl
sudo python3 /usr/lib/python3.6/site-packages/pgadmin4-web/setup.py

# Set permissions for pgAdmin directories to apache user:
sudo chown -R apache:apache /var/lib/pgadmin4 /var/log/pgadmin4


# If you have SELinux running in enforcing mode,
# create and apply a policy to allow Apache user access pgAdmin directories:
sudo semanage fcontext -a -t httpd_sys_rw_content_t "/var/lib/pgadmin4(/.*)?"
sudo semanage fcontext -a -t httpd_sys_rw_content_t "/var/log/pgadmin4(/.*)?"
sudo restorecon -Rv /var/lib/pgadmin4/
sudo restorecon -Rv /var/log/pgadmin4/

# 
sudo systemctl restart httpd

# if you have an active firewall service, allow http port
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload

# Open http://servername_or_ip/pgadmin4 to log in to the pgAdmin with the credentials created

