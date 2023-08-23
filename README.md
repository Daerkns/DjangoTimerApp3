# FitAlert
Hello, this is a forked project modified to suit our needs of building an application that reminds you to do healthy things. Modified by Souvik and Muhesena for Design Project 2.
## About
This is a simple app that allows you to create countdowns. You can create a countdown for any time in future, specify description, text that will be visible when countdown finishes. A login system is included for Django practice, even though it is optional. Note that the email that is sent to you to confirm mail or change password is sent to the VScode terminal.


## Try it out
Clone the repository:
```bash
git clone https://github.com/kokokojo2/CountDown
cd CountDown
```
Make and activate virtual environment:
```bash
python -m venv countdown_env
countdown_env\Scripts\activate
```
Install needed requirements:
```bash
pip install -r requirements.txt
```
Create sqlite3 database:
```bash
python manage.py makemigrations
python manage.py migrate
```
Run developement server:
```bash
python manage.py runserver
```
After following these steps, open [this](http://127.0.0.1:8000/) url in your browser to check out the work of application.
