import re
import numpy as np
from fractions import Fraction

vars = "xyz"

def read_expresion(string):
	string2 = re.sub("\s","",string)
	# Add coefficient 1 to single variables (replace "x" with "1x")
	for i in [i[-1] for i in re.findall("\D{1}[xyz]+"," " + string)]:
		string2 = re.sub(f"[{i}]","1"+i,string2)
	# List coefficients (including negatives, decimals and fractions)
	coefficients = re.findall("[-]?[0-9]+[,.]?[0-9]*[/]?[0-9]*[,.]?[0-9]*",string2)
	coefficients,constant = list(map(Fraction,coefficients[:-1])),Fraction(coefficients[-1]) # Get the constant
	# List variables
	variables = re.findall(f"[{vars}]+",string2)
	# Add remaining variables with coefficient 0
	for i,var in enumerate(list(vars)):
		if var not in variables:
			variables.insert(min(len(variables)-1,i),var)
			coefficients.insert(min(len(variables)-1,i),0)
	return coefficients,constant

def det(m):
	# Determinant of a matrix
	return round(np.linalg.det(m.astype(float)),2)

def adj(m):
	# Adjugate of a matrix (transpose of cofactor matrix)
	return np.array([
		[+det(np.array([[m[1,1],m[1,2]],[m[2,1],m[2,2]]])), -det(np.array([[m[0,1],m[0,2]],[m[2,1],m[2,2]]])), +det(np.array([[m[0,1],m[0,2]],[m[1,1],m[1,2]]]))],
		[-det(np.array([[m[1,0],m[1,2]],[m[2,0],m[2,2]]])), +det(np.array([[m[0,0],m[0,2]],[m[2,0],m[2,2]]])), -det(np.array([[m[0,0],m[0,2]],[m[1,0],m[1,2]]]))],
		[+det(np.array([[m[1,0],m[1,1]],[m[2,0],m[2,1]]])), -det(np.array([[m[0,0],m[0,1]],[m[2,0],m[2,1]]])), +det(np.array([[m[0,0],m[0,1]],[m[1,0],m[1,1]]]))]
	])

def inv(m):
	return adj(m)/det(m) # also np.linalg.inv(m)

def solve(eq1,eq2,eq3):
	variables = list(vars)
	c_M = np.empty((0,3)) # coefficient matrix
	constants = np.empty((0,1))
	for eq in (eq1,eq2,eq3):
		coefs,const = read_expresion(eq)
		c_M = np.vstack((c_M,coefs))
		constants = np.vstack((constants,const))
	a_M = np.concatenate((c_M,constants),axis=1) # augmented matrix

	if det(c_M) != 0: # Independent system
		# Cramer's rule
		Mx = np.copy(c_M)
		Mx[:,0] = constants[:,0]
		My = np.copy(c_M)
		My[:,1] = constants[:,0]
		Mz = np.copy(c_M)
		Mz[:,2] = constants[:,0]
		x = det(Mx)/det(c_M)
		y = det(My)/det(c_M)
		z = det(Mz)/det(c_M)
