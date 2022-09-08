import numpy as np
import matplotlib.pyplot as plt

points_attaque=np.linspace(1,20,20)

points_defense_cuir=7
points_defense_or=11
points_defense_mailles=12
points_defense_fer=15
points_defense_diamant_netherite=20

robustesse_comf=0
robustesse_diamant=8
robustesse_netherite=12

degats_cuir=[]
texte="Armure en cuir : "
for i in range(len(points_attaque)):
	degats_cuir.append(points_attaque[i]*(1-max(points_defense_cuir/5,points_defense_cuir-points_attaque[i]/(2+robustesse_comf/4))/25))
	texte+=str(round(degats_cuir[-1],2))+" "
print(texte)

degats_or=[]
texte="Armure en or : "
for i in range(len(points_attaque)):
	degats_or.append(points_attaque[i]*(1-max(points_defense_or/5,points_defense_or-points_attaque[i]/(2+robustesse_comf/4))/25))
	texte+=str(round(degats_or[-1],2))+" "
print(texte)

degats_mailles=[]
texte="Armure en cotte de mailles : "
for i in range(len(points_attaque)):
	degats_mailles.append(points_attaque[i]*(1-max(points_defense_mailles/5,points_defense_mailles-points_attaque[i]/(2+robustesse_comf/4))/25))
	texte+=str(round(degats_mailles[-1],2))+" "
print(texte)

degats_fer=[]
texte="Armure en fer : "
for i in range(len(points_attaque)):
	degats_fer.append(points_attaque[i]*(1-max(points_defense_fer/5,points_defense_fer-points_attaque[i]/(2+robustesse_comf/4))/25))
	texte+=str(round(degats_fer[-1],2))+" "
print(texte)

degats_diamant=[]
texte="Armure en diamant : "
for i in range(len(points_attaque)):
	degats_diamant.append(points_attaque[i]*(1-max(points_defense_diamant_netherite/5,points_defense_diamant_netherite-points_attaque[i]/(2+robustesse_diamant/4))/25))
	texte+=str(round(degats_diamant[-1],2))+" "
print(texte)

degats_netherite=[]
texte="Armure en netherite : "
for i in range(len(points_attaque)):
	degats_netherite.append(points_attaque[i]*(1-max(points_defense_diamant_netherite/5,points_defense_diamant_netherite-points_attaque[i]/(2+robustesse_netherite/4))/25))
	texte+=str(round(degats_netherite[-1],2))+" "
print(texte)

fig, ax=plt.subplots()
fig.set_size_inches(12.20,7.05)
ax.plot(points_attaque,degats_cuir, 'o-', label="Armure en cuir", color='#7F3300')
ax.plot(points_attaque,degats_or, 'o-', label="Armure en or", color='yellow')
ax.plot(points_attaque,degats_mailles, 'bo-', label="Armure en cotte de mailles", color='#686868')
ax.plot(points_attaque,degats_fer, 'o-', label="Armure en fer", color='#999999')
ax.plot(points_attaque,degats_diamant, 'o-', label="Armure en diamant", color='cyan')
ax.plot(points_attaque,degats_netherite, 'ko-', label="Armure en netherite")

ax.set_xlabel("Points d'attaque")
ax.set_ylabel("Dégâts subis")
ax.set_title("Atténuation de l'attaque par les différentes armures complètes")
ax.legend()
ax.grid(True)
ax.set_xticks(ticks=points_attaque)
ax.set_yticks(ticks=[j for j in range(1,21)])

plt.savefig('Atténuation attaques.svg',transparent=True)
plt.show()