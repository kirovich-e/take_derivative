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


def derivative_with_degree(func, var):
    degree = ""
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
        return f"{degree}{var}^{int(degree)-1}"
    else:
        pass
         # Здесь должна быть мейновая функция которую будет реверсивно вызывать


print(derivative_with_degree(function, variable))
