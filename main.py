import subprocess

# Target system
target = "127.0.0.1"

print("=== Starting Network Vulnerability Scan ===\n")

# Run Nmap scan and capture output
result = subprocess.run(["nmap", "-sV", target], capture_output=True, text=True)
nmap_output = result.stdout

print(nmap_output)


# Risk classification function
def classify_risk(port):
    high_risk = [445, 3306, 1433]
    medium_risk = [21, 22, 135, 903]

    if port in high_risk:
        return "High"
    elif port in medium_risk:
        return "Medium"
    else:
        return "Low"


# Parse Nmap output
report_data = []

for line in nmap_output.split("\n"):
    if "/tcp" in line and "open" in line:
        parts = line.split()

        try:
            port = int(parts[0].split("/")[0])
            service = parts[2].replace("?", "").split("/")[-1]
            risk = classify_risk(port)

            report_data.append((port, service, risk))
        except:
            continue

# Generate report file
with open("scan_report.txt", "w") as file:
    file.write("=== Network Vulnerability Scan Report ===\n\n")
    file.write(f"Target: {target}\n\n")

    for port, service, risk in report_data:
        file.write(f"Port: {port}\n")
        file.write(f"Service: {service}\n")
        file.write(f"Risk Level: {risk}\n")
        file.write("-----------------------------\n")

print("\n✅ Report generated successfully: scan_report.txt")