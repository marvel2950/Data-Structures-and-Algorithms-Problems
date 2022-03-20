hash_map = {}
def subsetsOfAString(ip,op):
    if len(ip)==0:
        hash_map[op] = 1
        return
    subsetsOfAString(ip[1:],op+ip[0])
    subsetsOfAString(ip[1:],op)
ip = 'abb'
op = ''
subsetsOfAString(ip,op)
print(list(hash_map.keys()))