sweets = int(input("Enter the total number of sweets: "))
pupils = int(input("Enter the number of pupils: "))


sweets_per_pupil = sweets // pupils
leftovers = sweets % pupils


print(f"Each pupil will get {sweets_per_pupil} sweet(s).")
print(f"The teacher will have {leftovers} sweet(s) left over.")
