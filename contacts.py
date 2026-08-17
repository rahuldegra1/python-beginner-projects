contacts = []
while True:
    print("1. add new contact")
    print("2. view contacts")
    print("3. quit")
    print("4. Delete contact")
    choice = input("Enter choice..")

    if choice == "1":
       user1 = input("Name: ")
       user2 = input("phone: ")
       user3 = input("Email: ")
       contact1 = {"name":user1, "phone": user2, "email": user3}
       contacts.append(contact1)
    elif choice == "2":
        for contact in contacts:
            print(contact["name"], contact["phone"], contact["email"])
    elif choice == "3":
        break
    elif choice == "4":
        name_to_delete = input("which name to Delete: ")
        for contact in contacts:
            if contact["name"] == name_to_delete:
                contacts.remove(contact)
                break
        else:
            print("contact not found")
    else:
        print("invalid choice")