# Guitar app

Upcoming guitar app built with Flask/SQLAlchemy, a bit of frontend (under decision) and with a pinch
of love.

## Development

The project is intended to be built inside the Python virtual environment. For that, use
`python -m venv venv` in the root of the project. Executing `source venv/bin/activate` will provide
an access into virtual env. Run `deactivate` to exit from the environment.

## Launching application

All required python modules are listed in `requirements.txt`. A `cfg.py` is comprised of
configuration classes definitions. An example of launching the application:
`python app.py config.ProductionConfig`.
