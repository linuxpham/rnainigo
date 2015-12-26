RNAinigo
---------
Contact: ptdtan@gmail.com
---------

To install, simply do as "root":
	$ cd rnainigo/
	$ python setup.py install

Usage:
$ aluline --reference <humrep.ref> <humsub.ref> --ThreadsN <number of threads> --reads <read1.fq> [read2.fq] --outdir [output directory]

Some parameters required to have the program work:
	--reference  Path to two reference sequences ALU and LINE
	--reads  Path to your short reads, in FASTQ format
Optional parameter:
	--ThreadsN  max Threads For parallel computing in BWA alignment process
Example:
$ aluline --reference rnainigo/lib/humrep.ref rnainigo/lib/humsub.ref --ThreadsN 32 --reads read1.fq.gz read2.fq.gz --outdir output

	
