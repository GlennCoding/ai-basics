def f(params):
    """Production cost — treat params as a black box."""
    x, y, z = params
    return (x - 20) ** 2 + (y - 5) ** 2 + (z - 50) ** 2


def numerical_gradient(f, params, h=1e-7):
    """Estimate gradient for EACH parameter independently."""
    gradients = []

    # f([x,y,z])
    # Get the slope individually
    # Change one value, keep the other two

    for i in range(len(params)):
        # TODO:
        params_with_step_back = params.copy()  # creates a new list
        params_with_step_front = params.copy()  # creates a new list

        params_with_step_back[i] -= h
        params_with_step_front[i] += h

        print(params_with_step_back, params_with_step_front)

        slope = (f(params_with_step_front) - f(params_with_step_back)) / (2 * h)
        gradients.append(slope)
    return gradients


def gradient_descent(f, starting_params, learning_rate, num_iterations):
    params = list(starting_params)

    for i in range(num_iterations):
        # TODO:
        x = params[i]
        grad = numerical_gradient(f, params, learning_rate)
        # for each param, go down the slope
        for g in grad:
            x = x - learning_rate * g

    return params


# Start far from the answer
start = [0.1, 0.2, 0.3]
result = gradient_descent(f, start, learning_rate=0.1, num_iterations=100)

print(f"Temperature: {result[0]:.2f}  (target: 20)")
print(f"Pressure:    {result[1]:.2f}  (target: 5)")
print(f"Speed:       {result[2]:.2f}  (target: 50)")
