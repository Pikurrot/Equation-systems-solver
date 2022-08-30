import re
import numpy as np

def read_expresion(string):
	string2 = string
	# Add coefficient 1 to single variables (replace "x" with "1x")
	for i in [i[-1] for i in re.findall("\D{1}[xyz]+"," " + string)]:
		string2 = re.sub(f"[{i}]","1"+i,string2)
	# List coefficients (including negatives, decimals and fractions)
	coefficients = re.findall("[-]?[0-9]+[,.]?[0-9]*[/]?[0-9]*[,.]?[0-9]*",string2)
	coefficients,constant = coefficients[:-1],coefficients[-1] # Get the constant
	# List variables
	variables = re.findall("[a-z]+",string2)
	return variables,coefficients,constant

def det(m):
	# Determinant of a matrix
	return round(np.linalg.det(m),2)

def adj(m):
	# Adjugate of a matrix (transpose of cofactor matrix)
	return np.array([
		[+det(np.array([[m[1,1],m[1,2]],[m[2,1],m[2,2]]])), -det(np.array([[m[0,1],m[0,2]],[m[2,1],m[2,2]]])), +det(np.array([[m[0,1],m[0,2]],[m[1,1],m[1,2]]]))],
		[-det(np.array([[m[1,0],m[1,2]],[m[2,0],m[2,2]]])), +det(np.array([[m[0,0],m[0,2]],[m[2,0],m[2,2]]])), -det(np.array([[m[0,0],m[0,2]],[m[1,0],m[1,2]]]))],
		[+det(np.array([[m[1,0],m[1,1]],[m[2,0],m[2,1]]])), -det(np.array([[m[0,0],m[0,1]],[m[2,0],m[2,1]]])), +det(np.array([[m[0,0],m[0,1]],[m[1,0],m[1,1]]]))]
	])

def inv(m):
	return adj(m)/det(m) # also np.linalg.inv(m)
