import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from my_pathfinder import Graph

# Initialize session state
if "graph" not in st.session_state:
    st.session_state.graph = Graph()

st.title("🚦 PathFinder – Smart Navigation with Dijkstra & A*")

# Sidebar for adding nodes and edges
st.sidebar.header("🔧 Graph Builder")

with st.sidebar.form("node_form"):
    node = st.text_input("Add Node", key="node_input")
    submitted_node = st.form_submit_button("Add Node")
    if submitted_node and node:
        st.session_state.graph.add_node(node)
        st.success(f"Node '{node}' added.")

with st.sidebar.form("edge_form"):
    node1 = st.selectbox("From", st.session_state.graph.get_nodes(), key="from_node")
    node2 = st.selectbox("To", st.session_state.graph.get_nodes(), key="to_node")
    weight = st.number_input("Distance", min_value=1.0, value=1.0, step=0.5)
    submitted_edge = st.form_submit_button("Add Edge")
    if submitted_edge:
        st.session_state.graph.add_edge(node1, node2, weight)
        st.success(f"Edge from '{node1}' to '{node2}' with distance {weight} added.")

st.markdown("---")

# Show graph
st.subheader("🧠 Visual Graph")
edges_data = [
    (u, v, w) for u in st.session_state.graph.get_nodes()
    for v, w in st.session_state.graph.adjacency.get(u, [])
]

G = nx.DiGraph()
G.add_weighted_edges_from(edges_data)

fig, ax = plt.subplots()
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, ax=ax)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d for u, v, d in G.edges(data="weight")}, ax=ax)
st.pyplot(fig)

st.markdown("---")

# Path Finding Section
st.subheader("🔍 Find Shortest Path")
if len(st.session_state.graph.get_nodes()) >= 2:
    start = st.selectbox("Start Node", st.session_state.graph.get_nodes(), key="start_node")
    end = st.selectbox("End Node", st.session_state.graph.get_nodes(), key="end_node")
    algorithm = st.radio("Select Algorithm", ["Dijkstra", "A*"])

    if st.button("Find Path"):
        if algorithm == "Dijkstra":
            path, cost = st.session_state.graph.dijkstra(start, end)
        else:
            path, cost = st.session_state.graph.a_star(start, end)

        if path:
            st.success(f"✅ Path found: {' ➡️ '.join(path)} (Total Distance: {cost})")
        else:
            st.error("❌ No path found.")
else:
    st.info("Please add at least two nodes to find a path.")

