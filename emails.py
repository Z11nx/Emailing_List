import smtplib
from time import sleep
from rich.progress import track

class registration:

    def __init__(self):
        self.email_list = {}
        pass

    def list_emails(self):
        count = 0
        print('')
        print('Entries added: ')
        for key,value in self.email_list.items():
            if key in self.email_list:
                count += 1
            #for j in i:
            line = f'{key}: {value}'
            print(line)
            #print('', sep='\n')
        print('Total: ' + str(count))
        print('')
        pass

    def add_email(self, email, name):
        key = name
        value = email
        self.email_list[key] = value

    def write_file(self):
        file = open('file.txt', 'w')
        for key,value in self.email_list.items():
            line = f'{key}: {value}'
            file.write(line)
            file.write('\n')
        file.close()
        pass

    def read_file(self):
        file = open('file.txt', 'r')
        contents = file.read()
        print('\n' + contents)
        pass

    def append_file(self):
        file = open('file.txt', 'a')
        for key,value in self.email_list.items():
            line = f'{key}: {value}'
            file.write(line)
            file.write('\n')
        file.close()
        pass

    def send_email(self):
        choice = input('Would you like to see the emails in your list? (Y/n): ')
        choice = choice.lower()
        if choice == 'y':
            file = open('file.txt', 'r')
            contents = file.read()
            print('\n' + contents)
        
        email_address = 'example@gmail.com'
        email_password = 'password'
        recipent_address = input('Enter recipients email: ')
        subject = input('Subject: ')
        body = input('Body: ')

        for step in track(range(10)):
            sleep(.8)
            step
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            #print('\nSending email...')
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            smtp.login(email_address, email_password)

            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(email_address, recipent_address, msg)
            print('Email sent\n')
        pass
        

