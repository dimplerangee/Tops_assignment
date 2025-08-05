appointments = {}
slots = ['10am','11am','12pm','1pm','2pm','3pm']

while True:
    print("\n 1.Bookk   2.View/cancle  3.Exit")
    ch = input("choice:")
    if ch == '1':
        name = input("Name:")
        age = input("Age:")
        mob = input("Moblie:")
        doc =input("Doctor :")

        if doc not in appointments:
            appointments[doc] = {s:[] for s in slots}
        for s in slots:
            print(f"{s} - {3 -len(appointments[doc][s])} slots left")

        slot = input("slot:") 
        if  slot in slots and len(appointments[doc][slot]) < 3:
            appointments[doc][slot].append({"name":name,"age":age,"mobile":mob})
            print("booked")
        else:
            print("slot full or invalid")
    elif ch == '2':
        mob = input("Enter mobile:")
        found = False
        for doc in appointments:
            for s in slots:
                for a in appointments[doc][s]:
                    if a['mobile'] == mob:
                        print(f" dr.{doc} at {s} - {a['name']} Age{a['age']}")
                        if  input ("cancel? (yes/no):") == "yes":
                            appointments[doc][s].remove(a)
                            print("cancelled")
                        found = True
                        break
        if not found:
            print("not found")

    elif ch =='3':
        break
    else:
        print("invalid choice")
