from flask_mail import Message
from flask import render_template
from . import mail

<<<<<<< HEAD
def mail_message(subject,template,to,**kwargs):
    sender_email ='pitch_time@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    email.html = render_template(template + ".html", **kwargs)
    mail.send(email)



=======

email = Message(subject, sender=sender_email, recipients=[to])
email.body = render_template(template + ".txt", **kwargs)
email.html = render_template(template + ".html", **kwargs)
mail.send(email)
>>>>>>> 0d40a78dc1505fb4a4dcabc5ff2491f48afa6777
