# Flask Rest API Example
> Api for the practical test of a selective process.

**This has among other things**
- Public and private routes;
- JWT authentication system;
- Unit testing coverage.

![Gif run tests api](https://github.com/luizhenriquemaia/system-verzel/raw/master/readme-media/pytest_example.gif "Gif run tests api")

---

## Installation

### Clone

- Clone this repo to your local machine using `https://github.com/luizhenriquemaia/system-verzel.git`.

### Setup

- Recommended have pipenv installed in your machine, see how in https://pypi.org/project/pipenv/;
- Install all dependencies from Pipfile;
> Inside the root of repository
```shell
$ pipenv install
```
- Create a mysql database named system_verzel;
> Inside the mysql shell
```shell
$ CREATE DATABASE system_verzel;
```
- Run the mysql server;
- Activate pipenv;
> Inside the root of repository
```shell
$ pipenv shell
```
- Run the migrations.
> Inside the pipenv shell
```shell
$ python manage.py db upgrade
```

---

## Usage
- To make requests, run the flask server;
> Inside the pipenv shell
```shell
$ python run.py
```

### Routes
#### Public routes
 - /api/auth/register -> Method = POST
 - /api/auth/login -> Method = POST

#### Private routes
- /api/show-products -> Method = GET
- /api/product -> Method = POST
- /api/product/id -> Methods = GET, DELETE, PUT

### JWT
- To get the jwt simply register and then login, the api will response you with the token string, which you can pass it as Authorization in the header of request;

### General
- If you want to do changes in models/database structure
> Inside the pipenv shell run to make migrations and apply them.
```shell
$ python manage.py db migrate
$ python manage.py db upgrade
```
- To change the configurations of access to data base go to instance/config.py and change the 
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/system_verzel'
```
> where the root:root is username and password, localhost is the ip address and system_verzel is the name of database.
- Have fun.

---

## Run Tests
- This api has unit testing coverage;
- To run all the tests:
> Inside the root of repository
```shell
$ pipenv shell
$ pytest
```
- To run the tests from expecific blueprint, for example authorization blueprint:
```shell
$ pipenv shell
$ pytest test_authorization.py
```

---

## Notes
- Inside the instance folder has the sensitive information about the api;
- This folder isn't listed in .gitignore file because this api is not going to be sended to a server;
- Don't use the same configuration as instance/config.py in production, remember of change the information.

---

## Team
> Yeah it's just me here lol

| <a href="https://github.com/luizhenriquemaia" target="_blank">**Luiz Henrique**</a> |
| :---:|
| ![Luiz Henrique](https://avatars1.githubusercontent.com/u/26177048?s=200&u=1deb4b3947a75f8baca3123f6a23e8a803f53493&v=4) |
| <a href="https://github.com/luizhenriquemaia" target="_blank">`github.com/luizhenriquemaia`</a> |
