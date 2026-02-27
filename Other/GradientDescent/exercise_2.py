def f(params):
    """Production cost — treat params as a black box."""
    x, y, z = params
    return (x - 20) ** 2 + (y - 5) ** 2 + (z - 50) ** 2


def numerical_gradient(f, params, h=1e-7):
    """Estimate gradient for EACH parameter independently."""
    gradients = []
    for i in range(len(params)):

        pass
    return gradients


def gradient_descent(f, starting_params, learning_rate, num_iterations):
    params = list(starting_params)

    for i in range(num_iterations):
        # TODO:
        # 1. Compute gradients using numerical_gradient
        # 2. Update EACH param: param = param - learning_rate * gradient
        pass

    return params


# Start far from the answer
start = [0.0, 0.0, 0.0]
result = gradient_descent(f, start, learning_rate=0.1, num_iterations=100)

print(f"Temperature: {result[0]:.2f}  (target: 20)")
print(f"Pressure:    {result[1]:.2f}  (target: 5)")
print(f"Speed:       {result[2]:.2f}  (target: 50)")
