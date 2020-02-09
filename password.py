import random
import string
from os import system, name
from time import sleep

def screen_clear():
   if name == 'nt':
      _ = system('cls')

def randomString(stringLength=32):
    """Generate a random string of fixed length """
    letters = string.ascii_uppercase + string.octdigits
    return ''.join(random.choice(letters) for i in range(stringLength))

ans=True
while ans:
    print ("""
    1. Username
    2. Password (16)
    3. Password (32)
    4. Password (48)
    5. Accounts (User:Pass)
    6. Exit
    """)
    ans=input("Please select an option: ") 
    if ans=="1": 
      screen_clear()
      print ("Username:", randomString(15) ) 
    elif ans=="2":
      screen_clear()
      print ("Password (16):", randomString(16) )
    elif ans=="3":
      screen_clear()
      print ("Password (32):", randomString(32) ) 
    elif ans=="4":
      screen_clear()
      print ("Password (48):", randomString(48) ) 
    elif ans=="5":
      print ("Accounts:") 
      print ("Username: ", randomString(16) )
      print ("Password:", randomString(20) )
    elif ans=="6":
      print ("Exiting")
      exit()
    elif ans !="":
      screen_clear()
      print("\n Invalid choice. ") 
