import socket

open_ports = []

target_ip = input("Enter target IP address: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

print(f"\n[*] Scanning {target_ip} from port {start_port} to {end_port}\n")

for port in range(start_port, end_port + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)

        s.close()  

    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user")
        break

    except socket.error:
        print("[!] Could not connect to target")
        break

print("\n[*] Scan complete")
print(f"[*] Open ports found: {len(open_ports)}")

if open_ports:
    print("[*] Open ports list:", open_ports)
