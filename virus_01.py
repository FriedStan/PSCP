"""Why no Count? Isn't it in string method"""


def virus(dna):
    """Virus101"""
    virus_body = 0
    for rna in dna:
        if rna == "o":
            virus_body += 1
    return virus_body


print(virus(str(input())))
