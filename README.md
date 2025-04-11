
# Lazors Puzzle Solver 🔥💡

This repository contains a Python implementation of a **Lazors puzzle solver**, which reads `.bff` puzzle files, simulates lazor beam behavior through various block types, and attempts to solve the puzzle by placing blocks to hit target points.

---

## 📜 Features

- ✅ Parses `.bff` puzzle definition files
- 🔍 Simulates lazor beams with physics-based reflection, refraction, and absorption
- 🧠 Solves puzzles using permutations of block placements
- 🧪 Includes unit tests for critical components

---

## 📁 Files

| File | Description |
|------|-------------|
| `LazorProjectv6.py` | Main script for parsing, simulating, and solving Lazors puzzles |
| `test_lazor_solver.py` | Unit tests for logic and utilities |
| `solution_output.txt` | Output file (created when a solution is found) |
| `lazor_log_*.txt` | Log file created with every run |

---

## 🧱 Block Types

- `A`: Reflective — lazor bounces off
- `B`: Opaque — lazor is absorbed
- `C`: Refractive — lazor passes through and reflects

---

## 🚀 How to Use

### 1. Place Your Puzzle

Put your `.bff` file (like `tiny_5.bff`) in the root folder.

### 2. Run the Solver

```bash
python LazorProjectv6.py
```

If a solution is found:
- The path and block layout are printed
- Results are saved to `solution_output.txt`

---

## ✅ Running Unit Tests

To test core functionality:

```bash
python test_lazor_solver.py
```

This will verify:
- Block physics
- Open space detection
- Placement logic
- Target hit checking

---

## 📌 Requirements

- Python 3.6+
- No external libraries required

---

## 🙌 Acknowledgments

Originally built as part of a software carpentry assignment.  
Docstrings, inline comments, and test coverage added with assistance from ChatGPT.

---

## 📄 License

This project is open-source. Use it freely and star ⭐ if you find it useful!
