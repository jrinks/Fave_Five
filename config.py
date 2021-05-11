import os
class Config():
    FLASK_APP=os.environ.get("FLASK_APP")
    FLASH_ENV=os.environ.get("FLASK_ENV")