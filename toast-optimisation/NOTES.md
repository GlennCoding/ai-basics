# Approach to gradient_ascent

- 3 variables -> one utility to maximise

- Look up slope of each isolated variable (checking front and back step) -> `((f(params_with_step_front) - f(params_with_step_back)) / (2 * h))`
  - Check if you're in range -> if not, return 0
  - Walk up that slope for each value -> `(params[i] = params[i] - learning_rate * gradients[i])`
  - Get utility for all three updated params & update best utility