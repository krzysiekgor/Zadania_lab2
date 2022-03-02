import math
#zadanie1
listaSportow = ["Siatkówka","Tenis","Tenis stołowy"]
listaSportow.reverse()
listaSportow.append("Piłka nożna")
listaSportow.append("Koszykówka")
listaSportow.append("Piłka ręczna")

#zadanie2

slownikSkrotow = {"wgl":"W ogóle","nwm":"nie wiem","k":"okej","bdb":"bardzo dobrze"}

#zadanie3

ulubioneGry = {"Wiedźmin 3":"RPG","Gothic":"RPG","Diablo":"Hack&Slash"}
print("liczba ulubionych gier to: " + str(len(ulubioneGry)))

#zadanie4

# zdanie = input("Podaj zdanie do policzenia w nim litery 'a'")
# print("ilość wystąpień 'a' w zdanie to: "+str(zdanie.count('a')))

#zadanie5

odczyt = open("input","r")
liczby = odczyt.readline().split(' ')
if(len(liczby) ==3):
    wynik = math.pow(int(liczby[0]),int(liczby[1])) + int(liczby[2])
else:
    print("w pliku nie ma równo trzech liczb oddzielonych od siebie spacjami")
zapis = open("output","w")
zapis.write(str(wynik))

#zadanie6

# lista = [0] * 3
# lista[0]= int(input("Podaj 1 liczbę: "))
# lista[1]= int(input("Podaj 2 liczbę: "))
# lista[2]= int(input("Podaj 3 liczbę: "))
# temp = lista[0]
# for element in lista:
#     if(temp<element):
#         temp=element
# print("Największą liczbą jest: "+ str(temp)+", jest to liczba numer: "+str(lista.index(temp)+1))

#zadanie7

# listaLiczb = [1,2,3,5.2,2.1,3]
# for i in range(len(listaLiczb)):
#      listaLiczb[i] = math.pow(listaLiczb[i],2)
# print(listaLiczb)

#zadanie8
# listaLiczb = [0]*10
# i=0
# wynik=0
# while i < 10:
#     listaLiczb[i] = int(input("Podaj "+ str(i+1) +" liczbę:"))
#     i+=1
# for e in listaLiczb:
#     if(e%2==0):
#         wynik = wynik+e
# print("Suma parzystych liczb to: "+str(wynik))

# zadanie9

pierwiastek = float(input("Podaj liczbę do pierwiastkowania: "))
try:
    print("Pierwiastek z liczby "+str(pierwiastek) +" to: "+str(math.sqrt(pierwiastek)))
except ValueError:
    print("tej liczby nie można pierwiastkować")
