# ============================================
# PYTHON PROJECT 2026
# Διαχείριση σχολικών λεσχών
# ============================================
#Xρώματα
from re import search

blue="\033[34m"
cyan="\033[36m"
magenta="\033[35m"
yellow="\033[33m"
green="\033[32m"
reset="\033[0m"
# --------------------------------------------
# 1.ΣΤΑΘΕΡΑ ΣΤΟΙΧΕΙΑ ΛΕΣΧΩΝ ΜΕ TUPLES
# --------------------------------------------
# Τα tuples χρησιμοποιούνται για σταθερές πληροφορίες
# --------------------------------------------
robotics_info = ("Ρομποτική", "κ.Παπαδόπουλος", "Δευτέρα")
theater_info = ("Θέατρο", "κ.Ιωάννου", "Τρίτη")
music_info = ("Μουσική", "κ.Δημητρίου", "Τετάρτη");
sports_info = ("Αθλητισμός", "κ.Κωνσταντίνου", "Πέμπτη")

# --------------------------------------------
# 2.ΣΥΝΟΛΑ ΜΑΘΗΤΩΝ ΑΝΑ ΛΕΣΧΗ
# --------------------------------------------
# Τα sets χρησιμοποιούνται για μοναδικά ονόματα μαθητών
# --------------------------------------------
robotics_club = {"Άννα", "Γιάννης", "Μαρία"}
theater_club = {"Μαρία", "Νίκος", "Ελένη"}
music_club = {"Πέτρος", "Άννα", "Σοφία"}
sports_club = {"Γιάννης", "Κώστας", "Ελένη"}

# --------------------------------------------
# 3.ΛΙΣΤΕΣ ΟΡΓΑΝΩΣΗΣ
# --------------------------------------------
# Oι lists χρησιμοποιούνται για την συνολική οργάνωση των δεδομένων
club_infos = [robotics_info, theater_info, music_info, sports_info]
club_students = [robotics_club, theater_club, music_club, sports_club]

# --------------------------------------------
# 4.ΜΕΝΟΥ ΕΠΙΛΟΓΩΝ
# --------------------------------------------
while True:
    print(f"{cyan}\nΜΕΝΟΥ ΔΙΑΧΕΙΡΙΣΗΣ ΛΕΣΧΩΝ{reset}\n")
    print(f"{cyan}1. Εμφάνιση όλων των λεσχών{reset}")  # Πρόσβαση σε στοιχεία tuples
# Ta tuple einai stoixeia ston katalogo club_info
    for info in club_infos:
        print("-",info[0])

    print(f"{cyan}\n2. Εμφάνιση στοιχείων της:{reset}")  # Διαπέραση tuple
    print(f"{blue}\nΡομποτικής λέσχης:{reset}")
    for item in robotics_info: print("-",item)
    print(f"{magenta}\n Μουσικής λέσχης{reset}")
    for item in music_info: print("-", item)
    print(f"{yellow}\nΘεατρικής λέσχης:{reset}")
    for item in theater_info: print("-", item)
    print(f"{green}\n Αθλητικής λέσχης{reset}")
    for item in sports_info: print("-", item)

    print(f"{cyan}\n3. Εμφάνιση μαθητών της:{reset}")
    print(f"{blue}\nΡομποτικής λέσχης:{reset}")
    for student in robotics_club: print("-", student)
    print(f"{magenta}\n Μουσικής λέσχης{reset}")
    for student in music_club: print("-", student)
    print(f"{yellow}\nΘεατρικής λέσχης:{reset}")
    for student in theater_club: print("-", student)
    print(f"{green}\n Αθλητικής λέσχης{reset}")
    for student in sports_club: print("-", student)

    print(f"{cyan}\n4. Αναζήτηση του μαθητή Πέτρος σε όλες τις λέσχες.{reset}")
    club_students=["Άννα", "Γιάννης", "Μαρία","Μαρία", "Νίκος", "Ελένη","Πέτρος", "Άννα", "Σοφία","Γιάννης", "Κώστας", "Ελένη"]
    search_names = "Πέτρος"
    if search_names in club_students:
        print(f"Βρέθηκε το όνομα:{search_names}")

    print(f"{cyan}\n5. Προσθήκη μαθητή στην Μουσική Λέσχη:{reset}")
    while True:
        name = input("Δώστε όνομα μαθητή:").strip()
        if name == "":
            print("Το όνομα δε μπορεί να είναι κενό.")
        else:
            break
    music_club.add(name)
    for student in music_club:
        print("-",student)

    print(f"{cyan}\n6. Διαγραφή μαθητή{reset}")
    name = robotics_club.pop()
    print(f"Διαγραφή του ονόματος:{name}")
    for student in robotics_club:
        print("-",student)

    print(f"{cyan}\n7. Εμφάνιση όλων των μοναδικών μαθητών σε όλο το σχολείο:{reset}")
    club_students = {"Άννα", "Γιάννης", "Μαρία", "Μαρία", "Νίκος", "Ελένη", "Πέτρος", "Άννα", "Σοφία", "Γιάννης",
                     "Κώστας", "Ελένη"}
    for student in club_students:
        print("-", student)

    print(f"{cyan}\n8. Εμφάνιση κοινών μαθητών της μουσικής και της θεατρικής λέσχης:{reset}")
    common_students = music_club.intersection(theater_club)
    if len(common_students) > 0:
        for student in common_students:
            print("-",common_students)
    else:
        print("Δεν υπάρχουν κοινοί μαθητές")
    print(f"{cyan}\nΕμφάνιση κοινών μαθητών της ρομποτικής και της θεατρικής λέσχης:{reset}")
    common_students = robotics_club.intersection(theater_club)
    if len(common_students) > 0:
        for student in common_students:
            print("-", common_students)
    else:
        print("Δεν υπάρχουν κοινοί μαθητές")

    print(f"{cyan}\n9. Εμφάνιση μαθητών μόνο της ρομποτικής και όχι και της θεατρικής:{reset}")
    robotics_club = {"Άννα", "Γιάννης", "Μαρία"}
    theater_club = {"Μαρία", "Νίκος", "Ελένη"}
    only_robotics_club = robotics_club - theater_club
    print("-",only_robotics_club)

    print(f"{cyan}\n10. Έξοδος{reset}")
    choice = input("Δώστε επιλογή:").strip()

    match choice:
        case "1":
            code = input("Δώστε κωδικό(1): ")
            if code == "1":
             print("pass!")
            break;
        case "2":
            code = input("Δώστε κωδικό(2): ")
            if code == "2":
             print("pass!")
            break;
        case "3":
            code = input("Δώστε κωδικό(3): ")
            if code == "3":
             print("pass!")
            break;
        case "4":
            code = input("Δώστε κωδικό(4): ")
            if code == "4":
             print("pass!")
            break;
        case "5":
            code = input("Δώστε κωδικό(5): ")
            if code == "5":
             print("pass!")
            break;
        case "6":
            code = input("Δώστε κωδικό(6): ")
            if code == "6":
             print("pass!")
            break;
        case "7":
            code = input("Δώστε κωδικό(7): ")
            if code == "7":
             print("pass!")
            break;
        case "8":
            code = input("Δώστε κωδικό(8): ")
            if code == "8":
             print("pass!")
            break;
        case "9":
            code = input("Δώστε κωδικό(9): ")
            if code == "9":
             print("pass!")
            break;
        case "10":
             print("Τέλος προγράμματος")
             break;
        case _:
             print("Μη έγκυρη επιλογή.")






















