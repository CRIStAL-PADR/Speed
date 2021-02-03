     
                                                    DCC
                                                    =
                                                  

**DCC** ( système de commande numérique ) est un standard utilisé  dans le modélisme ferroviaire pour commander individuellement des locomotives ou des accessoires de voie en modulant 
la tension d’alimentation de la voie

Les locomotives et leurs accessoires ( feux , effets ) ainsi que les accessoires du réseau possèdent chacune une adresse unique. 
Le signal  codé envoyé sur la voie donne des ordes aux équipements tout en fournissant la puissance.

                                                    Principe de fonctionnement
                                                    =
        
Le rôle du standard **DCC** est de générer un signal électrique en binaire pour envoyer  des informations à des locomotives ou des accessoires. 
Une suite de 0 et de 1 qui sont  traduits électriquement par des alternances positives et négatives longues (100us) pour  les 0 et courtes (58us) pour les 1. 
Les terminaux sur le circuit (Locomotives et accessoires ) sont équipés de décodeurs qui vont traduire ces messages  binaires en commandes .
		
                                                    Équipements
                                                    =
- Une centrale de commande constitué de carte électronique et d'une carte moteur dont l'objectif est de moduler la tension de la voie
- Les équipements mobiles (locomotives ) ou fixes (feux éclairages) qui sont dotés de décodeurs permettant d’interpréter les signaux de commande.

                                                    La centrale de commande
                                                    =
        
Elle peut être soit manuelle (ce que Philippe a fait) soit automatisée.
Pour l’automatisation il y a des logiciels de commande disponibles sous linux.
Comme logiciel de commande on pourra utiliser:
 -  **un microcontroleur Atmega 328 /2560**
 -  **un Arduino Uno / Mega**
 -  **RaspberryPI** 

    Il existe des API sur github qui nous permet d'utiliser l'une des cartes si dessus.
    Il est a noté également que l'Arduino et l'Atmega utilisent un logiciel libre DCC++  (https://www.locoduino.org/spip.php?article182) tandisque la raspberryPI utilise 
    un API python (https://github.com/hsanjuan/dccpi) 

			                                       La carte moteur ( le booster)
                                                   =
    Le choix d'utiliser une carte moteur est motivé par le fait que les cartes Arduino ou RaspberryPi ne sont pas capable de fournir assez de puissance
    Or le principe du standart DCC est de faire circuler une information « de commande » dans le circuit de puissance ( les rails) d’où l’importance d’avoir une carte moteur 

	Comme choix de carte moteur nous allons utiliser LMD18200. Cette carte conserve la forme de la tension du signal présent à leur entrée (donc l’information)
et amplifie le signal de sortie. La forme des impulsions sont conservée afin de conservée les codes transmis.

                                                    La RaspberryPI avec l'API _dccpi_
                                                    =
 Elle utilise l'API _dccpi_  qu'on peut installer avec  __pip install dccpi__
Cette API est capable de sortir  la direction et la vitesse des paquets codés DCC sur l’une des broches GPIO


	 
Lien qui peut ếtre utile pour comprendre comment les informations sont décodées
 (http://stephane.ravaut.free.fr/Train_miniature/LE_DCC/Le_DCC_Comment_ca_marche.html)
