import streamlit as st
import pandas as pd
import networkx as nx
from my_pathfinder import Graph

# Title and description
st.set_page_config(page_title="PathFinder", layout="wide")
st.title("🧭 PathFinder – Smart Navigation System using Graph Algorithms")
st.markdown("Visualize shortest paths using Dijkstra, BFS, DFS, and A* on a custom graph.")

# Load or initialize graph
if 'graph' not in st.session_state:
    st.session_state.graph = Graph()

uploaded_file = st.sidebar.file_uploader("Upload CSV (From, To, Weight)", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    for _, row in df.iterrows():
        st.session_state.graph.add_edge(row['From'], row['To'], row['Weight'])

# Select source and destination nodes
nodes = list(st.session_state.graph.graph.keys())
if nodes:
    node1 = st.sidebar.selectbox("From", nodes, key="from_node")
    node2 = st.sidebar.selectbox("To", nodes, key="to_node")
    algorithm = st.sidebar.selectbox("Algorithm", ["Dijkstra", "BFS", "DFS", "A*"])

    # Show graph edges
    st.subheader("📊 Graph Edges")
    edges_data = [(u, v, w) for u in st.session_state.graph.graph for v, w in st.session_state.graph.graph[u]]
    df_edges = pd.DataFrame(edges_data, columns=["From", "To", "Weight"])
    st.dataframe(df_edges)

    # Pathfinding
    if st.sidebar.button("🔍 Find Path"):
        path, cost = st.session_state.graph.find_path(node1, node2, algorithm)
        if path:
            st.success(f"✅ Path found: {' ➡️ '.join(path)} (Total Distance: {cost})")
        else:
            st.error("⚠️ No path found between the selected nodes.")
else:
    st.warning("Upload a graph CSV file to begin.")

# Footer
st.markdown("---")
st.markdown("Created by **Sukrit Kashyap Goswami** | Powered by Python + Streamlit 🚀")
