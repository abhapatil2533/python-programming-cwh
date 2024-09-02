sub1 = int(input("Enter marks in subject 1: "))
sub2 = int(input("Enter marks in subject 2: "))
sub3 = int(input("Enter marks in subject 3: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are FAIL cuz no 33")
if((sub1+sub2+sub3)/3 <40):
    print("You are FAIL cuz no 40")
else:
    print("you are Pass")

