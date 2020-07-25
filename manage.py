from app import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models import User

# set migrations
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@app.shell_context_processor
def make_shell_context():
    return dict(
        app=app,
        db=db,
        User=User
    )


if __name__ == '__main__':
    manager.run()