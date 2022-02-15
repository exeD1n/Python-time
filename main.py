import time

start = time.perf_counter()

print('Hello man')

end = time.perf_counter()
print(f'{end - start:0.4f} секунд прошло при выполнении кода')