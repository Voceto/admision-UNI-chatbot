# """Initialize Flask app."""

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager


# db = SQLAlchemy()

# def init_app():
#     """Construct core Flask application."""
#     application = Flask(__name__, instance_relative_config=False)
#     app = application
#     app.config.from_object('config.Config')
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     db.init_app(app)


#     login_manager = LoginManager()
#     login_manager.login_view = 'auth.login'
#     login_manager.init_app(app)




#     with app.app_context():
#         # Import parts of our core Flask app
#         # from . import train2
#         # from . import chat2
#         from . import routes
#         from .models import User
#         # Esta vaina, va en el application context?
#         from .models import User

#         @login_manager.user_loader
#         def load_user(user_id):
#             # since the user_id is just the primary key of our user table, use it in the query for the user
#             return User.query.get(int(user_id))
#         return app