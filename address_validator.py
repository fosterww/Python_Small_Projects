def AddressVal(address):
    # Function to validate an address based on the presence of '@' and '.' characters
    dot = address.find('.')
    at = address.find('@')
    if dot == -1 or at == -1:
        print("Invalid address")
    else:
        print("Valid address")
    
print("Enter the address, and the program will check if it is a valid address or not.")
# Main loop to repeatedly ask for an address until the user decides to exit
while True:
    print("A valid address contains an '@' and a '.' character.")
    address = input("Enter the address: ")
    AddressVal(address)
    
    exit = input("Exit the program? (yes/no): ")
    if exit.lower() == 'yes':
        print("Exiting the program...")
        break
    elif exit.lower() == 'no':
        print("Continuing...")
        continue 

