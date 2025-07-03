import re
import random

print("Bot: Καλωσήρθες στην Καφετέρια Chatbot!")

while True:
    user_input = input("Εσύ: ")

    # Αν αναγνωρίσουμε χαιρετισμό, να αρχίσουμε τη συζήτηση
    if re.search(r'γεια σου', user_input, re.IGNORECASE):
        print("Bot: Γεια σου! Τι να σου φτιάξω;")
    elif re.search(r'καλημέρα', user_input, re.IGNORECASE):
        print("Bot: Καλημέρα! Τι να σου φτιάξω;")
    elif re.search(r'καλησπέρα', user_input, re.IGNORECASE):
        print("Bot: Καλησπέρα! Τι να σου φτιάξω;")
    elif re.search(r'τι έχετε', user_input, re.IGNORECASE):
        print("Bot: Έχουμε καφέδες και χυμούς!")

    # Αν ζητάει καφέ, να του δώσουμε επιλογές
    elif re.search(r'θέλω καφέ', user_input, re.IGNORECASE):
        print("Bot: Τι καφέ θέλεις; Εσπρέσο, Καπουτσίνο, Φρέντο, Φραπέ;")
        coffee_choice = input("Εσύ: ")

        # Περιμένουμε την απάντηση για τον καφέ
        if re.search(r'θέλω (.*)', coffee_choice, re.IGNORECASE):
            coffe = re.findall(r'θέλω (.*)', coffee_choice, re.IGNORECASE)[0]
            print(f"Bot: Πως θα τον ήθελες τον {coffe}; Σκέτο, Μέτριο, Γλυκό;")
            sweetness = input("Εσύ: ")

            # Αν λέει για συγκεκριμένη γλυκύτητα (σκέτο, μέτριο, γλυκό)
            if re.search(r'σκέτο', sweetness, re.IGNORECASE):
                print(f"Bot: Ο {coffe} σκέτος καφές είναι έτοιμος και έτοιμος για να τον απολαύσεις! ☕")
                print("Bot: Θέλεις να πληρώσεις με μετρητά ή με κάρτα;")

            elif re.search(r'μέτριο', sweetness, re.IGNORECASE):
                print(f"Bot: Ο {coffe} μέτριος καφές είναι έτοιμος και έτοιμος για να τον απολαύσεις! ☕")
                print("Bot: Θέλεις να πληρώσεις με μετρητά ή με κάρτα;")

            elif re.search(r'γλυκό', sweetness, re.IGNORECASE):
                print(f"Bot: Ο {coffe} γλυκός καφές είναι έτοιμος και έτοιμος για να τον απολαύσεις! ☕")
                print("Bot: Θέλεις να πληρώσεις με μετρητά ή με κάρτα;")

        else:
            print("Bot: Δοκίμασε να γράψεις θέλω ... Διαφορετικά μάλλον δεν έχουμε αυτόν τον καφέ. Δοκίμασε Εσπρέσο, Καπουτσίνο, Φρέντο, Φραπέ.")

    #Αν ζητήσει κατευθείαν το είδος καφέ
    elif re.search(r'θέλω\s+(εσπρέσο|καπουτσίνο|φρέντο|φραπέ)', user_input, re.IGNORECASE):
        coffe = re.findall(r'θέλω\s+(εσπρέσο|καπουτσίνο|φρέντο|φραπέ)', user_input, re.IGNORECASE)[0]
        print(f"Bot: Πως θα ήθελες τον {coffe}; Σκέτο, Μέτριο ή Γλυκό;")
        sweetness = input("Εσύ: ")

        if re.search(r'σκέτο', sweetness, re.IGNORECASE):
            print(f"Bot: Ο {coffe} σκέτος καφές είναι έτοιμος και έτοιμος για να τον απολαύσεις! ☕")
            print("Bot: Θέλεις να πληρώσεις με μετρητά ή με κάρτα;")

        elif re.search(r'μέτριο', sweetness, re.IGNORECASE):
            print(f"Bot: Ο {coffe} μέτριος καφές είναι έτοιμος και έτοιμος για να τον απολαύσεις! ☕")
            print("Bot: Θέλεις να πληρώσεις με μετρητά ή με κάρτα;")

        elif re.search(r'γλυκό', sweetness, re.IGNORECASE):
            print(f"Bot: Ο {coffe} γλυκός καφές είναι έτοιμος και έτοιμος για να τον απολαύσεις! ☕")
            print("Bot: Θέλεις να πληρώσεις με μετρητά ή με κάρτα;")

        else:
            print("Bot: Δεν κατάλαβα τη γλυκύτητα. Πες μου αν τον θέλεις σκέτο, μέτριο ή γλυκό.")

    # Αν ζητήσει χυμό
    elif re.search(r'θέλω χυμό', user_input, re.IGNORECASE):
        print("Bot: Τι χυμό θα θέλατε; Βύσσινο, Πορτοκάλι, Ανάμεικτο; ☕")
        juice_choice = input("Εσύ: ")

        if re.search(r'θέλω (.*)', juice_choice, re.IGNORECASE):
            juice = re.findall(r'θέλω (.*)', juice_choice, re.IGNORECASE)[0]
            print(f"Bot: Ο χυμός {juice} είναι έτοιμος και μπορείς να τον απολαύσεις! ☕")
            print("Bot: Θέλεις να πληρώσεις με μετρητά ή με κάρτα;")

    # Αν ο χρήστης ρωτήσει την τιμή του καφέ
    elif re.search(r'πόσο κάνει ο καφές', user_input, re.IGNORECASE):
        print("Bot: Όλοι οι καφέδες έχουν 2€!")

    # Αν ο χρήστης ρωτήσει την τιμή του χυμού
    elif re.search(r'πόσο κάνει ο χυμός', user_input, re.IGNORECASE):
        print("Bot: Οι χυμοί κοστίζουν 1.50€!")
    # Αν ο χρήστης επιλέξει "μετρητά"
    elif re.search(r'μετρητά', user_input, re.IGNORECASE):
        # Ορίζουμε την τιμή του καφέ (2€)
        price = 2

        # Ζητάμε από τον χρήστη το ποσό που πληρώνει
        amount_paid = input("Bot: Πόσα χρήματα έδωσες; ")

        try:
            amount_paid = float(amount_paid)
            while amount_paid < price:
                print(f"Bot: Χρειάζεσαι {price - amount_paid}€ ακόμα για να καλύψεις το κόστος του καφέ.")
                amount_paid = input("Bot: Πόσα χρήματα έδωσες; ")  
                amount_paid = float(amount_paid)
            
            # Αφού πληρωθεί το ποσό σωστά
            change = amount_paid - price
            print(f"Bot: Η πληρωμή με μετρητά ολοκληρώθηκε με επιτυχία! Το υπόλοιπο είναι {change}€. Ευχαριστούμε για την παραγγελία! ☕")
        except ValueError:
            print("Bot: Συγγνώμη, δεν κατάλαβα το ποσό. Παρακαλώ δοκιμάστε ξανά με έναν αριθμό.")


    # Αν ο χρήστης επιλέξει "κάρτα"
    elif re.search(r'κάρτα', user_input, re.IGNORECASE):
        print("Bot: Η πληρωμή με κάρτα ολοκληρώθηκε με επιτυχία! Ευχαριστούμε για την παραγγελία! ☕")

    # Αν πει "ευχαριστώ"
    elif re.search(r'ευχαριστώ', user_input, re.IGNORECASE):
        print("Bot: Παρακαλώ! Καλή απόλαυση ☕")

    # Αν πει "τέλος"
    elif user_input.lower() == "τελος":
        print("Bot: Ευχαριστούμε! Τα λέμε!")
        break

    else:
        responses = [
            "Bot: Συγγνώμη, δεν κατάλαβα. Μπορείς να μου πεις ξανά; Δοκίμασε θέλω καφέ ή θέλω χυμό.",
            "Bot: Δεν καταλαβαίνω... Μπορείς να επαναλάβεις; Δοκίμασε θέλω καφέ ή θέλω χυμό.",
            "Bot: Συγγνώμη, αλλά δεν ξέρω τι θες. Θες καφέ;"
        ]
        print(random.choice(responses))
