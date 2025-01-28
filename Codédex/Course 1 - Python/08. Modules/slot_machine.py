import random

def play():
    simbolos = ['🍒', '🍇', '🍉', '7️⃣']

    while True:
        resultado = random.choices(simbolos, k=3)

        print(' | '.join(resultado))

        if resultado.count('7️⃣') == 3:
            print("Jackpot! 💰")
        else:
            print("Obrigado por jogar!")

        play_again = input("Você gostaria de jogar de novo? (S/N): ").strip().upper()
        if play_again != 'S':
            print("Tchau! Obrigado por jogar.")
            break

if __name__ == "__main__":
    play()