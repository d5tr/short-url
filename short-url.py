print('''
 ______   ____
          __               __                   __
   _____/ /_  ____  _____/ /_      __  _______/ /
  / ___/ __ \/ __ \/ ___/ __/_____/ / / / ___/ / 
 (__  ) / / / /_/ / /  / /_/_____/ /_/ / /  / /  
/____/_/ /_/\____/_/   \__/      \__,_/_/  /_/   
 
 
 ___ _________ _____________________ 
(  __  \ (  ____ \\__   __/(  ____ )
| (  \  )| (    \/   ) (   | (    )|
| |   ) || (____     | |   | (____)|
| |   | |(_____ \    | |   |     __)
| |   ) |      ) )   | |   | (\ (   
| (__/  )/\____) )   | |   | ) \ \__
(______/ \______/    )_(   |/   \__/
       # Thanks for use my tool #
 000   11  
0  00 111  
0 0 0  11  
00  0  11  
 000  11l1 
           
''')
import pyshorteners

def Shorten(url):
    link = pyshorteners.Shortener()
    return link.tinyurl.short(url)

if __name__ == "__main__":
    url = input("enter url : ")
    print(f"\n{Shorten(url)}")
