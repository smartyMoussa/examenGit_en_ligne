def addition(a, b):
    return a + b


def soustraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b if b != 0 else None


def pair(n):
    return n % 2 == 0


def factorielle(n):
    if n < 0:
        return None
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
    return resultat


def max_liste(lst):
    return max(lst) if lst else None


def min_liste(lst):
    return min(lst) if lst else None


def moyenne(lst):
    return sum(lst) / len(lst) if lst else None


def inverse_chaine(s):
    return s[::-1]
