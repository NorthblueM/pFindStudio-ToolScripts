
The primary function of this script is to reduce the original database and generate a smaller FASTA file based on the proteins identified by pFind.

**Application**:
For optimal efficiency, we recommend first using the [pFind3](https://github.com/pFindStudio/pFind3) search engine to identify regular linear peptides and mono-linked peptides. Then, based on the identified proteins, build a new, smaller database and feed it into [pLink3](https://github.com/pFindStudio/pLink3) for cross-linking analysis. This workflow will significantly reduce pLink's search time and improve sensitivity.

**Usage**:

1. Open the `build_pfind_fasta.ipynb` file (a Jupyter Notebook).
2. Modify the following paths:
   - `<fpath_fasta>`: Path to the original FASTA file.
   - `<fpath_pfind>`: Path to the pFind identification results.
   - `<fpath_out>`: Output path for the reduced FASTA file.
