def to_rna(dna_strand):
    transcribed_rna = []
    num_of_nucleotides = 0
    final_transcription = str()
    while num_of_nucleotides < 4:
        for nucleotides in dna_strand:
            if nucleotides == 'G':
                transcribed_rna.append('C')
                num_of_nucleotides += 1
            elif nucleotides == 'C':
                transcribed_rna.append('G')
                num_of_nucleotides += 1
            elif nucleotides == 'T':
                transcribed_rna.append('A')
                num_of_nucleotides += 1
            elif nucleotides == 'A':
                transcribed_rna.append('U')
                num_of_nucleotides += 1
        return final_transcription.join([item for item in transcribed_rna])

print(to_rna('GCTA'))