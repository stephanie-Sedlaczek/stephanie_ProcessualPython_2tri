def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
for i in range(1, 101):
    if primo(i):
        print(f"Número primo: {i}")
