#in the name of god | Coded By SardarCyberym | Yarnovin | GitHub.com/SardarCybery
from Leacher import Leacher
from colorama import Fore
from re import match
from os import system,name
system('clear' if name == 'posix' else 'cls')

def GiveUserName(): #Get Username
    global Username
    Username = input(Fore.GREEN + "Username : ")
    CheckUsername = match(r"^(?!.*\.\.)(?!.*\.$)[^\W][\w.]{0,29}$",Username)
    if CheckUsername:
        GivePassword()
    else:
        print(Fore.RED + "Incorrect Value")
        GiveUserName()

def GivePassword(): #Get Password
    global Password
    Password = input(Fore.GREEN + "Password : ")
    if int(len(Password)) < 8 :
        print(Fore.RED + "Incorrect Value")
        GivePassword()
    else:
        GiveTarget()

def GiveTarget(): #Get Target
    global Target
    Target = input(Fore.GREEN + "Target Username : ")
    CheckTarget = match(r"^(?!.*\.\.)(?!.*\.$)[^\W][\w.]{0,29}$",Target)
    if CheckTarget:
        FollowerOrFollowing()  
    else:
        print(Fore.RED + "Incorrect Value")
        GiveTarget()

def FollowerOrFollowing():
    Selection = input("Follower Or Following : ")
    if Selection == "follower":
        Leacher(Username,Password,Target).FollowersLeacher()
    elif Selection.lower == "following":
        Leacher(Username,Password,Target).Followingleacher()
    else:
        print(Fore.RED + "Incorrect Value")
        FollowerOrFollowing()

if __name__ == '__main__' :
    print(f"""
{Fore.LIGHTBLUE_EX}Telegram : {Fore.LIGHTGREEN_EX}t.me/Mr_Nazism
{Fore.LIGHTCYAN_EX }Github : {Fore.LIGHTYELLOW_EX}Github.com/SardarCybery
{Fore.LIGHTRED_EX}WebSite : {Fore.LIGHTMAGENTA_EX}YarNovin.ir
    """)
    GiveUserName()
