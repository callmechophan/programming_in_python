from employee import *

def create_dict(name, age, title):
    dict1 = {}
    dict1["first_name"] = name
    dict1["age"] = int(age)
    dict1["title"] = title

    return dict1

def write_json_to_file(json_obj, output_file):
    with open(output_file, 'w') as file:
        try:
            file.write(json_obj)
        except:
            file.write(" ")

def main():
    # print the contents of details()
    details()

    # create employee dictionary
    employee_dict = create_dict(employee_name, age, title)
    print("employee_dict: " + str(employee_dict))

    json_object = None
    print("json_object: " + str(json_object))

    # write out the json object to file
    write_json_to_file(json_object, "employee.json")

if __name__ == "__main__":
    main()