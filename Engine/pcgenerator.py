# -*- coding: utf-8 -*-
import json
import os

def generate(inputfile):
    with open(inputfile, "r") as pc:
        data = json.load(pc)
    print("Загружается файл %s" %(inputfile))
    # Debug
    print (data)
    # END
    statlist=["SaveMe","Strength","Agility","Intelligence","Willpower","Stamina","Charisma"]
    data["Name"]=input("Введите имя: ")
    data["Gender"]=input("Введите пол: ")
    bonus = 5
    while (bonus>0):
        print("Выберите параметры для увеличения (очков %i): " %(bonus))
        print("1: Сила - %i\n2: Ловкость - %i\n3: Интеллект - %i\n4: Сила воли - %i\n5: Выносливость - %i\n6:Харизма - %i" %(data["Strength"],data["Agility"],data["Intelligence"],data["Willpower"],data["Stamina"],data["Charisma"]))
        selector=int(input())
        stat=int(input("Как изменить параметр?"))
        data[statlist[selector]]+=stat
        if (1 > data[statlist[selector]] > 10): 
            print("Базовый параметр не может быть ниже 1 или больше 10")
            data[statlist[selector]]-=stat
        else:
            bonus-=stat
      
    data["HP"]=data["Strength"]*data["Stamina"]    
    data["MP"]=data["Intelligence"]*data["Willpower"]
    data["AP"]=data["Agility"]*data["Stamina"]
    # if (selector == 0):
    savename = input("Имя сохранения: ")
    os.mkdir("./saves/"+savename)
    with open("./saves/"+savename+"/pc.json", "w+") as save_file:
        json.dump(data, save_file)
        
generate("PC.json")