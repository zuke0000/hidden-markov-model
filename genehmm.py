import random

if __name__ == "__main__":
    ## TODO: Create input parameters
    ## EXAMPLE: genehmm emit > filename.out
    ## EXAMPLE: genehmm label < filename.in
    ## Take in 'emit' or 'label'
    ## take in '>' or '<'
    ## take in file name to specify what is being written to

    ## TODO: generate random sequence
    exonChance = {'exon': 0.95, 'end': 0.01, 'intron': 0.04}
    intronChance = {'intron': 0.95, 'exon': 0.05}
    exonLetters = {"A": 0.1,"C": 0.4,"G": 0.4,"T": 0.1}
    intronLetters = {"A": 0.4,"C": 0.1,"G": 0.1,"T": 0.4}

    endPrinted = False
    count = 0
    sequence = ''
    stateIsExon = True
    while (endPrinted == False):
        count += 1
        if (stateIsExon == True):
            randomStateChosen = random.choices(population=list(exonChance.keys()), weights=exonChance.values())[0]
        else:
            randomStateChosen = random.choices(population=list(intronChance.keys()), weights=intronChance.values())[0]

        if (randomStateChosen == 'exon'):
            stateIsExon = True
            randomLetter = random.choices(population=list(exonLetters.keys()), weights=exonLetters.values())[0] 
        if (randomStateChosen == 'intron'):
            stateIsExon = False
            randomLetter = random.choices(population=list(intronLetters.keys()), weights=intronLetters.values())[0]
        if (randomStateChosen == 'end'):
            endPrinted = True
    print('while loop ended, count:', count)
    # TODO: Left off here. From here, add letters to a sequence
    # Later on print this sequence with '/n' at the end

   # print('state', random.choices(population=list(exonChance.keys()), weights=exonChance.values())[0])
    #print('letter chosen', random.choices(population=list(exonLetters.keys()), weights=exonLetters.values())[0])


    ## TODO: write sequence to file