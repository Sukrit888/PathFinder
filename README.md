# 🧭 PathFinder – Smart Navigation System using Graph Algorithms

**PathFinder** is a Python + DSA-powered navigation system that lets users create custom graphs and find the shortest paths between nodes using classic graph algorithms like **Dijkstra**, **BFS**, and **A\***.

Built with:
- 🧠 Graph theory fundamentals
- 🔍 A* Search Algorithm
- 🚀 Streamlit for interactive UI
- ✅ Unit-tested for reliability

---

## ⚙️ Features

- ✅ Add nodes and weighted edges dynamically
- 📌 Select between **Dijkstra**, **BFS**, and **A\*** search
- 🧠 A* implementation using straight-line distance as heuristic
- 📈 Visual feedback on the shortest path and cost
- 📦 Modular backend in `my_pathfinder.py`
- 🧪 Unit tests with `pytest` in `test_pathfinder.py`
- 🌐 Streamlit-powered GUI

---

## 🏁 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/pathfinder.git
cd pathfinder
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit networkx matplotlib
```

---

## 🚀 Run the App

```bash
streamlit run app.py
```

Or in Google Colab, upload the files and run `app.py` using `!streamlit run app.py`.

---

## 🧪 Run Tests

```bash
pytest test_pathfinder.py
```

Tests for:
- Graph creation
- Dijkstra
- BFS
- A* shortest path
- Edge cases

---

## 🧠 Algorithms Implemented

| Algorithm  | Description |
|------------|-------------|
| Dijkstra   | Finds the shortest weighted path from source to target |
| BFS        | Unweighted shortest path (number of edges) |
| A\*        | Shortest path with heuristic (Euclidean distance) |

---

## 📁 Project Structure

```
pathfinder/
│
├── app.py                # Streamlit front-end
├── my_pathfinder.py      # Graph algorithms module
├── test_pathfinder.py    # Unit tests
├── requirements.txt
└── README.md
```

---

## 📸 Screenshots

> (You can insert Streamlit UI screenshots here if desired.)

---

## 🌍 Use Cases

- Smart City Navigation
- Logistics and Route Optimization
- Network Design Simulations
- Supply Chain Visualizations

---

## 📌 Future Improvements

- Add graph visualization with `networkx.draw`
- Save/load graph from file
- Add more heuristics (Manhattan, etc.)
- Integrate geolocation APIs for real maps

---

## 👨‍💻 Author

**Sukrit Kashyap Goswami**  
🧠 Product + Tech Enthusiast  
📬 [LinkedIn](https://www.linkedin.com/in/sukritkashyapgoswami/) | [Medium](medium.com/@6sukritgoswami)

---

## 📜 License

This project is licensed under the MIT License.
