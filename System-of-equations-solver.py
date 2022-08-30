import re

def read_expresion(string):
    string2 = string
    # Add coefficient 1 to single variables (replace "x" with "1x")
    for i in [i[-1] for i in re.findall("\D{1}[xyz]+"," " + string)]:
        string2 = re.sub(f"[{i}]","1"+i,string2)
    print(string2)

    coefficients = re.findall("[-]?[0-9]+[,.]?[0-9]*[/]?[0-9]*[,.]?[0-9]*",string2)
    coefficients,constant = coefficients[:-1],coefficients[-1]
    variables = re.findall("[a-z]+",string2)
    return variables,coefficients,constant
