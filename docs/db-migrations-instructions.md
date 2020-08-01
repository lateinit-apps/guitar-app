# Alembic migrations instructions

## Alembic in a nutshell

> Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database 
> Toolkit for Python.
> &mdash; *Introductory from the main Alembic webpage*

To be concise, Alembic provides comprehensible *werkzeugen* for undertaking DB manipulations.
It allows to organize series of changes as a row of revisions, akin to the Git. You can handle
multiple branches, upgrade and downgrade your DB state, and so on.

## Under-hood basics

Alembic operates a helper table &mdash; `alembic_version`. It holds only one string value for
tracking the most recent revision for the database. In order to associate Alembic with your
database, you need to edit `alembic.ini` configuration file located in the Alembic migration
environment.

![image depicting `alembic_version` contents](images/alembic-version-query.png)

Environment is a directory of scripts specific to a particular application. The environment is
created just once, and is then maintained along with the application’s source code itself. It is
generated using the `init` command of Alembic, and is then customizable to suit the specific
needs of the application. In our specific case, the environment is under the `/migrations` catalog.

Alembic can view the status of the database and compare against the table metadata in the
application, generating the *obvious* migrations based on a comparison. This is achieved using
the `--autogenerate` option to the alembic `revision` command, which places so-called "candidate"
migrations into the new migrations file.

There are two modes for migration conduction. In the `offline` mode, Alembic generates
SQL-expressions for the detected changes, so you can run these statements later &mdash; it is
useful when you don't have enough entitlements to access the DB. Conversely, the `online` mode is
to be used for direct database connection.

## How to prepare and run a migration

- Make some changes into the model on the SQLAlchemy level (e.g. create a new column `foo`
    for the table `Bar`)
- Edit `sqlalchemy.url` entry in the `alembic.ini` to specify actual URL for your DB instance
    (**do not push your credentials to the VCS; make sure modified `alembic.ini` is not included
    to the stage**). To ensure your connection is OK, you can execute `alembic current`. Moreover,
    in the case of clean initiation, it will create an `alembic_version` table.
- While in `.../rearguarde`, run `alembic revision --autogenerate -m <your revision message>`.
    Reckon revision messages as commit messages: keep'em concise and dense. This step will bring
    a Python migration script under `migrations/versions` with `upgrade` and `downgrade` functions.
- Review the generated file, (optionally) make some adjustments, and run `alembic upgrade head`.
    This command directly starts the database manipulations, so please be sure your changes are
    correct.

## More information

- [Alembic documentation](https://alembic.sqlalchemy.org/en/latest)
- [Migrations guide](https://www.compose.com/articles/schema-migrations-with-alembic-python-and-postgresql/)
