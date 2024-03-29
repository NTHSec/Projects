#!/bin/bash

# LazyRecon - Automating simple recon tasks

# ANSI escape codes for formatting
bold=$(tput bold)
normal=$(tput sgr0)
black=$(tput setaf 0)
red=$(tput setaf 1)
green=$(tput setaf 2)
yellow=$(tput setaf 3)
blue=$(tput setaf 4)
magenta=$(tput setaf 5)
cyan=$(tput setaf 6)
white=$(tput setaf 7)

# Check if the target IP address is provided
if [ -z "$1" ]; then
    echo "${bold}${red}Usage:${normal} ./lazyrecon.sh <target_ip>"
    exit 1
fi

# Assign the first argument to a variable
target_ip="$1"

# Function to run Nmap scan
run_nmap() {
    echo "${bold}${green}Running Nmap scan on target: ${normal}${bold}$target_ip"
    nmap -sC -sV -oN nmap_scan.txt "$target_ip" > /dev/null 2>&1
    echo "${bold}${green}Nmap scan outputted to ${yellow}> nmap_scan.txt${normal}"
}

# Function to run Gobuster scan
run_gobuster() {
    echo "${bold}${green}Port(s) ${cyan}80 and/or ${cyan}443 ${green}have been found, now running Gobuster scan on target: ${normal}${bold}$target_ip"
    gobuster dir -u "http://$target_ip" -w /usr/share/wordlists/dirb/common.txt -t 50 -o gobuster_scan.txt > /dev/null 2>&1
    echo "${bold}${green}Gobuster scan outputted to ${yellow}> gobuster_scan.txt${normal}"
}

# Main function
main() {
    run_nmap
    # Check if ports 80 or 443 are found open in the Nmap scan output
    if grep -qE '80/tcp open|443/tcp open' nmap_scan.txt; then
        run_gobuster
    else
        echo "${bold}${red}Ports 80 or 443 not found open. Skipping Gobuster scan.${normal}"
    fi
}

# Call the main function
main
