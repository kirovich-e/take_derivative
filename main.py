variable = input()
function = input()

signs = ["+", "-", "*", "/"]


# The function check right writing the variable
def check_variable(var):
    if len(var) > 1:
        return "Variable can't be longer the 1 symbol"
    elif len(var) == 0:
        return "Variable must have name"

    if not isinstance(var, str):
        return "Variable name must contains only letters"

    if (not (var.isupper() and "A" <= var <= "Z")) and (not (var.islower() and "a" <= var <= "z")):
        return "Variable names must contains only latin letters"

    return "OK"


# The function take derivative from function with degree
def derivative_with_degree(func, var):
    degree = ""
    coefficient = give_coefficient(func, var)
    if func.find(var) != -1 and func[func.find(var) + 2] == "(":
        for i in range(func.find(var) + 3, len(func)):
            if func[i] == ")":
                break
            degree += func[i]
    elif func.find(var) != -1 and func[func.find(var) + 2] != "(":
        for i in range(func.find(var) + 2, len(func)):
            if func[i] in signs:
                break
            degree += func[i]
        degree = int(degree)
    else:
        return "0"

    if isinstance(degree, int):
        if coefficient != "":
            return f"{degree * int(coefficient)}{var}^{int(degree)-1}"
        else:
            return f"{degree}{var}^{int(degree) - 1}"
    else:
        pass
         # Здесь должна быть мейновая функция которую будет реверсивно вызывать


def give_coefficient(func, var):
    coefficient = ""
    for i in func:
        if i != var and i not in signs:
            coefficient += i
        else:
            break
    return coefficient


def main_derivative(func, var):
    part = ""
    all_parts, all_sign = [], []
    for i in func:
        if i != "+" and i != "-":
            part += i
        else:
            if i == "+":
                all_sign.append("+")
            else:
                all_sign.append("-")
            if "^" in part:
                all_parts.append(derivative_with_degree(part, var))
            part = ""
    all_parts.append(derivative_with_degree(part, var))
    answer = ""
    for i in range(len(all_parts)):
        answer += all_parts[i]
        if i != len(all_parts) - 1:
            answer += all_sign[i]
    return answer


print(main_derivative(function, variable))
