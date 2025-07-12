import json
import os

PATIENT_FILE = "patient.json"

class Patient:
    def __init__(self,name,age,disease,admissionDate):
        self.name = name
        self.age = age
        self.disease = disease
        self.admissionDate = admissionDate

    def to_dict(self):
        return{
            "name": self.name,
            "age": self.age,
            "disease": self.disease,
            "admissionDate": self.admissionDate
        }
    
class ManagePatient:
    def __init__(self):
        self.Patient = []
        self.load_data()


    def load_data(self):
        if os.path.exists(PATIENT_FILE):
            with open(PATIENT_FILE, 'r') as file:
                data = json.load(file)
                for item in data:
                    self.Patient.append(Patient(item["name"],item["age"],item["disease"],item["admissionDate"]))
        
    def save_data(self):
        with open(PATIENT_FILE,'w') as file:
            json.dump([c.to_dict() for c in self.Patient],file,indent=5)

    def add_patient(self):
        name = input("enter the patient name!")
        age = input("enter the patient age")
        disease = input("enter the disease name")
        admissionDate = input("enter the admission date")
        self.Patient.append(Patient(name,age,disease,admissionDate))
        self.save_data()
        print("patient's data saved successfully!")

    def view_patient(self):
        name = input("enter the patient name")
        for c in self.Patient:
            if c.name.lower() == name.lower:
                print(f"name{c.name},age{c.age},disease{c.disease},admissionDate{c.admissionDate}")
                return
        print("patient not found")

    def update_patient(self):
        name = input("enter the patient name you want to update!")
        for c in self.Patient:
            if c.name.lower()==name.lower():
                c.name = input("enter the updated name")
                c.disease = input("enter the updated disease")
                c.age = input("enter the updated age")
                c.admissionDate = input("enter the updated admission date")
                self.save_data()
                return
        print("the patient not found!!")

    def delete_patient(self):
        name = input("enter the patient's name that you want to delete")
        for c in self.Patient:
            if c.name.lower()==name.lower():
                self.Patient.remove(c)
                self.save_data()
                print("successfully deleted")
                return
        print("the patient not found!")



manager = ManagePatient()
while True:
    print("1. add patient")
    print("2. view patient")
    print("3. update patient")
    print("4. delete patient")

    choice = input("make a choice")
    if choice == "1":
        manager.add_patient()
    elif choice =="2":
        manager.view_patient()
    elif choice =="3":
        manager.update_patient()
    elif choice == "4":
        manager.delete_patient()
    else: print("try again")

    