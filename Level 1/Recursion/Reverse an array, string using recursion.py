def reverseAnArray(ip_array):
    if len(ip_array)==1:
        return
    alpha = ip_array.pop(0)
    reverseAnArray(ip_array)
    ip_array.append(alpha)

ip_array = [1,2,3]
reverseAnArray(ip_array)
print(ip_array)