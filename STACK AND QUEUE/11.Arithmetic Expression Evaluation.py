"""
Arithmetic Expression Evaluation

The stack organization is very effective in evaluating arithmetic expressions. Expressions are usually represented in what is known as Infix notation, in which each operator is written between two operands (i.e., A + B). With this notation, we must distinguish between ( A + B )*C and A + ( B * C ) by using either parentheses or some operator-precedence convention. Thus, the order of operators and operands in an arithmetic expression does not uniquely determine the order in which the operations are to be performed. 

 

1. Polish notation (prefix notation) – 
It refers to the notation in which the operator is placed before its two operands. Here no parentheses are required, i.e., 
 

+AB 
 

2. Reverse Polish notation(postfix notation) – 
It refers to the analogous notation in which the operator is placed after its two operands. Again, no parentheses is required in Reverse Polish notation, i.e., 
 




AB+ 
Stack-organized computers are better suited for post-fix notation than the traditional infix notation. Thus, the infix notation must be converted to the postfix notation. The conversion from infix notation to postfix notation must take into consideration the operational hierarchy. 

There are 3 levels of precedence for 5 binary operators as given below: 
 

Highest: Exponentiation (^)
Next highest: Multiplication (*) and division (/)
Lowest: Addition (+) and Subtraction (-) 
For example – 
 

Infix notation: (A-B)*[C/(D+E)+F]
Post-fix notation: AB- CDE +/F +* 
"""

# Infix notation: (2+4) * (4+6)
# Post-fix notation: 2 4 + 4 6 + *
# Result: 60 


