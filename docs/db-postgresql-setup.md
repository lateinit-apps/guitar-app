# PostgreSQL database setup

## General information

You will need to install PostgreSQL distribution in order to setup the database. Please follow the
[link](https://www.postgresql.org/download/) to download the package suitable for your system. During
the basic installation process you may be asked to specify a password for the superadmin `postgres`
user. DBMS also should create a `postgres` database as well to enable you joining and configuring stuff.

For the time being, a dedicated DB-user will be established for connection to the PostgreSQL DBMS.
Before running python code for the database creation, one needs to create user via `psql` or
`pgAdmin4` utilities. Here, the command line approach will be enlightened (i.e. through `psql`).

## Linux notes

### User initiation

In Unix, PostgreSQL uses role-based authentication, which is enabled by default so instead of
logging in as a superuser (`postgres` initially), administrator should create another role with
limited but still powerful entitlements. Let it has a name `moderator`.

Connect to any of the databases presented in your DBMS. There should be a `postgres` database which
is originated along with the superuser, but feel free to use any else. For instance, let your
working database be called `medium`. As a `moderator`, you should be able to establish a connection
either with

```shell
psql -U moderator -d medium      # in case you have default peer auth
```

or

```shell
psql -U moderator -W -d medium   # in case you've enabled md5 auth
```

command.

Now, execute the following statement:

```shell
CREATE USER crack_user WITH ENCRYPTED PASSWORD 'crack_pass' CREATEDB;
```

It will create a user with an ability to create any databases inside the DBMS environment. To ensure
it can, use the `\du` command to display a table with roles configured in PostgreSQL and their
attributes.

### Authentication settings

For making possible to login as a newly created `crack_user`, you need to edit the
`/etc/postgresql/10/main/pg_hba.conf` to specify the authentication method for the user. Add the
following lines to the config for the `medium` (because we're using it for the first steps) and
the upcoming `crack` database:

```shell
local   medium   crack_user     md5
local   crack    crack_user     md5
```

For the changes to be applied one should consider restarting the `postgresql` daemon by
`sudo service postgresql restart`. Finally, by the `psql -U crack_user -W -d medium` a newly created
user can connect to the intermediate database.

### Database origination

Now it is time to 'crack' database to be created by the `crack_user`. Execute

```shell
CREATE DATABASE "crack" ENCODING 'UTF8';
```

You can assure database is created by entering `\l` command. Since this moment, you can access
the database from python's code.

## Windows notes

You can face an issue with 866 and 1251 encoding pages discrepancies in the Windows `cmd` and `psql`
if the default OS locale is not US English. To avoid such problem, before running the `psql` executable
specify `chcp 1251` in the shell to replace the default one. For additional info please refer to
[link](https://iu5bmstu.ru/index.php/PostgreSQL_-_%D0%9A%D0%B8%D1%80%D0%B8%D0%BB%D0%BB%D0%B8%D1%86%D0%B0_%D0%B2_psql_%D0%BF%D0%BE%D0%B4_Windows).
Then, make sure you do have the `<path_to_postgresql_installation>\bin\psql.exe` entry in your
PATH envionment variable. Next, all the setup process is similar to one described for Linux case
except you don't need to do any configuration file editing as the default authentication for
Windows is performed via password specification.
