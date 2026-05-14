# Centra: Basic Security Scanner

A simple Python tool to scan your project files for common security mistakes like hardcoded passwords, secret keys, or exposed IP addresses.

## How it works
It uses regular expressions (Regex) to search through common file types (`.py`, `.env`, `.js`, etc.) and alerts you if it finds anything that looks like a sensitive credential.

## Features
- Scans for hardcoded passwords and secrets.
- Finds exposed IP addresses.
- Easy to use and lightweight.

## Usage
1. Make sure you have Python installed.
2. Place `centra.py` in your project root.
3. Run the script:
   ```bash
   python centra.py
   ```

## Example Output
```text
--- Centra: Basic Security Scanner ---
Scanning current directory for hardcoded secrets and IPs...

[!] Issues in config.py:
    [Password/Secret] Line 5: DB_PASSWORD = "admin_password"
    [IP Address] Line 12: SERVER_IP = "192.168.1.100"

Scan complete!
```
