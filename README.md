# 📡 Network Vulnerability Scanner (Python + Nmap)

## 📌 Overview
This project is a **basic network vulnerability scanner** built using Python. It uses **Nmap** to scan a target system and identifies open ports along with their associated services. Based on predefined rules, it classifies each port into **High, Medium, or Low risk levels**.

---

## 🎯 Features
- 🔍 Scans target system using Nmap (`-sV` for service detection)
- 📊 Identifies open ports and running services
- ⚠️ Classifies risk levels:
  - High Risk
  - Medium Risk
  - Low Risk
- 📄 Generates a structured scan report (`scan_report.txt`)
- 🧠 Beginner-friendly and easy to understand

---

## 🛠️ Technologies Used
- Python
- Nmap
- Subprocess module

---

## ⚙️ Prerequisites

Make sure the following are installed:

### 1. Python
Check version:
```bash
python --version
