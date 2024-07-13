class LRU:
    def __init__(self, rozmiar_pamieci):
        self.rozmiar_pamieci = rozmiar_pamieci  # maksymalny rozmiar pamięci podręcznej
        self.strony = []  # lista przechowująca strony obecnie w pamięci podręcznej
        self.kolejnosc_dostepu = []  # lista przechowująca kolejność dostępu do stron

    def dostep_do_strony(self, strona):
        if strona in self.strony:
            # Jeśli strona jest już w pamięci podręcznej
            self.kolejnosc_dostepu.remove(strona)  # usuń ze zmiennej kolejności dostępu
            self.kolejnosc_dostepu.append(strona)  # dodaj na koniec, jako ostatnio użyta
            print(f"Strona {strona} w pamięci")
            return 0
        else:
            # Jeśli strona nie jest w pamięci podręcznej
            if len(self.strony) >= self.rozmiar_pamieci:
                # Usuń najdawniej używaną stronę
                lru_strona = self.kolejnosc_dostepu.pop(0)
                self.strony.remove(lru_strona)
                print(f"Usunięcie strony {lru_strona}")
            # Dodaj nową stronę do pamięci i kolejności dostępu
            self.strony.append(strona)
            self.kolejnosc_dostepu.append(strona)
            print(f"Załadowanie strony {strona}")
            return 1