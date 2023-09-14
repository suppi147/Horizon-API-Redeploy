# Horizon-API-Redeploy
  This repository is your go-to resource for efficiently managing and updating the API component of Horizon, the web-based user interface for OpenStack, ensuring seamless interaction with your cloud infrastructure.
## Setup
- Build virtual environment
  `python -m venv redeployhorizon`
- active virtual environment
  ![Alt text](image.png)
  `.\redeployhorizon\Scripts\activate`
- install django
  `pip install django`
- create horizon API project
  `python -m django startproject HorizonAPI`
- create app
  `python manage.py startapp SessionManager`
- make migration for session manager
  `python manage.py makemigrations SessionManager`
- migrate setting to project
  `python manage.py migrate`
## Login with Openstack API
- key-value store api key tested
![](https://hackmd.io/_uploads/S1gqnee1T.png)
- login UML
![](https://hackmd.io/_uploads/SkIypglk6.png)
