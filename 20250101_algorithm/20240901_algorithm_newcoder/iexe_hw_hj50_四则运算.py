# 分割原始字符串，提取数字与字符部分
def split_expr(expr: str):
    temp_num = ""
    res = []
    for index, chr in enumerate(expr):
        if chr in "0123456789":
            temp_num += chr
        elif chr == "-" and not (
                0 <= index - 1 < len(expr) and expr[index - 1] in "0123456789)]}"
        ):
            temp_num = "-" + temp_num
        else:
            if temp_num:
                res.append(int(temp_num))
                temp_num = ""
            res.append(chr)
    if temp_num:
        res.append(int(temp_num))
        temp_num = ""
    return res


# 将中缀表达式转为后缀表达式
def trans_infix_sufix(infix_expr: list):
    brace_dict = {"}": "{", "]": "[", ")": "("}
    priority_dict = {"+": 1, "-": 1, "*": 2, "/": 2}
    sufix_stack = []
    sufix_expr = []
    for elem in infix_expr:
        if str(elem) in "+-*/":
            while (
                    sufix_stack
                    and sufix_stack[-1] in priority_dict.keys()
                    and priority_dict[sufix_stack[-1]] >= priority_dict[elem]
            ):
                sufix_expr.append(sufix_stack.pop())
            sufix_stack.append(elem)
        elif str(elem) in "([{":
            sufix_stack.append(elem)
        elif str(elem) in ")]}":
            while sufix_stack and sufix_stack[-1] != brace_dict[elem]:
                sufix_expr.append(sufix_stack.pop())
            sufix_stack.pop()
        else:
            sufix_expr.append(elem)
    while sufix_stack:
        sufix_expr.append(sufix_stack.pop())
    return sufix_expr


# 计算后缀表达式的值
def compute_sufix(sufix_expr: list):
    compute_stack = []
    for elem in sufix_expr:
        if str(elem) in "+-*/":
            second_oper_num = compute_stack.pop() if compute_stack else 0
            first_oper_num = compute_stack.pop() if compute_stack else 0
            if elem == "+":
                compute_stack.append(first_oper_num + second_oper_num)
            elif elem == "-":
                compute_stack.append(first_oper_num - second_oper_num)
            elif elem == "*":
                compute_stack.append(first_oper_num * second_oper_num)
            else:
                compute_stack.append(first_oper_num // second_oper_num)
        else:
            compute_stack.append(elem)
    return compute_stack[0]


print(compute_sufix(trans_infix_sufix(split_expr(input()))))
