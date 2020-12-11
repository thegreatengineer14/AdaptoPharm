# Adapted from: https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/#:~:text=%20Here%20are%20four%20basic%20steps%20for%20sending,message%20using%20the%20SMTP%20server%20object.%20More%20
import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = str('YOUR YAHOO EMAIL HERE')
PASSWORD = str('THIRD PARTY PASSWORD HERE')

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    with open(filename, mode = 'r', encoding = 'utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def get_meds(filename):
    """
    Returns list of meds
    """
    locations = []
    meds = []
    with open(filename, mode = 'r', encoding = 'utf-8') as meds_file:
        for a_med in meds_file:
            locations.append(a_med.split()[0])
            meds.append(a_med.split()[1])
    return locations, meds

def read_template(filename):
    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r', encoding = 'utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('mycontacts.txt')
    locations, meds = get_meds('meds.txt')


    # setup SMTP server
    s = smtplib.SMTP(host='smtp.mail.yahoo.com', port='587')
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    #  For each contact send the email
    for name, email in zip(names, emails):
        msg = MIMEMultipart() # create message

        message = open('message.txt','r+')
        data = message.readlines()
        message.seek(0)
        message.truncate()
        message.write(data[0])
        message.seek(0,2)
        for i in range(0,len(meds)):
            message.write(locations[i] + ' has ' + meds[i] + '\n')
        message.close()

        message_template = read_template('message.txt')

        # add in the actual person's name to template
        message = message_template.substitute(PERSON_NAME=name.title())

        # prints out the message body
        print(message)

        # setup the parameters of the message
        msg['From']=MY_ADDRESS
        msg['To']=email
        msg['Subject']="This is a TEST"

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server
        s.send_message(msg)
        del msg

    # Terminate the SMTP session
    s.quit()

if __name__ == '__main__':
    main()
