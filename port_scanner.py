import nmap
nm=nmap.PortScanner()
ip_address = input("Please enter the IP address that you want to scan: \n")
a=0
try:
    nm.scan(ip_address)
    ip_state=nm[ip_address].state()
    print(f"The state of IP Address {ip_address} is: {ip_state}")
    if(ip_state=='up'):
        mode=int(input("Please enter '1' to scan first 1000 ports, and '0' to scan all the ports: \n"))
        if mode:
            for port in range(1, 1000):
                try:
                    port_state=(nm[ip_address]['tcp'][port]['state'])
                    print(f"Port {port} is {port_state}.")
                except:
                    a=a+1
        else:
            for port in range(1, 65535):
                try:
                    port_state=nm[ip_address]['tcp'][port]['state']
                    print(f"Port {port} is {port_state}.")
                except:
                    a=a+1
        print(f"{a+1} ports are closed.")
except:
    print("Error scanning (Maybe incorrect IP Address)")
