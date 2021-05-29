import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', "2OSwOA+nb/GcT5B+O9e297MftGgOR4zLRufPtFWmQkA=")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'SQLALCHEMY_DATABASE_URI', 
        "sqlite:///{}".format(os.path.join(os.getcwd(), "app/site.db"))
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
