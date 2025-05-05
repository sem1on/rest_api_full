import os
from dotenv import load_dotenv


load_dotenv()


class Headers:

    basic = {
        "api_key": f"{os.getenv('API_TOKEN')}"
    }