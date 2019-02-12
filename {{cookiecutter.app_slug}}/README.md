#{{cookiecutter.app_name}}

## Getting Started with Jenkis and Docker
### If you have a Jenkins server
- Check that a docker daemon is installed on Jenkis server
- Create a new pipeline from SCM and link the Jenkinsfile and launch it

### If you DO NOT have a Jenkis server
Launch a Jenkins server on local:
```sh
docker-compose -f docker/docker-infrastructure.yaml up
```
create a new pipeline from SCM and link the Jenkinsfile and launch it

## Getting Started without Jenkis and Docker

Create and activate a virtual environment, and then install the requirements.

### Set Environment Variables

Update *project/server/server_config.py*, and then run:

```sh
$ export APP_NAME="{{cookiecutter.app_name}}"
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
$ export FLASK_DEBUG=1
$ export DS_SETTINGS="project.config.data_science_config.DsDevelopmentConfig"
```

Using [Pipenv](https://docs.pipenv.org/) or [python-dotenv](https://github.com/theskumar/python-dotenv)? Use the *.env* file to set environment variables:

```sh
APP_NAME="{{cookiecutter.app_name}}"
APP_SETTINGS="project.server.config.DevelopmentConfig"
FLASK_DEBUG=1
DS_SETTINGS="project.config.data_science_config.DsDevelopmentConfig"
```


### Run the Application


```sh
$ python manage.py run
```

Access the application at the address [http://localhost:5000/](http://localhost:5000/)

### Testing

Without coverage:

```sh
$ python manage.py test
```

With coverage:

```sh
$ python manage.py cov
```

Run flake8 on the app:

```sh
$ python manage.py flake
```

or

```sh
$ flake8 project
```