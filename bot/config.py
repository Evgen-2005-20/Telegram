import os

from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseModel):
    TOKEN : str
    HOST : str
    PORT : int
    

TOKEN = os.getenv("TOKEN")
HOST = os.getenv("HOST")
PORT = int(os.getenv("PORT"))

settings = Settings(TOKEN=TOKEN,
                  HOST=HOST,
                  PORT=PORT)