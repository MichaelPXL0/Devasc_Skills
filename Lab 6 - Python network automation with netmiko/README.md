Lab 6 - Python network automation with netmiko

01. Voorbereiding en uitvoering van de taak:

	Voorbereiding:

		Netmiko-plugin installeren in Visual Studio Code: 

			Om Netmiko in Visual Studio Code te kunnen gebruiken, moet de Netmiko-plugin worden geïnstalleerd. Dit kan gedaan worden door de extensies te doorzoeken en de Netmiko-plugin te installeren.

		Downloaden en importeren van Netmiko-bibliotheken: 
		
			Netmiko-bibliotheken moeten gedownload en geïmporteerd worden in het Python-script om te kunnen communiceren met de netwerkapparatuur. De bibliotheken kunnen gedownload worden van de Python Package Index (PyPI) of via de terminal met behulp van pip-installatiecommando's. Eenmaal geïnstalleerd, kunnen de bibliotheken geïmporteerd worden in het script met behulp van de import-instructie.

		Opbouwen van het script:
		
			Voorbereiding van het script door een functie te programmeren wat de SSH verbinding opzet voor iedere module die gebruikte gaat worden in het script.

	Uitvoering:

		Verbinding maken met één iOS-apparaat:
		
			a. De "connect" module: Deze module maakt verbinding met een enkel iOS-apparaat door gebruik te maken van de Netmiko-bibliotheek. De module maakt een SSH-verbinding met het apparaat en slaat de verbinding op in een sessie-object.
			b. De "show" module: Deze module verzendt een show-commando naar het apparaat door gebruik te maken van het sessie-object dat in de vorige stap is gemaakt. De module toont de output van het commando op het scherm.
			c. De "configure" module: Deze module stuurt een configuratie-commando naar het apparaat door gebruik te maken van het sessie-object. Het bevestigt ook de uitvoering van het commando door de bevestiging op het scherm weer te geven.

		Ondersteuning voor meerdere iOS-apparaten:
		
			a. De "connect" module: Deze module is aangepast om verbinding te maken met meerdere apparaten. Het maakt SSH-verbindingen met elk apparaat en slaat de verbindingen op in afzonderlijke sessie-objecten.
			b. De "show" module: Deze module is aangepast om show-commando's naar meerdere apparaten te verzenden door gebruik te maken van de sessie-objecten. Het toont de output van de commando's voor elk apparaat op het scherm.
			c. De "configure" module: Deze module is aangepast om configuratie-commando's naar meerdere apparaten te sturen met behulp van de sessie-objecten. Het toont de bevestiging van de uitvoering van de commando's voor elk apparaat op het scherm.
			d. De "save" module: Deze module slaat de output van de show-commando's op voor elk apparaat in een bestand.
			e. De "backup" module: Deze module maakt een backup van de configuratie van elk apparaat en slaat deze op in een bestand.
			f. De "subset" module: Deze module configureert een subset van de interfaces van een apparaat.
			g. De "external" module: Deze module stuurt configuratie-commando's naar meerdere apparaten door gebruik te maken van een extern configuratiebestand.	
			
02. Probleemoplossing van de taak:

		Tijdens het testen van het script zijn verschillende problemen naar voren gekomen, zoals onjuiste functies en commando's die niet beschikbaar waren in de Netmiko-bibliotheek. Om deze problemen op te lossen, zijn de volgende stappen ondernomen:

			Foutieve functies corrigeren: 
			
				Bij het testen van de verschillende modules waren er enkele functies die niet correct werkten. Om deze problemen op te lossen, werden ze aangepast tot ze werkten. Dit doot het controleren van de documentatie van de Netmiko-bibliotheek en het raadplegen van Google.
			
			Ontbrekende commando's in de Netmiko-bibliotheek: 
			
				Tijdens het uitvoeren van de show- en configure-modules waren er enkele commando's die niet beschikbaar waren in de Netmiko-bibliotheek. Ook hier werd er onderzoek gedaan via Google om andere manieren te vinden om de commando's uit te voeren.
			
03. Verificatie van de taak:
	
		Verbinding maken met één iOS-apparaat:

			Het script werd uitgevoerd en er werd gecontroleerd of de "connect" module succesvol verbinding maakte met het iOS-apparaat zonder foutmeldingen.
			De "show" module werd getest door verschillende show-commando's naar het apparaat te sturen en te controleren of de juiste output correct op het scherm werd weergegeven.
			De "configure" module werd getest door configuratie-commando's naar het apparaat te sturen en te controleren of de bevestiging van de uitvoering van het commando correct op het scherm verscheen.
		
		Ondersteuning voor meerdere iOS-apparaten:

			Het script werd uitgevoerd en er werd gecontroleerd of de "connect" module succesvol verbinding maakte met de meerdere iOS-apparaten zonder foutmeldingen.
			De "show" module werd getest door verschillende show-commando's naar de meerdere apparaten te sturen en te controleren of de juiste output voor elk apparaat correct op het scherm verscheen.
			De "configure" module werd getest door configuratie-commando's naar de meerdere apparaten te sturen en te controleren of de bevestiging van de uitvoering van de commando's voor elk apparaat correct op het scherm verscheen.
			De "save" module werd getest door de output van de show-commando's voor elk apparaat op te slaan in een bestand en te controleren of de bestanden correct werden gegenereerd met de verwachte inhoud.
			De "backup" module werd getest door een backup van de configuratie van elk apparaat te maken en te controleren of de backup-bestanden correct werden gegenereerd met de juiste configuratie-informatie.
			De "subset" module werd getest door een subset van de interfaces van een apparaat te configureren en te controleren of alleen de gewenste interfaces werden aangepast.
			De "external" module werd getest door configuratie-commando's naar meerdere apparaten te sturen met behulp van een extern configuratiebestand en te controleren of de commando's correct werden uitgevoerd op de apparaten.


Lab 6 - Python network automation with netmiko - Challenge Script
			
01. Voorbereiding en uitvoering van de taak:

	Voorbereiding:
	
		Opbouwen van het script:
		
			Voorbereiding van het script door een functie te programmeren wat de SSH verbinding opzet voor iedere module die gebruikte gaat worden in het script.
			
	Uitvoering:
		
		Programmeren van verschillende onderdelen:
		
			Inloggegevens en doelapparaat opvragen:

				De gebruiker is gevraagd om inloggegevens (zoals gebruikersnaam en wachtwoord) en het IP-adres van het doelapparaat op te geven.
				
			Verbinding maken met het apparaat:

				De Netmiko-bibliotheek is gebruikt om een SSH-verbinding tot stand te brengen met het doelapparaat, met behulp van de opgegeven inloggegevens en het IP-adres.
				Als er problemen optreden bij het maken van de verbinding, is een foutmelding weergegeven en is het script beëindigd.
				
			Uitvoeren van show-opdrachten:

				De gebruiker kan één of meerdere show-opdrachten opgeven die moeten worden uitgevoerd.
				Voor elke opgegeven show-opdracht is de opdracht naar het apparaat verzonden en is de uitvoer ervan opgehaald.
				De uitvoer is getoond op het scherm.
				
			Uitvoeren van configuratie-opdrachten:

				De gebruiker kan één of meerdere configuratie-opdrachten opgeven die moeten worden uitgevoerd.
				Voor elke opgegeven configuratie-opdracht is de opdracht naar het apparaat verzonden en is de uitvoer ervan opgehaald.
				De uitvoer is getoond op het scherm.
				
			Verzenden van opdrachten naar meerdere apparaten:

				De gebruiker kan een lijst met doelapparaten opgeven, elk met hun eigen inloggegevens en IP-adres.
				Voor elk doelapparaat is er een aparte verbinding tot stand gebracht en worden de opgegeven show- en configuratie-opdrachten uitgevoerd.
				De uitvoer van elke opdracht voor elk apparaat is opgeslagen in een bestand.
				
			Configuratieback-up maken:

				De gebruiker kan aangeven of er een configuratieback-up moet worden gemaakt van het doelapparaat.
				Als er een back-up is aangevraagd, is de huidige configuratie van het apparaat opgehaald en opgeslagen in een bestand met behulp van een bestandsnaamconventie met het IP-adres en de huidige datum en tijd.
				
			Configuratie van een subset van interfaces:

				De gebruiker kan een lijst met interfaceconfiguraties opgeven die moeten worden toegepast op het doelapparaat.
				Voor elke opgegeven interfaceconfiguratie is de configuratie naar het apparaat verzonden en is de uitvoer ervan opgehaald.
				De uitvoer is getoond op het scherm.

02. Probleemoplossing van de taak:

		Verbindingsproblemen:

			Bij het maken van de SSH-verbinding met de netwerkapparaten waren er enkele problemen met time-outs en SSH-fouten.
			Om deze problemen op te lossen heb ik het fysieke netwerk opnieuw moeten troubleshooten, dit is op heden nog niet opgelost.
			HEt netwerk lijkt om de 15 minuten zijn verbinding te verbreken waardoor er niet meer gepingt kan worden en de SSH verbinding dus ook neit meer tot stand kan worden gebracht.
		
		Invoerfouten:

			Tijdens het schrijven en testen van het script waren er enkele problemen met ongeldige opdrachten of ontbrekende informatie.
			Foutmeldingen en instructies worden weergegeven om te begeleiden bij het correct invoeren van gegevens.
		
		Outputbeheer:

			Een ander probleem dat zich voordeed, was het beheren van de output van show-opdrachten en configuratie-opdrachten. Dit was niet overzichtelijk.
			Om dit probleem aan te pakken, is de uitvoer van elke opdracht opgeslagen en weergegeven op het scherm.
			De output van opdrachten naar meerdere apparaten is ook opgeslagen in afzonderlijke bestanden om het overzicht te behouden en gemakkelijk te kunnen analyseren.
		
03. Verificatie van de taak:

		Testen van individuele functies:

			Elke afzonderlijke functie die in het script is geïmplementeerd, is grondig getest om ervoor te zorgen dat deze correct werkt.
			Voor elke functie zijn verschillende testgevallen gemaakt, waarbij verschillende scenario's zijn getest.

		Integratietests:

			Nadat elke individuele functie met succes was getest, zijn er testen uitgevoerd om de samenwerking tussen de verschillende functies te verifiëren.
			Hierbij zijn verschillende gebruikersscenario's nagebootst om te controleren of het script correct reageert.

		Foutafhandeling en uitzonderingstests:

			Er zijn testen uitgevoerd om de foutafhandeling van het script te controleren in verschilene scenarios.