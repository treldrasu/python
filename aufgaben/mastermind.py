import random

print("Willkommen bei Mastermind!")
secret_code = [random.randint(1, 6) for _ in range(4)]
attempts = 0

while True:
    attempts += 1
    print(f"\nVersuch {attempts}")
    guess = [int(x) for x in input("Gib deine Vermutung (4 Zahlen von 1 bis 6): ").split()]
    
    if len(guess) != 4 or not all(1 <= num <= 6 for num in guess):
        print("")
        continue

    # Feedback 
    print("R = Richtig, V = Vorhanden, - = nicht Vorhanden")
    feedback = []
    #Prüfen auf R V oder - 


    print("Feedback:", " ".join(feedback))

    if feedback == ...:
        print("Herzlichen Glückwunsch! Du hast den Code geknackt!")
        break
    
    if attempts >= 12:
        print("Du hast alle Versuche aufgebraucht. Der geheime Code war:", secret_code)
        break