import socket

def scan_ports(target, start_port=1, end_port=1024, timeout=1.0):
    ip_adress = socket.gethostbyname(target)
    print(f"Scanning target {target} ({ip_adress}) from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)

            result = sock.connect_ex((target, port)) # 0 means port open
            if(result == 0):
                print(f"[+] Port {port} is OPEN")
                try:
                    banner = sock.recv(1024).decode().strip()
                    print(f"[+] Banner grabbed: {banner} on port {port}")
                except:
                    print(f"[!] Could not determine service running on port {port}")
                open_ports.append(port)

            sock.close()

        except KeyboardInterrupt:
            print(f"\n[!]Scan interrupted by user.")
            break
        
        except socket.gaierror:
            print("[!] Hostname could not be resolved.")
            break

        except socket.error:
            print("[!] Could not connect to the server.")

    print("\nScan complete.")
    return open_ports


if __name__ == "__main__":
    target_host = input("Enter target IP or domain: ").strip()
    scan_ports(target_host)