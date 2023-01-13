class Bankomat:
    def __init__(self):
        self.__bal = 500
        print("""BANKOMAT
                 Wybierz opcje:
                 1. Saldo
                 2. Wplata
                 3. Wyplata
                 4. Koniec
           """)

    def wplata(self):
        amt = int(input("Podaj kwote wplaty:"))
        self.__bal += amt
        print("\n Zdeponowane:", amt)

    def wyplata(self):
        amt = int(input("Podaj kwote wyplaty:"))
        if self.__bal >= amt:
            self.__bal -= amt
            print("\n Wyplacone:", amt)
        else:
            print("\n Brak srodkow!")

    def wyswietl(self):
        print("\n Stan konta=", self.__bal)

    def wybierz(self):
        while True:
            try:
                x = int(input("wybierz 1, 2, 3, 4:"))
            except:
                print("Blad: wprowadz 1, 2, 3, 4!\n")
                continue
            else:
                if x == 1:
                    s.wyswietl()
                elif x == 2:
                    s.wplata()
                elif x == 3:
                    s.wyplata()
                elif x == 4:
                    print("KONIEC")
                    break


s = Bankomat()
s.wybierz()

