import string

nameList = ["Nurislom", "Dadaxon", "Sharofiddin", "nur islom", "nuriSLOM","bobur"]
surnameList = ["Xurramov", "Muqimov", "Anvarov", "anvarov", "xuRRAMOV", "ro'ziyev"]
fatherNameList = ["Parda o'g'li", "Samadovich", "Sobitali o'g'li", "Samad o'g'li", "parda o'g'li", "G'anisher o'g'li"]
birthDayList = ["24.06.1996", "24/05/1991", "14-02-1997", "24 06 1996", "24061996", "27.12.1993"]
phoneNumberList = ["94-648-83-34","+998977006551","97 619 97 97", "88 789 83 34", "97 777 44 55", "78 456 83 34"]
addressList = ["Chilonzor birnima birnimalar", "Mirzo ulug'bek birnima bir nimalar", "Yunusobod birnima birnimalar", "chILONZOR bironnima bironnima", "Shayxontoxur tumani", "Olmazor tumani"]


def printFull(index):
    k=index+1
    print(f"""{k} - shaxs:""")
    k=0
    k+=1
    print(f""" {k}=> name: {nameList[index]}""")
    k+=1
    print(f""" {k}=> surname: {surnameList[index]}""")
    k+=1
    print(f""" {k}=> fathername: {fatherNameList[index]}""")
    k+=1
    print(f""" {k}=> birthday: {birthDayList[index]}""")
    k+=1
    print(f""" {k}=> phonenumber: {phoneNumberList[index]}""")
    k+=1
    print(f""" {k}=> address: {addressList[index]}\n""")

def clearPunt(word):
    return "".join(word.translate(str.maketrans('', '', string.punctuation)).lower().split())

def ifForSearch(index, search, word):
    clearPunt(search)
    clearPunt(word)
    if search in word:
        printFull(index)  
    
while True:
    print("""\n     Hi! select the required command:""")
    print(""" 1 => data entry   2 => Search   3 => view all data   4 => Exit""")
    com = int (input("select the command =>>> "))
    if(com == 1):
        print("\n<<<<<<<<<<<<<<<< Enter data >>>>>>>>>>>>>>>>>")
        nameList.append(input("Name: "))
        surnameList.append(input("Surname: "))
        fatherNameList.append(input("Name of father: "))
        birthDayList.append(input("Birth day: "))
        phoneNumberList.append(input("Phone number: "))
        addressList.append(input("Address: "))
    elif(com == 2):
        k=0
        search = input("kalit so'zni kiriting: ")
        for index, word in enumerate(nameList):
            ifForSearch(index, search, word)        
        for index, word  in enumerate(surnameList):
            ifForSearch(index, search, word)         
        for index, word  in enumerate(fatherNameList):
            ifForSearch(index, search, word)            
        for index, word  in enumerate(birthDayList):
            ifForSearch(index, search, word)            
        for index, word  in enumerate(phoneNumberList):
            ifForSearch(index, search, word)             
        for index, word  in enumerate(addressList):
            ifForSearch(index, search, word)             
              
    elif(com == 3):
        for index in range(len(nameList)):
           printFull(index)

    elif(com == 4):
      break
    else: 
        print("Siz mavjud bo'lmagan buyruqni kiritdinggiz")
        print("<<<<<<<<Iltimos qaytadan kiriting>>>>>>>>")