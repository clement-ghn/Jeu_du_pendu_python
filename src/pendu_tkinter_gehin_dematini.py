# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:28:32 2020

@author: clement, loris
"""

from tkinter import *#on importe les modules nécessaire à la création de notre jeu
import random



def Joueur_1():
    window.geometry("1000x800")#on crée la nouvelle fenetre, en retirant les elements de la page accueil (utilisation de destroy)
    window.config(background='white')
    frame.destroy()
    pendu_title.destroy()
    pendu_subtitle.destroy()
    
    global annonce#on crée un premier label, qui affiche le nombre d'essais restants
    annonce = Label(window, width=8, font="Times 15 bold", text=0, bg='white')
    annonce.pack(padx=5, pady=5)
    
    global compteur#On initialise le compteur d'erruers
    compteur=7
    
    global image_pendu
    canevas = Canvas(window, bg='white', height=500, width=620)#on crée le Canvas qui va accueillir la photo de notre pendu
    canevas.pack()

    photo=PhotoImage(file="0.png")#la premiere image est un fond blanc, et on la place dans le Canva prévu à cet effet
    image_pendu = Label(canevas, image=photo, border=0)
    image_pendu.place(x=0, y=0)


    global secret
    secret = random.choice(open('liste_francais.txt').readlines())
    print(secret)
    secret = secret[:-1]
    secret = secret.lower()#on definit le mot à trouver avec un mot au hasard dans notre dictionnaire
    global mot_en_progres#Pour initialiser le jeu, on remplace chaque lettre du mot par des •, pour cacher notre mot
    mot_en_progres = list("■" * (len(secret)))
    rond = "".join(mot_en_progres)

    
    global lbl
    lbl = Label(window, text=rond, font="Times 15 bold", bg='white', fg='black')#on affiche les ronds qui font la longueur du mot
    lbl.pack(padx=20, pady=20)
    
    ALPHA = "abcdefghijklmnopqrstuvwxyz"#ce sont les lettres sur lesquels on pourra cliquer
    
    for c in ALPHA:#on initialise les boutons, pour chaque lettre on crée un bouton
        btn = Button(window, text=c, bg='white', fg='black')
        btn.pack(side=LEFT, pady=10, padx=10)
        btn.bind("<Button-1>", choisir_lettre)#on fait interagir la souris avec les boutons lettres, dès que l'on clique dessus
    
        
    annonce["text"]=compteur #le label annonce prend la valeur du compteur (définit dans les fonctions plus bas)
    
    
    

def Joueur_2():
    window.geometry("500x300")#on crée la nouvelle fenetre, en retirant les elements de la page accueil, et on va créer la fenêtre dans laquelle le joueur va entrer son mot
    window.config(background='white')
    frame.destroy()
    pendu_title.destroy()
    pendu_subtitle.destroy()
    global L1
    global E1
    L1 = Label(window,font="Lato 20", bg='white', text="Joueur 1, Choisissez le mot :")#on crée un label pour donner l'instruction
    L1.pack(pady=20)
    global motsoumis
    E1 = Entry(window, bd =5)#on crée une zone d'entrée de texte
    E1.pack(pady=15)
    motsoumis = Button(window, text = "Soumettre",font="Lato 10", bg='white',fg="black", command= soumettre)#on crée un bouton qui éxecute la fonction soumettre, en utilisant comme mot secret lle mot entré par l'utilisateur
    motsoumis.pack()
    

def soumettre():
    window.geometry("1000x800")
    global E1, L1, motsoumis#on détruit la fenetre d'entrée, et on crée la fenetre de jeu
    user=E1.get()
    L1.destroy()
    E1.destroy()
    motsoumis.destroy()
   #Cette fenetre comporte les mêmes instruction que le mode joueur 1, sauf que le mot secret est le mot entré par l'utilisateur
    global phrase
    phrase = Label(window, font="Lato 20", text="Joueur 2, à vous de jouer !", bg='white')
    phrase.pack()
    
    global annonce
    annonce = Label(window, width=8, font="Times 15 bold", text=0, bg='white')
    annonce.pack(padx=5, pady=5)
    
    global compteur#On initialise le compteur d'erruers
    compteur=7
    
    
    global image_pendu
    canevas = Canvas(window, bg='white', height=500, width=620)
    canevas.pack()

    photo=PhotoImage(file="0.png")
    image_pendu = Label(canevas, image=photo, border=0)
    image_pendu.place(x=0, y=0)
    
    global secret
    secret = user#on definit le mot à trouver avec un mot au hasard dans notre dictionnaire
    
    global mot_en_progres
    mot_en_progres = list("⬛" * len(secret))
    rond = "".join(mot_en_progres)

    
    global lbl
    lbl = Label(window, text=rond, font="Times 15 bold", bg='white', fg='black')#on affiche les étoiles qui font la longueur du mot
    lbl.pack(padx=20, pady=20)
    
    ALPHA = "abcdefghijklmnopqrstuvwxyz"#ce sont les lettres sur lesquels on pourra cliquer
    
    for c in ALPHA:#on initialise les boutons
        btn = Button(window, text=c, bg='white', fg='black')
        btn.pack(side=LEFT, pady=10, padx=10)
        btn.bind("<Button-1>", choisir_lettre)#on fait interagir la souris avec les boutons lettres
    
    annonce["text"]=compteur
    


window = Tk()#creer fenetre
window.title("Pendu")#Nom de la fenetre
window.minsize(360, 270)#taille minimale de la fenetre
window.geometry("780x540")#taille de la fenetre qui apparait
window.config(background='white')

frame = Frame(window, bg='white')#creation de la frame
#premiere texte dans la fenetre
pendu_title = Label(window, text="Bienvenue dans le jeu du pendu !", font =("Lato", 20), bg='white')
pendu_title.pack(expand=YES )#position du texte
    
#Deuxieme texte
pendu_subtitle = Label(window, text="Choisissez votre mode de jeu :", font =("Lato", 15), bg='white', fg='black')
pendu_subtitle.pack(expand=YES)
    
#Bouton 1 joueur
joueursolo = Button(frame, text="1 joueur", font=("Lato", 18), bg='white', fg='black', command=Joueur_1)
joueursolo.pack()
    
frame.pack(expand=YES)
    
#Bouton 2 joueurs
joueurmulti = Button(frame, text="2 joueurs", font=("Lato", 18), bg='white', fg='black', command=Joueur_2)
joueurmulti.pack()

frame.pack(expand=YES)


def maj_mot_en_progres(mot_en_progres, lettre, secret):#on défini une fonction qui affiche la lettre si elle est trouvée
    n = (len(secret))
    solution=list(secret)
    for i in range(n):
        if secret[i] == lettre:#si la lettre sur laquelle on clique est dans le mot secret, on affiche la lettre
            mot_en_progres[i] = lettre
    if lettre not in secret:#Si la lettre n'est pas dans le mot on diminue le compteur
        global compteur
        compteur-=1
        annonce["text"]=compteur
        affichagependu=str(compteur)+".png"#l'affichage du pendu prend la valeur du compteur en chaine de caractere et va chercher le fichier correspondant
        global image_pendu
        photo=PhotoImage(file=affichagependu)
        image_pendu.config(image=photo)
        image_pendu.image=photo#on definit quelle sera l'image du pendu qui sera affichée dans le canva
    if compteur<=0:#on determine quand les fonctions de fin doivent apparaître (quand le compteur est à 0)
        fin() 
    elif solution==mot_en_progres:
        fin()




def choisir_lettre(event):#cette fonction sert à définir chaque lettre qui apparait
    mon_btn = event.widget
    lettre = mon_btn["text"]
    maj_mot_en_progres(mot_en_progres, lettre, secret)
    lbl["text"] = "".join(mot_en_progres)#si on appuie sur le bouton d'une lettre qui est dans le texte, la lettre affichée sur le bouton se rretrouve à sa place dans le mot



def fin():
    if compteur==0 :#Si le compteur vaut 0, on affiche la fenetre de defaite
        window.destroy()
        defaite = Tk()
        defaite.geometry("500x350")
        defaite.config(background='white')
        frame = Frame(defaite, bg='white')
        texte= Label(defaite, text="Défaite!", font =("Lato", 50), bg='white')
        montexte=StringVar()
        montexte.set(secret)#on met le mot secret dans une variable montexte
        solution= Label(defaite, text="Le mot était :", font =("Lato", 12), bg='white')#on affiche le mot que le joueur devait trouver ( en affichant la variable montexte)
        affichermot= Label(defaite, textvariable=montexte,  font =("Lato", 12,), bg='white', fg='red')
        canva_defaite = Canvas(defaite, bg='white', height=200, width=300)#on affiche le pendu en entier en cas de defaite dans un canva
        photodefaite=PhotoImage(file="Pendu.png")
        perdu = Label(canva_defaite, image=photodefaite, border=0)
        perdu.place(x=0, y=0)
        texte.pack(expand=YES)
        solution.pack(expand=YES)
        affichermot.pack(expand=YES)
        frame.pack(expand=YES)
        canva_defaite.pack()
        defaite.mainloop()
    else :
        window.destroy()#Sinon on affiche la fenetre de victoire
        victoire = Tk()
        victoire.geometry("500x290")
        victoire.config(background='white')
        frame = Frame(victoire, bg='black')
        montexte2=StringVar()
        montexte2.set(compteur)#cette fois la variable contient le nombre d'essais qu'il restait au joueur
        phrase= Label(victoire, text="Votre nombre de tentatives restantes était :", font =("Lato", 12), bg='white')
        coupsrestant= Label(victoire, textvariable=montexte2,  font =("Lato", 12,), bg='white', fg='red')
        texte = Label(victoire, text="Victoire!", font =("Lato", 50), bg='white')
        frame.pack(expand=YES)
        texte.pack(expand=YES)
        phrase.pack(expand=YES)
        coupsrestant.pack(expand=YES)
        victoire.mainloop()
        

    

window.mainloop()#afficher la fenetre
