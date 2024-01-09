import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


clientes = pd.read_excel('./alvoss.xlsx')

for index, cliente in clientes.iterrows():
    msg = MIMEMultipart()
    msg['subject'] = 'Email da PYcodebr :)'
    msg['from'] = 'logxpbr@gmail.com'
    msg['to'] = cliente['email']
    message = f"ola {cliente['nome']}, voce recebeu um email de teste"
    msg.attach(MIMEText(message,'plain'))

    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.starttls()
    server.login('logxpbr@gmail.com','senha_do_ google@')
    server.sendmail(msg['from'],msg['to'],msg.as_string())
    server.quit()