from cryptography.fernet import Fernet #Cryptography module is needed to be installed for this program

def write_key(): #creates a key file after the master password is given
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)
        
def load_key():
    file =  open("key.key","rb").read()
    key = file.read()
    file.close()
    return key


key = load_key() 
fer = Fernet(key)
write_key()



def view():
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ",user, "Password: ",
                  fer.decrypt(passw.encode()).decode())
            


def add():
    name = input('Account name: ')
    password = input("Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n" )



while True:
    option = input("Would you like to add a new password or view existing passwords?(type 'view', 'add' or 'quit' to exit ").lower()
    if option == "quit":
        break
    if option == "view":
        view()
    elif option == "add":
        add()
    else:
        print("Invalid option.")
        continue
