from main import simplex_method

# F = x1 + x2 -> max
maximize_func = [1, 1]

max_or_min = "min"

# 4x1 + 2x2 <= 1
# 2x1 + 3x2 <= 1
limitation_left_part = [[4, 2],
                        [2, 3]]

# Правая часть уравнения
limitation_right_part = [1, 1]

# Номер икса каждой перемнной
num_of_x = [[1, 2],
            [1, 2]]

# "-1" == "<="
# "0" == "="
# "1" == ">="
limitation_symbol = [1, 1]

simplex_method(maximize_func, limitation_left_part, limitation_right_part,
                    num_of_x, limitation_symbol, max_or_min)






# F = x1 + x2 -> max
maximize_func = [1, 1]

max_or_min = "max"

# 4x1 + 2x2 <= 1
# 2x1 + 3x2 <= 1
limitation_left_part = [[4, 2],
                        [2, 3]]

# Правая часть уравнения
limitation_right_part = [1, 1]

# Номер икса каждой перемнной
num_of_x = [[1, 2],
            [1, 2]]

# "-1" == "<="
# "0" == "="
# "1" == ">="
limitation_symbol = [-1, -1]

simplex_method(maximize_func, limitation_left_part, limitation_right_part,
                    num_of_x, limitation_symbol, max_or_min)


