# Joke-O-Matic: The Random Joke Generator &#x1f600;
This is a web application that generates random jokes using the [Joke API](https://official-joke-api.appspot.com/) built using Django framework.
## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
Python 3.x
Django 2.x or above
##### Installing
Clone the repository to your local machine
``` 
git clone https://github.com/<your-username>/joke-o-matic.git
```
Navigate to the project directory
```
cd joke-o-matic
```
Create a virtual environment and activate it
```
python3 -m venv venv
source venv/bin/activate (Linux/Mac) or venv\Scripts\activate (Windows)
```
Install the dependencies
```
pip install -r requirements.txt
```
Start the development server

```
python manage.py runserver
```
Open http://127.0.0.1:8000/ in your browser to access the application.

##### Built With
Django - The web framework used.

[Joke API](https://official-joke-api.appspot.com/) - The API used to fetch the jokes
