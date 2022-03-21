from file import handler
'''Creating a modular Login class that can be implemented in numerous softwares
can be passed the file name as an argument while initializing.
can create accounts in given format
can grant or deny access on the basis of login credentials'''
class Login:
    def __init__(self,file):
        self.file = '{}.bin'.format(file)

    def begin(self):
        handler.writer({},self.file)
    
    def greet(self
    ,cr_ps = 'The password is too short',
    cr_pnm = 'The entered passwords don\'t match',
    log_acc = 'Account doesn\'t exist',
    log_ip = 'Incorrect Password'):
        self.cr_ps = cr_ps 
        # password too short
        self.cr_pnm = cr_pnm
         #password doesn't  match
        self.log_acc = log_acc 
        # account doesn't exist
        self.log_ip = log_ip
        # password is incorrect
        
    def create(self,login,pass1):
        pass2 = input('Confirm Password')
        if pass1 == pass2 and len(pass2) >= 8:
            records = handler.reader(self.file)
            records[login] = pass1
            handler.writer(records,self.file)
            return (True,)  # signals successful creation of the account
        else:
            if pass1 != pass2:
                return (False,self.cr_pnm)
            else:
                return (False,self.cr_ps)

    def login(self,login):
        """Login function
            checks if the passed in value of the login exists.
            If the account exists then checks if the argument password matches the preset password.
            If it does --> returns True
            If the account doesn't exist then returns --> (False,"Incorrect password.")If the password is incorrect then returns --> (False,"Account doesn't exist.")
            """
        
        records = handler.reader(self.file)
        if login in records:
            pass1 = input("Enter password here")
            if records[login] == pass1:
                return (True,)  # returning in the form of tuple with single element to maintain uniformity.
            else:
                return (False,self.log_ip)
        else:
            return (False,self.log_acc)
                   
            
        
