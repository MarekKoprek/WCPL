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
cd Scripts
./activate
```  
**4. Gdy z lewej strony pojawi sie nazwa środowiska należy zainstalować pakiet Django poprzez komendę**
```bash
py -m pip install Django
```  
**5. Należy zainstalować bibliotekę**
```bash
py -m pip install Pillow
```  
**6. Należy sklonować projekt z github**
```bash
git clone https://github.com/MarekKoprek/WCPL.git
```
# Urochomienie
**Żeby urochomić serwer, znajdując w folderze z projektem, należy wywolać następne polecenie**
```python
python manage.py runserver
```

# Dostępne strony
## Strona administratora
**Adres strony `http://127.0.0.1:8000/admin/`**  
**Dane do konta administratora**
- Username: admin
- Password: admin

## Strona logowania 
**Adres strony `http://127.0.0.1:8000/login/`**  
**Dane konta testowego (student):**
- Username: testowy
- Password: testowehaslo
**(Firma)**
- Username: testFirm
- Password: Password123@

## Strona rejestracji 
**Adres strony `http://127.0.0.1:8000/register/`**  

## Strona z kalendarzem 
**Adres strony `http://127.0.0.1:8000/calendar/`**  

## Strona z wydarzeniami 
**Adres strony `http://127.0.0.1:8000/events/`**  

## Strona z profilem 
**Adres strony `http://127.0.0.1:8000/profile/<username>`**  

**Na przykład można użyć następującej strony:**
**`http://127.0.0.1:8000/profile/romanbeznosenko`**

## Strona z profilem 
**Adres strony `http://127.0.0.1:8000/profile/<username>`**  


