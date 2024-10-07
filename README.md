This README file provides a step-by-step guide to setting up the Job Recommendation System on your local machine for testing and development purposes. The system is built using Django and Django REST Framework and consists of APIs to add job listings and recommend jobs based on user data.

Prerequisites
Before you begin, make sure you have the following installed on your system:

Python 3.7+
pip (Python package manager)
Virtualenv (optional but recommended for creating isolated Python environments)
Git
Project Setup Instructions
Follow these steps to set up the project on your local machine:

Clone the Repository

1.First, clone the repository from GitHub:
    git clone https://github.com/maganite/Job_recommend.git

2.Create a Virtual Environment
    It's recommended to create a virtual environment to avoid conflicts with other Python packages.
    "python3 -m venv env"
    "source env/bin/activate"  # On Windows: env\Scripts\activate

3.Install Dependencies
    Install the required dependencies listed in the requirements.txt file:
    "pip install -r requirements.txt"

4.Set Up the Django Project
    After installing Django, set up the project by running migrations and creating a superuser:
    Migrate the database:
    "python manage.py migrate"
    Create a superuser to access the Django admin panel (optional):
    "python manage.py createsuperuser"

5.Run the Development Server
    Start the Django development server to test the application:
    "python manage.py runserver"
    The application will be running at http://127.0.0.1:8000/

6.API Endpoints
    POST/GET -> job/job/ : Add a new job to the system and get list of all jobs.
    POST -> job/getjob/ : Get job recommendations based on user input data (skills, experience, etc.).
    POST/GET -> user/adduser/ : Add a new user to the system and get list of all users in database.
    GET -> user/getjobbaseduser/<int:pk> : Get job recommendations based on only user id stored in database.


To test the API for job recommendation, you can use tools like Postman or curl to send a POST request to job/getjob/ with the following structure:
"{
    "skills": ["Python", "Django"],
    "experience_level": "Mid-level",
    "preferences": {
        "desired_roles": ["Backend Developer"],
        "locations": ["Bangalore"],
        "job_type": "Full-time"
    }
}"

