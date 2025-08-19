import os
import dotenv
dotenv.load_dotenv()


BASE_URL = "https://www.muztorg.ru/"
WRONG_PASSWORD = "<PASSWORD>"
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")