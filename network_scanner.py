import socket  # Handles network connections
import subprocess  # Runs system commands from Python
import ipaddress  # Works with IP addresses and networks
import platform  # Detects OS type
from concurrent.futures import ThreadPoolExecutor  # Enables multithreading

def get_local_network_info():
    # Figures out the local subnet automatically
    hostname = socket.gethostname()  # Get the computer's hostname
    local_ip = socket.gethostbyname(hostname)  # Get its local IP address

    # Extract the first three octets to form a subnet (e.g., "192.168.1.0/24")
    subnet = ".".join(local_ip.split(".")[:-1]) + ".0/24"
    return local_ip, subnet

def ping_host(ip):
    # Pings an IP to check if it's online (This should work across platforms but i have only tested it on Windows)
    os = "-n" if platform.system().lower() == "windows" else "-c"
    
    try:
        result = subprocess.run(["ping", os, "1", "-w", "500", ip], capture_output=True, text=True)
        if "Reply from" in result.stdout or "bytes from" in result.stdout:
            return ip  # If there's a reply, the device is up
    except Exception:
        return None
    return None

def scan_network(local_ip, subnet):
    # Scans the network to find devices that are online
    print(f"Scanning network: {subnet} ...")

    network = ipaddress.IPv4Network(subnet, strict=False)  # Get all usable IPs
    active_ips = []

    # Use threading to speed up scanning (you can adjust the workers if needed)
    with ThreadPoolExecutor(max_workers=20) as executor:
        results = executor.map(ping_host, [str(ip) for ip in network.hosts()])

    for ip in results:
        if ip and ip != local_ip:  # Skip the local machine
            active_ips.append(ip)

    return active_ips

def scan_ports(ip, ports=["22, 80, 443, 3389, 8080"]): # Enter the ports you wish to scan. I have inlcuded common ones.
    # Scans the list of ports
    open_ports = []
    for port in ports:
        # IPv4 + TCP connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)  # Reduced timeout for faster scanning
            # Try to connect, if connect_ex returns 0, the port is open
            if sock.connect_ex((ip, port)) == 0: 
                open_ports.append(port)
    return open_ports

def main():
    local_ip, subnet = get_local_network_info()  # Get subnet info
    devices = scan_network(local_ip, subnet)  # Find online devices

    print("\nDevices Found:")
    for ip in devices:
        ports = scan_ports(ip)  # Check open ports
        print(f"IP: {ip}, Open Ports: {ports}")

if __name__ == "__main__":
    main()
