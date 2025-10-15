import pandas as pd
from collections import Counter
from itertools import product

def generate_ngrams(sequence, n):
    """Generate n-grams from a given sequence"""
    return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]

def main():
    # 1️⃣ Charger le fichier CSV
    df = pd.read_csv("cytokines_dataframe.csv")

    # 2️⃣ Garder uniquement les colonnes utiles
    df = df[['id', 'séquence']]

    # 3️⃣ Définir tous les acides aminés possibles (Alphabet protéique)
    amino_acids = set("ACDEFGHIKLMNPQRSTVWY")  # Peut être ajusté selon vos données

    # 4️⃣ Créer toutes les combinaisons possibles pour 1-gram, 2-gram et 3-gram
    all_1grams = sorted(list(amino_acids))
    all_2grams = sorted([''.join(p) for p in product(amino_acids, repeat=2)])
    all_3grams = sorted([''.join(p) for p in product(amino_acids, repeat=3)])

    # 5️⃣ Liste finale de toutes les colonnes de features
    feature_columns = all_1grams + all_2grams + all_3grams

    # 6️⃣ Initialiser le tableau final des features
    features = []

    for _, row in df.iterrows():
        seq_id = row['id']
        sequence = str(row['séquence']).strip()

        # Générer n-grams
        grams_1 = generate_ngrams(sequence, 1)
        grams_2 = generate_ngrams(sequence, 2)
        grams_3 = generate_ngrams(sequence, 3)

        # Compter fréquences
        counts = Counter(grams_1 + grams_2 + grams_3)

        # Créer un dictionnaire avec id + fréquences
        row_features = {'id': seq_id}
        for gram in feature_columns:
            row_features[gram] = counts.get(gram, 0)

        features.append(row_features)

    # 7️⃣ Convertir en DataFrame final
    features_df = pd.DataFrame(features)

    # 8️⃣ Sauvegarder en CSV
    features_df.to_csv("features_ngrams.csv", index=False)
    print("✅ Extraction terminée ! Fichier enregistré : features_ngrams.csv")


if __name__ == "__main__":
    main()
