"""
Provided a string, find out if it satisfies the IPv4 address naming rules.
There are two versions of the Internet protocol, and thus two versions of addresses. 
One of them is the IPv4 address.
"""
def is_ipv4_address(ip_string):

    # Split the ip_string into the four pieces separated by dots.
    ip_pieces = ip_string.split('.')

    # Validate if there are exactly four pieces
    if len(ip_pieces) != 4:
        return False
    
    # Validate if each pieces is an integer between 0 and 255
    for pieces in ip_pieces:
        if not pieces.isdigit() or int(pieces) > 255 or (pieces[0] == '0' and len(pieces) > 1):
            return False
    
    return True


#inputString = "172.16.254.1"
inputString = "172.216.354.1"
#inputString = ".254.255.0"

print(is_ipv4_address(inputString))
