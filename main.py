from Client import *
import asyncio
import os

user: str = '19020@alumchat.fun'
password: str = '12341234'
def clear_console():
  os.system('cls' if os.name=='nt' else 'clear')

def data_setting():
  global user
  user = input('''
  Enter your email (user@alumchat.fun) 
  ''')
  global password
  password = input('''
  Enter your password 
  ''')

clear_console()
while True:
  if user != '' and password != '':
    option = input('''
    -------------------
    CHOOSE YOUR OPTION
    1. CREATE ACCOUNT
    2. LOG IN
    3. LOG OUT
    4. DELETE ACCOUNT
    5. SHOW USER LIST
    6. ADD CONTACT
    7. CONTACT DETAILS
    8. OPEN CHAT
    9. GROUP CHAT
    10. PRESSENCE MESSAGE
    11. NOTIFICATION SETTINGS
    12. FILE SENDING AND RECEIVING
    13. EXIT
    -------------------------
    ''')
    if option == '1':
      data_setting()
      client = Client(user=user, password=password)
      registered = client.signUp(user, password)
      client.disconnect()
      if registered == 1:
        print('ACCOUNT CREATED PROCEED TO LOGIN')
      else:
        print('FAILED REGISTRATION')
    elif option == '2':
      data_setting()
      print('LOG IN SUCCESSFUL')
    elif option == '3':
      client = SLIXClient(user, password, 0)
      client.disconnect()
      print('LOG OUT SUCCESSFUL')
      user = ''
      password = ''      
    elif option == '4':
      client = SLIXClient(user, password, 4)
      client.connect()
      client.process(forever=False)
    elif option == '5':
      client = SLIXClient(user, password, 5)
      client.connect()
      client.process(forever=False)
    elif option == '6':
      contact = input('WHICH CONTACT WOULD YOU LIKE TO ADD? ')
      client = SLIXClient(user, password, 6, contact=contact)
      client.connect()
      client.process(forever=False)
    elif option == '7':
      contact = input('WHICH USER WOULD YOU LIKE TO SEE? ')
      client = SLIXClient(user, password, 7, contact=contact)
      client.connect()
      client.process(forever=False)
    elif option == '8':
      contact = input('WHICH USER WOULD YOU LIKE TO TALK TO? ')
      client = SLIXClient(user, password, 8, contact=contact)
      client.connect()
      client.process(forever=False)
    elif option == '9':
      pass
    elif option == '10':
      newStatus = input('ENTER ')
      client = SLIXClient(user, password, 10, contact=newStatus)
      client.connect()
      client.process(forever=False)
    elif option == '11':
      pass
    elif option == '12':
      pass

    elif option == '13':
      print('THANKS... BYE')
      quit()

  else:
    option = input('''
    -------------------
    CHOOSE YOUR OPTION
    1. CREATE ACCOUNT
    2. LOG IN
    3. EXIT
    -------------------------
    ''')
    if option == '1':
      data_setting()
      client = Client(user=user, password=password)
      registered = client.signUp(user, password)
      client.disconnect()
      if registered == 1:
        print('ACCOUNT CREATED PROCEED TO LOGIN')
      else:
        user = ''
        password = ''
        print('FAILED REGISTRATION')
    elif option == '2':
      data_setting()
      print('LOG IN SUCCESSFUL')
    elif option == '3':
      print('THANKS... BYE')
      quit()

