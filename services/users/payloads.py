from faker import Faker


fake = Faker()

class Payloads:

    create_user = {
        "id": fake.random_int(min=100, max=200),
        "username": fake.name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(length=10),
        "phone": fake.phone_number(),
        "userStatus": fake.random_int(min=0, max=1)
    }
    