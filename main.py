age = int(input("Enter your age: "))
if age < 18:
  print("You are not eligible to vote. Nor purchase alcohol.")
elif age < 21 and age >= 18:
  print("You can not purchase alcohol. You can vote tho.")
elif age == 21:
  print("no way you are my age!")
elif age > 21: 
  print("Whats up unc. What was the jurassic period like?")