import smtplib
import random

sendemail = input("Enter the email address to send from: ")

subject = "vrovrooovroovrovrovrovrovrovrovro"

reciever_email = input("Enter the email address to send to: ")

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login(sendemail, "put your app password here")

count = 50

def randomize_string(string):
    """Randomizes the characters in a string."""
    char_list = list(string)
    random.shuffle(char_list)
    return ''.join(char_list)

for i in range(0, count):
    subject = randomize_string(subject) + str(count)
    if i == 0:
        message = "Hi dogmy name is putloolrobinokokokforsure"
    else:
        message = randomize_string(message)  + str(count)
    text = f"Subject:{subject}\n\n{message}"
    server.sendmail(sendemail, reciever_email, text)
    print("EMAIL HAS been sent")
    
