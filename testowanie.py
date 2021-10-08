def DNA_strand(dna):
    out=''
    code = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([code[i] for i in dna])

print(DNA_strand('ATTGC'))
    
