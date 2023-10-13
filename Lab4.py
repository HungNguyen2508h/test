#Hung Nguyen



class MythicalCreatures:
    def __init__(self, name, gender, hasWings):
        self.__name = name
        self.__gender = gender
        self.__hasWings = hasWings
    def get_name(self):
        return self.__name
    def get_gender(self):
        return self.__gender
    def has_wings(self):
        return self.__hasWings
    
class Dragons(MythicalCreatures):
    def __init__(self, name, gender, hasWings, fire, flying, spines, speak):
        MythicalCreatures.__init__(self,  name, gender, hasWings)
        self.__fire = fire
        self.__flying = flying
        self.__spines = spines
        self.__speak = speak

    def has_fire(self):
        return self.__fire

    def can_fly(self):
        return self.__flying

    def has_spines(self):
        return self.__spines

    def can_speak(self):
        return self.__speak

def main():
    try:
        with open('dragons.txt', "r") as file:
            print('Mythical Creatures in Movies\n')
            print('Type\tName\tGender\tWings\tFire\tFly\tSpines\tSpeak\n')
            
            for line in file:
                data = line.strip().split('\t')
                name, gender, hasWings, fire, flying, spines, speak = data
                dragon = Dragons(name, gender, hasWings == 'Y', fire == 'Y', flying == 'Y', spines == 'Y', speak == 'Y')
                print(f"Dragon\t{dragon.get_name()}\t{dragon.get_gender()}\t{'Yes' if dragon.has_wings() else 'No'}\t{'Yes' if dragon.has_fire() else 'No'}\t{'Yes' if dragon.can_fly() else 'No'}\t{'Yes' if dragon.has_spines() else 'No'}\t{'Yes' if dragon.can_speak() else 'No'}")

            print('\nEnd of results.')

    except IOError:
            print("Error:  Input file is not found.")

main()