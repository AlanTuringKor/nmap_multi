import concurrent.futures
import subprocess
import argparse
import os

# Function to run nmap scan
def scan_domain(domain):
    """Scans a domain with Nmap using -sC -sV and saves output to a file."""
    output_file = f"{domain}_output.txt"
    try:
        print(f"[+] Scanning {domain}...")
        result = subprocess.run(
            ["nmap", "-sC", "-sV", "-oN", output_file, domain],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode == 0:
            print(f"[✓] Scan of {domain} completed. Results saved to {output_file}")
        else:
            print(f"[✗] Scan of {domain} failed with error: {result.stderr}")
    except Exception as e:
        print(f"[!] Error scanning {domain}: {e}")

# Read domains from file
def load_domains(file_path):
    """Loads domains from a file, stripping whitespace and ignoring empty lines."""
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"[!] Error: The file {file_path} was not found.")
        return []

# Main function to execute scans concurrently
def main():
    # Argument parser
    parser = argparse.ArgumentParser(description="Multi-threaded Nmap Scanner")
    parser.add_argument("file_path", help="Path to the file containing domains")
    args = parser.parse_args()

    file_path = args.file_path

    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"[!] Error: The file '{file_path}' does not exist.")
        return

    domains = load_domains(file_path)

    if not domains:
        print("[!] No domains found in the file. Exiting.")
        return

    # Using ThreadPoolExecutor for multi-threading
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(scan_domain, domains)

if __name__ == "__main__":
    main()
