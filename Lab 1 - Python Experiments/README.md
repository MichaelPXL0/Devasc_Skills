Lab 1 - Python Experiments

1.1 Install different tools/packages on Ubuntu DEVASC-LABVM:

	01. Voorbereiding en uitvoering van de taak:

		De eerste stap is het besturingssysteem bijwerken met het commando "sudo apt update" om ervoor te zorgen dat alle pakketbronnen up-to-date zijn.
		Vervolgens is Python 3.8 geïnstalleerd met het commando "sudo apt install python3.8" omdat het nog niet aanwezig is op het systeem.
		Om PIP te installeren, is het commando "sudo apt install python3-pip" gebruikt.
		Om te controleren of Visual Studio Code al op het systeem is geïnstalleerd, is het commando "code --version" uitgevoerd.
		Om Jupyter te installeren, is het commando "pip3 install jupyter" gebruikt.

	02. Probleemoplossing van de taak:

		Tijdens de installatie van Jupyter waren er problemen met incompatibele versies van afhankelijkheden, zoals Jinja2, MarkupSafe, requests en zipp. Om de fouten op te lossen, zijn de modules gedowngraded naar compatibele versies.
		Het commando "pip install cookiecutter" is uitgevoerd om cookiecutter te installeren met compatibele versies van de afhankelijkheden, zoals Jinja2, MarkupSafe, charset-normalizer en requests.
		Het commando "pip install requests>=2.23.0" is uitgevoerd om de juiste versie van requests te installeren.
		Het commando "pip install --upgrade zipp>=3.1.0" is gebruikt om de juiste versie van zipp te installeren.
		Na het downgraden van de modules is de installatie van Jupyter opnieuw uitgevoerd met het commando "pip3 install jupyter".
		Bij het starten van Python IDLE treedt er ook een fout op met de melding "ImportError: cannot import name '_setup_dialog' from 'tkinter.simpledialog' (/usr/lib/python3.8/tkinter/simpledialog.py)". Om de fout op te lossen, is het commando "sudo apt-get install python3-tk" uitgevoerd. Dit om de juiste versie van Tkinter te installeren, die nodig is voor Python IDLE te kunnen starten.

	03. Verificatie van de taak:

		Na de installatie van Python 3.8 is de versie gecontroleerd met het commando "python3.8 --version".
		Na de installatie van PIP is de versie gecontroleerd met het commando "pip3 --version".
		Na de installatie van Visual Studio Code is de versie gecontroleerd met het commando "code --version".
		Na de installatie van Jupyter is de versie gecontroleerd met het commando "jupyter --version".
		Na de installatie van Python IDLE is de versie gecontroleerd met het commando "idle-python3.8".
		
1.2 Run geopy and timedate Python Scipts on the DEVASC-LABVM 

	01. Voorbereiding en uitvoering van de taak:

		Python in terminal:
		
			Terminal is gestart 
			Het script timedate.py is uitgevoerd door het commando python3.8 timedate.py in te gegeven.
		
		Visual Studio Code in terminal:
		
			Visual Studio Code is gestart
			Het script timedate.py is ingeladen en uitgevoerd door op de play knop te drukken.
			Het script geopy-geocoders_location.py is ingeladen en uitgevoerd door op de play knop te drukken.
			Het script location.py is ingeladen en uitgevoerd door op de play knop te drukken.
		
		Jupyter Notebook in Terminal & Web Browser:
		
			Jupyter Notebook is vanuit terminal gestart met het commando jupyter notebook.
			Een nieuw Python3-notebook is geopend.
			Het script timedate.py is ingeladen en uitgevoerd door het commando %run timedate.py in de notebook in te geven.
			Het script geopy-geocoders_location.py is ingeladen en uitgevoerd door het commando %run geopy-geocoders_location.py in de notebook in te geven.
			Het script location.py is ingeladen en uitgevoerd door het commando %run location.py in de notebook in te geven.
		
		Python IDLE in Terminal:
		
			Python IDLE is vanuit terminal gestart met het commando idle-python3.8.
			Het script timedate.py is ingeladen en uitgevoerd.
			Het script geopy-geocoders_location.py is ingeladen en uitgevoerd.
			Het script location.py is ingeladen en uitgevoerd.
			
	02. Probleemoplossing van de taak:
	
		Ontbrekende module 'geopy':
		
			Tijdens het uitvoeren van het script geopy-geocoders_location.py werd de foutmelding "No module named 'geopy'" getoond. Dit geeft aan dat de vereiste module 'geopy' niet was geïnstalleerd.
			Om dit probleem op te lossen, werd het commando sudo pip3 install geopy uitgevoerd in de terminal. Hiermee werd de 'geopy'-module geïnstalleerd, waardoor het script kon worden uitgevoerd zonder de foutmelding.
		
		Ontbrekende module 'folium':
		
			Na het installeren van de 'geopy'-module en het opnieuw uitvoeren van het script geopy-geocoders_location.py, werd de foutmelding "No module named 'folium'" weergegeven. Dit betekent dat de vereiste module 'folium' ontbrak.
			Om dit probleem op te lossen, werd het commando sudo pip3 install folium uitgevoerd in de terminal. Hiermee werd de 'folium'-module geïnstalleerd, waardoor het script zonder problemen kon worden uitgevoerd.
			
	03. Verificatie van de taak:
	
		Python in de terminal:
		
			Na het uitvoeren van het script timedate.py met het commando python3.8 timedate.py werd de juiste output verkregen, de huidige datum en tijd.
			Na het installeren van de vereiste modules ('geopy' en 'folium') en het opnieuw uitvoeren van het script geopy-geocoders_location.py met het commando python3.8 geopy-geocoders_location.py, werd de verwachte locatie-informatie getoont.
			Het script location.py werd ook succesvol uitgevoerd met het commando python3.8 location.py en de verwachte locatie-informatie werd getoont.
		
		Visual Studio Code in de terminal:
		
			Het script timedate.py werd succesvol uitgevoerd met het commando python3.8 timedate.py en de juiste output werd verkregen, de huidige datum en tijd.
			Het script geopy-geocoders_location.py werd uitgevoerd met het commando python3.8 geopy-geocoders_location.py en de verwachte locatie-informatie werd getoont.
			Het script location.py werd ook succesvol uitgevoerd met het commando python3.8 location.py en de verwachte locatie-informatie werd getoont.
		
		Jupyter Notebook in Terminal & Web Browser:
		
			Na het uitvoeren van het script timedate.py met werd de juiste output verkregen, de huidige datum en tijd.
			Het script geopy-geocoders_location.py werd succesvol uitgevoerd met het commando %run geopy-geocoders_location.py en de verwachte locatie-informatie werd getoont.
			Het script location.py werd ook succesvol uitgevoerd met het commando %run location.py en de verwachte locatie-informatie werd getoont.
		
		Python IDLE in Terminal:
		
			Nadat het script timedate.py werd geopend en uitgevoerd in Python IDLE, werd de juiste output verkregen, de huidige datum en tijd.
			Het script geopy-geocoders_location.py werd geopend en uitgevoerd, en de verwachte locatie-informatie werd getoont.
			Het script location.py werd ook geopend en uitgevoerd, en de verwachte locatie-informatie werd getoont.
			
1.3 Install different tools/packages on Windows OS

	01. Voorbereiding en uitvoering van de taak:

		Downloaden en installeren van Python 3.8

			Downloaden van Python 3.8 van de officiële Python-website (python.org).
			Na het downloaden werd het installatieprogramma uitgevoerd en de instructies gevolgd om Python te installeren. 
			Python werd tijdens de installatie aan het PATH toegevoegd.
		
		Downloaden en installeren van Visual Studio Code

			Downloaden van Visual Studio Code via de officiele website (code.visualstudio.com).
			Na het downloaden werd het installatieprogramma uitgevoerd en de instructies gevolgd om Visual Studio Code te installeren.

		Pip-pakketten installeren

			Via de terminal werden de Pip-pakketten geinstalleerd door de volgende commandos in te geven:
			
				pip install requests
				pip install geopy
				pip install folium
		
		Jupyter installeren

			Via de terminal werden jupyter geinstalleerd door de volgende commandos in te geven:

				pip install jupyter
				
		Build Tools for Visual Studio 2022 installeren

			Downloaden van de Build Tools for Visual Studio 2022 van de officiële Microsoft-website.
			Na het downloaden werd het installatieprogramma uitgevoerd en de instructies gevolgd om Visual C++ Build Tools te installeren.

	02. Probleemoplossing van de taak:
		
		"Microsoft Visual C++ 14.0 or greater is required" bij het installeren van Jupyter via pip3.

			Downloaden en installeren van de Build Tools for Visual Studio 2022. Dit zorgt ervoor dat de benodigde C++-compiler aanwezig is.
			Het commando pip3 install jupyter is daarna opnieuw uitgevoerd om Jupyter te installeren.

		Foutmelding "pip3: command not found" na het installeren van pip-23.0.1.

			Het commando python -m pip install --upgrade pip is uitgevoerd om pip bij te werken.
			Daarna is het commando pip3 install jupyter opnieuw uitgevoerd om Jupyter te installeren.
			
	03. Verificatie van de taak:
	
			Het commando python --version is uitgevoerd en de installatie bevestigd door de verwachte output te ontvangen.
			Het commando pip --version is uitgevoerd en geverifieerd dat pip correct was geïnstalleerd.
			Python's IDLE gestart door het commando python -m idlelib uit te voeren en het startte zonder problemen.
			Het commando jupyter notebook is uitgevoerd om te verifieren dat Jupyter Notebook zonder problemen start.
			Het script "location.py" getest.
			Het commando python location.py uitgevoerd en de verwachte output ontvangen.
			Python's IDLE geopend door het commando python -m idlelib uit te voeren.
			Visual Studio Code gestart en de werking geverifieerd.
		
1.4 Install different tools/packages on Ubuntu 22.04.01 LTS
		
	01. Voorbereiding en uitvoering van de taak:

		Downloaden ISO:

			Downloaden van de Ubuntu ISO via de officiële website.
			Installatie van een Ubuntu VM.

		Python:

			Om Python 3.8 te installeren, heb ik de volgende commandos uitgevoerd in de terminal:
			'sudo apt install software-properties-common' om de vereiste software-properties-common te installeren.
			'sudo add-apt-repository ppa:deadsnakes/ppa' om de PPA (Personal Package Archive) voor Python 3.8 toe te voegen.
			'sudo apt update' om de pakketinformatie bij te werken.
			'sudo apt install python3.8' om Python 3.8 te installeren.
			
			Voor het installeren van PIP voor Python 3.8 heb ik het commando 'sudo apt install python3-pip' uitgevoerd.
		
			Om de pakketten 'geopy' en 'folium' te installeren, heb ik de volgende commando's uitgevoerd:
			'sudo pip install geopy'
			'sudo pip install folium'

		Visual Studio Code:
		
			'sudo apt install software-properties-common apt-transport-https wget' om de benodigde pakketten te installeren.
			'wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -' om de Microsoft GPG-sleutel toe te voegen.
			'sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"' om de Visual Studio Code-repo toe te voegen.
			'sudo apt update' om de pakketinformatie bij te werken.
			'sudo apt install code' om Visual Studio Code te installeren.
		
		Jupyter Notebook:

			Om Jupyter Notebook te installeren, heb ik het 'sudo apt install jupyter-notebook' commando uitgevoerd in terminal
			
		Python IDLE:
		
			Om Python IDLE te installeren, heb ik het commando 'sudo apt install idle' uitgevoerd
			
	02. Probleemoplossing van de taak:
	
		"Package 'python3.8' has no installation candidate"
		
			Installatie van de benodigde software-properties-common met het commando 'sudo apt install software-properties-common'.
			Toevoegen van de PPA (Personal Package Archive) voor Python 3.8 toe met het commando 'sudo add-apt-repository ppa:deadsnakes/ppa'.
			Bijwerken paketten met het commando 'sudo apt update'.
			TInstallatie van Python 3.8 met het commando 'sudo apt install python3.8'.
		
		"idle-python3.8: command not found"
		
			Installatie van idle-python3.8 met het commando 'sudo apt install idle-python3.8'.
			
	03. Verificatie van de taak:
	
		Uitvoeren van het commando 'python3.8 --version' in de terminal om te verifieren dat het correct geïnstalleerd is.
		Uitvoeren van het commando 'sudo apt install python3-pip' in de terminal om te verifieren dat het correct geïnstalleerd is.
		Uitvoeren van het commando'pip3 show geopy' om informatie over het 'geopy'-pakket weer te geven.
		Uitvoeren van het commando'pip3 show folium' om informatie over het 'folium'-pakket weer te geven.
		Uitvoeren van het commando 'code' uit in de terminal om te controleren of Visual Studio Code correct werd gestart.
		Uitvoeren van het commando 'jupyter-notebook' in de terminal om te verifieren dat het correct geïnstalleerd is. Jupyter Notebook werd gestart en geopend in de webbrowser.
		Uitvoeren van het commando 'idle-python3.8' uit om te controleren of het correct werd gestart.