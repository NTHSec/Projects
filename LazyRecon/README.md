# LazyRecon
LazyRecon is a super simple bash script designed to automate simple reconnaissance tasks during Capture The Flag (CTF) competitions or simple security assessments. This project is going to be dynamic in the sense that I will be constantly revisiting the script, adding more tools and automation as I see fit.

## Purpose
The purpose of LazyRecon is to streamline the process of gathering basic information about a target system, such as open ports and web directories, using popular tools like Nmap and Gobuster. This script is intended to save time and effort by automating repetitive tasks, allowing users to focus on more advanced analysis and exploitation techniques.

## Features
- Automates Nmap scanning to identify open ports and services.
- Runs Gobuster to enumerate web directories if ports 80 or 443 are found open.
- Color-coded output for easy readability.
- Option to specify the target IP address as a command-line argument.

## Quick Start Guide
1. Clone the repository:
```bash
git clone https://github.com/your_username/LazyRecon.git
```

2. Navigate to the LazyRecon directory:
```bash
cd LazyRecon
```

3. Make the script executable:
```bash
chmod +x lazyrecon.sh
```

4. Run the script with the target IP address:
```bash
./lazyrecon.sh <target_ip>
```
*Replace <target_ip> with the IP address of your target.*

5. View the output files:

- nmap_scan.txt: Nmap scan results.
- gobuster_scan.txt: Gobuster scan results (if applicable).
  
## Requirements
- Bash 
- Nmap
- Gobuster
  
## Disclaimer
This script is provided for educational and ethical purposes only. Use it responsibly and ensure that you have proper authorization before conducting reconnaissance activities on any system or network.
