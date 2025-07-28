import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from my_pathfinder import Graph

# Title
st.title("🧭 PathFinder – Smart Navigation System using Graph Algorithms")
st.markdown("Visualize and compare shortest paths using Dijkstra and A* algorithms.")

# Sidebar inputs
st.sidebar.header("📍 Add Nodes and Edges")

# Initialize Graph
if 'graph' not in st.session_state:
    st.session_state.graph = Graph()

# Add node
new_node = st.sidebar.text_input("Add Node")
if st.sidebar.button("Add Node"):
    if new_node:
        st.session_state.graph.add_node(new_node)
        st.success(f"Node '{new_node}' added.")

# Add edge
node1 = st.sidebar.selectbox("From", st.session_state.graph.nodes, key="from_node")
node2 = st.sidebar.selectbox("To", st.session_state.graph.nodes, key="to_node")
distance = st.sidebar.number_input("Distance", min_value=0.0, step=1.0)

if st.sidebar.button("Add Edge"):
    if node1 != node2:
        st.session_state.graph.add_edge(node1, node2, distance)
        st.success(f"Edge from {node1} to {node2} with distance {distance} added.")
    else:
        st.warning("Source and destination cannot be the same.")

# Visualize Graph
st.subheader("🖼️ Graph View")
graph = nx.Graph()
for node in st.session_state.graph.nodes:
    graph.add_node(node)
for from_node, edges in st.session_state.graph.edges.items():
    for to_node, weight in edges.items():
        graph.add_edge(from_node, to_node, weight=weight)

fig, ax = plt.subplots()
pos = nx.spring_layout(graph, seed=42)
nx.draw(graph, pos, with_labels=True, node_color="skyblue", node_size=2000, font_size=16, ax=ax)
nx.draw_networkx_edge_labels(graph, pos, edge_labels={(u, v): d['weight'] for u, v, d in graph.edges(data=True)}, ax=ax)
st.pyplot(fig)

# Path Finder Section
st.subheader("🔍 Find Shortest Path")

start = st.selectbox("Select Source", st.session_state.graph.nodes, key="start")
end = st.selectbox("Select Destination", st.session_state.graph.nodes, key="end")
algorithm = st.radio("Choose Algorithm", ("Dijkstra", "A* Search"))

if st.button("Find Path"):
    if algorithm == "Dijkstra":
        path, cost = st.session_state.graph.dijkstra(start, end)
    else:
        path, cost = st.session_state.graph.a_star(start, end)

    if path is not None:
        st.success(f"✅ Path found: {' ➡️ '.join(path)} (Total Distance: {cost})")
    else:
        st.error("⚠️ No path found between the selected nodes.")
