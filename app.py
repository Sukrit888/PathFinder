import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx
import json
from io import StringIO
from my_pathfinder import Graph

st.set_page_config(page_title="PathFinder - Smart Navigation", layout="wide")
st.title("🧭 PathFinder – Smart Navigation using Graph Algorithms")

# Initialize session graph
if "graph" not in st.session_state:
    st.session_state.graph = Graph()

# Reset Graph Button
if st.button("🗑️ Reset Graph"):
    st.session_state.graph = Graph()
    st.success("Graph has been reset!")

# Sidebar for user input
st.sidebar.header("📌 Add Nodes & Edges")

# Add Node
node = st.sidebar.text_input("Add Node:")
if st.sidebar.button("Add Node"):
    if node:
        st.session_state.graph.add_node(node)
        st.sidebar.success(f"Node '{node}' added.")
    else:
        st.sidebar.warning("Please enter a valid node name.")

# Add Edge
n1 = st.sidebar.text_input("From Node")
n2 = st.sidebar.text_input("To Node")
weight = st.sidebar.number_input("Distance", min_value=0.0, format="%.2f")

if st.sidebar.button("Add Edge"):
    if n1 and n2 and n1 != n2:
        st.session_state.graph.add_edge(n1, n2, weight)
        st.sidebar.success(f"Edge added: {n1} ↔ {n2} (Weight: {weight})")
    else:
        st.sidebar.warning("Please provide valid distinct node names.")

# Select source and destination
nodes = list(st.session_state.graph.get_nodes())
if nodes:
    node1 = st.selectbox("Select Source", nodes, key="from_node")
    node2 = st.selectbox("Select Destination", nodes, key="to_node")

    if st.button("🔍 Find Shortest Path"):
        if node1 and node2:
            path, cost = st.session_state.graph.shortest_path(node1, node2)
            if path:
                st.success(f"✅ Path found: {' ➡️ '.join(path)} (Total Distance: {cost})")
            else:
                st.warning("⚠️ No path found between the selected nodes.")

# Draw Graph
G = nx.Graph()
for node in st.session_state.graph.get_nodes():
    G.add_node(node)
for node in st.session_state.graph.adjacency:
    for neighbor, weight in st.session_state.graph.adjacency[node]:
        G.add_edge(node, neighbor, weight=weight)

pos = nx.spring_layout(G)
plt.figure(figsize=(10, 6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=2000, font_size=16)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
st.pyplot(plt)

# Save or Load Graph
st.header("💾 Save or Load Graph")

# Export
if st.button("📥 Export Graph as JSON"):
    graph_data = {
        "nodes": list(st.session_state.graph.get_nodes()),
        "edges": [
            {"from": n1, "to": n2, "weight": w}
            for n1, neighbors in st.session_state.graph.adjacency.items()
            for n2, w in neighbors
        ]
    }
    json_str = json.dumps(graph_data, indent=2)
    st.download_button("Download JSON", json_str, file_name="graph.json", mime="application/json")

# Import
uploaded_file = st.file_uploader("Upload a graph JSON", type="json")
if uploaded_file:
    content = uploaded_file.read().decode("utf-8")
    try:
        data = json.loads(content)
        new_graph = Graph()
        for node in data.get("nodes", []):
            new_graph.add_node(node)
        for edge in data.get("edges", []):
            new_graph.add_edge(edge["from"], edge["to"], edge["weight"])
        st.session_state.graph = new_graph
        st.success("Graph loaded successfully from file.")
    except Exception as e:
        st.error(f"Failed to load graph: {e}")
