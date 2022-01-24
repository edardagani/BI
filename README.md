Business Intelligence System that does :

1) API aggregation once every quarter

2) Insertion of data to the staging area

3) Commence ETL pipeline procedures

4) Connection of normalized data with front end (GUI?)

5) Data visualization 

6) Data requests by the veterinarians to make educated decisions

######**PostGreSQL Setup Steps**

First of all you have to install PostGreSQL using postgres installer : 

Step 1:

Download Postgres Installer [here](https://www.postgresql.org/download/). Postgres Installer is available for PostgreSQL 9.5, 9.6, 10, 11, and 12(beta).

Step 2:

Click on the executable file to run the installer.

Step 3:

Select your preferred language.


![PGInstaller-GUI-installer-13](https://user-images.githubusercontent.com/24418024/150790398-3b5b267f-ce0b-420d-a165-742d75d2a8d0.jpg)


Step 4:

Specify directory where you want to install PostgreSQL.


![PGInstaller-GUI-installer3](https://user-images.githubusercontent.com/24418024/150790429-060a5885-3881-49ee-a6bb-95ec33701c47.jpg)


Step 5:

Specify PostgreSQL server port. You can leave this as default if you’re unsure what to enter.


![PGInstaller-GUI-installer](https://user-images.githubusercontent.com/24418024/150790451-16398af2-6750-4fbc-a55c-bdb39ab7a52b.jpg)


Step 6:

Specify data directory to initialize PostgreSQL database.

![PGInstaller-GUI-installer5](https://user-images.githubusercontent.com/24418024/150790757-c437ef1b-1e98-4255-a7d3-8143bf88f9e0.jpg)


Step 7:

Create a PostgreSQL user password.

![PGInstaller-GUI-installer6](https://user-images.githubusercontent.com/24418024/150790812-4df0e3a0-d60d-4592-adab-a869b97622f7.jpg)



Step 8:

Create password for database Superuser.

![PGInstaller-GUI-installer7](https://user-images.githubusercontent.com/24418024/150790802-9d3507c9-3db7-487f-a98d-a05a3b9f0844.jpg)



Step 9:

Click next to begin PostgreSQL installation.
