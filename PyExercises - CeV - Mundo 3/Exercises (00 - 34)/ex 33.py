result = {}
def grades():
    '''
    -----------------------------------------------------------------
    -> Function to analyze grades and situations of various students
    -----------------------------------------------------------------
    * grade: Student's grades;
    * c: Amount of grades registered;
    * total: Sum of grades;
    * higher: Highest grade;
    * lower: Lowest grade;
    * avg: Grade average;
    * show: To verify if the user wants to see the class situation.
    -----------------------------------------------------------------
    '''
    c = 1
    higher = lower = avg = total = 0
    while True:
        # Registering the grade and calculating the sum of grades
        print('-'* 45)
        grade = float(input('Insert the grade: '))
        while grade > 10 or grade < 0:
            grade = float(input('Please, insert a valid grade: '))
        total += grade
        # Cheking the biggest and smallest grades
        if c == 1:
            higher = lower = grade
        else:
            if higher < grade:
                higher = grade
            elif lower > grade:
                lower = grade
        # Verifying if the user wants to insert more grades
        cont = str(input('Do you want to insert more grades[y/n]?: ')).strip().lower()[0]
        while cont not in 'yn':
            cont = str(input('Do you want to insert more grades[y/n]?: ')).strip().lower()[0]
        if cont == 'n':
            break
        elif cont == 'y':
            c += 1
    print('-'* 45)
    # Registering the class data
    avg = float(f'{total/c:.1f}')
    result['Total'] = c
    result['Higher'] = higher
    result['Lower'] = lower
    result['Average'] = avg
    # Asking if the user wants to see the class situation
    show = str(input('Do you want to show the situation?[y/n]: '))
    while show not in 'yn':
        show = str(input('Do you want to show the situation?[y/n]: '))
    # Analyzing the class situation
    if show == 'y':
        if avg < 6:
            result['Situation'] = 'Poor'
        elif avg < 7:
            result['Situation'] = 'Moderate'
        elif avg < 9:
            result['Situation'] = 'Good'
        else:
            result['Situation'] = 'Excelent'


grades()
print('-'* 85)
print(result)
print('-'* 85)
