from roster import student_roster
#accessing iterator tools
import itertools

class ClassroomOrganizer:
    def __init__(self):
        self.sorted_names = self._sort_alphabetically(student_roster)

    def _sort_alphabetically(self,students):
        names = []
        for student in students:
            name = student['name']
            names.append(name)
        return sorted(names)
  
    def student_combination(self):
        #creating a list with all possible combinations of 2 students
        res = list(itertools.combinations(self.sorted_names, 2))
        return res

    def get_students_with_subject(self, subject):
        selected_students = []
        for student in student_roster:
            if student['favorite_subject'] == subject:
                selected_students.append((student['name'], subject))
        return selected_students

classroom1 = ClassroomOrganizer()
#creating an iterator object of our ClassroomOrganizer instance
classroom1_iter = iter(classroom1.sorted_names)
for i in range(10):
  print(next(classroom1_iter))