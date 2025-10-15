# liste des fichiers à fusionner
fichiers = [
    r"uniprotkb_cytokines_2025_10_13.fasta",
    r"uniprotkb_cytokines_AND_model_organism_2025_10_13.fasta",
    r"uniprotkb_cytokines_AND_model_organism_2025_10_13.fasta (1)",
    r"uniprotkb_cytokines_AND_model_organism_2025_10_13.fasta (2)",
    r"uniprotkb_cytokines_AND_model_organism_2025_10_13.fasta (3)",
    r"uniprotkb_cytokines_AND_model_organism_2025_10_13.fasta (4)"
]


# nom du fichier final
fichier_sortie = "fusion.txt"

# ouvrir le fichier de sortie en écriture
with open(fichier_sortie, "w", encoding="utf-8") as outfile:
    for nom_fichier in fichiers:
        with open(nom_fichier, "r", encoding="utf-8") as infile:
            contenu = infile.read()
            outfile.write(contenu)
            outfile.write("\n")  # ajouter un saut de ligne entre les fichiers
