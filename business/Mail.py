from django.conf import settings
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

class Mail:
    
    
    def sendddos(self, email, subject, text):
        
        gmail_user = "singleprojects@gmail.com"
        gmail_pwd = "s1ngl3pr0j3cts"
        msg = MIMEMultipart()
        msg['From'] = gmail_user
        msg['To'] = email
        msg['Subject'] = subject
        part = MIMEBase('application', 'octet-stream')
        

        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmail_user, gmail_pwd)
        mailServer.sendmail(gmail_user, email, msg.as_string())
        # Should be mailServer.quit(), but that crashes...
        mailServer.close()


    
    def send(self, email,subject,message):
        print("llegamos::::::::::::::::::::::::::")
        print(settings.BASE_EMAIL)
        print(email)
        print(subject)
        print(message)
        print(settings.BASE_EMAIL_PASSWORD)
        
        header  = 'From: %s\n' % settings.BASE_EMAIL
        header += 'To: %s\n' % ','.join(email)
        #header += 'Cc: %s\n' % ','.join("")
        header += 'Subject: %s\n\n' % subject
        message = header + message
        smtpserver='smtp.gmail.com:587'
        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(settings.BASE_EMAIL,"s1ngl3pr0j3cts")
        problems = server.sendmail(settings.BASE_EMAIL, email, message)
        server.quit()
        
        
    def newUser(self,userObject):
        message = """
Estimado(a) %s:

Ha sido registrado dentro del proyecto Single Projects con los siguientes datos:

Usuario: %s
Password: %s
Perfil: %s

O si lo prefieres, puedes ingresar utilizando tu cuenta de google +

Url del proyecto %s



atte.

Single Projects


""" % (userObject.name, userObject.username, userObject.password, userObject.profile.name,"http://bravopikino.kd.io:8000/")
        self.sendddos(userObject.email, "Acceso a Single Projects", message)
    
    
    