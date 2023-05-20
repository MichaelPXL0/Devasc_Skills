LAB 4 - Network Infrastructure and troubleshooting

01. Voorbereiding en uitvoering van de taak:

Voorbereiding:

	Opstellen van een netwerkschema waarin de IP's worden vastgelegd.
	Opstellen van de fysieke topology in Packet Tracer.
	Verbinden van de apparaten in pakket tracer volgens de netwerktopologie.
	
	Configuratie SW1:

		Activeren van de configuratiemodus op de switch met het commando "enable" en "configure terminal".
		Configuratie van de hostname van de switch met het commando "hostname SW1".
		Aanmaken van de gebruiker "Michael" aan met het wachtwoord "pxl" met de commando's "username Michael password pxl".
		Instellen van het enable secret wachtwoord in op "pxl" met het commando "enable secret pxl".
		Configuratie van het domein "pxl.be" met het commando "ip domain-name pxl.be".
		Genereren van een RSA-sleutel met een modulus van 2048 bits met het commando "crypto key generate rsa modulus 2048".
		Instellen van de SSH-versie op 2 met het commando "ip ssh version 2".
		Configuratie van de VTY-lijnen met het commando "line vty 0 4".
		Toestaan van SSH met het commando "transport input ssh".
		Instellen dat alleen lokale gebruikers kunnen inloggen met het commando "login local".
		Genereren van een RSA-sleutelpaar voor het domein "SW1.pxl.be" met het commando "ip ssh rsa keypair SW1.pxl.be".
		Configuratie van de GigabitEthernet0/1-interface als een trunk-poort die verkeer toestaat van VLAN's 1, 10 en 40 met het commando "interface GigabitEthernet0/1", "switchport mode trunk" en "switchport trunk allowed vlan 1,10,40".
		Aanmaken van het VLAN 10 genaamd "Management" met het commando "vlan 10" en configureer de interface van dit VLAN met een IP-adres van 172.16.4.6 en een subnetmasker van 255.255.255.240 met het commando "interface Vlan10", "ip address 172.16.4.6 255.255.255.240" en "ip default-gateway 172.16.4.2".
		Aanmaken van het VLAN 40 met het commando "vlan 40".
		Configuratie van de FastEthernet0/1 en FastEthernet0/2-interfaces als toegangspoorten die alleen verkeer toestaan van VLAN 40 met het commando "interface range FastEthernet0/1 - 2", "switchport mode access" en "switchport access vlan 40".
		Afsluiten van de configuratie met het commando "end".
		Kopieren van de configuratie naar een TFTP-server op IP-adres 10.199.64.134 met de bestandsnaam "Sw1_cfg_michael" met het commando "copy running-config tftp".
		Voorzien van een minimale configuratie om de configuratie terug op te laden van de tftp server.
		
	Configuratie R1:
	
		Activeren van de configuratiemodus op de router met het commando "enable" en "configure terminal".
		Configuratie van de hostname van de router met het commando "hostname R1".
		Aanmaken van de gebruiker "Michael" met het wachtwoord "pxl" met de commando's "username Michael password pxl".
		Instellen van het enable secret wachtwoord in op "pxl" met het commando "enable secret pxl".
		Configuratie van het domein "pxl.be" met het commando "ip domain-name pxl.be".
		Genereren van een RSA-sleutel met een modulus van 2048 bits met het commando "crypto key generate rsa modulus 2048".
		Instellen van de SSH-versie in op 2 met het commando "ip ssh version 2".
		Configuratie van de VTY-lijnen met het commando "line vty 0 4".
		Toestaan van SSH met het commando "transport input ssh".
		Instellen dat alleen lokale gebruikers kunnen inloggen met het commando "login local".
		Genereren van een RSA-sleutelpaar voor het domein "R1.pxl.be" met het commando "ip ssh rsa keypair R1.pxl.be".
		Configuratie van de GigabitEthernet0/1-interface met het commando "interface GigabitEthernet0/1".
		Activeren van de interface met het commando "no shutdown".
		Configuratie van de subinterfaces GigabitEthernet0/1.10 en GigabitEthernet0/1.40 voor respectievelijk VLAN 10 en VLAN 40 met het commando "interface GigabitEthernet0/1.10" en "interface GigabitEthernet0/1.40".
		Configuratie van de encapsulatie voor de subinterfaces met de commandos "encapsulation dot1Q 10" en "encapsulation dot1Q 40".
		Toewijzen van IP-adressen en subnetmaskers aan de subinterfaces met de commandos "ip address 172.16.4.2 255.255.255.240" en "ip address 172.16.4.49 255.255.255.240".
		Activeren van de subinterfaces met het commando "no shutdown".
		Configuratie van de GigabitEthernet0/0-interface met het commando "interface GigabitEthernet0/0".
		Toewijzen van een IP-adres en subnetmasker aan de interface met het commando "ip address 10.199.66.104 255.255.255.224".
		Activeren van de interface met het commando "no shutdown".
		Configuratie van het OSPF-routerprotocol met het commando "router ospf 1".
		Toevoegen van de netwerkadressen en subnetmaskers aan het OSPF-proces met de commandos: 
		  network 172.16.4.0 0.0.0.15 area 0
		  network 172.16.4.16 0.0.0.15 area 0
		  network 172.16.4.48 0.0.0.15 area 0
		  network 172.16.4.64 0.0.0.15 area 0
		  network 10.199.66.96 0.0.0.31 area 0
		Afsluiten van de configuratie af met het commando "end".
		Kopieren van de configuratie naar een TFTP-server op IP-adres 10.199.64.134 met de bestandsnaam "R1_cfg_michael" met het commando "copy running-config tftp".
		Voorzien van een minimale configuratie om de configuratie terug op te laden van de tftp server.		
		
02. Probleemoplossing van de taak:

		Onjuiste IP-adressen in de netwerk-topologie
		
			Er waren verkeerde IP adressen vastgelegd waardoor de configuratie niet klopte. De IP-adressen en subnetmaskers zijn aangepast in zowel de topology als op de apparaten zelf.

		Ontbrekende VLAN's op de trunk: 
		
			De switch had niet alle benodigde VLAN's geconfigureerd om over de trunk-poort te worden verzonden. Hierdoor konden de apparaten in verschillende VLAN's geen connectiviteit tot stand brengen.
			De switchconfiguratie is bijgewerkt om ervoor te zorgen dat alle vereiste VLAN's over de trunk-poort worden verzonden.

		SSH-verbinding niet geconfigureerd op versie 2: 
		
			De SSH-verbinding was niet geconfigureerd om versie 2 te gebruiken, wat een veiligere vorm van communicatie is. Hierdoor kreeg ik geen succesvolle SSH-verbinding.
			De SSH-configuratie is aangepast om SSH-versie 2 te gebruiken.

		Door deze configuraties toe te passen konden de apparaten correct met elkaar communiceren en kon ik mijn configuratie doorsturen naar de tftp server.
			
03. Verificatie van de taak:
	
		Verificatie van de fysieke verbindingen: 
		
			Er is gecontroleerd of alle apparaten correct zijn aangesloten door visuele inspectie van switch en router.

		Verificatie van IP-configuratie: 
		
			Er is gecontroleerd of de IP-configuratie van elk apparaat klopt. Dit door de IP-instellingen op elk apparaat te controleren en te vergelijken met de voorbereide topology.

		Verificatie van VLAN-configuratie: 
		
			Er is gecontroleerd of de VLAN-configuratie op de switch klopt door de configuratie op de switch te bekijken.

		Verificatie van OSPF-configuratie: 
		
			Er is gecontroleerd of de OSPF-configuratie op de router klopt door de OSPF-configuratie op de router te bekijken en te controleren of de juiste netwerken zijn geconfigureerd.

		Verificatie van SSH-configuratie: 
		
			Er is gecontroleerd of de SSH-configuratie op zowel de switch als de router om ervoor te zorgen dat de juiste versie en sleutels zijn geconfigureerd.

		Verificatie van connectiviteit: 
		
			Er is getest of de connectiviteit tussen de apparaten door ping-opdrachten uit te voeren vanaf de ene host naar de andere.