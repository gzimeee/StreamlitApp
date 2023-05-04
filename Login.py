# =============================================================================
# -----------------------Leukofit APP-------------------
#   Beschreibung: Das ist die "Login"-Seite
#   Hier werden die Informationen zum Login der Leukofit APP 
#   beschrieben 
#   
#    Datum: 02.05.2023
#    Autoren: Gzime Ramadani, Rinesa Shabija, Priya Jose
# =============================================================================


# Schritt 1: Erstellen der Multipage APP=======================================
#   Es wird eine Multipage APP erstellt.
#   Es wird der Seitentitel mir Icon definiert.
#   Es werden die Bilbiotheken / Packages importiert.
# =============================================================================
import streamlit as st
import streamlit_authenticator as stauth
import yaml
import os
import os.path


st.set_page_config(
    page_title="Loginseite",
    page_icon="🔒",
)


# Schritt 2: Lesen der Benutzerdaten===========================================
#   Die Benutzerdaten (Benutzername und Passwort)
#   werden aus der config.yaml gelesen.
# =============================================================================


from yaml.loader import SafeLoader
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
    
    #Authenticator Objekt
    authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
    
name, authentication_status, username = authenticator.login('Login', 'main')


# Schritt 3: Alle Pages in .txt umbennen=======================================
#   Hier wird eine Funktion definiert, welche alle Pages im Ordnern "pages"
#   von .py in .txt umbenennt. Die Funktion wird weiter unten gestartet
# =============================================================================

def totxt():
    if os.path.isfile("pages/Leukorechner.py"):
              os.rename("pages/Leukorechner.py", "pages/Leukorechner.txt")
    elif os.path.isfile("pages/JSON-Daten.py"):
              os.rename("pages/JSON-Daten.py", "pages/JSON-Daten.txt")
    elif os.path.isfile("pages/Funktionsweise.py"):
              os.rename("pages/Funktionsweise.py", "pages/Funktionsweise.txt")
    elif os.path.isfile("pages/Über.py"):
         os.rename("pages/Über.py", "pages/Über.txt")
    else:
        pass 
    
        


# Schritt 4: Login-Mechanismus=========n=======================================
#   Hier wird der komplette Login-Mechanismus ausgeführt
# =============================================================================    
     
     
     
if authentication_status:
    authenticator.logout('Logout', 'main')
    if username == 'benutzer': #Wenn Ebnutzer eingeloggt ist, dann sollen alle Pages in .py umbenannt werden
        st.write(f'Willkommen *{name}*')
        st.title('Alle Funktionen freigeschaltet')
        try: #Alle Pages im Ordner Pages werden von .txt in.py umbenannt
            os.rename("pages/Leukorechner.txt", "pages/Leukorechner.py")
            os.rename("pages/Funktionsweise.txt", "pages/Funktionsweise.py")
            os.rename("pages/JSON-Daten.txt", "pages/JSON-Daten.py")
            os.rename("pages/Über.txt", "pages/Über.py")
        except (Exception):
            pass
    elif username == 'gast': #Wenn aber Gast eingeloggt ist, sollen nur die zwei Pages in .py umbenannt werden
        st.write(f'Willkommen *{name}*')
        st.title('Beschränkter Zugriff auf Funktionen')
        try: #Die zwei Pages im Ordner Pages werden in .py umbenannt
            os.rename("pages/Funktionsweise.txt", "pages/Funktionsweise.py")
            os.rename("pages/Über.txt", "pages/Über.py")
        except (Exception):
            pass
      
elif authentication_status == False: #Wenn aber das Passwort oder Benutzername falsch ist, soll eine Fehlermeldung erscheinen. Zur sicherheit werden alle Dateien in .txt umbenannt
    st.error('Benutzername/Passwort ist falsch')
    try: #Zur Sicherheit werde alle Pages in .txt umbenannt, sodass diese nicht geöffnet werden können
        os.rename("pages/Leukorechner.py", "pages/Leukorechner.txt")
        os.rename("pages/Funktionsweise.py", "pages/Funktionsweise.txt")
        os.rename("pages/JSON-Daten.py", "pages/JSON-Daten.txt")
        os.rename("pages/Über.py", "pages/Über.txt")
    except (Exception):
        pass
elif authentication_status == None: #Ansonsten wenn niemand eingeloggt ist oder der Benutzer auf Logout klickt, sollen alle Pages wieder zurück zu .txt umbenannt werden
    st.warning('Bitte Benutzernamen und Passwort eingeben')
    totxt() #Die am Anfang definierte Funktion zum umbenennen in .txt wird aufgerufen

        
        


    
 
    

    
    
    
   