from graph_tools import Graph
#network sourceType="agent" targetType="agent" id="test" isDirected="true">
def make_strike_graph():
    raw_data = """<link source="Frank" target="Gill" type="double" value="1"/>
    <link source="Gill" target="Frank" type="double" value="1"/>
    <link source="Gill" target="Ike" type="double" value="1"/>
    <link source="Gill" target="Hal" type="double" value="1"/>
    <link source="Gill" target="John" type="double" value="1"/>
    <link source="Ike" target="Gill" type="double" value="1"/>
    <link source="Ike" target="Mike" type="double" value="1"/>
    <link source="Ike" target="Bob" type="double" value="1"/>
    <link source="Mike" target="Ike" type="double" value="1"/>
    <link source="Mike" target="Bob" type="double" value="1"/>
    <link source="Hal" target="Gill" type="double" value="1"/>
    <link source="Hal" target="John" type="double" value="1"/>
    <link source="Hal" target="Bob" type="double" value="1"/>
    <link source="John" target="Gill" type="double" value="1"/>
    <link source="John" target="Hal" type="double" value="1"/>
    <link source="John" target="Karl" type="double" value="1"/>
    <link source="John" target="Lanny" type="double" value="1"/>
    <link source="John" target="Bob" type="double" value="1"/>
    <link source="Karl" target="John" type="double" value="1"/>
    <link source="Karl" target="Lanny" type="double" value="1"/>
    <link source="Karl" target="Ozzie" type="double" value="1"/>
    <link source="Lanny" target="John" type="double" value="1"/>
    <link source="Lanny" target="Karl" type="double" value="1"/>
    <link source="Lanny" target="Bob" type="double" value="1"/>
    <link source="Bob" target="Ike" type="double" value="1"/>
    <link source="Bob" target="Mike" type="double" value="1"/>
    <link source="Bob" target="Hal" type="double" value="1"/>
    <link source="Bob" target="John" type="double" value="1"/>
    <link source="Bob" target="Lanny" type="double" value="1"/>
    <link source="Bob" target="Alejandro" type="double" value="1"/>
    <link source="Bob" target="Norm" type="double" value="1"/>
    <link source="Alejandro" target="Bob" type="double" value="1"/>
    <link source="Alejandro" target="Carlos" type="double" value="1"/>
    <link source="Alejandro" target="Eduardo" type="double" value="1"/>
    <link source="Alejandro" target="Domingo" type="double" value="1"/>
    <link source="Carlos" target="Alejandro" type="double" value="1"/>
    <link source="Carlos" target="Eduardo" type="double" value="1"/>
    <link source="Carlos" target="Domingo" type="double" value="1"/>
    <link source="Eduardo" target="Alejandro" type="double" value="1"/>
    <link source="Eduardo" target="Carlos" type="double" value="1"/>
    <link source="Eduardo" target="Domingo" type="double" value="1"/>
    <link source="Domingo" target="Alejandro" type="double" value="1"/>
    <link source="Domingo" target="Carlos" type="double" value="1"/>
    <link source="Domingo" target="Eduardo" type="double" value="1"/>
    <link source="Norm" target="Bob" type="double" value="1"/>
    <link source="Norm" target="Ozzie" type="double" value="1"/>
    <link source="Norm" target="Vern" type="double" value="1"/>
    <link source="Norm" target="Paul" type="double" value="1"/>
    <link source="Norm" target="Utrecht" type="double" value="1"/>
    <link source="Norm" target="Sam" type="double" value="1"/>
    <link source="Ozzie" target="Karl" type="double" value="1"/>
    <link source="Ozzie" target="Norm" type="double" value="1"/>
    <link source="Vern" target="Norm" type="double" value="1"/>
    <link source="Vern" target="Ted" type="double" value="1"/>
    <link source="Paul" target="Norm" type="double" value="1"/>
    <link source="Paul" target="Quint" type="double" value="1"/>
    <link source="Quint" target="Paul" type="double" value="1"/>
    <link source="Quint" target="Utrecht" type="double" value="1"/>
    <link source="Quint" target="Russ" type="double" value="1"/>
    <link source="Utrecht" target="Norm" type="double" value="1"/>
    <link source="Utrecht" target="Quint" type="double" value="1"/>
    <link source="Utrecht" target="Russ" type="double" value="1"/>
    <link source="Utrecht" target="Sam" type="double" value="1"/>
    <link source="Russ" target="Quint" type="double" value="1"/>
    <link source="Russ" target="Utrecht" type="double" value="1"/>
    <link source="Russ" target="Ted" type="double" value="1"/>
    <link source="Ted" target="Vern" type="double" value="1"/>
    <link source="Ted" target="Russ" type="double" value="1"/>
    <link source="Sam" target="Norm" type="double" value="1"/>
    <link source="Sam" target="Utrecht" type="double" value="1"/>
    <link source="Sam" target="Xavier" type="double" value="1"/>
    <link source="Sam" target="Wendle" type="double" value="1"/>
    <link source="Xavier" target="Sam" type="double" value="1"/>
    <link source="Xavier" target="Wendle" type="double" value="1"/>
    <link source="Wendle" target="Sam" type="double" value="1"/>
    <link source="Wendle" target="Xavier" type="double" value="1"/>"""

    raw_data_splitted = raw_data.split('<')
    strike_dict = {}
    for item in raw_data_splitted:
        if len(item) < 3:
            continue
        item = item.split('"')
        source = item[1]
        target = item[3]
        if source in strike_dict.keys():
            if target in strike_dict[source]:
                continue
            strike_dict[source].append(target)
        else:
            strike_dict[source] = [target]
    return strike_dict

def make_strike_labels():
    names = make_strike_graph().keys()
    labels_list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    labels = {}
    for counter, name in enumerate(names):
        labels[name] = labels_list[counter]
    groups = {1:[], 2:[], 3:[]}
    for label in labels.keys():
        groups[labels[label]].append(label)
    return labels, groups           

 
        