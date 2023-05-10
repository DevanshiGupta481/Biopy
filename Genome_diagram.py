from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO
record = SeqIO.read("Progenbank.gb", "genbank")
gd_diagram = GenomeDiagram.Diagram("Glioma pathogenesis related protein-1 - GLIPR1")
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_feature_set = gd_track_for_features.new_set()
for feature in record.features:
     if feature.type!= "gene":
         #exclude this feature
         continue
     if len(gd_feature_set) % 2 == 0:
         color = colors.blue
     else:
         color = colors.lightblue
     gd_feature_set.add_feature(feature, color=color, label=True)

gd_diagram.draw(format="linear", orientation="landscape", pagesize="A4", fragments=4, start=0, end=len(record),)
gd_diagram.write("GLIPR1.pdf", "PDF")
gd_diagram.write("GLIPR1.png", "PNG")
