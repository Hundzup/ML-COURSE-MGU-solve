def find_modified_max_argmax(L, f):
    filtered_int = 0
    result = ("m", "i")
    for i in range(len(L)):
        if type(L[i]) is int:
            if result[0] == "m":
                result = (f(L[i]), filtered_int)
            elif f(L[i]) > result[0]:
                result = (f(L[i]), filtered_int)
            filtered_int += 1
    if filtered_int == 0:
        return tuple()
    return result
