marks=int(input("Enter your marks:"))
if marks>100 or marks<0:
    print("invalid marks")
elif marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
else:
    print("Grade C")