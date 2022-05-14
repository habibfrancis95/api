To run this project on your machine you need to do the following:
1- execute test.sql file on MySql database server
2- run command: python -m venv venv
    to create the virtual environment for the project
3- install the following python packages: Flask, python-dotenv, pymysql
4- create .env file on the root folder for the project and write your database servdr connection details, like the following:
DB_HOST=localhost
DB_PORT=3306
DB_NAME=test
DB_USER=root
DB_PASSWORD= 
5- to run the project you can type in the command line flask run