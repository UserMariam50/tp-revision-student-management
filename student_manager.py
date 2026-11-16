
def calculate_average(grades):
    if len(grades) == 0:
        raise ValueError("La liste des notes est vide")

    return sum(grades) / len(grades)

def get_mention(average):
    if average < 10:
        return "Échec"
    elif average < 12:
        return "Passable"
    elif average < 14:
        return "Assez bien"
    elif average < 16:
        return "Bien"
    elif average < 18:
        return "Très bien"
    else:
        return "Excellent"
    
def is_admitted(average):
    return average >= 10

def validate_grades(grades):
    if len(grades) == 0:
        return False

    for grade in grades:
        if grade < 0 or grade > 20:
            return False

    return True

# C. Test manuel
notes = [12, 15, 18]

average = calculate_average(notes)

print("Moyenne :", average)
print("Mention :", get_mention(average))
print("Admis :", is_admitted(average))
print("Notes valides :", validate_grades(notes))
