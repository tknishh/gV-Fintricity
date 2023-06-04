from py2neo import Graph, Node

# Connect to Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

# Read data from CSV file
with open('data\gri_ghg_protocol.csv', 'r') as file:
    lines = file.readlines()

# Remove header line
lines = lines[1:]

# Create nodes
for line in lines:
    data = line.strip().split(',')

    # Extract node properties
    node_id = data[0]
    node_type = data[1]
    parent_id = data[2]
    name = data[3]
    source = data[4]
    target = data[5]
    reference_model_id = data[6]
    term_id = data[7]
    label = data[8]
    properties = data[10]
    description = data[11]
    Required = data[12]
    Quant_qual = data[13]


    # Create node
    node = Node(label)
    node['ID'] = node_id
    node['TYPE'] = node_type
    node['PARENT'] = parent_id
    node['NAME'] = name
    node['SOURCE'] = source
    node['TARGET'] = target
    node['REFERENCE_MODEL_ID'] = reference_model_id
    node['TERM_ID'] = term_id
    node['LABEL'] = label
    node['PROPERTIES'] = properties
    node['DESCRIPTION'] = description
    node['Required'] = Required
    node['Quant_qual'] = Quant_qual


    # Create or update node in Neo4j
    graph.merge(node, 'Label', 'ID')

print("Nodes created successfully.")
