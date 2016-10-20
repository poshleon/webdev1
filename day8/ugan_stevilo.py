import random
stevilo_vnosov = 0
vsi_vnosi = 3
pravo_stevilo = random.randint(1,100)
for stevilo_vnosov in range (vsi_vnosi):
    ugibano_stevilo = raw_input("Vnesi stevilo: ")
   
    if int(ugibano_stevilo) == pravo_stevilo:
        print("Uganil si stevilo!")
        break
    elif int(ugibano_stevilo) > pravo_stevilo:
        print("Tvoja stevilka je vecja.")
    elif int(ugibano_stevilo) < pravo_stevilo:
        print("Tvoja stevilka je manjsa.")
else:
    print("presegel si stevilo vnosov")
