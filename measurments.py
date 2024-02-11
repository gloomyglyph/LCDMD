from strike_graph import make_strike_labels
def f1_score(seed_node, predicted_community):   
    labels, groups = make_strike_labels()
    ct = groups[labels[seed_node]]
    cf = predicted_community
    cf_ct_commons = []
    for node in predicted_community:
        if node in ct:
            cf_ct_commons.append(node)
    recall = len(cf_ct_commons)/len(ct)
    precision = len(cf_ct_commons)/len(cf)
    recall = (2*precision*recall)/(precision + recall)
    return recall
