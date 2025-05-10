mark = input("enter user score or mark: ");
mark = int(mark);

if mark>=90 and mark<=100:
    print("Grade A")
elif mark>=80 and mark<=89:
    print("Grade B")
elif mark>=70 and mark<=79:
    print("Grade C")
elif mark>=60 and mark<=69:
    print("Grade D")
elif mark>=50 and mark<=59:
    print("Grade E")
elif mark>=40 and mark<=49:
    print("Grade E-")
else:
    print("Grade Fail or F")