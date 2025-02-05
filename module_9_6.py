def all_variants(text):
    n = len(text)
    for start in range(n):
        for end in range(start, n):
            yield text[start:end + 1]


a = all_variants("abcdef")
for i in a:
    print(i)
