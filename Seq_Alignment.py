from Bio import SeqIO
record = SeqIO.read("sequence.fasta", "fasta")
record
record.seq
record.id
record.name
record.description
record.dbxrefs
from Bio import AlignIO
alignment = AlignIO.read("sequence.fasta", "fasta")
print(alignment)
print("Alignment length %i" %alignment.get_alignment_length())
for record in alignment:
    print("%s - %s" %(record.seq, record.id))
