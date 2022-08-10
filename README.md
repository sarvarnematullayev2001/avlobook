# Install dependencies
```bash
sudo apt-get install aptitude

sudo aptitude install gdal-bin libgdal-dev
sudo aptitude install python3-gdal
sudo aptitude install binutils libproj-dev
sudo apt install postgis postgresql-11-postgis-3
sudo apt-get install postgresql-11-postgis-3-scripts
```

# Database setup
```
bash
CREATE USER avlobook_user WITH PASSWORD 'avlobook_user_1234';
CREATE DATABASE avlobook WITH OWNER avlobook_user;

\c avlobook;

CREATE EXTENSION postgis;
```