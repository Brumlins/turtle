import turtle
import zelva



x=5


while (x!=0):
    x=int(input("1. kruh\n2. spirala\n3. ctverec\n4. srdce\n0. konec\nvolba: "))
    if x==1:
        zelva.kruh()
    elif x==2:
        zelva.spirala()
    elif x==3:
        zelva.ctverec()
    elif x==4:
        zelva.srdce()