import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from PIL import Image

def ondegrav(temps,separation,distance,masse):
    '''
    Fonction qui retourne l'amplitude de l'onde gravitationnelle en fonction du temps pour des fréquences, séparation, distance et masses données
	'''
    G = 6.67E-11  # constante gravitationelle 
    c = 2.99E8  # vitesse de la lumière en m/s
    T = np.sqrt(4.* np.pi**2 / G / (2.* masse) * separation**3 )
    print("Période =",T,"seconde","fréquence=",1/T)
    omega = 2.*np.pi / T 
    mu = masse / 2.
    ondegrav = -1./distance * (4. * G * mu * omega**2 * separation**2)/c**4 * np.sin(2.*omega * temps)    
    return ondegrav

def bruit(temps):
    bruit= np.random.normal(0.,1.e-23,len(temps))
    return bruit


t_values = np.arange(0.,0.01,0.00001)
h_values = ondegrav(t_values,10.,2.E7,1.E20)
bruit_values = bruit(t_values)

masse_proposee = 1		#set variables to be able to easily toggle off the user input process 
separation_proposee = 1
distance_proposee = 1
masse_proposee=float(input("Proposez une masse de trous noirs en kg"))
separation_proposee=float(input("Proposez une distance entre les trous noirs en mètres"))
distance_proposee=float(input("Proposez la distance entre la Terre et les trous noirs"))

h_values_proposed = ondegrav(t_values,separation_proposee,distance_proposee,masse_proposee)

plt.plot(t_values,h_values+bruit_values,label='Signal observé')
plt.plot(t_values,h_values_proposed,label='Signal Théorique proposé')
plt.legend(loc='upper left')
plt.xlabel("Temps [s]")
plt.ylabel("Amplitude de l'onde gravitationelle $h$")
plt.ylim(-2.E-22,2.E-22)
plt.title("Signal observé et proposé")
plt.savefig('signal.png', facecolor='#ffffff', edgecolor=None, width=100)  # sauvegarde la figure en png avec une width de 100px--une résolution de 600 dpi--

plotted = Image.open("signal.png")

width = plotted.width
height = plotted.height

window = Tk()
bg = "#000000"
canvas = Canvas(window, width=width, height=height, bg=bg)
canvas.pack()

# img = PhotoImage(width=width, height=height)
img = PhotoImage(file="signal.png")
canvas.create_image((width//2, height//2), image=img, state="normal")

mainloop()
