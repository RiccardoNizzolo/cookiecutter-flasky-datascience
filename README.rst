cookiecutter-flask
==================

A Data Science template with flask, docker and jenkins for cookiecutter_.

.. _cookiecutter: https://github.com/audreyr/cookiecutter




Use it now
----------
::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/RiccardoNizzolo/cookiecutter-devops-datascience.git

You will be asked about your basic info (name, project name, app name, etc.). This info will be used in your new project.

Features
--------

- Expose Restfull for each trained model
- Modularization of the data science development process
- Testing for the data science pipeline
- Automatic model persistence with metadata
- History of all trainded models with performance, commit and statistics
- Flask-SQLAlchemy ready
- Easy database migrations with Flask-Migrate
- Configuration in environment variables, as per `The Twelve-Factor App <https://12factor.net/config>`_
- Flask's Click CLI configured with simple commands
- Utilizes best practices: `Blueprints <http://flask.pocoo.org/docs/blueprints/>`_ and `Application Factory <http://flask.pocoo.org/docs/patterns/appfactories/>`_ patterns



Inspiration
-----------

- https://github.com/realpython/cookiecutter-flask-skeleton

License
-------

MIT licensed.
