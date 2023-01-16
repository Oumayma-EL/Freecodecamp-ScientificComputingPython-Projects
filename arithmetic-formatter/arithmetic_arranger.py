import re
def arithmetic_arranger(problems ,results=False):
  if len(problems)>5:
    return "Error: Too many problems."
  lines_1 = list()
  lines_2 = list()
  lines_3 = list()
  lines_4 = list()
  for problem in problems : 
    operand=re.search("[+]", problem) or re.search("[-]", problem)
    if operand:
      if re.search("[+]", problem):
        operator="+"
      else:
        operator="-"
    else:
      return "Error: Operator must be '+' or '-'."
    lst=problem.split(operator)
    distance=max(len(lst[0]), len(lst[1]))
    operands=list()
    for element in lst : 
      element=element.strip()
      if len(element)>4:
        return "Error: Numbers cannot be more than four digits."
      try:
        element=int(element)
        operands.append(element)
      except:
        return "Error: Numbers must only contain digits."

    if operator=="+":
      res=operands[0]+operands[1]
    else:
      res=operands[0]-operands[1]

    line_1=str(operands[0])
    line_2=str(operands[1])
    line_3=len(line_1.rjust(distance+1))*"-"
    line_4=str(res)
    # Making the lines in the same order
    lines_1.append(line_1.rjust(distance+1))
    lines_2.append(f"{operator} "+line_2.rjust(distance-1))
    lines_3.append(line_3)
    lines_4.append(line_4.rjust(distance+1))
    # Adding the \n to the end of each list 
  lines_1[len(lines_1)-1]=lines_1[len(lines_1)-1]+"\n"
  lines_2[len(lines_2) - 1] = lines_2[len(lines_2) - 1] +"\n"
  if results:
    lines_3[len(lines_3) - 1] = lines_3[len(lines_3) - 1]+"\n"
  else:
    lines_3[len(lines_3) - 1] = lines_3[len(lines_3) - 1]
  
  # Joining them :
  l1="    ".join(map(str, lines_1))
  l2="    ".join(map(str, lines_2))
  l3="    ".join(map(str, lines_3))
  l4="    ".join(map(str, lines_4))
  
  if results:
    arranged_problems=l1+l2+l3+l4
  else:
    arranged_problems=l1+l2+l3
  
  return arranged_problems
    
    # return arranged_problems

