def f(params):
    """Production cost — treat params as a black box."""
    x, y, z = params
    return (x - 20) ** 2 + (y - 5) ** 2 + (z - 50) ** 2


def numerical_gradient(f, params, h=1e-7):
    """Estimate gradient for EACH parameter independently."""
    gradients = []
    for i in range(len(params)):
        # TODO:
        # 1. Make a copy of params, nudge params[i] UP by h → compute f
        # 2. Make a copy of params, nudge params[i] DOWN by h → compute f
        # 3. slope = (f_up - f_down) / (2 * h)
        # 4. Append slope to gradients
        params_with_step_back = params.copy()
        params_with_step_front = params.copy()

        params_with_step_back[i] = params_with_step_back[i] - h
        params_with_step_front[i] = params_with_step_front[i] + h

        slope = (f(params_with_step_front) - f(params_with_step_back)) / (2 * h)
        gradients.append(slope)

    return gradients


def gradient_descent(f, starting_params, learning_rate, num_iterations):
    params = list(starting_params)

    for _ in range(num_iterations):
        # 1. Compute gradients using numerical_gradient
        gradients = numerical_gradient(f, params)

        # 2. Update EACH param: param = param - learning_rate * gradient
        for i in range(len(params)):
            params[i] = params[i] - learning_rate * gradients[i]

    return params


# Start far from the answer
start = [0.0, 0.0, 0.0]
result = gradient_descent(f, start, learning_rate=0.1, num_iterations=100)

print(f"Temperature: {result[0]:.2f}  (target: 20)")
print(f"Pressure:    {result[1]:.2f}  (target: 5)")
print(f"Speed:       {result[2]:.2f}  (target: 50)")
