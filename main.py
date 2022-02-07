variable = input()
function = input()

signs = ["+", "-", "*", "/"]


# The function check right writing the variable
def check_variable():
    if len(variable) > 1:
        return "Variable can't be longer the 1 symbol"
    elif len(variable) == 0:
        return "Variable must have name"

    if not isinstance(variable, str):
        return "Variable name must contains only letters"

    if (not (variable.isupper() and "A" <= variable <= "Z")) and (not (variable.islower() and "a" <= variable <= "z")):
        return "Variable names must contains only latin letters"

    return "OK"


# The function take derivative from function with degree
def derivative_with_degree(func):
    degree = ""
    coefficient = find_coefficient(func)
    if func.find(variable) != -1 and func[func.find(variable) + 2] == "(":
        for i in range(func.find(variable) + 3, len(func)):
            if func[i] == ")":
                break
            degree += func[i]
    elif func.find(variable) != -1 and func[func.find(variable) + 2] != "(":
        for i in range(func.find(variable) + 2, len(func)):
            if func[i] in signs:
                break
            degree += func[i]
        degree = int(degree)
    else:
        return "0"

    if isinstance(degree, int):
        if coefficient != "":
            if int(degree) - 1 != 1:
                return f"{degree * int(coefficient)}{variable}^{int(degree)-1}"
            else:
                return f"{degree * int(coefficient)}{variable}"
        else:
            if int(degree) - 1 != 1:
                return f"{degree}{variable}^{int(degree) - 1}"
            else:
                return f"{degree}{variable}"
    else:
        pass
         # Здесь должна быть мейновая функция которую будет реверсивно вызывать


# The function find coefficient in part of function
def find_coefficient(func):
    coefficient = ""
    for i in func:
        if i != variable and i not in signs:
            coefficient += i
        else:
            break
    return coefficient


# The function use another functions the work with derivative
def work_with_derivative(func):
    if "^" in func:
        return derivative_with_degree(func)
    elif func == variable:
        if find_coefficient(func) != "":
            return find_coefficient(func)
        else:
            return "1"


# The function take derivative
def derivative(func):
    part = ""
    all_parts, all_sign = [], []
    for i in func:
        if i != "+" and i != "-":
            part += i
        else:
            if variable in part:
                if i == "+":
                    all_sign.append("+")
                else:
                    all_sign.append("-")
                all_parts.append(work_with_derivative(part))

            part = ""
    if variable in part:
        all_parts.append(work_with_derivative(part))
    answer = ""
    for i in range(len(all_parts)):
        answer += all_parts[i]
        if i != len(all_parts) - 1:
            answer += all_sign[i]
    return answer


print(check_variable())
print(derivative(function))
