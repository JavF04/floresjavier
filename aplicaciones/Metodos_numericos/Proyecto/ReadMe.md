# 🧮 Scientific Computing & Numerical Methods Suite

A comprehensive, interactive Python application equipped with a **Graphical User Interface (GUI)** designed to compute approximations, interpolate data points, and solve non-linear equations or complex matrix systems. 

This suite bridges algebraic algorithms with a functional visual workspace, using **Tkinter** for the desktop interfaces, **SymPy** for runtime symbolic expression parsing, and **NumPy** for vector optimization and matrix solvers (such as Jacobian determinants in multi-variable spaces).

---

## 🛠️ Core Toolkit & Libraries

- **Language:** Python 3.x
- **GUI Engine:** Tkinter (Custom modular windows, dynamically updated multi-entry tables, and error message prompts).
- **Symbolic Math:** SymPy (Enables users to input raw mathematical strings like `x**2 + sin(x)` and dynamically parses derivatives or symbolic values).
- **Linear Algebra & Arrays:** NumPy (Array vectorization, multi-dimensional matrix structures, and linear solvers via `np.linalg.solve`).
- **Data Architecture:** Pandas (Data management matrices for sorting divided difference values).

---

## 📁 Mathematical Engine Breakdown

The application splits specific analytical routines into independent structural modules:

### 🎯 Interpolation, Curve Fitting & Approximation
- **`Lagrange.py`:** Generates high-degree interpolation polynomials across a coordinate set utilizing Lagrange multipliers. Computes exact polynomial formulas and instant scalar evaluations.
- **`diferenciaDivididas.py`:** Implements Newton's Divided Differences polynomial pipeline. Dynamically calculates and renders structured triangular coefficient matrices.
- **`newton.py` / `puntoFijo.py`:** Handles localized interpolation matrices (Forward/Backward setups) alongside numerical Fixed-Point iteration loops for system convergence.
- **`interfazMC.py`:** A dedicated GUI module performing the **Method of Least Squares (Linear Regression)**. Fits an optimal regression line ($y = mx + b$) across custom coordinate data and computes the total squared residual error.

### 📉 Root-Finding & Non-Linear Matrix Solvers
- **`newton_raphson_metodos_numericos.py`:** A multi-variable solver designed to approximate solutions for non-linear systems of equations. It handles symbolic multi-input matrices, constructs runtime **Jacobian Matrices** dynamically via derivative calculations, and executes optimization loops until meeting convergence thresholds.

### 📐 Numerical Integration (Calculus Solvers)
- **`simpson1tercio.py` / `trapecio.py`:** Multi-interval integration modules. Approximates definite integrals using piecewise quadratic functions (Simpson's 1/3 and 3/8 Rules) and linear approximations (Trapezoidal Rule) with user-defined boundaries and segment counts.

---

## 🚀 Key Engineering & UI Highlights

1. **Robust Exception & Divergence Handling:** The system wraps operational blocks inside input validation loops. It detects dividing-by-zero anomalies, invalid numerical constraints, or matrix singularity flags, alerting users via explicit modal alerts.
2. **On-the-Fly Expression Parsing:** Eliminates hardcoded functions. Thanks to `SymPy`, mathematical operations are read as fluid text formats directly from text inputs and processed cleanly into lambda expressions.
3. **Decoupled Architecture:** Each interface acts as a self-contained desktop component. It receives standalone execution callbacks, making the environment completely modular and easy to scale with additional mathematical methods.

---

## ⚙️ How to Run the Project

1. **Install Prerequisites:** Ensure you have the core packages installed in your working directory environment:
   ```bash
   pip install numpy sympy pandas