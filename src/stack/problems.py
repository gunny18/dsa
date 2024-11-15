from main import Stack


def infixToPostfix():
    precedenceMapping = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
    s = Stack()
    expr = input("Enter infix expression:\t")
    postfix = ""
    for char in expr:
        if char in precedenceMapping:
            if s.isEmpty():
                s.push(char)
            else:
                while True:
                    if s.isEmpty():
                        s.push(char)
                        break
                    topOpr = s.getTop()
                    if precedenceMapping[char] > precedenceMapping[topOpr]:
                        s.push(char)
                        break
                    else:
                        topVal = s.pop()
                        postfix += topVal
        else:
            postfix += char

    while not s.isEmpty():
        val = s.pop()
        postfix += val
    print(f"Infix: {expr}\nPostfix: {postfix}\n")


def evaluatePostfix(postfix: str):
    s = Stack()
    for char in postfix:
        if char.isdigit():
            s.push(char)
        else:
            rgt = s.pop()
            lft = s.pop()
            res = eval(f"{lft} {char} {rgt}")
            s.push(res)
    result = s.pop()
    print(f"{postfix} ==> {result}")


def infixToPostfixComplex():
    precedenceMapping = {
        "+": {"out": 1, "in": 2},
        "-": {"out": 1, "in": 2},
        "*": {"out": 3, "in": 4},
        "/": {"out": 3, "in": 4},
        "^": {"out": 6, "in": 5},
        "(": {"out": 7, "in": 0},
        ")": {"out": 0, "in": None},
    }
    s = Stack()
    expr = input("Enter infix expression:\t")
    postfix = ""
    for char in expr:
        if char in precedenceMapping:
            if s.isEmpty():
                s.push(char)
            else:
                while True:
                    if s.isEmpty():
                        s.push(char)
                        break
                    topOpr = s.getTop()
                    if (
                        precedenceMapping[char]["out"]
                        == precedenceMapping[topOpr]["in"]
                    ):
                        # only occurs for ) -> out and ( -> in case!!!, just remove from stack and move on!
                        s.pop()
                        break
                    elif (
                        precedenceMapping[char]["out"] > precedenceMapping[topOpr]["in"]
                    ):
                        s.push(char)
                        break

                    else:
                        topVal = s.pop()
                        postfix += topVal
        else:
            postfix += char

    while not s.isEmpty():
        val = s.pop()
        postfix += val
    print(f"Infix: {expr}\nPostfix: {postfix}\n")
    return postfix


def parenthesisMatching():
    """
    Purely checks parenthesis matching, and not expression matching!!!
    """
    s = Stack()
    expr = input("Enter parenthesis expression")
    for char in expr:
        if char == "(":
            s.push(char)
        elif char == ")":
            if s.isEmpty():
                print(f"Parenthesis is not balanced in {expr}")
                return
            else:
                s.pop()
    if s.isEmpty():
        print(f"Parenthesis is balanced in {expr}")
    else:
        print(f"Parenthesis is not balanced in {expr}")


if __name__ == "__main__":
    # parenthesisMatching()
    ps = infixToPostfixComplex()
    evaluatePostfix(ps)
