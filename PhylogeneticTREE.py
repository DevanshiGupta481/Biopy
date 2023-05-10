from Bio import Phylo
tree = Phylo.read("clustalw.dnd","newick")
print(tree)
Phylo.draw_ascii(tree)
tree.rooted = True
Phylo.draw(tree)
