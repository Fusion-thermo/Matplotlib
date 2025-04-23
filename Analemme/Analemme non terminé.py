import matplotlib.pyplot as plt
import numpy as np
from math import pi
from scipy.integrate import romb
import time as time_module
#annalemme  est la figure tracée dans le ciel par les différentes positions du soleil relevées à une même heure et depuis un même lieu au cours d’une année calendaire.
#si j'ai bien compris l'annalemme ne dépend que de l'inclinaison de le terre par rapport au plan 
# de l'écliptique et du fait que la trajectoire est une ellipse 
#l'inclinaison définit la hauteur de l'annalemme = la partie verticale, pour la partie horizontale
def radian(angle):
    return angle*pi/180
def degre(angle):
    return angle/pi*180

def make_kepler_orbit(eccentricity,orbital_period,nStep):
    ##########################################################
    # Units: orbital period [years]                          #
    # returns: nStep true anomaly values throughout the orbit  #
    ##########################################################
    tRange = np.linspace(0.0,orbital_period/2,(nStep+2)//2)
    
    theta = []
    for time in tRange:
        PsiDiff = 1.0
        M = 2*np.pi*time/orbital_period
        PsiOld = M
        while PsiDiff > 1e-10:
            PsiNew = M + eccentricity*np.sin(PsiOld)
            PsiDiff = PsiNew-PsiOld
            PsiOld = PsiNew
        theta0 = 2*np.arctan(((1+eccentricity)/(1-eccentricity))**(0.5)*np.tan(PsiOld/2.))
        theta.append(theta0)        
    return np.concatenate((theta,-np.flip(theta)[1:-1]))

def orbit(semimajor_axis,eccentricity,true_anomaly): 
    ##############################################
    # Units: separation [au] #
    ##############################################
    
    # define the shape equation
    r_orbit = semimajor_axis*(1 - eccentricity**2)/(1 + eccentricity*np.cos(true_anomaly))
    x_orbit = r_orbit*np.cos(true_anomaly)
    y_orbit = r_orbit*np.sin(true_anomaly)
     
    au = 149597870700
    return x_orbit*au,y_orbit*au


inclinaison = radian(23+26/60+11/3600) #aussi appelée obliquité, = 23.436389 °
obliquite =  #obliquite de la terre sur un an
rayon_terre = 6378.137*1e3
duree_rotation = 24
jour_solaire = 23 + 56/60
m = 5.972*10**24     #m = mass of earth
L = 2/5*m*rayon_terre**2 * 2*pi/(23*3600+56*60)     #L = angular momentum earth rotation is correct
# L = 2.67*10**40     #L = angular momentum earth rotation around the sun is correct
M = 1.99*10**30     #M = mass of sun
G = 6.674*10**-11   #G = Gravitationl constant
k = G*M*m        
p = L**2/(m*k) 
a = 152.1*1e9  # demi-longueur du grand axe en m
b = 147.1*1e9  # demi-longueur du petit axe en m

# Définir les paramètres de l'ellipse
orbital_period = 1.0
e = 0.016710218 #eccentricité de la terre
# e = 0.5 #eccentricité de test
precision = 50
precision = 365*24*60 #pour avoir des nombres entiers correspondant à chaque minute
temps = np.linspace(0,orbital_period*365*24*60,precision) #en minutes
a = time_module.time()
true_anomaly = make_kepler_orbit(e,orbital_period,precision)
b = time_module.time()
semimajor_axis = orbital_period**(2/3) #orbital period en années uniquement
c = time_module.time()
x, y = orbit(semimajor_axis,e,true_anomaly)
d = time_module.time()
print(b-a,c-b,d-c)

n = -1
# plt.figure(figsize=(15,10))
# plt.axis('equal')
# plt.title('Earth orbit')
# # The Sun is located at the origin.
# plt.scatter(0,0, color='orange')
# plt.scatter(x[:],y[:])
# plt.show()

# dt = true_anomaly * (365*24*60) / (2 *pi) #identique à temps
#durée constante entre 2 positions, mais vitesse angulaire et linéaire variable
#à cause de la forme d'ellipse



# # distance_centre = np.sqrt(x**2+y**2) #distance de la terre au centre de l'ellipse pour chaque position

# #Calculer le périmètre de l'ellipse
# # convergence=[]
# #Méthode 1 plus précise
# # for k in range(2,15):
# # k=12 #pour pouvoir effectuer une romberg integration, k testé par convergence, bon résultats
# # precision = 2**k + 1
# # intervalle = np.linspace(0,pi/2,precision)
# # fonction = np.sqrt(1-e**2*np.sin(intervalle)**2)
# # perimetre = 4*a*romb(fonction,(pi/2)/precision)
# perimetre = 955372523045.8243 # m
# # convergence.append(perimetre)
# # plt.plot(convergence)
# # plt.show()
# # #Méthode 2
# # h = (a-b)**2/(a+b)**2
# # ramanujan = pi*(a+b)*(1+3*h/(10+np.sqrt(4-3*h)))
# # print(perimetre)
# # print(ramanujan)

#vitesse angulaire
omega = np.diff(true_anomaly)/np.diff(temps/60) #rad/h
omega[np.argmin(omega)] = 0
#vitesse linéaire
delta_distance = np.sqrt(np.diff(x)**2 + np.diff(y)**2) #en réalité c'est un arc
vitesse = delta_distance*1e-3/np.diff(temps/60) #en km/h, attendu ~ 107 000 km/h
print(np.mean(omega),np.mean(vitesse))
# plt.plot(omega)
# plt.plot(vitesse)
# plt.show()


#Equation du temps partie ellipticité 

# theta = pi/2
n_minutes_phi = 23*60+56
# periode_phi = np.linspace(0,n_minutes_phi, n_minutes_phi)
phi_solo = np.linspace(0, 2*pi, n_minutes_phi)
# omega_phi = 2*pi/(23*60+56)
#phi = l'angle de la terre par rapport au soleil pour chaque minute de l'année
phi = np.array([phi_solo[i%len(phi_solo)] for i in range(len(true_anomaly))])
# print(phi[0],phi[n_minutes_phi],degre(phi[24*60]),degre(phi[-1]))
#les deux mesures : on relève leur angle respectif tous les jours à la même minute
mesure_phi = np.array([phi[i] for i in range(0,len(phi),24*60)])
mesure_true_anomaly = np.array([true_anomaly[i] for i in range(0,len(true_anomaly),24*60)])
print(true_anomaly[-5:],phi[-5:],np.count_nonzero(phi == 0))
# beta = mesure_true_anomaly - mesure_phi
# beta = degre(pi - mesure_phi + mesure_true_anomaly)
#beta : décalage en minute = equation du temps partie ellipticité 
beta = degre(mesure_phi - mesure_true_anomaly) 
beta[beta>100] -= 360
print(max(beta)-min(beta)) #amplitude plutôt correcte ! 7.53 au lieu de 7.66
# print(true_anomaly[-1],mesure_true_anomaly[-1])
# plt.plot(phi[-25:])
# plt.plot(mesure_true_anomaly[350:])
# plt.plot(beta[:]) #la courbe du temps pour cette partie

#Equation du temps partie obliquité 
"""
Point de vue géocentrique :
En 24h le soleil parcourt une certaine distance sur le plan de l'écliptique, sauf qu'on
le regarde sur le plan de l'équateur, donc il faut projeter sa trajectoire sur le plan de l'équateur
La composante de l'axe vernal ne change pas, celle perpendiculaire selon cos(90-inclinaison) = sin(inclinaison)
Uniquement les 4mn de rotation supplémentaire ?
"""

# #Coordonnées du point d'observation
#sur le plan x,y le point d'observation est à l'intersection entre l'axe soleil-terre et la surface de la terre,
#donc même orbite mais plus courte
# declinaison = (pi/2-inclinaison)*np.cos(true_anomaly) 
# declinaison = (inclinaison)*np.cos(true_anomaly) 
#normalement fonctionne quand même
# px = rayon_terre * np.cos(true_anomaly) + x
# py = rayon_terre * np.sin(true_anomaly) + y
# px = (a-rayon_terre) * np.cos(true_anomaly)
# py = (b-rayon_terre) * np.sin(true_anomaly)
# pz = rayon_terre * np.sin(declinaison)


# plt.plot(degre(declinaison))
plt.grid()
plt.minorticks_on()
# plt.show()


