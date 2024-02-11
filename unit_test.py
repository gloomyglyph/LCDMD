from graph_tools import Graph





if __name__ == '__main__':
    g = {'A': ['B', 'C'],
             'B': ['C', 'D','A'],
             'C': ['A','B','D', 'F'],
             'D': ['B','C'],
             'E': [],
             'F': ['C']}
    graph = Graph(g)
    ###################################################
    assert graph.are_same_nodes('A', 'B') == False
    ###################################################
    assert graph.find_node_neighbors('A') == g['A']
    ###################################################
    assert graph.is_node_in_community('D', graph.find_node_neighbors('C')) == True
    ###################################################
    assert graph.are_nodes_connected('D', 'E') == False
    ###################################################
    assert graph.node_degree('D') == 2
    ###################################################
    assert graph.common_nodes(graph.find_node_neighbors('A'), ['B', 'C']) == ['B', 'C']
    ###################################################
    # assert graph.jaccard_coefficient('C', 'D') == 1/3
    # assert graph.jaccard_coefficient('A', 'F') == 1 / 2
    # assert graph.jaccard_coefficient('B', 'F') == 1 / 3
    # assert graph.jaccard_coefficient('E', 'F') == 0
    ###################################################
    assert graph.internal_tightness(['A', 'B', 'C']) == graph.jaccard_coefficient('A', 'B') + \
           graph.jaccard_coefficient('A', 'C') + graph.jaccard_coefficient('C', 'B')
    ###################################################
    # print(graph.jaccard_coefficient('A', 'B'))
    # print(graph.jaccard_coefficient('A', 'C'))
    # print(graph.jaccard_coefficient('C', 'B'))
    # print(graph.internal_tightness(['F', 'B', 'C']))
    # print(graph.external_tightness(['D', 'B', 'C']))
    #print(graph.external_tightness(['A','B','C']))
    # print(graph.community_tightness(['A', 'B', 'C']))
    # print(graph.community_tightness(['B', 'C']))
    # print(graph.community_tightness(['A', 'B']))
    # print(graph.community_tightness(['A']))
    # print(graph.community_tightness(['A', 'B', 'F']))
    # print(graph.community_tightness(['F']))
    ###################################################
    assert graph.community_outside_degree(['A','B', 'C']) == 3
    assert graph.community_outside_degree(['E']) == 0
    assert graph.community_outside_degree(['F']) == 1
    ###################################################
    assert graph.community_degree(['A', 'B', 'C']) == 9
    assert graph.community_degree(['E']) == 0
    assert graph.community_degree(['A', 'B', 'C']) == 9
    assert graph.community_degree(['F', 'B']) == 4
    ###################################################
    assert graph.community_inside_degree(['A', 'B', 'C']) == 3
    assert graph.community_inside_degree(['A', 'C']) == 1
    assert graph.community_inside_degree(['C']) == 0
    assert graph.community_inside_degree(['F', 'B', 'C']) == 2
    assert graph.community_inside_degree(['D', 'E', 'C']) == 1
    assert graph.community_inside_degree(['F']) == 0
    assert graph.community_inside_degree(['E']) == 0
    ###################################################
    assert graph.pc(['A', 'B', 'C']) == 1
    assert graph.pc(['A', 'E', 'C']) == 1/3
    assert graph.pc(['B', 'E', 'C']) == 1/3
    assert graph.pc(['F', 'E']) == 0
    assert graph.pc(['A', 'B', 'D']) == 2/3
    assert graph.pc(['A']) == 0
    ###################################################
    assert graph.r('A', ['A', 'B', 'C']) == 1
    assert graph.r('B', ['A', 'B', 'D']) == 0
    ###################################################
    assert graph.node_community_similarity('A', ['A', 'B', 'C']) == 0
    assert graph.node_community_similarity('B', ['A', 'D', 'B']) == 1
    assert graph.node_community_similarity('C', ['A', 'F', 'C']) == 1
    assert graph.node_community_similarity('C', ['E', 'F', 'C']) == 1
    assert graph.node_community_similarity('F', ['B', 'F', 'C']) == 0
    ###################################################

    
    
    
    
    
    
    
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
    #assert (graph.community_tightness(['1','2']) - graph.community_tightness(community)) == 0.2409
    print(graph.community_tightness(['1','2']))
    print(graph.community_tightness(['1','3']))
    print(graph.community_tightness(['1','4']))
    #print(graph.local_modularity_density(['2'], '1'))
    print(graph.local_modularity_density(['2'], '3'))
    
    print("salam bar khomeini")
    print("salam bar khamenei")