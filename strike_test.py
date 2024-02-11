#include all the necessary tools
from strike_graph import make_strike_graph
from graph_tools import Graph
from LCDMD import LCDMD
from measurments import f1_score

# make a list implementation of your graph
# here I have used strike graph
strike_graph = make_strike_graph()
c = 0
for ke in strike_graph.keys():
    c += len(strike_graph[ke])
print("strike network has ", len(strike_graph.keys())," nodes ")
print("strike network has ", c," edges ")
g = Graph(strike_graph)

#make an LCDMD instance for executing the
#article's algorithms
lcdmd = LCDMD()

#Find each node's community found by LCDMD
#calculate f1 score for the found community 
#calculate the average of f1 score for all nodes of the graph
sum = 0
for node in strike_graph.keys():
    seed_node = node
    
    #find the core area according to what is mentioned in the article
    core_area = lcdmd.core_area_detection(g, seed_node)
    
    #extend the found core area community
    extended_community = lcdmd.local_community_extension(g, core_area)
    
    #calculate the f1 score of that
    f1 = f1_score(seed_node, extended_community)
    
    
    #print(f1)
    sum += f1
    
#report the average value
print("the average value of f1 score is ", sum/len(strike_graph.keys()))
