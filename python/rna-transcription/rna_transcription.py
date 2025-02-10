def to_rna(dna_strand: str):

    dna = "GCTA"
    rna = "CGAU"

    return dna_strand.translate(str.maketrans(dna, rna))
