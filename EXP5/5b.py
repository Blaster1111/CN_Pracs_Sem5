import socket 

def is_valid_ip(ip): 
    """Check if the IP address is valid.""" 
    if len(ip) != 4: 
        return False 
    for octet in ip: 
        if not (0 <= octet <= 255):
            return False  
    return True  

def main(): 
    try: 
        hostname = input("Enter the URL: ") 
        ip = socket.gethostbyname(hostname) 
    except socket.gaierror: 
        print("Invalid URL or unable to resolve hostname.") 
        return 
    print("Your Computer Name is: " + hostname) 
    print("Your Computer IP Address is: " + ip) 
    ip_arr = ip.split('.') 
    if len(ip_arr) != 4: 
        print("Invalid IP") 
        return 
    try: 
        ip_arr = [int(i) for i in ip_arr] 
    except ValueError: 
        print("Invalid IP") 
        return 
    if not is_valid_ip(ip_arr): 
        print("Invalid IP") 
        return 
    first_octet = ip_arr[0] 
    if 0 <= first_octet <= 127: 
        print("Class A") 
        print("Subnet Mask: 255.0.0.0") 
        subnet_address = f"{ip_arr[0]}.0.0.0" 
    elif 128 <= first_octet <= 191: 
        print("Class B") 
        print("Subnet Mask: 255.255.0.0") 
        subnet_address = f"{ip_arr[0]}.{ip_arr[1]}.0.0" 
    elif 192 <= first_octet <= 223: 
        print("Class C") 
        print("Subnet Mask: 255.255.255.0") 
        subnet_address = f"{ip_arr[0]}.{ip_arr[1]}.{ip_arr[2]}.0" 
    elif 224 <= first_octet <= 239: 
        print("Class D") 
        print("Subnet Address does not exist") 
        return 
    elif 240 <= first_octet <= 255: 
        print("Class E") 
        print("Subnet Address does not exist") 
        return 
    else: 
        print("This IP address is not within the range of Classes A, B, or C.") 
        return 
    print(f"Subnet Address: {subnet_address}") 
if __name__ == "__main__": 
    main()