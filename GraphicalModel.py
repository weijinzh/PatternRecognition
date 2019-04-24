import bif_parser
import prettytable
import pydotplus
from IPython.core.display import display, Image
from bayesian.bbn import *


# Basic Function for Generating Graphs
# def show_graphgiz_image(graphviz_data):
#    graph = pydotplus.graph_from_dot_data(graphviz_data)
#    graph.write_png('temp.png')
#    return 'temp.png'

name = 'asia'
module_name = bif_parser.parse(name)
module = __import__(module_name)
bg = module.create_bbn()



# Initializing Potentials
assignments = jt.assign_clusters(bg)
jt.initialize_potentials(assignments, bg)


jt.propagate()

# Query with Evidences
#jt.query(Xray='True')

bronc_clust = [i for i in jt.clique_nodes for v in i.variable_names if v =='xray']
pot = bronc_clust[0].potential_tt

# A function to return the sum for a specific assignment, such as 'bronc,yes'
sum_assignments =lambda imap, tup: sum([v for k, v in imap.iteritems() for i in k if i == tup])
print pot

# Get the sum for bronc=yes and bronc=no
yes, no =[sum_assignments(pot, ('xray', i)) for i in ['yes', 'no']]
print 'xray: yes ', yes/float(yes+no), " no ", no/float(yes+no)
