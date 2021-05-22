import os
from emails import registration

data = registration()
def main():
    while(True):
        choice = input('Enter 1 to add a new email, 2 to see list of emails added, 3 to upload to file\nEnter 4 to read file, 5 to send email, 0 to quit: ')
        if choice == '1':
            os.system('cls')
            email = input('Enter an email: ')
            name = input('Enter a name: ')
            data.add_email(email, name)
            pass
        if choice == '2':
            os.system('cls')
            data.list_emails()
        if choice == '3':
            os.system('cls')
            ch = input('Would you like to write or append? (W/a): ')
            ch = ch.upper()
            write_to_file(ch)
            pass
        if choice == '4':
            os.system('cls')
            data.read_file()
            pass
        if choice == '5':
            os.system('cls')
            data.send_email()
            pass
        if choice == '0':
            os.system('cls')
            print('Goodbye!')
            quit()
    pass

def write_to_file(input):
    if input == 'W':
        data.write_file()
        print('File created')
    if input == 'A':
        data.append_file()
        print('Entries have been added')
    pass

main()