# Lazor Solver – EN.540.635 Software Carpentry Project

This repository contains a Python solver for the mobile puzzle game [Lazors](https://play.google.com/store/apps/details?id=net.pyrosphere.lazors). The solver reads `.bff` level files, places blocks using brute-force search, and simulates lazor paths with accurate physics to determine valid solutions.

---

## Project Overview

**Course**: EN.540.635 – Software Carpentry  
**Semester**: Spring 2025  
**Instructors**: F. Shaikh, A. Roy  
**Contributors**: Chun-Chiao  

---

## Files Included

| File                      | Description                                  |
|---------------------------|----------------------------------------------|
| `lazor_solver_final.py`   | Main solver script (edge-based interactions) |
| `mad_1.bff`               | Sample input puzzle file                     |
| `solution.txt`            | Output solution of block placement           |
| `README.md`               | This documentation                          |

---

## How to Use

### 1. Install Python

Make sure you have **Python 3.7+** installed.

### 2. Clone the Repository

```bash
git clone https://github.com/<your-username>/lazor-solver.git
cd lazor-solver
```

### 3. Run the Solver

The script is set to solve `mad_1.bff` by default:

```bash
python lazor_solver_final.py
```

It will output the solution in a file called `solution.txt`.

---

## Example Output

A solved board may look like:

```
A . . .
C . A .
. . . .
. . . .
```

Each letter represents a block:
- `A` = Reflect block
- `B` = Opaque block (not used in this example)
- `C` = Refract block
- `.` = Empty cell

---

## Unit Tests

Run basic unit tests with:

```bash
python lazor_solver_final.py unittest
```

---

## Notes

- The script uses a brute-force search and may take several seconds for larger boards.
- Block interactions follow the Lazors game's edge-based physics: lazors reflect/refract when crossing a block edge, not the center.

---

## License

MIT License – feel free to use and modify for educational purposes.

---

## Contact

For issues or collaboration, reach out via GitHub or [add your contact info here].
