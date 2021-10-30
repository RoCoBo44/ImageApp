# ImageApp
##### _Task AIGecko Job Position_


The task consists in building a very basic RESTful API that enables a set of functionalities to
the client/user. Create a simple web page using HTML + CSS + Javascript as the
front-end for the user interaction. The front-end must connect to the Flask + Python that will
act as the backend of the solution.

Technology stack
- Python (any version of python is acceptable).
- Flask (python library).
- Javascript.
- HTML.
- CSS.
- Docker (preferably docker-compose).
- Git.

## Features

- Load images from local or URL
- List images
- By given the id return the height and width

## Installation

For a local set-up copy the repo and run the following commands

```sh
cd App
pip install -r requirements.txt
flask run
```

Then go to the localhost:5000


## Development

In the App folder/app.py there is all the flask code used for this task 
Then in App/templates there are all the html files
And in App/static there is the css file used

#### Requeriments

There is a requeriments.txt with all the libraries used for this task


## Docker

If you want to run it in docker copy the repo and run the docker-compose

```sh
docker-compose up
```
