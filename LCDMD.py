
class LCDMD:
    def __init__(self):
        return
    
    def core_area_detection(self, graph, seed_node):
        community = [seed_node]
        community_tightness = 0
        while community_tightness < 1:
            Vc = []
            community_neighbors = graph.find_community_neighbors(community)
            for node in community_neighbors:
                new_community = graph.add_node_to_community(node, community)
                new_community_tightness = graph.community_tightness(new_community)
                delta_tightness = new_community_tightness - community_tightness
                if delta_tightness >= 0:
                    Vc.append(node)
            if len(Vc)==0:
                print("No node was added to Vc !!!!!")
                break
            max_node = graph.max_local_modularity_density(community, Vc)
            community = graph.add_node_to_community(max_node, community)
            community_tightness = graph.community_tightness(community)
        return community

    def local_community_extension(self, graph, community):
        first_community = community
        community_tightness = graph.community_tightness(community)
        while community_tightness > 1:
            Sc = [];
            # Sc contains tuples of the nodes indexes and their influence in order (only nodes that have influence higher than 1)
            community_neighbors = graph.find_community_neighbors(community)
            for index, node in enumerate(community_neighbors):
                influence  = graph.node_influence(node, community)
                if influence > 1:
                    Sc.append((index, influence))
            if len(Sc) == 0:
                break
            Sc_prime = sorted(Sc, key=lambda x: x[1], reverse=True)
            lambda_value = 0.5
            #according to the article 0.5 as lambda value gives the highest accuracy
            Sns = []
            max_index = 0
            max_simcom = -1000
            # Sc contains tuples of the nodes indexes and their similarity with community in order
            # (only nodes that have similarity higher than lambda_value)
            for element in Sc_prime:
                node_index = element[0]
                simcom = graph.node_community_similarity(community_neighbors[node_index], community)
                if simcom > lambda_value:
                    Sns.append((node_index, simcom))
                if simcom > max_simcom:
                    max_simcom = simcom
                    max_index = node_index
            if not len(Sns) == 0:
                Smc = community_neighbors[max_index]
                community = graph.add_node_to_community(Smc, community)
            else:
                break
            community_tightness = graph.community_tightness(community)
        return community



