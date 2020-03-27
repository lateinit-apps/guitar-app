# User initiation

Instructions are provided for Linux PostgreSQL installation.

For the time being, a dedicated DB-user will be established for connection to the PostgreSQL DBMS.
Before running python code for the database creation, one needs to create user via `psql` or 
`pgAdmin3` utilities.

In Unix, PostgreSQL uses role-based authentication, which is enabled by default so instead of 
logging in as a superuser (`postgres` initially), administrator should create another role with 
limited but still powerful entitlements. Let it has a name `moderator`. 

Connect to any of the databases presented in your DBMS. There should be a `postgres` database which
is originated along with the superuser, but feel free to use any else. For simplicity, let it be 
called `medium`. As a `moderator`, you are able to execute the following statement:

```
CREATE USER crack_user WITH ENCRYPTED PASSWORD 'crack_pass' CREATEDB;
```

It will create a user with an ability to create any databases inside the DBMS environment. To ensure
it can, use the `\du` command to display a table with roles configured in PostgreSQL and their 
attributes. 

# Authentication settings

For making possible to login as a newly created `crack_user`, you need to edit the 
`/etc/postgresql/10/main/pg_hba.conf` to specify the authentication method for the user. Add the 
following lines to the config for the `medium` (because we're using it for the first steps) and 
the upcoming `crack` database:

```
local   medium   crack_user     md5
local   crack    crack_user     md5
```

For the changes to be applied one should consider restarting the `postgresql` daemon by
`sudo service postgresql restart`. Finally, by the `psql -U crack_user -W -d medium` a newly created 
user can connect to the intermediate database.

# Database origination

Now it is time to 'crack' database to be created by the `crack_user`. Execute 

```
CREATE DATABASE "crack" ENCODING 'UTF8';
```

You can assure database is created by entering `\l` command. Since this moment, you can access
the database from python's code.
