class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///example.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'your_secret_key'
    SECURITY_PASSWORD_SALT = 'your_password_salt'