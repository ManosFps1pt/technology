from time import perf_counter

t1: float = perf_counter()

for i in range(1_000_000_000):
    ...

t2: float = perf_counter()

print(f"execution time: {t2-t1} seconds")
