import re

def check_cb(cnum):
    if not bool(re.match(r"^[4,5,6]",cnum)):return "Invalid"
    if not bool(re.match(r"^\d{4}-\d{4}-\d{4}-\d{4}$|^\d{4}\d{4}\d{4}\d{4}$",cnum)):return "Invalid"
    if bool(re.search(r'(.)\1{3}',re.sub(r'\D', '', cnum))):return "Invalid"
    return "Valid"   
n = int(input())
print("\n".join([check_cb(input()) for _ in range(n)]))
