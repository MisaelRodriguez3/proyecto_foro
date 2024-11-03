from decouple import config


class Config():
    SECRET_KEY = config("SECRET_KEY")   
    DEBUG = config("DEBUG", default = True, cast = bool)
    SQLALCHEMY_DATABASE_URI = config("DATA_BASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = config("TRACK_MODIFICATIONS", default = False, cast = bool)
