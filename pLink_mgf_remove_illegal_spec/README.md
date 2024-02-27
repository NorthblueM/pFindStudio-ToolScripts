
* **`mgf_remove_illegal_spec.py`**
## Function Introduction
* Since pLink does not support .d data from Bruker timsTOF, you need to extract the spectra as mgf files before using pLink to search them.
* However, some of the spectra in the mgf files extracted by third-party software lack the charge information of the precursor ion, which affects pLink’s ability to calculate its mass based on the mz information. In this case, you just need to remove these spectra from the mgf files. But don’t worry, the number of spectra missing header information such as charge is very small, and it will not affect the identification result.
* This script is for removing invalid spectra in mgf files that are missing some header information.

## How to Use
* You need to have python installed on your computer first to run this script.
1. Open the command window in the same folder as `mgf_remove_illegal_spec.py`. To do this, go to the folder where `mgf_remove_illegal_spec.py` is located and type `cmd` in the address bar, then press `Enter`.
2. Next, type the following command. `python mgf_remove_illegal_spec.py your_mgf_path`, where `your_mgf_path` is the path of your mgf file.
3. This will generate a new mgf file with `_legal.mgf` at the end in the same folder.
4. Then you just need to use pLink to load the new mgf ending with `_legal.mgf`.