class FCFS:
    def __init__(self):
        self.zadania = []  # lista do przechowywania zadań

    def dodaj_zadanie(self, nazwa, czas_trwania):
        self.zadania.append((nazwa, czas_trwania))  # dodaj zadanie do listy

    def uruchom(self):
        for nazwa, czas_trwania in self.zadania:
            print(f" {nazwa} - czas trwania {czas_trwania}")