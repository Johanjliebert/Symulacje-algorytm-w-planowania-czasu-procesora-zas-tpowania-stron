class FIFO:
    def __init__(self, rozmiar_pamieci):
        self.rozmiar_pamieci = rozmiar_pamieci  # maksymalny rozmiar pamięci podręcznej
        self.strony = []  # lista przechowująca strony obecnie w pamięci podręcznej

    def dostep_do_strony(self, strona):
        if strona not in self.strony:
            # Jeśli strona nie jest w pamięci podręcznej
            if len(self.strony) >= self.rozmiar_pamieci:
                # Jeśli pamięć jest pełna, usuń najstarszą stronę
                usunieta_strona = self.strony.pop(0)  # usuń pierwszy element (najstarszy)
                print(f"Usunięcie strony {usunieta_strona}")
            # Dodaj nową stronę do pamięci
            self.strony.append(strona)
            print(f"Załadowanie strony {strona}")
            return 1
        else:
            # Jeśli strona jest już w pamięci podręcznej
            print(f"Strona {strona} już w pamięci")
            return 0