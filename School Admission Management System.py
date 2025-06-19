import json

class School_admission():
    def __init__(self,filereading):
        self.filereading = filereading
        self.__fee = None
        
    def fee_get(self):
        return self.__fee
    def set_fee(self,fees):
        self.__fee = fees
    def get_fee(self):
        return self.__fee

class Add_new_student(School_admission):
    def add_new_students(self):
        name = input("Enter your Name :")
        age = int(input("Enter your Age :"))
        class_name = input("Enter your Class Name :")
        admission_number = int(input("Enter your Admission Number :"))
        fees = int(input("Enter your Fees :"))
        self.set_fee(fees)
        
        dict_student = {
            "name":name,
            "age":age,
            "cls_name":class_name,
            "admit_num":admission_number,
            "fees":fees
        }

        try:
            with open(self.filereading,"r") as file_upload_read:
                data = json.load(file_upload_read)
        except (json.JSONDecodeError,FileNotFoundError):
            data = []

        data.append(dict_student)

        with open(self.filereading,"w") as file_upload_write:
            json.dump(data,file_upload_write,indent=2)

class Admission_number(School_admission):
    def search_admission_number(self):

        search = input("Enter your Admission Number :")
        try:
            with open(self.filereading,"r") as file_admission_read:
                file_admit_read = json.load(file_admission_read)

                for admit in file_admit_read:
                    if search == str(admit["admit_num"]):
                        print(admit["name"])
                        print(admit["age"])
                        print(admit["cls_name"])
                        print(admit["admit_num"])
                        print(admit["fees"])

        except FileNotFoundError:
            print("Student data file not found")
        except json.JSONDecodeError:
            print("Error reading student data")

class Update_student_class(School_admission):
    def update(self):

        admit_nums = input("Enter your Admission Number :")
        new_fees = int(input("Enter your fees :"))

        with open(self.filereading,"r") as file_update_read:
            student_list = json.load(file_update_read)

            for student in student_list:
                if admit_nums == str(student.get("admit_num")):
                    student["fees"] = new_fees
                    print(student)
            
            with open(self.filereading,"w") as file_update_write:
                json.dump(student_list,file_update_write,indent=2)

class Total_students(School_admission):

    @classmethod
    def total_student(cls,filereading):
        cls.filereading = filereading
        try:
            with open(cls.filereading,"r") as file_total_read:
                file_read = json.load(file_total_read)
                print(f"Total Students: {len(file_read)}")
                
        except json.JSONDecodeError:
            print("No record file")

class Total_fees_collected(School_admission):
    def fees_collect(self):  

        try: 
            with open(self.filereading,"r") as file_read:
                file_collect_read = json.load(file_read)

            sum=0
            expense = {} 

            for line in file_collect_read:
                sum += line["fees"]

            expense["total_collect_fees"] = [sum]
            print(expense)
        except json.JSONDecodeError:
            print("file no record")


class choices(Add_new_student,Admission_number,Update_student_class,Total_students,Total_fees_collected):
    def choices(self,filereading):
        choice = input("Enter your choice:")

        if choice == "upload":
            self.add_new_students()
        elif choice == "search":
            self.search_admission_number()
        elif choice == "update":
            self.update()
        elif choice == "total":
            Total_students.total_student(filereading)
        elif choice == "collect":
            self.fees_collect()
        elif choice == "exit":
            print("Exit Program")

school_admission = choices("School_admission_management_system.txt")
school_admission.choices("School_admission_management_system.txt")
