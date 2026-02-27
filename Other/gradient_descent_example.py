# Gradient Descent from scratch
# Goal: find the minimum of f(x) = x²
# The true minimum is at x = 0

# ----- The function and its gradient -----


def f(x):
    """Our function: f(x) = x²"""
    return x**2


def gradient(x):
    """The derivative of x² is 2x.
    This tells us the slope at any point x."""
    return 2 * x


# ----- Gradient Descent -----


def gradient_descent(starting_x, learning_rate, num_steps):
    x = starting_x
    history = [x]  # track where we've been

    for step in range(num_steps):
        grad = gradient(x)  # 1. compute the slope at current x
        x = x - learning_rate * grad  # 2. step in the opposite direction
        history.append(x)

        print(
            f"Step {step+1:2d}: x = {x:+.6f},  f(x) = {f(x):.6f},  gradient = {grad:+.6f}"
        )

    print(f"\nFinal answer: x = {x:.6f}  (true minimum is x = 0)")
    return x, history


# ----- Run it -----

print("=" * 60)
print("Minimising f(x) = x²  (minimum is at x = 0)")
print("=" * 60)
print(f"Starting at x = 10, learning rate = 0.1\n")

final_x, history = gradient_descent(starting_x=10, learning_rate=0.1, num_steps=20)


# ----- What happens with a bad learning rate? -----

print("\n" + "=" * 60)
print("What if the learning rate is too HIGH? (lr = 1.1)")
print("=" * 60)

x = 10
for step in range(8):
    grad = gradient(x)
    x = x - 1.1 * grad
    print(f"Step {step+1}: x = {x:+.2f},  f(x) = {f(x):.2f}")

print("\nNotice: x explodes! The learning rate is too large.")


print("\n" + "=" * 60)
print("What if the learning rate is too LOW? (lr = 0.001)")
print("=" * 60)

x = 10
for step in range(20):
    grad = gradient(x)
    x = x - 0.001 * grad
    if step < 5 or step == 19:
        print(f"Step {step+1:2d}: x = {x:.6f},  f(x) = {f(x):.6f}")
    elif step == 5:
        print("  ...")

print("\nNotice: barely moved after 20 steps. Learning rate too small.")
