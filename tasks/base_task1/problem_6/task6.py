def check(x: str, file: str):
    f = open(file, "w")
    words_count = {}
    x = x.split()
    x = [s.lower() for s in x]
    for word in x:
        if word not in words_count.keys():
            words_count[word] = 1
        else:
            words_count[word] += 1
    for word in sorted(words_count):
        f.write(f"{word} {words_count[word]}\n")
    f.close()
