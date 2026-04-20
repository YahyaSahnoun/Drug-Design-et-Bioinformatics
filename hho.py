from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors

smiles = "CCO"
mol = Chem.MolFromSmiles(smiles)

print(mol)

img = Draw.MolToImage(mol)
img.show()


def molecule_features(smiles):
    mol = Chem.MolFromSmiles(smiles)

    return [
        Descriptors.MolWt(mol),        # poids moléculaire
        Descriptors.NumHDonors(mol),   # donneurs d’hydrogène
        Descriptors.NumHAcceptors(mol) # accepteurs
    ]