from copy import deepcopy
class Graph:
    #list implementation of the graph
    def __init__(self, graph):
        self.graph = graph

    # returns a new list in which the given node is added
    def add_node_to_community(self, node, community):
        new_community = deepcopy(community)
        new_community.append(node)
        return new_community

    # returns a list of the nodes neighbors
    def find_node_neighbors(self, node):
        return self.graph[node]
    
    # returns boolean if nodes are the same
    def are_same_nodes(self, u_node, v_node):
        return u_node == v_node

    # returns boolean if a node is in that community
    def is_node_in_community(self, node, community):
        return node in community

    # returns boolean if two nodes have an edge which connects them together
    def are_nodes_connected(self, u_node, v_node):
        return v_node in self.graph[u_node]

    # returns in integer of number of nodes vertices
    def node_degree(self, node):
        return len(self.graph[node])
    
    # node influence coefficient of the article
    def node_influence(self, node, community):
        node_neighbors = self.find_node_neighbors(node)
        deg_in = 0
        deg_out = 0
        for neighbor in node_neighbors:
            if self.is_node_in_community(neighbor, community):
                deg_in += 1
            else:
                deg_out += 1
        if deg_out == 0:
            return 0
        influence = deg_in/deg_out
        return influence
    
    # max local modularity density coefficient of the article
    def max_local_modularity_density(self, community, nodes):
        independent_value = self.independent_lmd_value(community)
        qc = []
        qlmax = -1000
        max_element_index = 0
        for index, node in enumerate(nodes):
            q = independent_value + self.r(node, community)
            if q > qlmax:
                qlmax = q
                max_element_index = index
            qc.append(q)
        try:
            return nodes[max_element_index]
        except:
            print('as')

    # independent lmd value coefficient of the article
    def independent_lmd_value(self, community):
        try:
            cid = self.community_inside_degree(community)
            cod = self.community_outside_degree(community)
            cd = self.community_degree(community)
            pc = self.pc(community)
            return (cid / cd) * pc - (cod / (cd * pc)) ** 2
        except:
            print("Makhraj 0 shod haji")
        
    # local modularity density coefficient of the article
    def local_modularity_density(self, community, node):
        community =  self.add_node_to_community(node, community)
        return self.independent_lmd_value(community) + self.r(node, community)

    # returns a list of nodes outside a community which are connected to it by a vertice
    def find_community_neighbors(self, community):
        community_neighbors = []
        neighbors_set = set()
        for node in community:
            node_neighbors = self.find_node_neighbors(node)
            for neighbor in node_neighbors:
                if not self.is_node_in_community(neighbor, community):
                    neighbor_hash = str(neighbor)
                    if neighbor_hash in neighbors_set:
                        continue
                    else:
                        neighbors_set.add(neighbor_hash)
                        community_neighbors.append(neighbor)
        return community_neighbors

    # counting how many edges are there inside a community
    def community_connecting_edges_number(self, community):
        edges_number = 0
        # community_connecting_edges returns number of edges connecting a community members to each other
        seen_vertices = set()
        # seen_vertices are for saving the compared two nodes' hash in order to avoid repetitive comparison
        for node in community:
            for other_node in community:
                if self.are_same_nodes(node, other_node):
                    continue
                vertice = str(node) + str(other_node)
                if vertice in seen_vertices:
                    continue
                else:
                    # two possible sequence of hashes are saved in order to access any sequence and avoid extra hash making
                    second_vertice = str(other_node) + str(node)
                    seen_vertices.add(vertice)
                    seen_vertices.add(second_vertice)
                    if self.are_nodes_connected(other_node, node):
                        edges_number += 1
                    else:
                        continue
        return edges_number

    # pc coefficient of the article
    def pc(self, community):
        Ec = self.community_connecting_edges_number(community)
        Vc = len(community)
        if Vc == 1:
            return 1
        return 2*Ec/(Vc*(Vc-1))

    # r coefficient of the article
    def r(self, node, community):
        neighbors = self.find_node_neighbors(node)
        neighbors_in_commnity = []
        for neighbor in neighbors:
            if self.is_node_in_community(neighbor, community):
                neighbors_in_commnity.append(neighbor)
        ksi_summation = self.community_connecting_edges_number(neighbors_in_commnity)
        try:
            r_value = ksi_summation / (len(neighbors_in_commnity)*(len(neighbors_in_commnity)-1)/2)
            return r_value
        except:
            return 0       

    # node community similarity coefficient of the article
    def node_community_similarity(self, node, community):
        node_neighbors = self.find_node_neighbors(node)
        community_neighbors = self.find_community_neighbors(community)
        common_neighbors = self.common_nodes(node_neighbors, community_neighbors)
        return len(common_neighbors)/min(len(node_neighbors), len(community_neighbors))

    # community inside degree is the sum of all of the edges which connect 
    # two nodes of that community to outside
    def community_outside_degree(self, community):
        seen_vertices = set()
        degree_summation = 0
        for node in community:
            node_neighbors = self.find_node_neighbors(node)
            for neighbor in node_neighbors:
                vertice = str(node) + str(neighbor)
                if vertice in seen_vertices:
                    continue
                else:
                    if not self.is_node_in_community(neighbor, community):
                        degree_summation += 1
                        second_vertice = str(neighbor) + str(node)
                        seen_vertices.add(vertice)
                        seen_vertices.add(second_vertice)
        return degree_summation

    # community inside degree is the sum of all of the edges which connect 
    # two nodes of that community together
    def community_inside_degree(self, community):
        seen_vertices = set()
        degree_summation = 0
        for node in community:
            node_neighbors = self.find_node_neighbors(node)
            for neighbor in node_neighbors:
                vertice = str(node) + str(neighbor)
                if vertice in seen_vertices:
                    continue
                else:
                    if self.is_node_in_community(neighbor, community):
                        degree_summation += 1
                        second_vertice = str(neighbor) + str(node)
                        seen_vertices.add(vertice)
                        seen_vertices.add(second_vertice)
        return degree_summation

    # community degree is the sum of all of its nodes degrees
    def community_degree(self, community):
        community_degree = 0
        for node in community:
            community_degree += self.node_degree(node)
        return community_degree

    # tightness of a community 
    def community_tightness(self, community):
        external_tightness_value = self.external_tightness(community)
        internal_tightness_value = self.internal_tightness(community)
        if external_tightness_value == 0:
            return 0
        community_tighness = internal_tightness_value / external_tightness_value
        return community_tighness

    # integral tightness of a community 
    def external_tightness(self, community):
        # jaccard_summation has the accumulated values of every two possible nodes which are connected
        jaccard_summation = 0
        seen_vertices = set()
        # seen_vertices are for saving the compared two nodes' hash in order to avoid repetitive comparison
        for node in community:
            node_neighbors = self.find_node_neighbors(node)
            for neighbor in node_neighbors:
                vertice = str(node) + str(neighbor)
                if vertice in seen_vertices:
                    continue
                else:
                    # two possible sequence of hashes are saved in order to access any sequence and avoid extra hash making
                    second_vertice = str(neighbor) + str(node)
                    seen_vertices.add(vertice)
                    seen_vertices.add(second_vertice)
                    if not self.is_node_in_community(neighbor, community):
                        if self.are_nodes_connected(node, neighbor):
                            jaccard_summation += self.jaccard_coefficient(node, neighbor)
        return jaccard_summation

    # integral tightness of a community 
    def internal_tightness(self, community):
        #jaccard_summation has the accumulated values of every two possible nodes which are connected
        jaccard_summation = 0
        seen_vertices = set()
        # seen_vertices are for saving the compared two nodes' hash in order to avoid repetitive comparison
        for node in community:
            for other_node in community:
                if self.are_same_nodes(node, other_node):
                    continue
                vertice = str(node) + str(other_node)
                if vertice in seen_vertices:
                    continue
                else:
                    # two possible sequence of hashes are saved in order to access any sequence and avoid extra hash making
                    second_vertice = str(other_node) + str(node)
                    seen_vertices.add(vertice)
                    seen_vertices.add(second_vertice)
                    if self.are_nodes_connected(other_node, node):
                        jaccard_number = self.jaccard_coefficient(node, other_node)
                        jaccard_summation += jaccard_number
                    else:
                        continue
        return jaccard_summation

    # jaccard coefficient of two series 
    def jaccard_coefficient(self, u_node, v_node):
        u_neighbors = self.find_node_neighbors(u_node)
        v_neighbors = self.find_node_neighbors(v_node)
        # # counter nodes in each others neighbors should not be considered
        # if v_node in u_neighbors:
        #     u_neighbors.remove(v_node)
        # if u_node in v_neighbors:
        #     v_neighbors.remove(u_node)
        common_neighbors = self.common_nodes(u_neighbors, v_neighbors)
        accumulated_neighbors = self.accumulation_of_nodes(u_neighbors, v_neighbors)
        #unique nodes are the ones which do not exist in common neighbors
        jaccard_number = len(common_neighbors) / len(accumulated_neighbors)
        return jaccard_number

    # make a set of unified nodes from u and v series
    def accumulation_of_nodes(self, u_series, v_series):
        unique_node_names = set()
        for node in u_series:
            temp = str(node)
            if not temp in unique_node_names:
                unique_node_names.add(temp) 
        for node in v_series:
            temp = str(node)
            if not temp in unique_node_names: 
                unique_node_names.add(temp)
        return unique_node_names
          
    #find common nodes in two series     
    def common_nodes(self, u_series, v_series):
        #finds same nodes in two given series
        same_nodes = []
        for u_node in u_series:
            for v_node in v_series:
                if self.are_same_nodes(u_node, v_node):
                    same_nodes.append(u_node)
        return same_nodes
    
    # showing the grapgh in a plot
    def visualize_graph(self):
        # First networkx library is imported
        # along with matplotlib
        import networkx as nx
        import matplotlib.pyplot as plt
        class GraphVisualization:
            def __init__(self):
                self.visual = []

            def addEdge(self, a, b):
                temp = [a, b]
                self.visual.append(temp)
                
            def visualize(self):
                G = nx.Graph()
                G.add_edges_from(self.visual)
                nx.draw_networkx(G)
                plt.show()

        G = GraphVisualization()
        seen_vertices = set()
        for node in self.graph:
            neighbors = self.find_node_neighbors(node)
            for neighbor in neighbors:
                vertice = str(node) + str(neighbor)
                if vertice in seen_vertices:
                    continue
                second_vertice = str(neighbor) + str(node)
                seen_vertices.add(vertice)
                seen_vertices.add(second_vertice)
                G.addEdge(node, neighbor)
        G.visualize()
