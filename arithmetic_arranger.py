LEFT_OPERAND = 0
OPERATOR = 1
RIGHT_OPERAND = 2
DASHES = 3
RESULT = 4

def arithmetic_arranger(problems, result = False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    standard_table = list()
    for problem in problems:
        split = problem.split()
        #Validate data 
        if split[OPERATOR] != '+' and split[OPERATOR] != '-':
            return "Error: Operator must be '+' or '-'."
        if not (split[LEFT_OPERAND].isnumeric() and split[RIGHT_OPERAND].isnumeric()):
            return 'Error: Numbers must only contain digits.'
        if len(split[LEFT_OPERAND]) > 4 or len(split[RIGHT_OPERAND]) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        #Standardize data
        while len(split[LEFT_OPERAND]) > len(split[RIGHT_OPERAND]):
            split[RIGHT_OPERAND] = ' ' + split[RIGHT_OPERAND]
        while len(split[LEFT_OPERAND]) < len(split[RIGHT_OPERAND]):
            split[LEFT_OPERAND] = ' ' + split[LEFT_OPERAND]

        split[RIGHT_OPERAND] = split[OPERATOR] + ' ' + split[RIGHT_OPERAND]
        split.append('-' * len(split[RIGHT_OPERAND]))
        
        if result:
            caculation = 0
            if split[OPERATOR] == '-':
                caculation = split[LEFT_OPERAND] - split[RIGHT_OPERAND]
            else:
                caculation = split[LEFT_OPERAND] + split[RIGHT_OPERAND]
            caculation = str(caculation)
            while len(caculation) < len(split[RIGHT_OPERAND]):
                caculation = ' ' + caculation
            split.append(caculation)

        standard_table.append(split)

    arranged_problems = ''
    #First Row
    for collum in standard_table:
        arranged_problems += collum[LEFT_OPERAND]
        if collum == standard_table[-1]:
            arranged_problems += '\n'
        else: 
            arranged_problems += ' ' * 4
    
    #Second Row
    for collum in standard_table:
        arranged_problems += collum[RIGHT_OPERAND]
        if collum == standard_table[-1]:
            arranged_problems += '\n'
        else:
            arranged_problems += ' ' * 4
    
    #Third Row
    for collum in standard_table:
        arranged_problems += collum[DASHES]
        if collum == standard_table[-1]:
            arranged_problems += '\n'
        else:
            arranged_problems += ' ' * 4
    
    #Fourth Row
    if result:
        for collum in standard_table:
            arranged_problems += collum[RESULT]
        if collum == standard_table[-1]:
            arranged_problems += '\n'
        else:
            arranged_problems += ' ' * 4

    return arranged_problems