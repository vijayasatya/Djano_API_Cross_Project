## For our cross platform application we created the Django API to interface the frontend with the backend python code

## Getting Started with Create DJango

## Available Scripts

In the project directory, you can run:
## Django_Installation

 **step:1**

 Install pip- Open command prompt and enter following command-
 `python -m pip install -U pip`

**step:2**

Install virtual environment- Enter following command in cmd-

`pip install virtualenv`

`virtualenv env_site`

**step:3**

Change directory to env_site by this command-

`cd env_site/Scripts/activate`

**step:4**

Install Django- Install django by giving following command-

`pip install django`

**step:5**

Change directory to your project path where you want to create a project

`django-admin startproject Project_Name`

`cd Project_Name`

`python manage.py runserver`


Runs the app in the development mode.\
Open [http://localhost:8000](http://localhost:8000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.


See the section about [Check the installation document for reference](https://docs.djangoproject.com/en/4.0/intro/install/) for more information.


# Django API Features

`DO read and write operations to the files stored in the django server and pre configured Sample Django Project`

`while sending a post request to the server accepts data in the form of json file. Then write the respective files and save them`

`Similarly while sending a get request to the server read the respective files and sends the data in the form of json file.`

`when the user writes a wrong backend code we Added a feature to reflect error message in the user's demo server `

`It reflects the same backend and frotend code in the pre configured sample django project. So the user can able to download it at the end from the main server. It is workable in local and deployable in any cloud platform.` 


# Trouble shootings

`Issue with the reflecting the django backend code needs sever restart. It is fixed using python script.`

`Issue when the user saves the wrong python error code. It crashes the main server. It is fixed by using try except block.`

