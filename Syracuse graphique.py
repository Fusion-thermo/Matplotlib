import matplotlib.pyplot as plt



#Initialisation
nombre=27
initial=nombre
compteur=0
x=[0]
y=[nombre]

#Calcul selon les règles de la conjoncture de Syracuse
while nombre!=1:
	compteur+=1
	x.append(compteur)
	if nombre%2==0:
		nombre=nombre//2
	else:
		nombre=nombre*3+1
	#print(nombre)
	y.append(nombre)
#print(x,y)


#Affichage du graphique
fig, ax=plt.subplots()
fig.set_size_inches(12.20,7.05)
ax.plot(x,y, '.-', label="Etapes", color='purple')
ax.set_xlabel("Nombres")
ax.set_ylabel("Nombre d'étapes")
ax.set_title("Nombre d'étapes avant de vérifier la conjoncture de Syracuse pour "+str(initial))
ax.legend()
ax.grid(True)
plt.show()

