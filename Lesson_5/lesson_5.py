#This is solution of assigned homework, also present in JPY

#Ambulance
#Nursing 700/hr, Doctor 1 500/hr
#We need to input km, if nursing staff or doctor is needed on board
#avg speed is 60km/hr

nurse = 700
doctor = 1500

km = int(input("Km?: \n"))
basicFee = 800 + (km*25)

print("What staff is required? \n1) Nursing\n2) Doctor\n3) Both")
staff = int(input())

staffFee = 0
if staff == 1:
    staffFee = nurse
elif staff == 2:
    staffFee = doctor
elif staff == 3:
    staffFee = nurse + doctor

finalCost = (km/60)*(staffFee+basicFee)

print(finalCost)