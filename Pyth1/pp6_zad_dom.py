#a

print("*"*1+ 8*" " + "*"*1)
print("*"*2+ 6*" " + "*"*2)
print("*"*3+ 4*" " + "*"*3)
print("*"*4+ 2*" " + "*"*4)
print("*"*5+ 0*" " + "*"*5)
print("*"*4+ 2*" " + "*"*4)
print("*"*3+ 4*" " + "*"*3)
print("*"*2+ 6*" " + "*"*2)
print("*"*1+ 8*" " + "*"*1 +"\n")

#b

#1 terabajt to 1024 gigabajty (1 TB = 1024 GB)
#1 terabajt to 1 048 576 megabajty (1 TB = 1 048 576 MB)
#plik o rozmiarze 194 MB udało się pobrać w 5 sekund

string_number1 = input("Podaj ile TB chcesz pobrac:")
print("Zajmie to: " + str(round(int(string_number1)*1_048_576/194*5/60/60))+" godzin. " +"\n")

#c

L = 30_000
r1=7.5/100/4
r2=8/100/4
r3=8.25/100/4

print("Saldo w PLN po kazdym kwartale wynosi:", str(round(L*(1+r1),2)) + ", "+ str(round(L*(1+r1)*(1+r1),2)) +", "+ str(round(L*(1+r1)*(1+r1)*(1+r1),2)) +", " + str(round(L*(1+r1)*(1+r1)*(1+r1)*(1+r1),2)) +", roczny zysk to: " +str(round(L*(1+r1)*(1+r1)*(1+r1)*(1+r1)-L,2))+" zl.")

print("Saldo w PLN po kazdym kwartale wynosi:", str(round(L*(1+r2),2)) + ", "+ str(round(L*(1+r2)*(1+r2),2)) +", "+ str(round(L*(1+r2)*(1+r2)*(1+r2),2)) +", " + str(round(L*(1+r2)*(1+r2)*(1+r2)*(1+r2),2)) +", roczny zysk to: " +str(round(L*(1+r2)*(1+r2)*(1+r2)*(1+r2)-L,2))+" zl.")

print("Saldo w PLN po kazdym kwartale wynosi:", str(round(L*(1+r3),2)) + ", "+ str(round(L*(1+r3)*(1+r3),2)) +", "+ str(round(L*(1+r3)*(1+r3)*(1+r3),2)) +", " + str(round(L*(1+r3)*(1+r3)*(1+r3)*(1+r3),2)) +", roczny zysk to: " +str(round(L*(1+r3)*(1+r3)*(1+r3)*(1+r3)-L,2))+" zl.")