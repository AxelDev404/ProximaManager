
class Credentials:
    def __init__(self, password , username , email , product):
        
       if password == "":
            print("[ Password can't be empty]")
       else: 
            self.__password = password

       self.__username = username

       if email == "":
           print("[ Email can't be empty ]")
       else:
           self.__email = email

       if product == "":
           print("[ Product can't be empty]")
       else:
           self.__product = product

    #Getters

    @property
    def password(self):
        return self.__password
    
    @property
    def username(self):
        return self.__username
    
    @property
    def email(self):
        return self.__email
    
    @property
    def product(self):
        return self.__product
    
    #Setters
    
    @password.setter
    def password(self, password):
       if password == "":
            print("[ Password can't be empty ]")
       else:
            self.__password = password
    
    @username.setter
    def username(self, username):
        self.__username = username

    @email.setter
    def email(self, email):
       if email == "":
            print("[ Email can't be empty ]")
       else:
           self.__email - email
    
    @product.setter
    def product(self, product):
       if product == "":
            print("[ Product can't be empty ]")
       else:
            self.__product = product