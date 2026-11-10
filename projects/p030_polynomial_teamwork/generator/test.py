import numpy as np
from plotly import data

class DataGenerator:
    def __init__(self, n=1000, noise_sd=0.5 , seed=[42, 404], puissance=[9, 4]):
        # """Initialise le générateur de données.

        # Args:
        #     size (int): Nombre de valeurs à générer.
        #     seed (int | None): Graine pour la reproductibilité.
        # """
        self.n = n
        self.noise_sd = noise_sd
        self.seed = seed
        self.puissance = puissance

    def get_data(self):
        """Retourne un tableau NumPy de forme (n, 2)."""
        # print(self.seed[0])
        # print(self.seed[1])
        # print(self.n//2)
        for i in range(2):
            # print(i)
            data = np.empty((0, 3))
            for j in range(2):
                #variable group
                group = j+1

                rng = np.random.default_rng(self.seed[i])

                # Génération de x selon une loi normale N(0, 1)
                divise = self.n//2
                
                x = rng.normal(loc=0, scale=1, size=divise)

                # Bruit gaussien centré, indépendant de x
                epsilon = rng.normal(
                    loc=0,
                    scale=self.noise_sd,
                    size=divise
                )
                
                # print(self.puissance[i]+1)
                
                # Coefficients aléatoires du polynôme
                coefficients = rng.normal(loc=0, scale=1, size=self.puissance[i]+1)
                
                print(f"coefficients_puissance_{self.puissance[i]}___: {coefficients}")

                # Polynôme de degré 4
                y1 = np.polynomial.polynomial.polyval(x, coefficients)


                # Ajout du bruit
                y = y1 + epsilon


                # Colonne 0 : x ; colonne 1 : y
                data_test = np.column_stack((x, y, np.full(len(x), group)))
                
                data = np.vstack((data, data_test))

                
                nomfichier = "data_group_"+str(i+1)+"__puissance_"+str(self.puissance[i])+"__"+str(self.seed[i])+".csv"

                np.savetxt(
                    nomfichier,
                    data,
                    delimiter=";",
                    header="x,y,group",
                    comments="",
                    fmt="%g"
                )
            # print(f"Data_du_Seed_: {self.seed[i]}")
            
            # print(data)
                              
        return data            
if __name__ == "__main__":
    generator = DataGenerator(n=200, noise_sd=0.5, seed=[42, 404], puissance=[9, 4])
    data = generator.get_data()        
    assert isinstance(data, np.ndarray), "Ce n est pas un tableau numpy"
    print("C est un tableau numpy")  
    