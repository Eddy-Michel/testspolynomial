import numpy as np
from plotly import data
from pathlib import Path


class DataGenerator:
    def __init__(self, n=1000, noise_sd=0.5, seed=[42, 404], puissance=[9, 4]):
        # """Initialise le générateur de données.

        # Args:
        #     size (int): Nombre de valeurs à générer.
        #     seed (int | None): Graine pour la reproductibilité.
        # """
        self.n = n
        self.noise_sd = noise_sd
        self.seed = seed
        self.puissance = puissance

    def get_data(self):        #"""Retourne un tableau NumPy de forme (n, 2)."""
        # print(self.seed[0])
        # print(self.seed[1])
        # print(self.n//2)
        
        coefficients_9 = [-0.06, -0.73, -0.41,  0.63,  0.0, 0.34,  0.67, -0.37,  0.76,  0.38]
        
        coefficients_4 = [-1.02,  0.37, -1.4,  -2.06, -0.99]
        
        fich = ["A", "B"]
        
        for i in range(2):
            # print(i)
            
            data = np.empty((0, 3))
            
            for j in range(2):
                #variable group
                group = j+1
                # print(f"groupe_: {group}")

                rng = np.random.default_rng(self.seed[i])

                # Génération de x selon une loi normale N(0, 1)
                divise = self.n//2
                
                # print(f"nombre_valeurs_: {divise}")
                
                x = rng.normal(loc=0, scale=1, size=divise)

                # Bruit gaussien centré, indépendant de x
                epsilon = rng.normal(
                    loc=0,
                    scale=self.noise_sd,
                    size=divise
                )
                
                # # Génération de X
                # x = rng.uniform(-10, 10, size=divise)

                # # Génération du bruit
                # epsilon = rng.uniform(-0.5, 0.5, size=divise)
                                
                                    
                # print(self.puissance[j])
                
                # Coefficients aléatoires du polynôme

                # coefficients = np.round(rng.normal(loc=0, scale=1, size=self.puissance[i]+1),2)

                # print(f"coefficients_puissance_{self.puissance[i]}___: {coefficients}") 
                               
                # print(f"coefficients_du_Seed_: {self.seed[i]}")
                
                if(self.puissance[j] == 9):
                    coefficients = coefficients_9
                
                else:
                    coefficients = coefficients_4
                    
                # print(f"coefficient_puissance_{self.puissance[j]}___: {coefficients}")                
                
                # print(f"seed_du_coefficient: {self.seed[i]}")
                
                # Polynôme de degré n
                y1 = np.polynomial.polynomial.polyval(x, coefficients)

                # Ajout du bruit
                y = y1 + epsilon

                # Colonne 0 : x ; colonne 1 : y
                data_test = np.column_stack((x, y, np.full(len(x), group)))
                
                data = np.vstack((data, data_test))
                
            # Chemin du dossier où se trouve les data fichiers csv.
            chemin1 = str(Path(__file__).resolve().parents[3])+"\\data\\p030_polynomial_teamwork"
            
            cheminfichier = chemin1 +"\\"+ f"data_group_{fich[i]}.csv"
            
            print(cheminfichier)
            
            # nomfichier = "data_group_"+str(i+1)+"__"+str(self.seed[i])+".csv"
            
            nomfichier = cheminfichier
                                     
            np.savetxt(
                nomfichier,
                data,
                delimiter=";",
                header="x;y;group",
                comments="",
                fmt="%g"
            )
            # print(f"Data_du_Seed_: {self.seed[i]}")
            
            # print(data)
                              
        return data            
if __name__ == "__main__":
    generator = DataGenerator(n=1000, noise_sd=0.5, seed=[42, 404], puissance=[9, 4])
    data = generator.get_data()        
    assert isinstance(data, np.ndarray), "Ce n est pas un tableau numpy"
    print("C est un tableau numpy")  
    