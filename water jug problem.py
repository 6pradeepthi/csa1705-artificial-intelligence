def water_jug_problem(x, y, target):
    jug_x = 0  
    jug_y = 0

    while jug_x != target and jug_y != target:
        if jug_x == 0:  
            jug_x = x
        elif jug_y == y:  
            jug_y = 0
        else:
        
            pour_amount = min(jug_x, y - jug_y)
            jug_x -= pour_amount
            jug_y += pour_amount

    
    return jug_x, jug_y

x_capacity = 5
y_capacity = 3
target_amount = 4

result = water_jug_problem(x_capacity, y_capacity, target_amount)
print(f"The final amount in Jug X is {result[0]} and in Jug Y is {result[1]}")
