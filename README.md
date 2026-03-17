# DevSecOps Sample Project

This is a demonstration of a DevSecOps project lifecycle, including automated security scanning and containerization.

## Features

- **Sample App**: A simple Python Flask application.
- **CI/CD Pipeline**: Automated GitHub Actions workflow.
- **Security Scans**:
  - **Bandit**: Static Application Security Testing (SAST).
  - **Safety**: Software Composition Analysis (SCA) for dependencies.
  - **TruffleHog**: Secret scanning to detect hardcoded credentials.
  - **Trivy**: Container image vulnerability scanning.

## Getting Started

### Prerequisites

- Docker
- Python 3.9+

### Running Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python src/app.py
   ```

### Building the Docker Image

```bash
docker build -t devsecops-sample-app .
```

### Running Security Tools Manually

#### Bandit (SAST)
```bash
bandit -r src/
```

#### Safety (SCA)
```bash
safety check
```
