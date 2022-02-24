# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 16:47:24 2020

@author: Gehin Dematini
"""

import random
from tkinter import * #on importe les repertoires necessaires

window = Tk()#creer fenetre
window.title("Pendu")#Nom de la fenetre
window.minsize(360, 270)#taille minimale de la fenetre
window.geometry("780x540")#taille de la fenetre qui apparait
window.config(background='#FFA91C')

#frame = Frame(window, bg='#FFA91C')#creation de la frame
#premiere texte dans la fenetre
#pendu_title = Label(window, text="Bienvenue dans le jeu du pendu !", font =("Lato", 20), bg='#FFA91C')
#pendu_title.pack(expand=YES )#position du texte

#Deuxieme texte
#pendu_subtitle = Label(window, text="Choisissez votre mode de jeu :", font =("Lato", 15), bg='#FFA91C', fg='white')
#pendu_subtitle.pack(expand=YES)

#Bouton 1 joueur
#joueursolo_button = Button(frame, text="1 joueur", font=("Lato", 18), bg='#FFA91C', fg='white',)
#joueursolo_button.pack()

#frame.pack(expand=YES)

#Bouton 2 joueurs
#joueurmulti_button = Button(frame, text="2 joueurs", font=("Lato", 18), bg='#FFA91C', fg='white',)
#joueurmulti_button.pack()

#frame.pack(expand=YES)


#window.mainloop()#afficher la fenetre
def joueur_1() :
    mots = ["arrosoir", "aristocrate", "attentat", "action","abricot", "alentour", "analphabète", "alcool", "asticot", "animal", "bricolage","brebis", "bouton", "blanchir" "beurre", "boulette", "bélier","bleu", "blanchisserie","bourreau", "bureau", "collant" "cigarette", "cavalier", "carreau", "confinement", "coupure", "couteau", "clafoutis", "caramel", "coupable", "dessin", "desirable", "destin", "distant", "dedoubler", "discuter", "discours", "divin", "deposer", "décorer", "embeter", "enivrer", "esclave", "eprouver", "emballage", "epurer", "esperer", "evident", "essuyer", "effacer", "finale", "forteresse", "fortifier", "fouler", "finir", "fondant", "flouter", "fenouille", "festin", "futur", "gastronomie", "gaufre", "gouverner", "girafe", "gestion", "gouter", "grammaire", "gagner", "gourmand", "galactique", "habitation", "habit", "hippocampe", "hache", "haleine","halte", "hallucinant","hameconner", "handicap", "harceler", "ignoble", "irresistible", "inhabitable", "inespere", "irrespect", "illogique", "inoui", "interieur","inspecteur", "idiot", "impossible", "joie", "jouet", "juste", "jolie", "jouer", "jeu", "jouable", "jacuzzi", "jaloux", "jambe", "kiwi", "kayak", "karate", "karma", "kebab", "kangourou", "katana", "kayakiste", "kart", "karaoke", "lion", "livre", "lecture", "lycee", "lourd", "leger", "lisser", "lymphe", "laver", "larve", "mais", "mystere", "miserable", "mignon", "miroir", "mouton", "mangue", "mozambie", "moustique", "merveilleux", "nouveau", "nouvelle", "neon", "naissance", "novice", "noyau", "noyer", "nounours", "noeud", "nuage", "osculter", "ouvrir", "obese", "obligation", "obligatoire", "omelette", "oublier", "ours", "obstacle", "offrir", "pleuvoir", "pluie", "poussiere", "pousser", "pleurer", "pistolet", "poubelle", "promettre", "poussette", "pneu", "quiproquo", "qualifier", "quitter", "quittance", "quarantaine", "quiche", "qualite", "quartz", "quarante", "quart", "rateau", "rester", "redoutable", "rire", "regle", "risible", "rougir", "rouge", "rigoler", "retenir", "salive", "sable","saluer", "singe", "songe", "signer", "souffler", "sourire", "souris", "the", "tomate", "tisane", "trophee", "terrain", "tente", "tante", "tirer", "trou", "ulcere", "ultime", "ultra", "urbanisme", "un", "urgence", "usurpation", "utile", "utilite", "use", "violet", "voler", "volet", "voir", "venir", "viande", "vilain", "vacarme", "ver", "verre", "wagon", "web","wifi", "xylophone", "zizanie", "zone", "zoo"] 
    #on crée un dictionnaire de mots
    mot_cache = random.choice(mots) #on choisit un mot aleatoirement dans le dictionnaire
    essais = 7 #on determine un nombre d'essais pour deviner les lettres
    affichage = ""
    lettres_trouvees = "" #on affecte a lettres_trouvees le nombre de lettres deja trouvees
    
    for i in mot_cache:
      affichage += "_ " #on affiche le nombre de lettres dans le mot
    
    print("    •Pendu• ")
    
    while essais > 0: #tant que le nombre d'essais le permet on continue
      print("Mot à trouver : ", affichage)
      lettre_proposee = str(input("Choisissez une lettre : "))
    #on demande au joueur de proposer une lettre
      if lettre_proposee in mot_cache:
          lettres_trouvees = lettres_trouvees + lettre_proposee
          print("->Bravo !") #si la lettre fait partie du mot on l'affiche à sa place 
      else:
        essais-=1 #sinon on retire un essai

        print("->Dommage")
        if essais==0:
            print(" ========Y= ")
        if essais<=1:
            print(" ||/     |  ")
        if essais<=2:
            print(" ||      0  ")
        if essais<=3:
            print(" ||     /|\ ")
        if essais<=4:
            print(" ||     /|\ ")
        if essais<=5:                    
            print("/||         ")
        if essais<=6:
            print("============\n")
    
      affichage = ""
      for x in mot_cache:
          if x in lettres_trouvees:
              affichage += x + " "
          else:
              affichage += "_ "
    
      if "_" not in affichage: #si toutes les lettres sont trouvees le joueur a gagne et on affiche partie terminee
          print(" Victoire ! ")
          break
      
      if essais==0:
            print("Le mot était :", mot_cache)
            print(" ► Défaite... ◄")
            break
         
    print("\n * Fin de la partie * ")
  
def joueur_2():
    mot_choisi = input("Joueur 1 choisissez un mot : ")#on demande au premier joueur de choisir le mot de son choix
    mot_choisi = str(mot_choisi)
    essais = 7
    affichage = ""
    lettres_trouvees = ""
    
    for i in mot_choisi:
      affichage+="_ "
    
    print("    •Pendu• ")
    
    while essais > 0:
      print("\nMot à trouver : ", affichage)
      lettre_proposee = input("Choisissez une lettre : ")[0:1].lower()
    
      if lettre_proposee in mot_choisi:
          lettres_trouvees = lettres_trouvees + lettre_proposee
          print("->Bravo")
      else:
        essais-=1
        print("->Dommage")
        if essais==0:
            print(" ========Y= ")
        if essais<=1:
            print(" ||/     |  ")
        if essais<=2:
            print(" ||      0  ")
        if essais<=3:
            print(" ||     /|\ ")
        if essais<=4:
            print(" ||     /|\ ")
        if essais<=5:                    
            print("/||         ")
        if essais<=6:
            print("============\n")
    
      affichage = ""
      for x in mot_choisi:
          if x in lettres_trouvees:
              affichage += x + " "
          else:
              affichage += "_ "
    
      if "_" not in affichage:
          print("► Victoire! ◄")
          break

      if essais==0:
          print("Le mot était :", mot_choisi)
          print(" ► Défaite... ◄")
          break
   
    print("\n    * Fin de la partie *    ")


joueur=int (input("choisissez le nombre de joueur(s) :")) #on commence par demander le nombre de joueur
if joueur==1:
    joueur_1()
elif joueur==2:
    joueur_2()
else:
    print("Choisir 1 ou 2")

#Une fois que l'on connait le nombre de joueur, on peut lancer la fonction adequat
