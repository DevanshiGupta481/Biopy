from Bio import AlignIO
alignment = AlignIO.read("clustalomega.sth", "stockholm")
print(alignment)
print("Alignment length %i" %alignment.get_alignment_length())
for record in alignment:
     print("%s - %s" % (record.seq, record.id))
for record in alignment:
     if record.dbxrefs:
         print("%s %s" % (record.id, record.dbxrefs))
        
for record in alignment:
     print(record)
from Bio import Phylo
tree = Phylo.read("clustalomega.sth","newick")
print(tree)
Phylo.draw_ascii(tree)
tree.rooted = True
Phylo.draw(tree)
