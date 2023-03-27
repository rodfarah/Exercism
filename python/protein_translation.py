def rna_to_codons(rna: str) -> list:
    '''Separates full rna strand into 3 by 3 nucleotides'''
    num_of_codons = int(len(rna) / 3)
    codons = []
    i = 0
    while len(codons) < num_of_codons:
        codons.append(rna[i:i+3])
        i += 3
    return codons


def proteins(strand: str) -> list:

    copro = {
        "Methionine": ["AUG"],
        "Phenylalanine": ["UUU", "UUC"],
        "Leucine": ["UUA", "UUG"],
        "Serine": ["UCU", "UCC", "UCA", "UCG"],
        "Tyrosine": ["UAU", "UAC"],
        "Cysteine": ["UGU", "UGC"],
        "Tryptophan": ["UGG"],
        "STOP": ["UAA", "UAG", "UGA"]}

    result = []
    break_out_flag = False
    for codon in rna_to_codons(strand):
        for k, v in copro.items():
            if codon in v and k == 'STOP':
                break_out_flag = True
            elif codon in v:
                result.append(k)
        if break_out_flag:
            break
    return result


print(proteins("AUGUUUUCUUAAAUG"))
