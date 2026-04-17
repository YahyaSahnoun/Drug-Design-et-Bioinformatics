import random
from typing import List

def fitness(molecule: List[float]) -> float:
    activity, toxicity, solubility = molecule
    return activity - toxicity + solubility


def generate_molecule() -> List[float]:
    return [
        random.uniform(0, 10),  # activité
        random.uniform(0, 10),  # toxicité
        random.uniform(0, 10)   # solubilité
    ]


def mutate(molecule: List[float]) -> List[float]:
    return [
        value + random.uniform(-1, 1)
        for value in molecule
    ]


def optimize(iterations: int=100):

    # créer population initiale
    population = [generate_molecule() for _ in range(10)]

    for i in range(iterations):

        # trier selon le score
        population = sorted(population, key=fitness, reverse=True)

        # garder les meilleurs
        best = population[:5]

        # créer nouvelle population
        new_population = best.copy()

        for mol in best:
            new_population.append(mutate(mol))

        population = new_population

    # meilleur résultat final
    best_molecule = max(population, key=fitness)
    return best_molecule, fitness(best_molecule)


if __name__ == "__main__":
    best =  optimize()
    print("the best result is", best[0], "with a score of", best[1])
