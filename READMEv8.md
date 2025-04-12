# Lazors Puzzle Solver

Lazors Puzzle Solver is a Python-based program that solves the Lazors puzzle by simulating laser beam paths and exploring block placement permutations. It parses `.bff` configuration files to set up the grid, available block counts, laser starting positions, and target points, then searches for block placements that enable the laser to hit all the targets.

## Features

- **Laser Beam Simulation:**  
  Simulates the physics of laser beams interacting with different block types.
  
- **Block Types:**  
  - **A (Reflective):** Reflects the laser beam.
  - **B (Opaque):** Absorbs the laser beam.
  - **C (Refractive):** Splits the laser beam (passes through and reflects).

- **Configuration Parsing:**  
  Reads `.bff` files to extract grid layouts, block counts, lazor start positions/directions, and target points.

- **Block Placement Permutations:**  
  Uses combinations and permutations to try different block placements on available grid positions.

- **Detailed Logging:**  
  Logs beam paths and configuration attempts—including 2D grid outputs—when debugging repeated beam segments.

- **Unit Testing:**  
  Comes with a comprehensive set of unit tests for key components, ensuring that edge calculations, block interactions, grid configuration, and simulation behavior work as expected.

<<<<<<< HEAD
## Repository Structure
=======
| File | Description |
|------|-------------|
| `LazorProjectv6.py` | Main script for parsing, simulating, and solving Lazors puzzles |
| `test_lazor_solver.py` | Unit tests for logic and utilities |
| `solution_output.txt` | Output file (created when a solution is found) |
| `lazor_log_*.txt` | Log file created with every run |
>>>>>>> 42790863c85031c8e605a7f94572d0c068557620

```
├── lazor_solver.py       # Main solver script
├── test_lazors.py        # Unit tests for the solver
├── yarn_5.bff            # Example puzzle configuration file
├── solution_output.txt   # Output file generated when a solution is found
└── README.md             # Project documentation (this file)
```

## Requirements

- **Python 3.x** (Tested with Python 3.8+)
- Standard libraries: `datetime`, `sys`, `itertools`, `copy`, `collections`, and `unittest`.

## Installation

Clone the repository with Git:

```bash
git clone https://github.com/yourusername/lazors-puzzle-solver.git
cd lazors-puzzle-solver
```

## Usage

To run the solver with a `.bff` configuration file (e.g., `yarn_5.bff`), execute:

```bash
<<<<<<< HEAD
python lazor_solver.py
=======
python LazorProjectv6.py
>>>>>>> 42790863c85031c8e605a7f94572d0c068557620
```

This will:
- Parse the configuration file.
- Log the simulation progress and any repeated beam segments with the current 2D grid configuration.
- Output the solution (if found) to `solution_output.txt`.

## Unit Testing

Unit tests are provided to verify the correctness of different components, such as the Block class, edge calculation, block placement, target checking, and simulation. To run the unit tests, execute:

```bash
python -m unittest test_lazors.py
```

Or simply:

```bash
python test_lazors.py
```

## Code Overview

- **`Block` Class:**  
  Represents the interactive blocks on the grid. The class includes a `__repr__` method to display the block type for debugging.

- **`get_block_edges()` Function:**  
  Calculates the edge coordinates for a given block on the grid.

- **`get_block_interaction_edge_directional()` Function:**  
  Determines how a laser beam interacts with a block based on the edge type and the block type (reflective, opaque, or refractive).

- **`simulate_lazor_with_directional_logic()` Function:**  
  Simulates the beam’s path through the grid, logs branch splits, and detects repeated beam segments. It prints the grid configuration (using the `print_grid()` function) when a beam segment repeats too many times.

- **`print_grid()` Function:**  
  Prints the grid in a clean 2D layout. For example, open positions are printed as `o`, `None` as `x`, and blocks by their block type.

- **`parse_bff()` Function:**  
  Parses the `.bff` file to extract grid layout, block counts, lazor start positions/directions, and target points.

- **`place_blocks()` and `find_open_positions()` Functions:**  
  These functions help generate new grid configurations by placing blocks at specified open positions.

- **`solve_with_permutations()` Function:**  
  Iterates through possible block configurations using permutations and combinations, simulating the laser path for each configuration to find the one that hits all targets.

## Future Improvements

- **Optimization:**  
  Consider switching to a recursive backtracking approach with early pruning to reduce the combinatorial search space.

- **Performance:**  
  Optimize collision detection in the simulation loop (e.g., through spatial indexing) and reduce the need for deep copies.

- **Parsing Robustness:**  
  Enhance the `.bff` file parsing to handle different file formatting variations more robustly.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Inspired by the Lazors game and puzzle solvers.
- Enhanced with thorough unit testing and debugging support.
- Documentation and project enhancements provided with help from ChatGPT.
