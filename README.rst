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
	--reference  Path to reference sequences: ALU and L1HS
	--reads  Path to your short reads, in FASTQ format

Optional parameter:
	--ThreadsN  max Threads For parallel computing in BWA alignment process
	--outdir  Output directory

Example:

For human:
	$ aluline --reference rnainigo/lib/ref.fa --ThreadsN 32 --reads read1.fq.gz read2.fq.gz --outdir output

For mouse:
	$ aluline --reference rnainigo/lib/mousub.ref --ThreadsN 32 --reads read1.fq.gz read2.fq.gz --outdir output
