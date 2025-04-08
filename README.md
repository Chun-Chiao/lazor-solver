# Lazor Puzzle Solver

The **Lazor Puzzle Solver** is a Python program designed to solve laser reflection puzzles by simulating the paths of laser beams (lazors) through a configurable grid. The goal is to determine a placement of blocks that allows the lazors to hit all target points.

## Overview

This solver:
- Parses puzzle configurations from `.bff` files.
- Simulates lazor beam paths using directional logic and block interaction behavior.
- Attempts to solve the puzzle by testing permutations of block placements.
- Outputs a solution grid and lazor path if a solution is found.

## Block Types

- **A (Reflective)**: Reflects the lazor.
- **B (Opaque)**: Absorbs and stops the lazor.
- **C (Splitter)**: Splits the lazor into two — one continues straight, and the other reflects.

## Files

- `LazorProjectv4`: The main script implementing the lazor logic, puzzle parsing, and solving.
- `mad_4.bff`: Input configuration file specifying grid, block types, lazors, and targets.
- `solution_output.txt`: Output file containing the solution grid, lazor path, and hit status for targets.
- `lazor_log_YYYYMMDD_HHMMSS.txt`: Runtime log file capturing lazor simulation details.

## How to Use

1. Ensure Python 3 is installed.
2. Place the `.bff` file (e.g. `mad_4.bff`) in the working directory.
3. Run the script:
   ```bash
   python LazorProjectv3
   ```
4. The script will attempt to solve the puzzle and write the results to `solution_output.txt`.

## Output

The solution file includes:
- A text-based grid showing where blocks were placed.
- A list of all coordinates traversed by the lazor.
- The status (HIT or MISS) of each target point.

## Customization

You can modify or create `.bff` files with custom puzzles. Each file should include:
- A grid definition with `x` for fixed blocks and `o` for open positions.
- Counts of movable blocks.
- Lazor start points and directions.
- Target points.

## License

This project is provided for educational and puzzle-solving purposes.

---

Created as part of EN.540.635 Software Carpentry (JHU).
