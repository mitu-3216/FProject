import socket
import ipaddress
import re

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535

open_ports = []

while True:
    ip_add_entered = st.text_input("\nPlease enter the ip address that you want to scan: "))
    if(st.button("Submit")):
    try:
        ip_address_obj = ipaddress.ip_address(ip_add_entered)
        st.write("You entered a valid ip address.")
        break
    except:
        st.write("You entered an invalid ip address")

while True:
   
    st.write("Please enter the range of ports you want to scan in format: (example would be 60-120)")
    port_range =st.write_input("Enter port range: ")
    if(st.button("Submit")):
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

for port in range(port_min, port_max + 1):
   
    try:
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            
            s.settimeout(0.5)
            
            s.connect((ip_add_entered, port))
            open_ports.append(port)

    except:

        pass

for port in open_ports:
    st.write(f"Port {port} is open",", protocols is tcp")
    #print(socket.getservbyport({open_ports}))
    #print({port}'-v -sS -sV -sC -A -O')
    #print(socket.getservbyport(open_ports[ip_add_entered]))
    #print(socket.getservbyport(int(open_ports)))
    #print(scanner[ip_add_entered].all_protocols())

    st.write("\n\n----------------Solution---------------\n\n")

    print("1. Access ports using a secure virtual private network (VPn).\n2. Use multi-factor authentication.\n3. Implement network segmentation.\n4.Change Port number from standard to random unused one to help obfuscate. \n5.Setup firewall to restrict incoming traffic only to valid sources though up can be spoofed./n"
    "6.Blocking/restricting ports at the router \n7.configuring a firewall on the system the service is running on and blocking/restricting ports at the system - sometimes this firewall is part of an antivirus package \n8.Running monitoring software on your network that A) logs traffic for later analysis, B) updates and enacts IP and other blocklists from a service, and/or C) looks for patterns in incoming traffic and sends alerts if anything unusual is found.\n"

"9.inserting a device (dedicated firewall, security device) between router and core switch that does any of the above\n"

"10.Software blacklisting on systems (specific executables can't be run, very often integrated with antivirus or other security suite)\n"

"11.Software whitelisting on systems (only specific executables can be run)\n"

"12.Restricting access through physical network topology or VLAN assignments\n"

"13.VPN/encrypted tunnel services, running on edge of network (on or between router and core switch), that only allow external access when authenticated and encrypted.")
