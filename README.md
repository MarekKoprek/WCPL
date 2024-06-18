# Instalacja
**1. Należy zainstalować python w wersji 3.12.0**
```
https://www.python.org/downloads/release/python-3120/
```

**2. Należy stworzyć środowisko w terminalu**
```bash
py -m venv (nazwa_środowiska)
```  
**3.Należy wykonać następujące polecenia**  
```bash
cd nazwa_środowiska
Scripts\activate
```  
**4. Gdy z lewej strony pojawi sie nazwa środowiska należy zainstalować pakiet Django poprzez komendę**
```bash
py -m pip install Django
```  
**5. Należy zainstalować bibliotekę**
```bash
py -m pip install Pillow  
py -m pip isntall django-formtools
```  
**6. Należy sklonować projekt z github**
```bash
git clone https://github.com/MarekKoprek/WCPL.git
```
# Urochomienie
**Żeby urochomić serwer, znajdując się w folderze z projektem, należy wywolać następne polecenie**
```python
python manage.py runserver
```

# Dostępne strony
## Strona administratora
**Adres strony `http://127.0.0.1:8000/admin/`**  
**Dane do konta administratora**
- Username: admin
- Password: admin

### Opis: ###
Strona administratora umożliwia przeglądanie bazy danych, wprowadzanie zmian w niej, oraz dodawanie nowych rekordów.
Aby wprowadzić zmiany należy wybrać po lewej stronie model, a następnie przejść do wybranego rekordu poprzez kliknięcie pierwszej kolumny w danym rekordzie. Po wprowadzeniu zmian należy je na dole zapisać. Można również dodać rekord w prawym górnym rogu każdego modelu.

Dostępne są 4 modele: 
- Użytkownicy (login, haslo (zaszyfrowane), imię, nazwisko, email, uprawnienia itd.)
- Profile użytkowników (Dane zależne od typu użytkonika (student, firma))
- Wydarzenia (zdjęcie, autor, uczestnicy (nie należy dodawać administratora ręcznie do uczestników), tytuł, opis, data rozpoczęcia i zakończenie)
- Zgłoszenia błędów (autor, strona na której wystąpił błąd, opis)
Wydarzenia zgłaszane przez użytkowników dodawane są do bazy danych z polem 'accepted' ustawionym postawowo na 0 zmiania tego pola na dowolną wartośś różną od 0 sprawi, że wydarzenie zostanie zatwierdzone i będzie się wyswietlało na stronie głównej.
Zalogowanie się do strony administratora kontem uprzywilejowanym sprawi, że będzie on zalogowany też na głównej stronie, więc zalecane jest przelogowanie się po powrocie na główną stronę.

## Strona logowania 
**Adres strony `http://127.0.0.1:8000/login/`**  
**Dane konta testowego (Student):**
- Username: testowy
- Password: testowehaslo   

**Dane konta testowego (Firma):**
- Username: testFirm
- Password: Password123@

## Strona rejestracji 
**Adres strony `http://127.0.0.1:8000/register/`**  

## Strona z kalendarzem 
**Adres strony `http://127.0.0.1:8000/calendar/`**  
### Opis: ###
Strona kalendarza wyświetla widok kalendarza, który pokazuje wydarzenia, w których zalogowany użytkownik bierze udział.

### Funkcje: ###
- **Widok kalendarza:** Prezentuje miesięczny widok kalendarza.   
- **Wyświetlanie Wydarzeń:** Pokazuje kiedy zaczyna i kończy się wydarzenie.   
- **Nawigacja:** Umożliwia użytkownikom poruszanie się między miesiącami oraz powrót do dzisiejszej daty.
- **Link do wydarzeń:** Kliknięcie w wydarzenie w kalendarzu przeniesie do strony informacyjnej tego wydarzenia.

## Strona z wydarzeniami 
**Adres strony `http://127.0.0.1:8000/events/`**  
### Opis: ###
Strona z listą wszystkich zatwierdzonych przez administratora wydarzeń w kolejności chronologicznej.

### Funkcje: ###
- **Wyświetlenie szczegółów wydarzenia:** Po kliknięciu w dowolne wydarzenie na liście, po prawej stronie wyświetli się jego dokładniejszy opis.
- **Linki do uczestników:** W informacjach o wydarzeniach w dolnej części znajduje się lista pierwszych 12 uczestników. Kliknięcie danego uczestnika przekieruje do jego profilu.
- **Zgłoszenie udziału:** W informacjach o wydarzeniach w dolnej części przyciskiem można zgłosić udział w wydarzeniu co automatycznie doda je do kalendarza, jeżeli użytkownik bierze udział w wydarzeniu tym przyciskiem będzie mógł wypisać się z tego wydarzenia.
- **Dodanie wydarzenia:** Przycisk pod listą wydarzeń przeniesie do strony z dodawaniem wydarzenia. Zdjęcie musi być w formacie jpg lub png, lecz nie jest wymagane, jeżeli nie będzie dodane to ustawione zostanie podstawowe zdjęcie wydarzenia. Tytuł może mnieć maksymalnie 100 znaków. Opis może mieć maksymalnie 620 znaków. Data rozpoczęcia nie może być wcześniejsza niż data w momencie dodawania ogłoszenia. Data zakończenie nie może być wcześniej niż data rozpoczęcia. Jeżeli formularz przejdzie walidację to nastąpi przekierowanie do strony z listą wydarzeń, a zgłoszenie zostanie zapisane. W przeciwnym wypadku nie nastąpi przekierowanie, co oznacza, że któreś pole nie spełnia wymagań. Aby zatwierdzić wydarzenie należy przejść do strony administratora. Zalogowanie się do strony administratora kontem administratora wiąże się z automatycznym przelogowaniem na to konto również na głównej stronie, więc po powrocie na główną stronę zalecane jest ponowne zalogowanie się na konto testowe.
- **Edycja ogłoszenia:** Jeżeli jest się autorem wydarzenia to na stronie informacyjnej tego wydarzenia pojawi się opcja do edycji go. Kliknięcie tego przycisku przekieruje do formularza jak w przypadku dodawania ogłoszenia z tą różnicą, że nie dodanie zdjęcia będzie się wiązało z pozostawieniem starego, a nie ustawieniem podstawowego. Przesłanie poprawnego formularza sprawi, że wydarzenie będzie wymagało ponownego zatwierdzenia przez administratora.

## Strona z profilem 
**Adres strony `http://127.0.0.1:8000/profile/<username>`**  

**Na przykład można użyć następującej strony:**
**`http://127.0.0.1:8000/profile/romanbeznosenko`**

### Opis: ###
Strona profilu użytkownika wyświetla informacje o użytkowniku, jego dane osobowe oraz zdjęcie.

### Funkcje: ###
- **Wyświetlanie danych użytkownika:** Pokazuje nazwę użytkownika, dane osobowe, zdjęcie profilowe.   
- **Edycja profilu:** Umożliwia użytkownikowi edytowanie swojego profilu, w tym zmianę danych osobowych oraz zdjęcia profilowego.   
- **Zgłaszanie błędów:** Użytkownik może zgłosić błąd.    


## Strona ze zgłoszeniem błędu ##
**Adres strony `http://127.0.0.1:8000/bug/`**  
### Opis: ###
Strona ze zgłoszeniem błędu umożliwia użytkownikom zgłaszanie problemów związanych z aplikacją.

### Funkcje: ###
- **Formularz zgłaszania błędu:** Użytkownicy mogą wypełnić formularz, aby opisać napotkany problem.   
