import random


def jeu_nombre():
    secret = random.randint(1, 100)
    essais = 0
    print("Devine le nombre entre 1 et 100")

    while True:
        try:
            proposition = int(input("Ton choix: "))
            essais += 1
            if proposition < secret:
                print("Trop petit")
            elif proposition > secret:
                print("Trop grand")
            else:
                print(f"Gagne en {essais} essais")
                break
        except ValueError:
            print("Entre un entier valide.")


if __name__ == "__main__":
    jeu_nombre()
