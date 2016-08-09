Student Advisement System
==================================


 The goal of the project is to give students academic Advisement automatically for Computer Science Department of Southern University. I developed  and deployed it successfully. And it is maintained by a stuff of department. I spent two months on this project. It save thousands hour per year for students and faculty. Students and faculies from other deparments or universities can not use the system directly. But they may can modify on it to compatible their context.
 
 
 features:
 upload file
 database (search delete edit and table copy from web page)
 extraction data from html
 admin panel
 generate a printable and neat report 
 

Usage (Python 2.7 Django 1.8)
------------------
First ensure you have Django 1.8 installed. Then:

    $ git clone https://github.com/hezhi-lin/Student-Advisement-System.git
Setup Web Service
 1.	Go to venv directory
 2.	Source bin/activate
 3.	Go to project directory
 4.	cd src/myproject
 5.	python manage.py migrate (just for the first time)
 6.	python manage.py runserver 0.0.0.0:80
 7.	if any error, read error prompt and go back to Setup Python2.7 step 5
 8.	open 80 port in firewall process



Setup Environment For Linux:
 1.	Download “get-pip.py”
 2.	Type “Python get-pip.py” in command-line
 3.	Type “pip install virtualenv” in command-line
 4.	Go to project directory
 5.	Check if you install Python 2.7. If not Go to Setup Python2.7 For Linux step1
 6.	virturalenv venv (virturalenv –p /user/local/bin/python2.7 venv)
 7.	Source venv/bin/activate
 8.	Go to requirement.txt directory
 9.	Pip install –r requirement.txt

Setup Python2.7 For Linux:
 1.	Download Python package
 2.	Tar xvfz package
 3.	Go to directory
 4.	Make clean
 5.	If linux lacks some important module. Please install them. (Yum install openssl libreadline-gplv2-dev libcursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev)
 6.	./configure –prefix=/usr/local/
 7.	Make install


Setup Python2.7 For Window:
 1.	Download Python installer
 2.	Double click installer
 3.	Setup execute path ( example:  add ;C:\Python27\;C:\Python27\Scripts; to path)
 http://www.howtogeek.com/197947/how-to-install-python-on-windows/


Setup Environment For Window:
 1.	Download “get-pip.py”
 2.	Type “Python get-pip.py” in command-line
 3.	Type “pip install virtualenv” in command-line
 4.	Go to project directory
 5.	Check if you install Python 2.7. If not Go to Setup Python2.7 For Windows step1
 6.	virturalenv venv
 7.	Source venv/Script/activate
 8.	Go to requirement.txt directory
 9.	Pip install –r requirement.txt



