# Flask settings
FLASK_SERVER_NAME = '127.0.0.1:8888'
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False
DATABASE = "db.sqlite"

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+DATABASE
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False

#JWT settings
JWT_SECRET = 'oS&&QET@ea4J(LXMRR#X3s@J&uL_tE)VYvBCxmN+xlxZ*OAgS5!FknacRX8d1RYnnk8htcK#O80+tXZ1*Xr585r8I=f$cRo(*MTYkT6RXrAn6&pCkbJ=8g0Vl5H'

#TESTING settings
TESTING = False
