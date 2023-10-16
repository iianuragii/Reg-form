db = client.registration
collection = db.reg

db1 = client.members
collection1 = db1.reg

d = input("Sign-up or Log-in ")
decision = 'NO'
if d == 's':
    user = input("Enter your username")
    password = input("Enter your password")
    confpassword = input("Re-Enter your password")
    g = input("Gmail = ")
    p = int(input("Phone No. = "))
    dic1 = {
        "USER" : user,
        "PASSWORD" : password,
        "GMAIL" : g,
        "PHONE" : p
        }
    collection.insert_one(dic1)
    decision = 'YES'
else:
    user = input("Enter your username")
    password = input("Enter your password")
    query = collection.find_one({"PASSWORD" : password}) 
    if query != None :
        decision = 'YES1'

if decision == 'YES':
    a = input("Name = ")
    t = input("Position you want to apply")
    s = input("Why should we hire you?")
    dic2 = {
        "NAME" : a,
        "POS" : t,
        "HIRE" : s
        }
    print(dic2)
    collection1.insert_one(dic2)
elif decision == "YES1":
    print("Your informations are:\n")
    print(query)
else:
    print("Wrong Password or Username given")

