# 🍔 Restaurant Management & Inventory System

A Python-based CLI application built to simulate an interactive food ordering and business operations platform. The project showcases robust **Object-Oriented Programming (OOP)** practices, utilizing structural design patterns, data inheritance, abstraction, and local persistence using the `pandas` library to interface with flat CSV files.

The architecture isolates workflows into distinct user experiences: a **Customer Interface** for account management, menu viewing, and transactional orders, and an **Administrative Interface** for tracking operating metrics, auditing ingredient stock levels, and automated business restocking.

---

## 🛠️ Tech Stack & Concepts Demonstrated

- **Core Language:** Python 3
- **Data Engineering:** Pandas (DataFrame structures, local CSV database reads/writes, matrix manipulation).
- **OOP Architecture:** Abstraction (`abc.ABCMeta`), Encapsulation, Custom Property Getters/Setters, Modular Class Structures.
- **Data Persistence:** Automated handling of transactional logs (`Pedidos.csv`), client data directories (`Clientes.csv`), and inventory balance sheets (`IngredientesFinal.csv`).

---

## 📁 Core Code Architecture

The project relies on a modular file layout that isolates abstractions from business logic and execution handlers:

- **`MainCliente.py` & `MainAdmin.py`:** Entry-point scripts executing the localized runtime loops for customers and administrators respectively.
- **`InterfazPersona.py` & `InterfazAlimentos.py`:** Formal base definitions using Python's Abstract Base Classes (`ABC`) ensuring strict encapsulation and contractual method structures across downstream classes.
- **`AdministradorPersonas.py`:** Handles credential authentication and secure input validation workflows for both user sign-ins and new account sign-ups.
- **`AdministradorPedidos.py`:** Orchestrates the core transactional matrix. Maps real-time burger orders directly to specific ingredient volume outputs and dynamically calculates revenue margins.
- **`AdministradorProductos.py`:** Manages the active resource inventory profiles, monitoring physical stock weight and ingredient constraints.

---

## 🚀 System Features & Workflows

### 👥 Client Hub (`MainCliente.py`)
1. **Authentication Flow:** Secure login loops and unique-username validation schemas during sign-up.
2. **Menu Querying:** Generates dynamic tabular structures parsing multi-attribute food properties from persistent storage tables.
3. **Automated Order Processing:** Interactive multi-product ordering cart. The system validates whether operating times fall within the valid schedule bounds (`12:00 PM` to `10:00 PM`) prior to ledger entry creation.

### 💼 Administrator Panel (`MainAdmin.py`)
1. **Auditing & Live Tracking:** Direct streaming of relational storage balances tracking item descriptions, cost indices, and remaining metric quantities (kg).
2. **Dynamic Stock Replenishment:** Interactive reordering console. Buying new ingredients automatically checks cost constraints against the corporate treasury cash flow (`ValoresEmpresa.csv`), modifying matrix coordinates in-place.

---

## 📊 Database Schema (CSV Persistence)

The storage backend maps data records into functional `.csv` data-stores within the database layer:
- **`Clientes.csv` / `Administradores.csv`:** Stores structured records including unique identifiers, encrypted authentication paths, contact vectors, and operational card strings.
- **`IngredientesFinal.csv`:** Tracks live factory weights and structural parameters tied directly to real-time warehouse states.
- **`Pedidos.csv`:** Longitudinal operational log storing active transactional fields, multidimensional index strings of chosen plates, financial volumes, and automated timestamps.

---

## 💡 Engineering Practices Highlighted

1. **Transactional Integrity:** Placing or updating an order triggers multi-table synchronization steps. It instantly deducts fractional ingredient amounts from `IngredientesFinal.csv`, logs order specifics to `Pedidos.csv`, and adds revenue records to `ValoresEmpresa.csv` using sequential dataset operations.
2. **Rigorous Abstraction:** Implements standard development designs by utilizing structured base contracts (`IntPersona`, `AlimentoInt`), ensuring scalable expansions for additional menu entries or new staff layers.
3. **Defensive Input Handling:** Built-in loop handlers filter data anomalies, type mismatches, out-of-range numerical options, and duplicate ledger constraints.