import random
import ctypes
import time

LowNum=int(input("Low:"))
MaxNum=int(input("Max:"))

Seed1=ctypes.addressof(ctypes.c_int(LowNum))
Seed2=ctypes.addressof(ctypes.c_int(MaxNum))
Seed3=time.time()
Seed=Seed1+Seed2+Seed3
random.seed(Seed)
print("The seed has been set.The current seed is : %d" % Seed)

if LowNum>MaxNum:
    print("Low number is greater than max number.")
    LowNum=int(input("Low:"))
    MaxNum=int(input("Max:"))

print("--------------------")

while True:
    print(random.randint(LowNum,MaxNum))
    UserInput=input("Press enter to continue.Type 'exit' to quit.Type 'settings' to change settings:")
    if UserInput=="exit":
        break
    elif UserInput=="settings":
        print("--------------------")
        print("Settings:")
        print("Type '1' to change the low number.")
        print("Type '2' to change the max number.")
        print("Type '3' to change the seed.")
        SettingInput=input("Setting:")
        if SettingInput=="1":
            LowNum=int(input("Low:"))
        elif SettingInput=="2":
            MaxNum=int(input("Max:"))
        elif SettingInput=="3":
            Seed=int(input("Pless enter a number as the seed:"))
            random.seed(Seed)
        print("--------------------")
    else:
        pass