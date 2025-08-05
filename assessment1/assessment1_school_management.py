##step:1 crete an emty dictioney to store student date
students = {}
student_id = 1 # this will auto-increment for each new student 

#step 2 :run menuu in a loop

while True:
    print("\n ---school management System---")
    print("1.New Admission")
    print("2.View Student Details")
    print("3.Update Student info")
    print("4.remove Student record")
    print("5.Exit System")

    choice  = input("Enter your Choice (1-5):")

    #step 3 : new Adimission 
    if choice == "1":
        name = input("Enter student name:")
        age = int(input("Enter age(5 to 18):"))
        if age < 5 or age > 18:
            print("Invalid age .admission failed .")
            continue

        class_num = int(input("Enter class(1 to 12):"))
        if class_num < 1 or class_num > 12:
            print("Invaild class .Admission failed.")
            continue

        mobile = input("Enter gurdian's 10- digit mobile number:")
        if len(mobile) !=10 or not mobile.isdigit():
            print("invaild mobile number. Admission failed.")
            continue

        students[student_id] = {
            "Name":name,
            "Age":age,
            "Class":class_num,
            "Mobile":mobile
            }
        print(f"Student adimission successfully. Student ID = {student_id}")
        student_id += 1

        #step 4 : view student details
    elif choice == "2":
        sid = int(input("Enter student ID to view:"))
        if sid in students:
            print("Student details:")
            for key, value in students[sid].items():
                print(f"{key}: {value}")
        else:
            print("student not found.")

    #step 5 :update students info
    elif choice == "3":
        sid = int(input("enter student ID to udate:"))
        if sid in students:
            print("what do you want to update?")
            print("1.mobile Number")
            print("2.class")
            update_choice = input("enter choice (1 to 2):")

            if update_choice == "1":
                new_mob = input("enter new 10-digit mobile number:")
                if len(new_mob) == 10 and new_mob.isdigit():
                    students[sid]["Mobile"] = new_mob
                    print("mobile number updated.")
                else:
                    print("Invailed mobile number.")

            elif update_choice =="2":
                new_Class = int(input("Enter new class(1 to 12:)"))
                if 1 <= new_Class <= 12:
                    students[sid]["Class"] = new_Class
                    print("class updated")
                else:
                    print("invailed class.")
        else:
            print("student id not found.")
    
    #step 6 : Remove  student 
    elif choice == "4":
        sid = int(input("enter student ID to remove:"))
        if sid in students:
            del students[sid]
            print("student record removed.")
        else:
            print("Student not fount.")



    #step 7: exit system
    elif choice == "5":
        print("Exiting system.goodbyy....!")
        break

    else:
        print("invaild choice.try again.")

