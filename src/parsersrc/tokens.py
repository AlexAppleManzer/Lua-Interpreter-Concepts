from enum import Enum


class Tokens(Enum):
    id = 0
    literal_integer = 1
    assignment_operator = 2
    le_operator = 3
    lt_operator = 4
    ge_operator = 5
    gt_operator = 6
    eq_operator = 7
    ne_operator = 8
    add_operator = 9
    sub_operator = 10
    mul_operator = 11
    div_operator = 12
    left_paren = 13
    right_paren = 14
    function_keyword = 15
    print_keyword = 16
    end_keyword = 17
    while_keyword = 18
    do_keyword = 19
    repeat_keyword = 20
    until_keyword = 21
    if_keyword = 22
    then_keyword = 23
    else_keyword = 24
    unknown = 25

