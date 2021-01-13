class Hamming:
    def distance(self, gene1, gene2):
        if len(gene1) != len(gene2):
            raise ValueError('Genes have different lenghts')
        diff = 0
        for i in range(0, len(gene1)):
            if gene1[i] != gene2[i]:
                diff += 1
        return diff