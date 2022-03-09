import re
class DNA:
    def __init__(self, sequence: str):
        self.sequence = sequence
        self.dna_check()

    def dna_check(self):
        bad_seq = r'[^ATGC]'
        if re.search(bad_seq, self.sequence):
            raise ValueError("Wrong sequence. The string should contain only A, T, G, C.")

    def gc_content(self):
        counter = 0
        for position in self.sequence:
            if position == 'G' or position == 'C':
                counter += 1
        content = counter / len(self.sequence) * 100
        return content

    def reverse_complement(self):
        complement_table = {'A': 'T',
                      'T': 'A',
                      'G': 'C',
                      'C': 'G'}
        complement_sequence = []
        for nuc in self.sequence:
            complement_sequence.append(complement_table[nuc])
        complement_sequence.reverse()
        reverse_sequence = ''.join(map(str, complement_sequence))
        return reverse_sequence

    def transcribe(self):
        transcribe_table = {'A': 'U',
                                 'T': 'A',
                                 'G': 'C',
                                 'C': 'G'}
        rna = []
        for nuc in self.sequence:
            rna.append(transcribe_table[nuc])
        sequence = ''.join(map(str, rna))
        return RNA(sequence)

    def __iter__(self):
        return iter(self.sequence)




class RNA:
    def __init__(self, sequence: str):
        self.sequence = sequence
        self.rna_check()


    def rna_check(self):
        bad_seq = r'[^AUGC]'
        if re.search(bad_seq, self.sequence):
            raise ValueError("Wrong sequence. The string should contain only A, U, G, C.")

    def gc_content(self):
        counter = 0
        for position in self.sequence:
            if position == 'G' or position == 'C':
                counter += 1
        content = counter / len(self.sequence) * 100
        return content

    def reverse_complement(self):
        complement_table = {'A': 'U',
                            'U': 'A',
                            'G': 'C',
                            'C': 'G'}
        complement_sequence = []
        for nuc in self.sequence:
            complement_sequence.append(complement_table[nuc])
        complement_sequence.reverse()
        reverse_sequence = ''.join(map(str, complement_sequence))
        return reverse_sequence

    def __iter__(self):
        return iter(self.sequence)

