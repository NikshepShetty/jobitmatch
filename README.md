# Job Recommendation Platform - JobITmatch


## Overview
This Django-based website is designed to help users find jobs that are a good fit for them, based on their resumes and personality test results. It not only suggests jobs but also recommends relevant online courses to enhance users' skills and qualifications for these roles.


## Features
- **Job Recommendations:** Users upload their CV, and the system analyzes it to suggest jobs that match their experience and skills.
- **Personality Test:** A simple personality test to understand the user's preferences and strengths, further refining job suggestions.
- **Course Suggestions:** For each job recommendation, the platform suggests online courses that can help users prepare for these roles.


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.


### Prerequisites  
What things you need to install the software and how to install them:

Code was developed and tested on Python 3.8, performance on newer python versions unknown.


### Installing  
A step by step series of examples that tell you how to get a development environment running:


**Clone the Repository**


**Install Required Packages**  
pip install -r requirements.txt


**Initial Setup**  
python manage.py makemigrations  
python manage.py migrate  
python manage.py createsuperuser


**Run the Server**  
python manage.py runserver
