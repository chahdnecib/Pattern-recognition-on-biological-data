import pandas as pd

fichier = r"uniprotkb_cytokines_AND_model_organism_2025_10_13.fasta"


# listes pour stocker les données
ids = []
noms = []
espèces = []
sequences = []

with open(fichier, 'r', encoding='utf-8') as f:
    sequence_courante = ""
    for ligne in f:
        ligne = ligne.strip()
        if ligne.startswith(">"):
            # si une séquence précédente existe, la stocker
            if sequence_courante:
                sequences.append(sequence_courante)
                sequence_courante = ""
            
            # analyser l'en-tête
            # exemple : >tr|A0A023HIB6|A0A023HIB6_HV1 Protein Tat OS=Human immunodeficiency virus type 1 OX=11676 GN=tat PE=3 SV=1
            parts = ligne[1:].split()  # enlever '>' et séparer par espaces
            
            # ID : deuxième élément après split('|')
            ids.append(parts[0].split('|')[1])
            
            # Nom : tout ce qui est avant "OS="
            nom = ' '.join(parts[1:])  # concatène le reste
            if "OS=" in nom:
                nom = nom.split("OS=")[0].strip()
            noms.append(nom)
            
            # Espèce : entre OS= et OX=
            espece = ""
            for part in parts:
                if part.startswith("OS="):
                    espece = part[3:]  # enlève "OS="
                    # Si le nom de l'espèce contient des espaces, concaténer jusqu'à trouver "OX="
                    i = parts.index(part) + 1
                    while i < len(parts) and not parts[i].startswith("OX="):
                        espece += " " + parts[i]
                        i += 1
                    espece = espece.strip()
                    break
            espèces.append(espece)
            
        else:
            # ajouter la ligne à la séquence courante
            sequence_courante += ligne

    # ajouter la dernière séquence
    if sequence_courante:
        sequences.append(sequence_courante)

# créer le DataFrame
df = pd.DataFrame({
    "id": ids,
    "nom": noms,
    "espèce": espèces,
    "séquence": sequences
})

# afficher les premières lignes
print(df.head())

# sauvegarder si besoin
df.to_csv("cytokines_dataframe.csv", index=False)
