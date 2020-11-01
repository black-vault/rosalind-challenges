import os


def transcribe_dna(dataset):
    """ACGTA to ACGUA"""
    dataset = dataset.replace("T", "U")
    return dataset


def read_dataset():
    """Read dataset from a file"""
    with open(os.path.join(os.getcwd(), "dataset"),) as dataset:
        return dataset.read()


def main():
    dataset = read_dataset()
    rna = transcribe_dna(dataset)
    print(rna)


if __name__ == "__main__":
    main()