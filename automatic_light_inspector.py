
class lecture_hall:
    def __init__(self, name, is_empty, lights_on):
        self.name = name
        self.is_empty = is_empty
        self.lights_on = lights_on

class Office:
    def __init__(self, name, is_empty, lights_on):
        self.name = name
        self.is_empty = is_empty
        self.lights_on = lights_on


lecture_halls = [
    lecture_hall("Lecture Hall 1", False, False),
    lecture_hall("Lecture Hall 2", True, False),
    lecture_hall("Lecture Hall 3", True, True),
    lecture_hall("Lecture Hall 4", True, False),
    lecture_hall("Lecture Hall 5", True, True),
    lecture_hall("Lecture Hall 6", True, False),
    lecture_hall("Lecture Hall 7", False, True),
    lecture_hall("Lecture Hall 8", True, True),
    lecture_hall("Lecture Hall 9", True, False),
    lecture_hall("Lecture Hall 10", True, True),
    ]

offices = [
    Office("Office 1", False, True),
    Office("Office 2", True, False),
    Office("Office 3", True, True),
    Office("Office 4", True, True),
    Office("Office 5", True, True),
    Office("Office 6", True, False),
    Office("Office 7", False, True),
    Office("Office 8", True, True),
    Office("Office 9", True, False),
    Office("Office 10", False, True),
    Office("Office 11", False, True),
    Office("Office 12", False, True),
    Office("Office 13", True, True),
    Office("Office 14", True, True),
    Office("Office 15", False, False),
    ]

def conserve_power(list_of_objs):
    count = 0
    for room in list_of_objs:
        if room.is_empty and room.lights_on:
            count = count +1
            print(f"{room.name} lights turned off")
    return count


def inspect_halls():
    print("Inspecting Lecture Halls...")
    total = conserve_power(lecture_halls)
    print(f"----------> a total of {total} lights turned off")
    print("================================")

def inspect_offices():
    print("Inspecting Offices...")
    total = conserve_power(offices)
    print(f"----------> a total of {total} lights turned off")
    print("================================")


inspect_halls()
inspect_offices()


        
        



