def translate(plant_abbv: list) -> list:
    result_list = []
    for double in plant_abbv:
        for single in double:
            if single == 'R':
                result_list.append('Radishes')
            if single == 'C':
                result_list.append('Clover')
            if single == 'G':
                result_list.append('Grass')
            if single == 'V':
                result_list.append('Violets')
    return result_list


class Garden:
    def __init__(self, diagram, students=[
        'Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry'
    ]):
        self.diagram = diagram
        self.students = sorted(students)

    def plants(self, student_name):
        splited_diagram = self.diagram.split('\n')
        result_dict = dict()
        num_of_students = len(splited_diagram[0])/2
        idx = 0
        student_idx = 0
        if type(self.students) is list:
            while student_idx < num_of_students:
                result_dict.update({self.students[student_idx]: [
                    splited_diagram[0][idx], splited_diagram[0][idx+1], splited_diagram[1][idx], splited_diagram[1][idx+1]]})
                idx += 2
                student_idx += 1
            initials = [result_dict.get(student_name)]

            return translate(initials)
        else:
            return translate(splited_diagram)
