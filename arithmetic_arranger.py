import json
def arithmetic_arranger(problems, answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    probList = []
    addend1 = []
    addend2 = []
    columnTotal = []
    operator = []
    
    # Validate and set addends, operation and total
    for i, problem in enumerate(problems):
        parts = problem.split(" ")
        if (len(parts[0]) > 4) or (len(parts[2]) > 4):
            return "Error: Numbers cannot be more than four digits."
        else: 
            if (parts[0].isdigit() and parts[2].isdigit()):
                addend1.append(parts[0])
                addend2.append(parts[2])
            else:
                return "Error: Numbers must only contain digits."
        if (parts[1]) == '+' or (parts[1]) == '-':
            operator.append(parts[1])
        else: 
            return "Error: Operator must be '+' or '-'."
        if (answers):
            if ((parts[1]) == '-'):
                columnTotal.append(str(int(addend1[i]) - int(addend2[i])))
            else:
                columnTotal.append(str(int(addend1[i]) + int(addend2[i])))

    spacer = '    '
    line0 = ''
    line1 = '\n'
    line2 = '\n'
    line3 = '\n'
    for i in range(len(addend1)):
        # End of line
        if (i == (len(addend1) - 1)): 
            spacer = ''
        # Determine larger width, but add one space to count for operator on line 2
        width = len(addend1[i]) if len(addend1[i]) > len(addend2[i]) else len(addend2[i]) 
        width = width + 1
        line0 += (" " * (len(addend1[i]) - width)) + addend1[i].rjust(width + 1, ' ') + spacer
        line1 += operator[i] + addend2[i].rjust(width, ' ') + spacer
        line2 += ("-" * (width + 1)) + spacer
        if (answers):
            line3 += columnTotal[i].rjust(width + 1, ' ') + spacer
    if not (answers):
        line3 = ''
    
    arranged_problems = line0 + line1 + line2 + line3

    return arranged_problems