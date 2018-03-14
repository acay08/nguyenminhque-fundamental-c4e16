ds = [10,7,8,9,4,-10]
new_ds = []

while True:
    n = min(ds)
    new_ds.append(n)
    ds.remove(n)
    if len(ds) == 0:
        break
print(*new_ds)
