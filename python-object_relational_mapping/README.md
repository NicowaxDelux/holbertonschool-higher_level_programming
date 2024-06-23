 ![Project badge](https://intranet.hbtn.io/assets/pathway/003_color-0c5b38973bfe29fff8dd86f65a213ea2d2499a7d0d9e4549f440c50dc84c9618.png) 
# Python - Object-relational mapping
## Details
Amateur By: Guillaume Weight: 1 Migrated to checker v2: Your score will be updated as you progress.## Before you start…
Please make sure your MySQL server is in 8.0  ->  [How to install MySQL 8.0 in Ubuntu 20.04](https://intranet.hbtn.io/rltoken/MrRq4s05-Qo6TOgGKWIumA) 

## Background Context
In this project, you will link two amazing worlds: Databases and Python!
In the first part, you will use the module   ` MySQLdb `   to connect to a MySQL database and execute your SQL queries.
In the second part, you will use the module   ` SQLAlchemy `   (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM). 
The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.
Without ORM:
```bash
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()

```
With an ORM:
```bash
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()

```
Do you see the difference? Cool, right? 
The biggest difficulty with ORM is: The syntax!
Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something. 
## Resources
Read or watch :
* [Object-relational mappers](https://intranet.hbtn.io/rltoken/tCytNeWUzuWhAn9APwtp9A) 

* [mysqlclient/MySQLdb documentation](https://intranet.hbtn.io/rltoken/V8KJv3QCReECPZ0V-kXRwg) 
 (please don’t pay attention to  ` _mysql ` )
* [MySQLdb tutorial](https://intranet.hbtn.io/rltoken/j_7jU3C9Jsa0o53pgfwxOQ) 

* [SQLAlchemy tutorial](https://intranet.hbtn.io/rltoken/7y1s8FDE_0S-uhBtCgt5-A) 

* [SQLAlchemy](https://intranet.hbtn.io/rltoken/j6kxlUETdjiFwiu0k_JI6Q) 

* [mysqlclient/MySQLdb](https://intranet.hbtn.io/rltoken/vzsiR8tCdY3_OWsMH33jUA) 

* [Introduction to SQLAlchemy](https://intranet.hbtn.io/rltoken/7m6F57mBASM7A2r_GcIeMA) 

* [Flask SQLAlchemy](https://intranet.hbtn.io/rltoken/riV6WcWo1MGRpF3WSmv4Zw) 

* [10 common stumbling blocks for SQLAlchemy newbies](https://intranet.hbtn.io/rltoken/uRrjdEkHmjrVenCqjwJRWQ) 

* [Python SQLAlchemy Cheatsheet](https://intranet.hbtn.io/rltoken/RfLwdV21O_TVoQU4iwaIFw) 

* [SQLAlchemy ORM Tutorial for Python Developers](https://intranet.hbtn.io/rltoken/2BoGpuT2vAaoeuC3SN_wPA) 
 (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)
* [SQLAlchemy Tutorial](https://intranet.hbtn.io/rltoken/DrwY56jSHCOADKEbSOBa0A) 

## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/zAH3PxVw_N-4dQ45aCW8yw) 
 ,  without the help of Google :
### General
* How to connect to a MySQL database from a Python script
* How to  ` SELECT `  rows in a MySQL table from a Python script
* How to  ` INSERT `  rows in a MySQL table from a Python script 
* What ORM means
* How to map a Python Class to a MySQL table
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using  ` python3 `  (version 3.8.5)
* Your files will be executed with  ` MySQLdb `  version  ` 2.0.x ` 
* Your files will be executed with  ` SQLAlchemy `  version  ` 1.4.x ` 
* All your files should end with a new line
* The first line of all your files should be exactly  ` #!/usr/bin/python3 ` 
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.7.*)
* All your files must be executable
* The length of your files will be tested using  ` wc ` 
* All your modules should have a documentation ( ` python3 -c 'print(__import__("my_module").__doc__)' ` )
* All your classes should have a documentation ( ` python3 -c 'print(__import__("my_module").MyClass.__doc__)' ` )
* All your functions (inside and outside a class) should have a documentation ( ` python3 -c 'print(__import__("my_module").my_function.__doc__)' `  and  ` python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)' ` )
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
* You are not allowed to use  ` execute `  with sqlalchemy
## More Info
### Install MySQL 8.0 on Ubuntu 20.04 LTS
```bash
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$

```
Connect to your MySQL server:
```bash
$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$

```
### Install MySQLdb module version 2.0.x
For installing   ` MySQLdb `  , you need to have   ` MySQL `   installed.
```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)

```
### Install SQLAlchemy module version 1.4.x
```bash
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'

```
Also, you can have this warning message:
```bash
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                                    
  cursor.execute(statement, parameters)  

```
You can ignore it.
