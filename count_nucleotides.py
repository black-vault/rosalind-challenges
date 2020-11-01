import os


def calc_nucelotide(dataset, A, C, G, T):
    """Calculate ACGT in dataset"""

    for i in dataset:
        if i == "A":
            A+=1
        if i == "C":
            C+=1
        if i == "G":
            G+=1
        if i == "T":
            T+=1

    return A, C, G, T


def read_dataset():
    """Read dataset from a file"""
    with open(os.path.join(os.getcwd(), "dataset"),) as dataset:
        return dataset.read()


def main():
    dataset = read_dataset()
    A = 0
    C = 0
    G = 0
    T = 0
    A, C, G, T = calc_nucelotide(dataset, A, C, G, T)
    print(A,C,G,T)


if __name__ == "__main__":
    main()