students = [113, 175, 12]
group_size = 24

for student_count in students:
    full_groups = student_count // group_size
    leftover_students = student_count % group_size
    print(f"For {student_count} students: {full_groups} full groups and {leftover_students} students in the smaller group.")