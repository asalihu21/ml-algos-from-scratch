#Creating the functions to calculate loss and gradient for both m and c values
def gradientM(m,c,data_x, data_y):
    n = len(data_x)
    for i in range(n):
        loss = (data_x[i] * ((m*data_x[i] + c) - data_y[i]))
    gradient_m = (-2/n) * loss
    return gradient_m
    
def gradientC(m,c,data_x, data_y):
    n = len(data_x)
    for i in range(n):
        loss = (((m*data_x[i] + c) - data_y[i]))
    gradient_c = (-2/n) * loss
    return gradient_c


#Step function, this updates the m and c values based on the gradients, learning rate and current m or c values.
def step(starting_m, starting_c,data_x, data_y, learning_rate, iterations):
    
    current_m = starting_m
    current_c = starting_c
    
    for t in range(iterations):
        m_gradient = gradientM(current_m, current_c, data_x,data_y)
        current_m = current_m - (learning_rate * m_gradient)
        c_gradient = gradientC(current_m, current_c, data_x,data_y)
        current_c = current_c - (learning_rate * c_gradient)

    return [current_m, current_c]