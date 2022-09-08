import numpy as np
import matplotlib.pyplot as plt

puissance_saut=np.linspace(0.4,1.0,num=14)
hauteur_saut=-0.1817584952 * puissance_saut**3 + 3.689713992 * puissance_saut**2 + 2.128599134 * puissance_saut - 0.343930367
abscisses=[]
a=0.5
while a<=5:
	a+=0.5
	abscisses.append(a)

fig, ax=plt.subplots()
fig.set_size_inches(12.20,7.05)
ax.plot(puissance_saut,hauteur_saut)
ax.set_xlabel("Puissance de saut")
ax.set_ylabel("Hauteur de saut")
ax.set_title("Hauteur de saut en fonction de la puissance de saut")
ax.grid(True)
ax.set_xticks(ticks=[round(i,2) for i in puissance_saut])
ax.set_yticks(ticks=abscisses)
plt.savefig('Hauteur de saut.svg',transparent=True)
plt.show()