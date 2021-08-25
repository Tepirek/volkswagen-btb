# VOLKSWAGEN - BE THE BEST

## Wstęp 

W Panśtwa ręce oddajemy efekt wielu godzin naszej pracy - kod wykonany na konkurs VOLKSWAGEN - BE THE BEST dotyczący stworzenia aplikacji WEB usprawniającej proces lakierowania. 

## Wykonane zadania 
- [x] System tworzenia raportów i mechanizm nanoszenia punktów na poszczególne komponenty.
- [x] Panel do szczegółowego przeglądania utworzonych raportów.
- [x] Panel użytkownika.
- [x] Historia (dziennik) aktywności pracowników.
- [x] Mechanizm mapowania punktów z bazy danych na motyle.
- [x] Mechanizm tworzenia podsumowań z podanego przedziału czasu i panel do ich przeglądania.
- [x] Dodanie mechanizmu umożliwiającego zmianę jezyka aplikacji.

## Do zrobienia - plany na rozwój aplikacji
- [x] Modele 3D aut z naniesionymi punktami.
- [x] Dostosowanie systemu uprawnień według firmowych wymagań i hierarchii pracowniczej.
- [x] Rozwinięcie mechanizmu tworzenia podsumowań według dodatkowych wymagań.

## Wymagana konfiguracja 
- Do uruchomienia aplikacji potrzebny jest interprter Python zainstalowany na komputerze. Konieczne jest również dokonanie instalacji pip (`sudo apt install python3-pip`) oraz npm.
- Gorąco polecamy uruchomienie aplikacji używając systemu z rodziny Linux(np. Ubuntu), ponieważ głównie na nim skupiać będzie się opis instrukcji uruchomienia. Proces ten powinien być w znacznej części bardzo podobny do tego, który należy przeprowadzić pod Windowsem, jednakże nie będzie on identyczny.

## Instrukcja uruchomienia aplikacji 

### Pobranie projektu 
1. Pierwszym krokiem do uruchomienia aplikacji jest jej pobranie lub sklonowanie repozytorium.
- W tym celu przechodzimy do miejsca, gdzie chcemy zainstalować naszą aplikację, a następnie możemy użyć komendy:

`git clone <link_do_repozytorium> VOLKSWAGEN_KONKURS`

### Uruchomienie aplikacji serwerowej
1. Przechodzimy do folderu zawierającego naszą aplikację.
- `cd VOLKSWAGEN_KONKURS`
2. Kolejnym krokiem jest instalacja i uruchomienie środowiska wirtualnego.
- `pip install virtualenv`
- `virtualenv venv`
- `source venv/bin/activate`
3. W głównym folderze aplikacji powinien znajdować się skrypt (`run.sh`), w którym zawarte są komendy instalujące niezbędne biblioteki. Skryptowi nadajemy uprawnienia do uruchamiania i wywołujemy go.
- `chmod +x run.sh`
- `sudo ./run.sh`
(Potencjalnym problemem może być interpreter bash -> można wtedy zamienić pierwszą linię skryptu np. na `!#/bin/bash`. Jeśli to nie pomoże, zachęcamy do ręcznego zainstalowania bibliotek znajdujących się w skrypcie.
4. Przechodzimy do podkatalogu 'App'.
- `cd App/`
5. Niezbędnym krokiem jest wykonanie migracji.
- `python manage.py migrate`
6. Możemy teraz utworzyć superusera - jest to niezbędne, aby przejść do kolejnych kroków.
- `python manage.py createsuperuser`
- następnie wpisujemy login, hasło i potwierdzamy hasło (np. login: root password: root). Możemy zostać zapytani o zrobienie wyjątku, jeśli hasło, które podamy będzie zbyt słabe - można się na to wyjątkowo zgodzić 😉
7. Teraz możemy wypełnić bazę sztucznymi danymi za pomocą napisanej przez nas komendy (w terminalu mogą pojawić się ostrzeżenia - nie trzeba się nimi przejmować).
  - _Losowość wygenerowanych danych może powodować w niektórych miejscach niepoprawne zachowanie aplikacji. W normalnym scenariuszu pewne kombinacje danych nie wystąpują. Przykładem niepoprawnego zachowania przez losowe dane może być: raport ze statusem **wysłano**, mimo braku daty wysłania._
  - `python manage.py GlobalSeeder`
8. Gdy baza danych zostanie już wypełniona, możemy uruchomić sam serwer.
- `python manage.py runserver`

Gdy wszystko zostanie wykonane poprawnie, możemy cieszyć się działającą częścią serwerową aplikacji!

### Uruchomienie aplikacji klienckiej 
1. Otwórzmy nowy terminal, a następnie przejdźmy do folderu, w którym znajduje się nasz projekt - tak jak w poprzednim etapie (czyli np.VOLKSWAGEN_KONKURS)
- najlepiej klikając przycisk otwarcia nowego terminala w lewym górnym rogu okienka.
2. Przechodzimy do podkatalogu 'client'.
- `cd ../client` lub `cd client`
3. Dokonujemy instalacji.
- `sudo npm install`
4. Budujemy front aplikacji.
- `npm run serve`
- Może to potrwać, ale już po chwili nasza aplikacja będzie dostępna na: `http://localhost:8080/`

Miłego użytkowania!

### Dodatkowe informacje

W razie kłopotów z uruchomieniem programu prosimy o kontakt mailowy:
-tomasz.tomaszewski2000@wp.pl
-arkadiusz.tepper@gmail.com

Serdecznie zachęcamy do zadawania pytań dotyczących aplikacji.

Pozdrawiamy! 😉
