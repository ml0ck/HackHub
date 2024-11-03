import os
import sys
from colorama import Fore, Back, Style, init

# Initialiser Colorama
init(autoreset=True)

def print_header():
    header = """
     ▄ .▄ ▄▄▄· ▐▄• ▄  ▄ .▄▄• ▄▌▄▄▄▄· 
    ██▪▐█▐█ ▀█  █▌█▌▪██▪▐██▪██▌▐█ ▀█▪
    ██▀▐█▄█▀▀█  ·██· ██▀▐██▌▐█▌▐█▀▀█▄
    ██▌▐▀▐█ ▪▐▌▪▐█·█▌██▌▐▀▐█▄█▌██▄▪▐█
    ▀▀▀ · ▀  ▀ •▀▀ ▀▀▀▀▀ · ▀▀▀ ·▀▀▀▀ 
    """
    # Afficher l'en-tête en dégradé
    for i, line in enumerate(header.splitlines()):
        if line.strip():  # Ignore les lignes vides
            color = Fore.RED if i % 4 == 0 else Fore.GREEN if i % 4 == 1 else Fore.BLUE if i % 4 == 2 else Fore.YELLOW
            print(color + line)

def display_menu():
    print(Fore.CYAN + "\nMenu HackHub")
    print(Fore.MAGENTA + "Choisissez un site :")
    print(Fore.WHITE + "1. HackForums")
    print(Fore.WHITE + "2. Null Byte")
    print(Fore.WHITE + "3. Reddit - r/hacking")
    print(Fore.WHITE + "4. Offensive Security")
    print(Fore.WHITE + "5. Dark Reading")
    print(Fore.WHITE + "6. Krebs on Security")
    print(Fore.WHITE + "7. BleepingComputer")
    print(Fore.WHITE + "8. Security Focus")
    print(Fore.WHITE + "9. Threatpost")
    print(Fore.WHITE + "10. SANS Internet Storm Center")
    print(Fore.WHITE + "11. Black Hat")
    print(Fore.WHITE + "12. Cybrary")
    print(Fore.WHITE + "13. The Hacker News")
    print(Fore.WHITE + "14. InfoSec Write-ups")
    print(Fore.WHITE + "15. OpenSource Security")
    print(Fore.WHITE + "16. OSINT Framework")
    print(Fore.WHITE + "17. Packet Storm")
    print(Fore.WHITE + "18. Exploit Database")
    print(Fore.WHITE + "19. GitHub - Offensive Security")
    print(Fore.WHITE + "20. SecTools")

def get_choice():
    try:
        choice = int(input(Fore.CYAN + "\nEntrez votre choix (1-20) : "))
        if 1 <= choice <= 20:
            return choice
        else:
            print(Fore.RED + "Choix invalide. Veuillez entrer un nombre entre 1 et 20.")
            return get_choice()
    except ValueError:
        print(Fore.RED + "Erreur : Veuillez entrer un nombre valide.")
        return get_choice()

def redirect(choice):
    sites = [
        "https://hackforums.net/",
        "https://null-byte.wonderhowto.com/",
        "https://www.reddit.com/r/hacking/",
        "https://www.offensive-security.com/",
        "https://www.darkreading.com/",
        "https://krebsonsecurity.com/",
        "https://www.bleepingcomputer.com/",
        "https://www.securityfocus.com/",
        "https://threatpost.com/",
        "https://isc.sans.edu/",
        "https://www.blackhat.com/",
        "https://www.cybrary.it/",
        "https://thehackernews.com/",
        "https://medium.com/@InfosecWriteUps",
        "https://www.opensource-security.com/",
        "https://osintframework.com/",
        "https://packetstormsecurity.com/",
        "https://www.exploit-db.com/",
        "https://github.com/offensive-security/",
        "https://sectools.org/"
    ]

    print(Fore.GREEN + f"Vous êtes redirigé vers : {sites[choice - 1]}")
    os.startfile(sites[choice - 1])  # Ouvre le site par défaut dans le navigateur

def main():
    print_header()
    display_menu()
    choice = get_choice()
    redirect(choice)

if __name__ == "__main__":
    main()
