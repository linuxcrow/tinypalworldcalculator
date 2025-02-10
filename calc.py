print("Welcome to the LinuxCrow Medical Supply Calculator!")
print("If you do not need a drug, type 0 or else the program will crash.")
LGResult = 0
Horns = 0
Bones = 0
Ingots = 0
LGMS = int(input("How many LowGrade Medical Supplies do you need? "))
if LGMS >= 1:
    LGResult = LGMS*5
    Horns = LGMS*2
else:
    print("No LGMS is needed.")
MS = int(input("How many Medical Supplies do you need? "))
if MS >= 1:
    Ingots = MS*3
    Bones = MS*1
    Horns += (MS*3)
else:
    print("No MS is needed.")
HGMS = int(input("How many High Grade Medical Supplies do you need? "))
if HGMS >= 1:
    Ingots += (HGMS*5)
    Bones += (HGMS*2)
    Horns += (HGMS*5)

else:
    print("No HGMS is needed.")

if LGMS <= 0 and MS <= 0 and HGMS <= 0:
    print("Why'd you open this? TF you on?! Nitrogen?!")
# elif LGMS <= 0 and MS <= 0 and HGMS <= 0:
#    print("Why'd you open this? TF you on?! Nitrogen?!")
else:
    print("You need {0} Berries, {1} Horns, {2} Ingots, {3} Bones.".format(
        LGResult, Horns, Ingots, Bones))
