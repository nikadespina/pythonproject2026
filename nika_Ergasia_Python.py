# ============================================
# PYTHON PROJECT 2026
# Διαχείριση σχολικών λεσχών
# ============================================

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
    print("\nΜΕΝΟΥ ΔΙΑΧΕΙΡΙΣΗΣ ΛΕΣΧΩΝ\n")
    print("1. Εμφάνιση όλων των λεσχών")
    print(robotics_info[0])
    print(theater_info[0])
    print(music_info[0])
    print(sports_info[0])

    print("\n2. Εμφάνιση στοιχείων της Ρομποτικής λέσχης")
    print(club_infos[0])

    print("\n3. Εμφάνιση μαθητών της Μουσικής Λέσχης")
    for student in music_club:
        print("-", student)

    print("\n4. Αναζήτηση του μαθητή Πέτρος")
    if "Πέτρος" in music_club:
        print("Το όνομα βρέθηκε στο set music_club")

    print("\n5. Προσθήκη μαθητή στην Μουσική Λέσχη:")
    while True:
        name = input("Δώστε όνομα μαθητή:").strip()
        if name == "":
            print("Το όνομα δε μπορεί να είναι κενό.")
        else:
            break
    music_club.add(name)
    for student in music_club:
        print("-", student)

    print("\n6. Διαγραφή μαθητή")
    name = robotics_club.pop()
    print(f"Διαγραφή του ονόματος:{name}")
    for student in robotics_club:
        print("-", student)

    print("\n7. Εμφάνιση όλων των μοναδικών μαθητών της Αθλητικής Λέσχης:")
    for student in sports_club:
        print("-", student)

    print("\n8. Εμφάνιση κοινών μαθητών της μουσικής και της θεατρικής λέσχης:")
    common_students = music_club.intersection(theater_club)
    if len(common_students) > 0:
        for student in common_students:
            print("-", common_students)
    else:
        print("Δεν υπάρχουν κοινοί μαθητές")

    print("\n9. Εμφάνιση μαθητών μόνο της ρομποτικής και όχι και της θεατρικής:")
    only_robotics_club = robotics_club - theater_club
    print("-", student)

    while True:
     print("\n10. Έξοδος")
     choice = input("Δώστε επιλογή:").strip()

     match choice:
        case "1":
            code = input("Δώστε κωδικό(1234): ")
            if code == "1234":
                print("Σωστός κωδικός.")
            else:
                print("Λάθος κωδικός.")
            break
        case "2":
            print("Τέλος προγράμματος")
            break
        case _:
             print("Μη έγκυρη επιλογή.")
    break






















