import socket
from common_ports import ports_and_services

def get_open_ports(target, port_range, verbose=False):
    try:
        ip_address = socket.gethostbyname(target)
    except socket.gaierror:
        try:
            # Check if target is an IP address
            socket.inet_aton(target)
            return "Error: Invalid IP address"
        except socket.error:
            return "Error: Invalid hostname"

    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((ip_address, port)) == 0:
                open_ports.append(port)

    if verbose:
        hostname = target
        try:
            hostname = socket.gethostbyaddr(ip_address)[0]
        except socket.herror:
            pass

        open_ports_info = f"Open ports for {hostname} ({ip_address})\nPORT     SERVICE"
        for port in open_ports:
            service_name = ports_and_services.get(port, "UNKNOWN")
            open_ports_info += f"\n{port:<9}{service_name}"
        return open_ports_info
    else:
        return open_ports
