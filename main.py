import sympy as sp
import fileinput


class RPNCore():

    def __init__(self) -> None:
        self.stack = []
        self.operation_map = {
            "+\n": self.handle_binary_operator,
            "-\n": self.handle_binary_operator,
            "*\n": self.handle_binary_operator,
            "/\n": self.handle_binary_operator,
            "<suppr>\n": self.handle_unary_operator,
            "²\n": self.handle_unary_operator,
            "sqrt\n": self.handle_unary_operator
        }

    def debug_print(self):
        print(f"STACK : {self.stack}\n{[type(k) for k in self.stack]}")
    
    def handle_binary_operator(self,op:str):
        try:
            sp1 = self.stack.pop()
            sp2 = self.stack.pop()
            if op[:-1] == "+":
                self.stack.append(sp1 + sp2)
            elif op[:-1] == "-":
                self.stack.append(sp1 - sp2)
            elif op[:-1] == "*":
                self.stack.append(sp1 * sp2)
            elif op[:-1] == "/":
                self.stack.append(sp1 / sp2)
        except IndexError:
            pass


    def handle_unary_operator(self,op:str):
        """Expects op without \n"""
        try:
            e = self.stack.pop()
            print(f"TYPE E : {type(e)} ")
            if op == "<suppr>":
                pass
            elif op == "²":
                self.stack.append(e * e)
            elif op == "sqrt":
                self.stack.append(sp.sqrt(e))
        except IndexError:
            pass


    def digest_line(self,line:str):
        """
        - parse
            match parse
            "a number of some sort" -> in the stack
            "a sympy function" -> how many parameters ? can we apply it to the top of the stack ?
            "a special code like <suppr>" -> custom handler
        """
        try:
            spnumber = sp.parse_expr(line)
            self.stack.append(spnumber)
        except SyntaxError:
            self.operation_map[line](line[:-1])


core = RPNCore()

while True:
    for line in fileinput.input():
        core.digest_line(line)
        core.debug_print()
