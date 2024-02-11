from graph_tools import Graph
  
if __name__ == '__main__': 
    g = {'1': ['2', '3','4'],
              '2': ['1', '3','4','5'],
              '3': ['1','2','4', '5','6'],
              '4': ['5','3','1','2','7'],
              '5': ['3','2','4','6','7'],
              '6': ['3', '5', '14', '12','13'],
              '7': ['4', '5', '8', '9','10'],
              '8': ['7','9','10','11'],
              '9': ['7','8','10','11'],
              '10': ['7','8','9','11'],
              '11': ['8','9','10'],
              '12': ['6','13','14','15'],
              '13': ['6','12','14','15'],
              '14': ['6','12','13','15'],
              '15': ['12','13','14']}
    graph = Graph(g)
    ###################################################
    community = ['2']
    assert graph.community_tightness(community) == 0
    print(graph.community_tightness(['1','2']))
    print(graph.community_tightness(['1','3']))
    print(graph.community_tightness(['1','4']))
    print(graph.community_tightness(['1','5']))
    print(graph.local_modularity_density(['2'], '1'))
    print(graph.local_modularity_density(['2'], '3'))
    
    
    community = ['1','2']
    print(graph.local_modularity_density(community, '3'))
    print(graph.local_modularity_density(community, '4'))
    print(graph.local_modularity_density(community, '5'))
