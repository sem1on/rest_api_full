
HOST = "https://petstore.swagger.io/v2"

class Endpoints:

    create_user = f"{HOST}/user"
    get_user_by_user_name = lambda self, username: f"{HOST}/user/{username}"
    