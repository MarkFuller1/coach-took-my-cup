## This app can be found at 
coach-took-my-cup.herokuapp.com

## How to start the frontend (react)

1. `npm install`
2. `npm start`

## How to start the backend
> Step one creates your python package virtual environment (do this only once)
1. `virtualenv -m venv venv`
> Step 2 loads that environment, you will need to set this every time you open a new console 
2. `source bin/activate`
> to leave the environment run 

`deactivate`
> To load the current dependencies run

3. `pip install -r requirements.txt`

> then to start the application

4. `gunicorn wsgi`

backend `localhost:8000`
frontend `localhost:3000`