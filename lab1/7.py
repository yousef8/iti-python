dict = {
    "name": "jone",
    "email": "jane@outlook.com",
    "age": 25,
    "job": "engineer",
    "address": "cairo, Egypt",
}


def isExists(dict):
    if "job" in dict:
        print("job key exists")
    if "card_number" in dict:
        print("card_number exists")


isExists(dict)
