RNAinigo
---------
Contact: ptdtan@gmail.com
---------

To install, simply do as "root":
	$ cd rnainigo/
	$ python setup.py install

Usage:
	$ rnainigo -r=<reference/path> -f=<reads/path> [-n=maxThreads]

Some parameters required to have the program work:
	-r=<reference/path> Path to your reference sequence
	-f=<reads/path> Path to your short reads, in FASTQ format
Optional parameter:
	-n=<maxThreads> For parallel computing in BWA alignment process
	
