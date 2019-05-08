# IMPORTATION DES MODULES
import time as time
import tkinter as tk
from random import randint

# DEFINITION DES VARIABLES UTILEES POUR LE PROGRAMME
#	TAILLE DE FENETRE (INTEGERS)

largeur_fen = 1000
hauteur_fen = 800

#	KIT COULEUR (STRINGS)

color = 'steel blue'
pour_couleur = [['green','red'],['blue','yellow']]  # MATRICE POUR AUTOMATISER L'ATTRIBUTION DES COULEURS AU RECTANGLES/CARREES

#	SCHEMA DE L'ORDINATEUR/A SUIVRE

IA = []

#	COMPTEURS DE ROUNDS / CLICS

cnt = 0
cnt_clic = -1 # -1 POUR ETRE A 0 LORS DU 1ER CLIC POUR DIRECTEMENT UTILISER LA VALEUR POUR LA VERIFICATION
dele = 5

#	LONGS TEXT

lose_text = 'Vous avez perdu !' + '\n'* 2 + 'PRESS RESTART FOR TRY AGAIN'

# 	POLICE D'ECRITURE

fnt_title = "{courier new} 26 bold"
fnt_but = "{courier new} 20 bold"

# DEFINITION DES DIFFERENTES FONCTIONS
# 	RESTERT DE LA GAME

def refresh() :

	global dele
	canvas.delete(dele)
	canvas.delete(dele+1)
	dele += 2

	global IA, cnt
	IA = []
	cnt = 0

	button['command'] = redebind
	button['text'] = '  PLAY   '
	label['text'] = "ROUND 0"

# 	INTINVIENS QUANS L'USER PERDS

def lost() :

	#	DESACTIVATION DE L'EVENT CLIC SOURIS

	canvas.create_rectangle(100,200,500,400,fill='black')
	canvas.create_text(300,300,text=lose_text,fill='white',justify='center')
	button['command'] = refresh

#	VERIFIE LES CLICS PAR RAPPORT AU SCHEMA QUI L'USER DOIT SUIVRE

def analyse() :
	
	if select_tag[0] != IA[cnt_clic] :

		lost()

	else :

		if cnt_clic + 1 == cnt :

			round()

		else : 

			return

# 	RETOUR DE L'EVENEMENT LIE AU CANEVAS

def choice(event):

	global select_tag, cnt_clic
	select_tag = canvas.find_closest(event.x,event.y)
	cnt_clic+=1
	analyse()

# 	INTERVIENS QUAND LE PROGRAMME DETECTE QU'IL PASSE DANS UN NOUVEAU ROUND
def rebind():

	canvas.bind('<Button-1>',choice)

def redebind():

	canvas.unbind('<Button-1>')
	round()

def round() :

	
	global cnt_clic,cnt
	cnt_clic = -1
	cnt += 1

	label['text'] = "ROUND %d" % cnt
	button['text'] = '  RESET  '
	button['command'] = refresh
	IA.append(randint(1,4))
	print(IA)		

	for i in IA :

		save = canvas.itemcget(i,"fill")
		main.after(1000,canvas.itemconfigure(i,fill='white'))
		canvas.update_idletasks()
		main.after(1000,canvas.itemconfigure(i,fill=save))

	rebind()	

# COEUR DU PROGRAMME
# 	CREATION DE LA FENETRE PRINCIPALE

main = tk.Tk()
main['bg'] = color
main.title("Simon")
main.geometry("%dx%d" % (largeur_fen,hauteur_fen))

# 	CONFIGURATION DE LA GRILLE DE LA FENETRE PRINCIPALE

main.columnconfigure(0,weight=1)
main.columnconfigure(1,weight=1)
main.rowconfigure(0,weight=1)
main.rowconfigure(1,weight=3)

# 	CREATION DES WIDGETS (LABEL/BOUTON/CANEVAS)

label = tk.Label(main,padx=20,pady=5,text="ROUND 0",font=fnt_title,relief='groove',bd=3)
label.grid(row=0,column=0,columnspan=2)

canvas = tk.Canvas(main,width=600,height=600,relief='raised',bd=6,bg='black')
canvas.grid(row=1,column=0)

button = tk.Button(main,text='  PLAY   ',command=redebind,font=fnt_but,padx=10,pady=2,bd=3)
button.grid(row=1,column=1)

# 	CREATIONS DES DESSINS DANS LE CANVAS (TAGS = [1,2]/[3,4])
# 		POINTS INITIAUX

x = 0
xx = 300
y = 0
yy = 300

# 		AUTOMATISATION DE LA GENERATION DES RECTANGLES

for i in range(2) :

	for j in range(2) :

		canvas.create_rectangle(x,y,xx,yy,fill=pour_couleur[i][j],outline='')
		x += 300 + 5
		xx += 300 + 5

	x = 0
	xx = 300
	y += 300 + 5
	yy += 300 + 5

# 	BOUCLAGE DE LA FENETRE PRINCIPALE

main.mainloop()