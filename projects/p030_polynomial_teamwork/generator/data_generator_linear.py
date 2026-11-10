import numpy as np

class DataGenerator:
    def __init__(self, n=100, a=2.0, b=1.0 , noise_sd=0.5 , seed=42):
        """Initialise le générateur de données.

        Args:
            size (int): Nombre de valeurs à générer.
            seed (int | None): Graine pour la reproductibilité.
        """
        self.n = n
        self.a = a
        self.b = b
        self.noise_sd = noise_sd
        self.seed = seed

    def get_data(self):
        """Génère un vecteur selon une loi normale N(0, 1).

        Returns:
            numpy.ndarray: Vecteur de réels, de forme (size,).
        """
        x = np.random.normal(loc=0, scale=1, size=self.n)
        y = self.a * x + self.b

        data= np.column_stack((x, y))
        
        return data
if __name__ == "__main__":
    generator = DataGenerator(n=100, a=2.0, b=1.0, noise_sd=0.5, seed=42)
    data = generator.get_data()
    print(data)

