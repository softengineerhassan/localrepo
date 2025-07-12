import json
import os

CONTACT_FILE = 'contact.json'

class Contact:
    def __init__(self,name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return{
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }
    
class Contactmanager:
    def __init__(self):
        self.Contact = []
        self.load_contact()

    def load_contact(self):
        if os.path.exists(CONTACT_FILE):
            with open (CONTACT_FILE, 'r') as file:
                data =json.load(file)
                for item in data:
                    self.Contact.append(Contact(item["name"],item["phone"],item["email"]))
    def save_contact(self):
        with open (CONTACT_FILE, 'w') as file:
            json.dump([c.to_dict() for c in self.Contact],file,indent=4)

    def add_contact(self):
        name = input("enter name!")
        phone = input("enter phone number")
        email = input("enter email address")
        self.Contact.append(Contact(name,phone,email))
        self.save_contact()
        print("the phone number saved!!")

    def view_contact(self):
        name = input("enter the name you want to view")
        if not self.Contact:
            print("there is no contact of this name!")
            return
        for c in self.Contact:
            print(f"name{c.name},phone{c.phone},email{c.email}")

    def update_contact(self):
        name = input("enter the name you want to update")
        for c in self.Contact:
            if c.name.lower() == name.lower():
                c.phone = "enter the updated phone number!"
                c.email = "enter the updated email address!"
                return

            
        print("there is no contact that you enter!")

    def delete_contact(self):
        name = input("enter the contact that you want to delete!")
        for c in self.Contact:
            if c.name.lower() ==  name.lower():
                self.Contact.remove(c)
                self.save_contact()
                print("contact deleted successfully")
                return

            
        print("you entered wrong contact!")

    def search_contact(self):
        keyword = input("enter the name you want to search for!")
        for c in self.Contact:
            if keyword.lower() in c.name.lower():
                print(f"name{c.name},phone{c.phone},email{c.email}")
                return
        print("not found this name")


manager = Contactmanager()
while True:
   
    print("1. for add contact")
    print("2. for view contact")
    print("3. for update contact")
    print("4. for delete contact")
    print("5. for search contact")
    print("6. for exit contact")

    choice = input("choose an option!")
    if choice=="1":
        manager.add_contact()
    elif choice=="2":
        manager.view_contact()
    elif choice == "3":
        manager.update_contact()
    elif choice=="4":
        manager.delete_contact()
    elif choice == "5":
        manager.search_contact()
    elif choice =="6":
        print("Thank you!")
    else: print("try again!!")
            

