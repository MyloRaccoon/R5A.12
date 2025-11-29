import csv
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gammaincc
from fonctions import get_numbers, recup_all_in_one

# 6400/4 : pass pass
# 3200/8 : pass pass
# 1600/16: pass pass
# 800/32 : fail fail
# 400/64 : fail fail
# 200/128: fail pass X
# 100/256: fail pass
# 50/512 : fail pass
# 25/1024: fail pass

DEFAULT_N = 400
DEFAULT_M = 64


def test2(number: str, N = DEFAULT_N, M = DEFAULT_M, verbos = True) -> bool:

	if verbos:
		print(f'N = {N} | M = {M}')

	splited_number = []
	i = 0
	temp = []
	for n in number:

		temp.append(n)
		i += 1

		if i == M:
			i = 0
			splited_number.append(temp.copy())
			temp = []

	prs = []

	for part in splited_number:
		pr = 0
		for n in part:
			if n == '1':
				pr += 1
		prs.append(pr/M)

	weird_sum = 0
	for pr in prs:
		weird_sum += (pr - 1/2)**2

	val = 4 * M * weird_sum

	if verbos:
		print(f'val = {val}')

	igamcc = gammaincc(N/2, val/2)

	if verbos:
		print(f'igamcc = {igamcc}')

	return igamcc > 0.01,prs

def plot_histogram(prs1: list[float], prs2: list[float], N: int, M: int):
    """
    Génère et affiche l'histogramme comparatif des proportions de blocs.
    """
    plt.figure(figsize=(10, 6))
    
    # Détermination des intervalles (bins) pour l'histogramme
    # Les proportions de 1 sont des multiples de 1/M. Pour M=64, 1/M ≈ 0.0156.
    # On utilise un nombre de bins basé sur M pour une bonne résolution.
    bins = np.arange(0, 1.0 + 1/M, 1/M) 

    # Tracé des deux générateurs
    plt.hist(prs1, bins=bins, alpha=0.6, label='Générateur 1 (Biais de Proportion)', color='red', density=True)
    plt.hist(prs2, bins=bins, alpha=0.6, label='Générateur 2 (Biais de Structure)', color='green', density=True)
    
    # Ligne idéale
    # Pour M=64 et N=400, la proportion théorique suit approximativement une loi normale 
    # centrée sur 0.5 avec un écart type d'environ sqrt(0.25/M) ≈ 0.0625
    mu = 0.5
    sigma = np.sqrt(0.25 / M)
    x = np.linspace(0, 1, 1000)
    ideal_distribution = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma)**2)
    plt.plot(x, ideal_distribution, 'b--', label='Distribution Idéale (Théorique)')
    
    # Mise en forme du graphique
    plt.axvline(0.5, color='gray', linestyle=':', linewidth=1, label='Proportion Idéale (0.5)')
    plt.title(f'Distribution de la Proportion de "1" dans {N} Blocs de {M} Bits (Test 2)')
    plt.xlabel('Proportion de 1 dans le Bloc (pr_i)')
    plt.ylabel('Densité de Fréquence (Normalisée)')
    plt.legend()
    plt.grid(axis='y', alpha=0.5)
    plt.xlim(0.25, 0.75) # Limite l'affichage aux zones intéressantes
    plt.show()


def main():
    # --- Chargement des données (simulé) ---
    # Ces lignes nécessitent les fonctions et les fichiers de votre environnement
    # numbers_g1 = recup_all_in_one(get_numbers("generator1.csv"))
    # numbers_g2 = recup_all_in_one(get_numbers("generator2.csv"))
    
    # --- Données factices pour l'exemple (à remplacer par vos lignes ci-dessus) ---
    # Vous devez décommenter et utiliser vos données réelles
    # Si vous exécutez le code, vous devez vous assurer que les lignes 'numbers_g1' et 'numbers_g2' sont fonctionnelles.
    # Simuler un scénario basé sur vos résultats :
    # Generator 1 (biais vers 1)
    # Generator 2 (équilibré mais trop variable)
    
    try:
        numbers_g1 = recup_all_in_one(get_numbers("generator1.csv"))
        numbers_g2 = recup_all_in_one(get_numbers("generator2.csv"))
    except:
        print("\n--- ATTENTION: Impossible de charger les données CSV. Exécution interrompue. ---")
        print("Veuillez vous assurer que les fichiers 'generator1.csv' et 'generator2.csv' existent et que la librairie 'fonctions' est accessible.")
        return # Arrête l'exécution si les données ne sont pas chargées
    
    # --- Exécution du Test 2 pour G1 et G2 ---
    print("\n--- Résultats du Test 2 pour N=400, M=64 ---")
    
    print("\nGenerator 1")
    is_valid_g1, prs_g1 = test2(numbers_g1)
    
    print("\nGenerator 2")
    is_valid_g2, prs_g2 = test2(numbers_g2)
    
    # --- Génération du Graphique ---
    print("\n--- Génération de l'histogramme de comparaison ---")
    plot_histogram(prs_g1, prs_g2, DEFAULT_N, DEFAULT_M)

if __name__ == '__main__':
	main()
