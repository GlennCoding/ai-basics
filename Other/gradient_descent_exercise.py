def f(x):
    """The function we want to minimize."""
    return (x - 3) ** 2 + 5


def df(x):
    """The derivative (gradient) of f."""
    return 2 * (x - 3)


def gradient_descent(starting_x, learning_rate, num_iterations):
    x = starting_x
    history = [x]

    for i in range(num_iterations):
        # TODO:
        # 1. Compute the gradient at the current x
        # 2. Update x using the gradient descent rule
        # 3. Append the new x to history
        pass

    return x, history


# Run it!
final_x, history = gradient_descent(
    starting_x=10.0, learning_rate=0.1, num_iterations=50
)
print(f"Minimum found at x = {final_x:.6f}")
print(f"f(x) = {f(final_x):.6f}")
