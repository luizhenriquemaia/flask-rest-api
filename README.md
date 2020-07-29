# system-verzel
> Api for the practical test of a selective process from Verzel.

**This has among other things**
- Public and private routes;
- JWT authentication system;
- Unit testing coverage.

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
> To see the routes available 
- Open the __init__.py file inside the folder "app" and search for blueprints;
- You will see the names of the files that are imported as blueprint;
- Open one of these files and search for the @app.route decorator, for example:
```python
@app.route('/api/auth/register', methods=['POST'])
```
- With the route has the decorator @jwt_required it means that is a private route:
```python
@bp_products.route('/api/show-products', methods=['GET'])
@jwt_required
```
- To get the jwt simply register and then login, the api will response you with the token string, which you can pass it as Authorization in the header of request;
- If you want to do changes in models and data base structure
> Inside the pipenv shell run to apply changes.
```shell
$ python manage.py db migrate
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
