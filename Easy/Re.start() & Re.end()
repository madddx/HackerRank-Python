import re
s,k = [input() for _ in range(2)]
p = r'(?=(%s))' % re.escape(k)
print("\n".join("(%s, %s)"%(match.start(1),match.end(1)-1) for match in re.finditer(p, s)) or "(-1, -1)")
