from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(username,email):
    # Creating message subject and sender
    subject = 'Welcome to the Neighbourhood'
    sender = 'moringatester@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/welcome.txt',{"username":username})
    html_content = render_to_string('email/welcome.html',{"username":username})

    msg = EmailMultiAlternatives(subject,text_content,sender,[email])
    msg.attach_alternative(html_content,'text/html')
    msg.send()