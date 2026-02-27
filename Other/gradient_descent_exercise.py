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
        # Take x and see if I should go left or right using the derivative -> by using df(x) rule
        gradient = df(x)
        # Calculate new value for x, by doing x +/- learning rate
        x = x - learning_rate * gradient
        # Append the new x to history
        history.append(x)

    return x, history


# Run it!
final_x, history = gradient_descent(
    starting_x=10.0, learning_rate=0.1, num_iterations=50
)
print(f"Minimum found at x = {final_x:.6f}")
print(f"f(x) = {f(final_x):.6f}")
