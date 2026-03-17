# 🛡️ Centra: Secure DevSecOps Pipeline

[![DevSecOps Pipeline](https://github.com/USER_NAME/centra/actions/workflows/security.yml/badge.svg)](https://github.com/USER_NAME/centra/actions/workflows/security.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Centra** is a production-grade **DevSecOps CI/CD pipeline** for a Python (FastAPI) web application. The goal is to integrate security at every stage of the software development lifecycle (SDLC), ensuring that vulnerabilities are identified and mitigated before reaching production.

## 🚀 Project Overview

This repository contains a simple REST API with intentional security flaws to demonstrate how automated tools catch them. The pipeline includes SAST, SCA, Secret Scanning, Container Scanning, and SBOM generation.

### 🏗️ Architecture Diagram

```ascii
      +-----------------+
      |  Developer Push |
      +--------+--------+
               |
               v
      +-----------------+      +-----------------------+
      | GitHub Actions  +------>  Security Scans (SAST) |
      | (CI/CD)         |      | (Semgrep, CodeQL)     |
      +--------+--------+      +-----------+-----------+
               |                           |
               v                           v
      +-----------------+      +-----------------------+
      |  Centra Build   |      |  Dependency Scan (SCA)|
      | & Scan (Trivy)  |      |  (Snyk, Safety)       |
      +--------+--------+      +-----------+-----------+
...
               v                           v
      +-----------------+      +-----------------------+
      | SBOM Generation |      |  Secret Scanning      |
      | (Syft)          |      |  (Gitleaks)           |
      +--------+--------+      +-----------------------+
               |
               v
      +-----------------+
      | Docker Hub/ECR  |
      +-----------------+
```

## 🛠️ Tools & Technologies

*   **Application:** Python 3.11, FastAPI, Uvicorn, JWT.
*   **Containerization:** Docker (Multi-stage build, Non-root user).
*   **Orchestration:** Docker Compose.
*   **CI/CD:** GitHub Actions.
*   **Security Tools:**
    *   **SAST:** [Semgrep](https://semgrep.dev/) - Static Analysis Security Testing.
    *   **SCA:** [Snyk](https://snyk.io/) - Software Composition Analysis.
    *   **Secrets:** [Gitleaks](https://github.com/gitleaks/gitleaks) - Hardcoded secret detection.
    *   **Container Scan:** [Trivy](https://github.com/aquasecurity/trivy) - Image vulnerability scanning.
    *   **SBOM:** [Syft](https://github.com/anchore/syft) - Software Bill of Materials.

## 🛡️ DevSecOps Implementation

1.  **Shift-Left Security:** Scans run on every pull request to catch issues early.
2.  **Infrastructure as Code (IaC) Security:** Dockerfile follows best practices (minimal base image, non-root user).
3.  **Vulnerability Management:** The pipeline fails if **High** or **Critical** vulnerabilities are detected.
4.  **Supply Chain Security:** Generates a CycloneDX SBOM for transparency in third-party dependencies.

## 🏃 How to Run Locally

### Prerequisites
*   Docker & Docker Compose
*   Python 3.11 (optional for local dev)

### Steps
1.  **Clone the repo:**
    ```bash
    git clone https://github.com/USER_NAME/centra.git
    cd centra
    ```

2.  **Run with Docker Compose:**
    ```bash
    docker-compose up --build
    ```

3.  **Access the API:**
    *   API Home: `http://localhost:8000/`
    *   Interactive Swagger Docs: `http://localhost:8000/docs`

## 📊 Pipeline Explanation

*   **SAST (Semgrep):** Analyzes source code for common security patterns and vulnerabilities (e.g., hardcoded secrets, SQLi).
*   **SCA (Snyk):** Checks `requirements.txt` for known vulnerabilities in third-party libraries.
*   **Secret Scan (Gitleaks):** Scans the git history for leaked credentials, API keys, and tokens.
*   **Container Scan (Trivy):** Scans the final Docker image for OS-level vulnerabilities and insecure configurations.
*   **SBOM Generation:** Creates a machine-readable list of all components used in the application.

## 🔮 Future Improvements

*   [ ] Add DAST (Dynamic Analysis) using OWASP ZAP.
*   [ ] Integrate Kubernetes (EKS/Minikube) deployment manifests.
*   [ ] Implement OPA (Open Policy Agent) for container policy enforcement.
*   [ ] Add Cloud Infrastructure scanning (Terraform/TFLint).

## 📄 License
Distributed under the MIT License. See `LICENSE` for more information.

---
*Created as a DevSecOps Portfolio Project by [Your Name]*
