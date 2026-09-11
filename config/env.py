"""Use of this file?
read '.env' file and expose the values as a single clean object
the rest of your framework can import."""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    base_url = os.environ.get("BASE_URL").rstrip(
        "/"
    )  # Remove trailing slash if present
    username = os.environ.get("SWAGLABS_USERNAME")
    password = os.environ.get("SWAGLABS_PASSWORD")


settings = (
    Settings()
)  # creating instance(Object) of a 'Settings' class to access the values of the class variables
