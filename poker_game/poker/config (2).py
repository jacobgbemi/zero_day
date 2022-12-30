import os


class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245' # os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db' # os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER: 'smtp.gmail.com'
    MAIL_PORT: 465
    MAIL_USE_TLS: False
    MAIL_USE_SSL: True
    MAIL_USERNAME: os.environ.get('EMAIL_USER')
    MAIL_PASSWORD: os.environ.get('EMAIL_PASSWORD')