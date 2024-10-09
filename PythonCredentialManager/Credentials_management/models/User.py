
class User:
   def __init__(self , username, password, name, email, numberphone):

     if username == "":
        print("[ Name can't be empty ]")
     else:
        self.__username = username
     
     if len(password) <8 or password == "":
        print("[ Password can't be empty and it must be more or equal to 8 characters ]")
     else:
        self.__password = password

     if name == "":
        print("[ Name can't be empty ]")
     else:
        self.__name = name

     if email == "":
        print("[ Email can't be empty ]")
     else:
        self.__email = email

     if len(numberphone) < 10 or len(numberphone) > 10:
         print("[ Number phone must be more or equal to 10 numbers ]")
     else:
        self.__numberphone = numberphone

   #Getters

   @property
   def username(self):
      return self.__username
    
   @property
   def password(self):
      return self.__password
    
   @property
   def name(self):
      return self.__name
   
   @property 
   def email(self):
      return self.__email
   
   @property
   def numberphone(self):
      return self.__numberphone
   
   #Setters

   @username.setter
   def username(self, username):
     if username == "":
         print("[ Name can't be empty ]")
     else:
         self.__username = username

   @password.setter
   def password(self, password):
     if len(password)<8:
         print("[ Password can't be empty and it must be more or equal to 8 characters ]")
     else:
        self.__password = password

   @email.setter
   def email(self, email):
     if email == "":
         print("[ Email can't be empty ]")
     else:
        self.__email = email

   @numberphone.setter
   def numberphone(self, numberphone):
     if len(numberphone) < 10 or len(numberphone) > 10:
         print("[ Invalid phone number ]")
     else:
         self.__numberphone = numberphone

