# match statement
# - a match statement compares a value to serveral different conditions until one is met

http_status = 100

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print("Bad request")
    case 404:
        print("Not Found")
    case 500 | 501:
        print("Server Error")
    case _:
        print("Unknown")
