
className = input("What's the class name?")

numCategories = int(
    input("How many grade categories are there on the syllabus (like quizzes, participation, final exam, etc)?"))
categories = {}
for num in range(numCategories):
    category = input("Name of category " + str(num + 1))
    categories[category] = -1

for category in categories:
    categories[category] = float(input("What percentage of your final grade is from "+category+"(in decimal form, listed on the syllabus)?"))


gradesMissing = input("Now for your grades. Are there any categories where you have no grades for? (usually final exam category) enter \"y\" for yes or \"n\" for no")
totalPercentage = 1.0
while gradesMissing:
    if gradesMissing == "y":
        missingCategories = input("name of categories with no grade (separate with comma)")
        missingCategories = missingCategories.split()
        for missingCategory in missingCategories:
            totalPercentage = totalPercentage-categories[missingCategory]
            del categories[missingCategory]
        break
    elif gradesMissing == "n":
        break
    else:
        gradesMissing = input("Please enter \"y\" for yes there are categories with no grade or \"n\" for no")

yourGrades = []
for category in categories:
    grade = float(input("What is your grade in "+category+" (percentage form, don't include percent sign)"))
    yourGrades.append(grade)

i = 0
total = 0
for category in categories:
    total = total+((yourGrades[i])*(categories[category]))
    i += 1

finalPercentage = total/totalPercentage
print("Your grade in "+str(className)+ " is "+str(finalPercentage))
