# manage.py

from flask_script import Manager

from main import app, settings

manager = Manager(app.create_app(settings))

if __name__ == "__main__":
    manager.run()
