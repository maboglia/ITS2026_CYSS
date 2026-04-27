import sys


if len(sys.argv) != 3:
    print("Uso: python modulo_02.py nome eta")
    sys.exit(1)

nome = sys.argv[1]
eta = int(sys.argv[2])

print(nome, eta)

print(sys.version)
print(sys.platform)

print(sys.path)

x = [1,2,3]
print(sys.getsizeof(x))
print(id(x))
