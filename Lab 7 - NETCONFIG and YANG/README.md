Lab 7 - NETCONFIG and YANG

01. Voorbereiding en uitvoering van de taak:

	Voorbereiding:

		Opbouwen van het script:
		
			Voorbereiding van het script door de json en requests modules te importeren. 
			Uitschakelen van de SSL-waarschuwing.

	Uitvoering:

		GET:
		
			a. Maak api_url met de RESTCONF-interface-URL.
			b. Maak headers met Accept en Content-type.
			c. Maak basicauth met gebruikersnaam en wachtwoord.
			d. Gebruik requests.get() met de variabelen voor een GET-verzoek.
			e. Print de responscode met print(resp).
			f. Converteer de JSON-respons naar een Python-dictionary.
			g. Gebruik print(json.dumps(response_json, indent=4)) om de JSON data weer te geven.
			
		PUT:
		
			a. Maak api_url voor het maken van een nieuwe Loopback-interface.
			b. Definieer headers en basicauth.
			c. Maak yangConfig met de juiste YANG gegevens.
			d. Gebruik requests.put() met de variabelen voor een PUT-verzoek.
			e. Controleer de statuscode van de respons.
			f. Geef succes als output als de statuscode binnen de succesvolle codes ligt, geef anders een foutbericht.
			
02. Probleemoplossing van de taak:
		
		Er waren heel veel problemen met het verkrijgen van het juiste IP adressen doordat de DHCP scope zo goed als op was. Uiteindelijk na 2 uur een correct IP gekregen.
		Tijdens het testen van het script zijn verschillende problemen naar voren gekomen, zoals geen juiste output en problemen met ssh. Wegens stijdsgebrek heb ik deze ook niet uitgebreid kunnen troubleshooten.
		Het SSH probleem heb ik kunnen oplossen door SSH uit te schakelen.
			
03. Verificatie van de taak:
	
		Controle dat alle modules zoals json en requests geïmporteerd zijn.
		Controle API-URL.
		Controle gebruikersnaam en wachtwoord.
		Controle van de headers met de juiste waarden Accept en Content-type.
		Controle van SSL. Ik heb ervoor gezorgd dat de juiste certificaten waren geïnstalleerd en dat de config van het script overeenkwam met de CSR1kv-certificaten.
		Testen verzenden van de RESTCONF requests: Ik heb het Python-script uitgevoerd en gecontroleerd of de requests succesvol werden verzonden. 
		Controle van de respons.