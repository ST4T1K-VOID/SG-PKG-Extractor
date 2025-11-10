**CLI tool for .pkg extraction from SuperGiant games (Hades, Pyre, etc.).**

Comes packaged with [deppth](https://github.com/quaerus/deppth) by quaerus, which is used for .pkg extraction.
Currently, deppth only allows for single file extraction, this tool solve that problem by allowing you to enter a directory; the tool will search all files and sub-directorys for files with the `.pkg` file extention and than run the extraction command on it.

this tool also solves the problem of deppth extracting the files into the directory they were found, instead they are moved after extraction to a default (./output) or specified directory.

*tested games:*
- Hades II

*theoretically compatible:*
- Hades (I am unable to test this one myself currently), I
- Pyre,
- transistor,
- other, non-supergiant, .pkg files??

**possible issues**
deppth may not install properly unless you have the c++ buildtools installed (via visual studio)   
this is *roughly* what you should have:
<img width="891" height="210" alt="image" src="https://github.com/user-attachments/assets/ce2d69a7-effa-484e-94bd-6a9e433ee17f" />
<img width="1209" height="370" alt="image-1" src="https://github.com/user-attachments/assets/1dafaad0-b692-4ecc-aae7-5684c307c95b" />
(note the sidebar on this image)
