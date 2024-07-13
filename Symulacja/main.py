from fcfs import FCFS
from roundrobin import RoundRobin
from fifo import FIFO
from lru import LRU

def wczytaj_dane_planowanie_procesora(sciezka):
    zadania = []
    with open(sciezka, 'r') as plik:
        for linia in plik:
            nazwa, czas_trwania = linia.strip().split(', ')
            zadania.append((nazwa, int(czas_trwania)))
    return zadania

def wczytaj_dane_zastepowanie_stron(sciezka):
    strony = []
    with open(sciezka, 'r') as plik:
        for linia in plik:
            strony.append(int(linia.strip()))
    return strony

def test_fcfs(czas, ilosc):
    fcfs = FCFS()
    zadania = wczytaj_dane_planowanie_procesora('cpu_scheduling.txt')
    czaslaczny=0
    for nazwa, czas_trwania in zadania:
        fcfs.dodaj_zadanie(nazwa, czas_trwania)
        czas+=czas+czas_trwania-ilosc
        ilosc+=1
    czas = czas - czas_trwania + ilosc - 1
    czas/=2
    czas -= ilosc-1
    fcfs.uruchom()
    print (f"czas sredni {czas/ilosc}")

def test_round_robin(ilosc):
    rr = RoundRobin(3)
    zadania = wczytaj_dane_planowanie_procesora('cpu_scheduling.txt')
    for nazwa, czas_trwania in zadania:
        rr.dodaj_zadanie(nazwa, czas_trwania)
        ilosc += 1
    czas=rr.uruchom(ilosc, 0)
    print (f"czas sredni {czas/ilosc}")

def test_fifo():
    fifo = FIFO(3)
    bledy_fifo = 0
    strony = wczytaj_dane_zastepowanie_stron('page_replacement.txt')
    for strona in strony:
        bledy_fifo+=fifo.dostep_do_strony(strona)
    print(f"ilosc bledow - {bledy_fifo}")

def test_lru():
    lru = LRU(3)
    bledy_lru = 0
    strony = wczytaj_dane_zastepowanie_stron('page_replacement.txt')
    for strona in strony:
        bledy_lru+=lru.dostep_do_strony(strona)
    print(f"ilosc bledow - {bledy_lru}")

if __name__ == "__main__":
    print("Testowanie FCFS")
    test_fcfs(0,0)
    print("\nTestowanie Round-Robin")
    test_round_robin(0)
    print("\nTestowanie FIFO")
    test_fifo()
    print("\nTestowanie LRU")
    test_lru()