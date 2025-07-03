print("How many students?")
students = int(input())
print("Required group size?")
group_size = int(input())


num_groups = students // group_size
leftover = students % group_size


group_word = "group" if num_groups == 1 else "groups"
student_word = "student" if leftover == 1 else "students"


print(f"There will be {num_groups} {group_word} with {leftover} {student_word} left over.")