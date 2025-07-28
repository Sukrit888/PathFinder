import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
from my_pathfinder import Graph

# Initialize session state
if "graph" not in st.session_state:
    st.session_state.graph = Graph()

st.title("🔍 PathFinder – Smart Navigation System")

st.sidebar.header("📍 Add Nodes and Edges")

# Add Nodes
node1 = st.sidebar.text_input("Node 1 (From):", key="node1")
node2 = st.sidebar.text_input("Node 2 (To):", key="node2")
weight = st.sidebar.number_input("Distance (weight):", min_value=1, value=1, step=1)

if st.sidebar.button("➕ Add Edge"):
    if node1 and node2:
        st.session_state.graph.add_edge(node1.strip(), node2.strip(), weight)
        st.success(f"Edge added: {node1} ➡️ {node2} ({weight})")
    else:
        st.warning("Both nodes must be provided!")

# Show Graph Data
with st.expander("📊 View Graph Data"):
    st.write("**Nodes:**", st.session_state.graph.get_nodes())
    st.write("**Edges:**", st.session_state.graph.get_edges())

# Shortest Path Section
st.header("🚦 Find Shortest Path")

nodes = st.session_state.graph.get_nodes()
if nodes:
    from_node = st.selectbox("From", nodes, key="from_node_select")
    to_node = st.selectbox("To", nodes, key="to_node_select")

    if st.button("🔍 Find Path"):
        if from_node != to_node:
            path, cost = st.session_state.graph.dijkstra(from_node, to_node)
            if path:
                st.success(f"✅ Path found: {' ➡️ '.join(path)} (Total Distance: {cost})")
            else:
                st.error("❌ No path found between the selected nodes.")
        else:
            st.warning("Please choose two different nodes.")
else:
    st.info("Add some nodes and edges to get started.")

# Draw Graph
st.header("📈 Network Graph")

G = nx.Graph()

for node in st.session_state.graph.get_nodes():
    G.add_node(node)

for n1, n2, weight in st.session_state.graph.get_edges():
    G.add_edge(n1, n2, weight=weight)

pos = nx.spring_layout(G)
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
st.pyplot(plt)
