kapA=int(input("Anfangskapital: "))
zins=float(input("Zins: "))
kapE=int(input("Endkapital: "))
zuw=0
kap=kapA
jahr=0
while kap<kapE:
    jahr=jahr+1
    zuw=zuw+(kap*zins)/100
    kap=kapA+zuw
    print("kapital: %.2f"%kap)
    print("zuwachs: %.2f"%zuw)
    print("jahr:",jahr)
input()
     
