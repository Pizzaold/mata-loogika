'''
Kasutaja sisend ja arvutused

Liiklusseaduse järgi määratakse suurima lubatud sõidukiiruse ületamise korral hoiatustrahv, mille suurus eurodes saadakse lubatud sõidukiirust ületanud kilomeetrite arvu korrutamisel arvuga 3. Hoiatustrahvi maksimaalmäär on 190 eurot.
'''

name = input("Nimi: ")
speed_allowed = int(input("Lubatud kiirus: "))
speed_actual = int(input("Tegelik kiirus: "))

fine = (speed_actual - speed_allowed) * 3

fine = min(190, fine)
fine = max(0, fine)

print(f"{name}, kiiruse ületamise eest on teie trahv {fine}€")