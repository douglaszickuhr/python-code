import re

x = "192.123.332.12"

def val_ip(ip):
    if ip.count(".") != 3:
        return False

    return not [x for x in ip.split('.') if int(x) > 255]