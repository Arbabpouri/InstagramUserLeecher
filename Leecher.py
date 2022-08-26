#in the name of god | Coded By SardarCyberym | Yarnovin | GitHub.com/SardarCybery
import instaloader
from time import sleep
from colorama import Fore
app = instaloader.Instaloader()
class Leacher:
    def __init__(self,Username:str,Password:str,Target:str) -> None:
        self.Username = Username
        self.Passsord = Password
        self.Target = Target
    def FollowersLeacher(self):
        try:
            app.login(self.Username,self.Passsord)
            print(Fore.LIGHTGREEN_EX + "Login . . .")
            FollowerList = []
            Profile = instaloader.Profile.from_username(app.context,self.Target)
            SleepTime = 0
            AntiBan = 0
            count = 0
            FileFollowers = open("Followers.txt", "a+")
            for Followers in Profile.get_followers():
                print(Followers.username)
                FollowerList.append(Followers.username)  
                FileFollowers.write(f'{FollowerList[count]}\n')
                count += 1
                SleepTime += 1
                AntiBan += 1
                if SleepTime == 100:
                    sleep(30)
                    SleepTime = 0
                if AntiBan == 8000:
                    print(Fore.LIGHTRED_EX + "Sleep 3600 Second(1 Hours) , Do not exit the App")
                    sleep(3600)
                    AntiBan = 0
            FileFollowers.close()
        except Exception as ex:
            print(str(ex))