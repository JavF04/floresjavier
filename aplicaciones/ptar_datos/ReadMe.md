# 🌊 Wastewater Treatment Plant Data Management System (PTAR)



A full-stack web application built to monitor, manage, and log operational analytics for a Wastewater Treatment Plant (**PTAR** - *Planta de Tratamiento de Aguas Residuales*). This system moves away from flat-file storage to deliver a dynamic **Client-Server Architecture**, leveraging a relational database cluster to manage environmental metrics, equipment status, and administrative access privileges.



The platform provides an end-to-end operational hub featuring dynamic data visualization via JavaScript, structural server-side routing via PHP, and secure transactional queries managed through MySQL.



---



## 🛠️ Tech Stack & Architecture



- **Frontend:** HTML5, CSS3 (Modular layouts & stylesheets), JavaScript (Dynamic UI interaction and form handling).

- **Backend Environment:** PHP (Server-side rendering, secure session handling, and relational endpoint management).

- **Database Engine:** MySQL / MariaDB (Relational schema modeling, foreign key constraints, and transactional query optimizations).

- **Architecture Pattern:** Traditional Client-Server architecture with explicit isolation between structural visual assets (`css_admin/`, `scripts/`) and backend controller endpoints.



---


# 🚀 Key Features & Enterprise Workflows

## 📊 Operational Metrics & Data Ingestion

- Relational Logging: Operators can seamlessly submit, modify, and track fluid parameters (such as pH levels, biochemical oxygen demand, chemical oxygen demand, and total suspended solids).
- Data Integrity Constraints: Dynamic database verification steps prevent type mismatches or out-of-bounds readings prior to mutating the relational schema tables.

## 🛡️ Administrative Portal (Admin_page/)

- Secure Access Control: Utilizes PHP session cookies and access management matrices to verify user clearance before executing sensitive script assets.

- System Auditing: Dedicated viewpoints (views/) allow administrators to analyze overall plant efficiency, review processing histories, and oversee general operations.



## 🗄️ Relational Database Layout (DB/ptar_datos.sql)

- Formulated around optimized MySQL schemas to guarantee transactional durability.

- Indexes operational timestamps and automated fields, optimizing retrieval latency for long-term historical trend analysis.

---

## 💡 Software Engineering Highlights

- Explicit Separation of Concerns: Isolates stylistic definitions (css_admin/) and interactive components (php/) from the foundational business controllers written in PHP.

- Defensive Database Connectivity: Embedded PHP scripts handle connection states gracefully, providing error reporting while securing operational parameters against injection risks.

- Optimized Resource Scaling: The modular architecture allows effortless scaling—enabling new plant sensor feeds or additional tracking fields to be deployed simply by expanding the MySQL table configurations and matching endpoint parameters.



## ⚙️ Deployment & Setup Instructions

- Database Initialization: Import the structural scripts located inside DB/ptar_datos.sql into your target MySQL instance to set up tables and keys.

- Environment Configuration: Adjust your local database credentials (host, username, password, database name) inside the global entry parameters file located in the core config/ directory.

- Web Server Deployment: Serve the root directory utilizing a stack configuration engine (such as Apache via XAMPP/WAMP or a standalone web proxy server environment supporting PHP 8.x). 

--- 


## 📁 Project Directory Structure



Based on the production tree, the system separates administrative privileges from public-facing user views and static assets:



```text

├── Admin_page/              # Restricted Administrative Control Center

│   ├── config/              # Configuration

│   ├── css_admin/           # Admin-specific rendering layouts

│   ├── scripts/             # Administrative event handlers and async scripts

│   ├── php/                 # Server-side validation, database triggers, and admin controllers

├── DB/                      # Database Schema Definition & Setup

    └── ptar_datos.sql       # Relational SQL schema definitions, table DDLs, and indexing
