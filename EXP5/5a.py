def isValid(ip): 
    if len(ip) != 4: 
        print("Invalid IP") 
        return False 
    for octet in ip: 
        if not (0 <= octet <= 255): 
            print("Invalid IP") 
            return False 
    return True 
def main(): 
    ip = input("Enter the IP address: ") 
    ipArr = ip.split('.') 
     
    if len(ipArr) != 4: 
        print("Invalid IP") 
        return 
    try: 
        ipArr = [int(i) for i in ipArr] 
    except ValueError: 
        print("Invalid IP") 
        return 
    if not isValid(ipArr): 
        return 
    range = ipArr[0] 
    if 0 <= range <= 127: 
        print("Class A") 
        print("Subnet Mask: 255.0.0.0") 
        subAdd = f"{ipArr[0]}.0.0.0" 
        print(f"Subnet Address: {subAdd}") 
    elif 128 <= range <= 191: 
        print("Class B") 
        print("Subnet Mask: 255.255.0.0") 
        subAdd = f"{ipArr[0]}.{ipArr[1]}.0.0" 
        print(f"Subnet Address: {subAdd}") 
    elif 192 <= range <= 223: 
        print("Class C") 
        print("Subnet Mask: 255.255.255.0") 
        subAdd = f"{ipArr[0]}.{ipArr[1]}.{ipArr[2]}.0" 
        print(f"Subnet Address: {subAdd}") 
    elif 224 <= range <= 239: 
        print("Class D") 
        print("Subnet Address does not exists") 
    elif 240<=range<=255: 
        print("Class E") 
        print("Subnet Address does not exists") 
    else: 
        print("This IP address is not within the range of Classes A, B, or C.") 
if __name__ == "__main__": 
    main() 