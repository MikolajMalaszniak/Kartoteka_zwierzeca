# Kartoteka_zwierzeca
Simple PyQT5 project, which let you informations about, yours pets and appointments

### Requierments

+ Python3,
+ PyQt5,
+ Postgresql database,
+ Pyscopg2-binary



### Installation
Download application using this command in terminal or by installing it manualy
```
git clone https://github.com/MikolajMalaszniak/Kartoteka_zwierzeca && cd Kartoteka_zwierzeca
```
Create new python environment **.venv name could be changed to your preferances**
```
python3 -m venv .venv
```
##### Python 2+ if python3 is not availble **NOT RECOMENDED**
```
python -m venv .venv
```
#### Linux
```
source .venv/bin/activate
```
#### Windows
```
source .venv\Scripts\activate
```
Upgrade pip to avoid installation difficulties
```
python -m pip install --upgrade pip
```
Install all requierments
```
pip install -r requierments.txt
```
### Configuration

Change database.ini file
```
[postgresql]
host=[ip of your host] # ex. 127.0.0.1
database=[name of postgresql database] # ex. pets
user=[postgresql user name]  # postgres
password=[password of postgresql user] # postgres
port=5432 # Do not change if you don't need
```
## Ready to go
Lunch application
```
python logowanie.py
```
# Enjoy



