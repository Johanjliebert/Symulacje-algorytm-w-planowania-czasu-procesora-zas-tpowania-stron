class RoundRobin:
    def __init__(self, kwant_czasu):
        self.zadania = []  # lista do przechowywania zadań
        self.kwant_czasu = kwant_czasu  # kwant czasu dla algorytmu Round Robin


    def dodaj_zadanie(self, nazwa, czas_trwania):
        self.zadania.append([nazwa, czas_trwania])  # dodaj zadanie do listy zadań

    def uruchom(self, ilosc, czassredni):
        while self.zadania:
            if(ilosc>0):
                ilosc-=1
                czassredni+=3*ilosc
            nazwa, czas_pozostaly = self.zadania.pop(0)  # pobierz pierwsze zadanie z listy
            if czas_pozostaly <= self.kwant_czasu:
                print(f"Wykonanie zadania {nazwa} z czasem pozostałym {czas_pozostaly}")
            else:
                # Jeśli czas potrzebny do wykonania zadania jest większy od kwantu czasu
                print(f"Wykonanie zadania {nazwa} przez {self.kwant_czasu} jednostki czasu")
                # Dodaj zadanie z pozostałym czasem do wykonania z powrotem do listy
                self.zadania.append([nazwa, czas_pozostaly - self.kwant_czasu])
        return czassredni
