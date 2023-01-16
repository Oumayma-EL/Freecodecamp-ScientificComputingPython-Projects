class Category:
  def __init__(self, budget_categories: str):
    self.budget_categories = budget_categories
    self.ledger = list()

    assert self.budget_categories == "Food" or "Clothing" or "Auto"

  def deposit(self, amount: float, description=""):
    assert len(format(amount,".2f"))<=7,"The number can't be more than 4 digits"
    dep = dict()
    dep["amount"] = float(amount)
    dep["description"] = description
    self.ledger.append(dep)

    
  def withdraw(self, amount: float, description=""):
    assert len(format(amount,".2f"))<=7,"The number can't be more than 4 digits"
    wit = dict()
    wit["amount"] = float(-1 * amount)
    wit["description"] = description
    if self.check_funds(amount):
        self.ledger.append(wit)
        return True
    else:
        return False

  def get_balance(self):
    sum = 0
    for ele in self.ledger:
        # print(ele)
        sum += ele["amount"]
    return float(sum)

  def transfer(self, amount: float, budget):
    assert len(format(amount,".2f"))<=7,"The number can't be more than 4 digits"
    if self.check_funds(amount):
        description1 = f"Transfer to {budget.budget_categories}"
        self.withdraw(amount=amount, description=description1)
        description2 = f"Transfer from {self.budget_categories}"
        budget.deposit(amount=amount, description=description2)
        return True
    else:
        return False

      
  def check_funds(self , amount:float):
    total=self.get_balance()
    if total<amount:
        return False
    return True

  def __repr__(self):
    line_1=self.budget_categories.center(30,"*")
        
    descs=list()
    for ele in self.ledger:
        for key, value in ele.items():
            descs.append(value)

    word=str()
    longueur=len(descs)
    for i in range(longueur):
      if i%2==0:
        continue
      else:
        word=word+f"{descs[i][:23]}"+format(descs[i-1],'.2f')[:7].rjust(len(line_1)-len(descs[i][:23]))+"\n"
      line_2="Total: "+format(self.get_balance(),'.2f')
    return line_1+"\n"+word+line_2




def create_spend_chart(categories):
  global medium
  list_nbr = list()
  names_list = list()
  list_percentage = list()
  for obj in categories:
    s = 0
    for element in obj.ledger:
      if element["amount"] < 0:
        element["amount"] = -1 * element["amount"]
        s += element["amount"]
    names_list.append(obj.budget_categories)
    list_nbr.append(round(s, 2))
  for nbr in list_nbr:
    p = (nbr / sum(list_nbr)) * 100
    # print(p)
    if p % 10 < 5:
        p = p - (p % 10)
    elif p % 10 > 5:
        p = p - ( p % 10)
    else:
        p = p
    list_percentage.append(int(p))

    # print(list_nbr)
    # print(list_percentage)
    # print(names_list)

  list_of_lists_of_signs = list()
  for i in list_percentage:
    list_of_signs = list()
    for nbr in range(i + 10, 110, 10):
      sign = " "
      list_of_signs.append(sign)

    for nbr in range(0, i + 10, 10):
      sign = "o"
      list_of_signs.append(sign)
    list_of_lists_of_signs.append(list_of_signs)
      # print(list_of_signs)
  list_of_lists_of_names = list()
  lengths = list()
  for name in names_list:
    name = list(name)
    length = len(name)
    list_of_lists_of_names.append(name)
    lengths.append(length)

  longueur = max(lengths) + 1
  for lst in list_of_lists_of_names:
    if len(lst) < longueur:
      space = [" "] * (longueur - len(lst))
      # print(space)
      lst.extend(space)
      # print(lst)

    # print(list_of_lists_of_signs)
  whole_word = str()
  whole_letters=str()
  for i in range(11):
    signs = ""

    for j in range(len(list_of_lists_of_signs)):
      signs = signs + " " + list_of_lists_of_signs[j][i] + " "
      if j == len(list_of_lists_of_signs) - 1:
        signs = signs + " "
    signs = f"{100 - i * 10}".rjust(3) + "|" + signs
    medium =" ".rjust(4)+("-" * (len(signs)-4))
    whole_word = whole_word + signs + "\n"
  # print(whole_word)

  for i in range(longueur):
    letters = ""

    for k in range(len(list_of_lists_of_signs)):
      letters = letters + " " + list_of_lists_of_names[k][i] + " "
      if k == len(list_of_lists_of_names) - 1:
        letters = letters + " "
    letters=" ".rjust(4)+letters
    whole_letters=(whole_letters+"\n"+letters).rjust(6)
  

   
  return "Percentage spent by category"+"\n"+whole_word+medium+whole_letters.rstrip()+"  "
 