input1 = "abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb"
input2 = ""
input3 = "abcdefghijklmnopqrstuvwxyz\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb"
input4 = "abcdefghijklmnopqrstuvwxyz\na\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz"
input5 = "\n\n"
input6 = "abcdefghijklmnopqrstuvwxyz\na\nb\nc\nd\ne\nf\ng\nh\ni\nj\nk\nl\nm\nn\no\np\nq\nr\ns\nt\nu\nv\nw\nx\ny\nz\n\na"
input7 = "abc\n\na\nb\nc\n\nab\nac\n\na\na\na\na\n\nb\n\n"
input8 = "\n\n\n\n"





def count_answers_per_group(input_str: str) -> int:
    """return the sum of counts to which any person answered yes to a question across groups"""
    groups = input_str.split('\n\n')
    count = 0
    for index, g in enumerate(groups):
        group_unique_answers = set()
        for individual_answers in g.split('\n'):
            group_unique_answers = group_unique_answers | set(individual_answers)
        count += len(group_unique_answers)
    return count


def count_answers_per_group2(input_str: str) -> int:
    """return the sum of counts to which any person answered yes to a question across groups"""
    total = 0
    newline_counter = 0
    current_groups_answers = set()
    for i in range(len(input_str)):
        char = input_str[i]
        if char != '\n':
            newline_counter = 0
            current_groups_answers.add(char)
        else:
            newline_counter += 1
            if newline_counter == 2:
                total += len(current_groups_answers)
                current_groups_answers = set()
                newline_counter = 0
    total += len(current_groups_answers)
    return total

assert count_answers_per_group(input_str=input1) == 11
assert count_answers_per_group(input_str=input2) == 0
assert count_answers_per_group(input_str=input3) == 34
assert count_answers_per_group(input_str=input4) == 26
assert count_answers_per_group(input_str=input5) == 0
assert count_answers_per_group(input_str=input6) == 27
assert count_answers_per_group(input_str=input7) == 11
assert count_answers_per_group(input_str=input8) == 0

assert count_answers_per_group2(input_str=input1) == 11
assert count_answers_per_group2(input_str=input2) == 0
assert count_answers_per_group2(input_str=input3) == 34
assert count_answers_per_group2(input_str=input4) == 26
assert count_answers_per_group2(input_str=input5) == 0
assert count_answers_per_group2(input_str=input6) == 27
assert count_answers_per_group2(input_str=input7) == 11
assert count_answers_per_group2(input_str=input8) == 0