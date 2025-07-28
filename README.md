# 🧭 PathFinder – Smart Navigation System using Graph Algorithms

PathFinder is a Python-based smart navigation tool built with classical graph algorithms like Dijkstra and A* (A-Star), designed for interactive shortest path finding, education, and practical route optimization.

---

## 🚀 Features

- **Graph Class Implementation** (OOP in Python)
- **Support for Dijkstra and A\*** Algorithms
- **Heuristic-based A\* using Euclidean Distance**
- **Interactive UI with Streamlit**
- **Graph Visualization** with NetworkX and Matplotlib
- **Unit Testing** using `unittest`

---

## 🧱 Project Structure

```
pathfinder/
├── my_pathfinder.py       # Core Graph class and algorithms
├── test_pathfinder.py     # Unit tests for Dijkstra and A*
├── app.py                 # Streamlit dashboard for user interaction
└── README.md              # Project documentation
```

---

## 📦 Setup Instructions

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/pathfinder.git
cd pathfinder
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, install manually:
```bash
pip install streamlit networkx matplotlib
```

3. **Run unit tests**:
```bash
python -m unittest test_pathfinder.py
```

4. **Launch the Streamlit App**:
```bash
streamlit run app.py
```

---

## 🎯 Streamlit Dashboard Features

- Add nodes with (x, y) coordinates
- Add weighted edges between nodes
- Visualize the graph interactively
- Select start and end nodes
- Choose between Dijkstra and A* for pathfinding
- Displays shortest path and total cost

![Screenshot](screenshot.png) <!-- Optional: Add a screenshot -->

---

## 🧪 Testing

Tests are implemented using `unittest`. Run:
```bash
python -m unittest test_pathfinder.py
```

---

## 🛠️ Algorithms

### ✅ Dijkstra's Algorithm
- Computes shortest paths using greedy strategy.
- Suitable for graphs with non-negative weights.

### 🌟 A* Search Algorithm
- Uses **g(n) + h(n)** where `g(n)` is actual cost, and `h(n)` is Euclidean heuristic.
- More efficient for pathfinding in physical spaces.

---

## 🔮 Future Enhancements
- Save/load graphs (JSON or Pickle)
- Support edge editing and deletion
- Visualize algorithm steps with animation
- Deploy app on Streamlit Cloud

---

## 🤝 Contributing

1. Fork this repo
2. Create a new branch
3. Commit your changes
4. Push to your fork
5. Create a Pull Request

---

## 🧑‍💻 Author

**Sukrit Kashyap Goswami**

---

## 📄 License

This project is licensed under the MIT License.

---

## 🌐 Connect

[LinkedIn](https://www.linkedin.com/in/sukritkashyapgoswami/) | [Medium](https://medium.com/@6sukritgoswami)
