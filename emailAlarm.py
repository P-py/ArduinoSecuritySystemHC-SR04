"""
*********************************************************************
Email sending alarm - integrado com ArduinoUNO + HC-SR04
(c) Copyright (c) 2021 Pedro Salviano Santos
License: MIT.
*********************************************************************

Para usar esse script corretamente:
LEIA A DOCUMENTAÇÃO EM github.com/P-py/Arduino/base_com_emailnotify.

"""

import smtplib #SPara envio do email
from email.message import EmailMessage #Para compor a mensagem de e-mail

def email_send(subject, body, to):
    #Create the message and sets the body/content of it.
    #Cria a mensagem e configura o conteúdo dela.
    message = EmailMessage()
    message.set_content(body)
    message['subject'] = subject
    message['to'] = to

    """
    Caso queira utilizar corretamente vai precisar mudar as variáveis abaixo.

    Por isso, POR FAVOR, LEIA A DOCUMENTAÇÃO EM github.com/P-py/arduino/base_com_emailnotify.

    POR FAVOR, LEIA A DOCUMENTAÇÃO EM github.com/P-py/arduino/base_com_emailnotify.
    POR FAVOR, LEIA A DOCUMENTAÇÃO EM github.com/P-py/arduino/base_com_emailnotify.
    POR FAVOR, LEIA A DOCUMENTAÇÃO EM github.com/P-py/arduino/base_com_emailnotify.
    """
    
    user = "###"
    password = "###"
    message['from'] = user

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls() #Necessário para o gmail.
    server.login(user, password)
    server.send_message(message)
    server.quit()

if __name__ == "__main__":
    email_send("Testing SMTP - python", "This is a test of SMTPlib in python", "###")