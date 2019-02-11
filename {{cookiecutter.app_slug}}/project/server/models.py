# project/server/models.py


import datetime

from flask import current_app

from project.server import db, bcrypt

class ModelsHistory(db.Model):

    __tablename__ = "models_history"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model_name=db.Column(db.String(255), unique=True, nullable=False)
    s1_data_interface = db.Column(db.String(255))
    s2_target_generator = db.Column(db.String(255))
    s3_feature_eng = db.Column(db.String(255))
    s4_model = db.Column(db.String(255))
    metric = db.Column(db.String(255))
    train_performance = db.Column(db.Float)
    validation_performance = db.Column(db.Float)
    test_performance = db.Column(db.Float)
    train_test_split= db.Column(db.String(255))
    train_set_lines = db.Column(db.Integer)
    test_set_lines = db.Column(db.Integer)



    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, current_app.config.get("BCRYPT_LOG_ROUNDS")
        ).decode("utf-8")
        self.registered_on = datetime.datetime.now()
        self.admin = admin



class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, current_app.config.get("BCRYPT_LOG_ROUNDS")
        ).decode("utf-8")
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return "<User {0}>".format(self.email)

