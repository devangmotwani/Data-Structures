# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position+1

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = input()#sys.stdin.read()

    opening_brackets_stack = []
    break_var=0
    #print(enumerate(text))
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
                # Process opening bracket, write your code here
            new_bracket=Bracket(next,i)
            opening_brackets_stack.append(new_bracket)
        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack)==0:
                print(i+1) ##position of the first unmatched closing bracket
                break_var=2
                break
            else:
                check_Match=opening_brackets_stack[-1].Match(next)
                if check_Match==True:
                    opening_brackets_stack.pop()
                else:
                    print(i+1)
                    break_var=2
                    break
         #print(i,next,end="\n")
    if break_var==0:
        if opening_brackets_stack==[]:
            print("Success")
        else:
            print(opening_brackets_stack[-1].position)
    # Printing answer, write your code here
