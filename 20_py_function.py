""" 
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.
The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

"""
def is_mac_forty_eight(mac_address):

    # Check if the mac address has a length between 15 and 20 characters
    if len(mac_address) < 15 or len(mac_address) > 20:
        return False
    
    # Split the mac address into groups of two hexadecimal digits
    groups = mac_address.split("-")
    
    # Check if there are exactly six groups
    if len(groups) != 6:
        return False
    
    # Check if each group contains exactly two hexadecimal digits
    for group in groups:
        if len(group) != 2:
            return False
        
        # Check if each hexadecimal digit is valid
        for char in group:
            if not (char.isdigit() or char in ["A", "B", "C", "D", "E", "F"]):
                return False
    
    return True

mac_one = "00-1B-63-84-45-E6"
mac_two = "Z1-1B-63-84-45-E6"
mac_three = "not a MAC-48 address"

print(is_mac_forty_eight(mac_one))
print(is_mac_forty_eight(mac_two))
print(is_mac_forty_eight(mac_three))