import json

website = input("Enter the name of the website: ")
email = input("Enter email: ")
password = input("Enter password: ")

new_data = {
    website: {
        "email": email,
        "password": password,
    }
}

try:
    with open("my_json_file.json", 'r') as myFile:
        data = json.load(myFile)

except FileNotFoundError:
    with open("my_json_file.json", 'w') as  myFile:
        json.dump(new_data, myFile, indent= 6)

else:
    data.update(new_data)

    with open("my_json_file.json", 'w') as myFile:
        json.dump(data, myFile, indent= 6)

finally:
    choice = input("Enter the name of the website you want to search detials: ")

    if choice in data:
        web = data[choice]
        em = web['email']
        pas = web['password']
        print(f"website: {choice}\nemail: {em}\npassword: {pas}")
    else:
        print("No details for the website found")