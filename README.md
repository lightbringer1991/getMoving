# getMoving
Govhack 2017 project
django 1.8
python 2.7.*

requests
psycopg2
patterns
jsonfield

# needs to be run everytime models.py gets updated
# regarding tables and columns
python manage.py makemigrations
python manage.py migrate


# VPS SERVER apt installation/update
sudo apt-get install postgresql postgresql-contrib

sudo adduser getmoving
password 7giug87y+s

sudo -i -u postgres //switch to postgres id for posgresql
psql CREATE DATABASE getmoving; // create getmoving database

/etc/postgresql/9.5/main/postgresql.conf
listen_addresses = '*'

/etc/postgresql/9.5/main/pg_hba.conf
host all all 0.0.0.0/0 trust


### Installation
1. clone project
2. install npm dependencies `npm install`
3. run `node_modules/.bin/gulp` to compile public data. Alternatively, run `node_modules/.bin/gulp devChange` to watch to changes during development
4. ensure `pip` is installed
5. install django: `pip install django==1.8`
6. install postgres database
  - `sudo apt-get install postgresql postgresql-contrib`
  - `sudo adduser getmoving`
  - `sudo -i -u postgres // switch to postgres id for posgresql`
  - `psql CREATE DATABASE getmoving; // create getmoving database`
  - edit the following files with the corresponding values
    ```bash
        /etc/postgresql/9.5/main/postgresql.conf
        listen_addresses = '*'
    ```

    ```bash
        /etc/postgresql/9.5/main/pg_hba.conf
        host all all 0.0.0.0/0 trust
    ```
7. `python manage.py makemigrations && python manage.py migrate`