from optimization.optimization_problem import Optimization_Problem
from typing import List


class Optimization_Algorithms:
    """
    Optimization class with different optimization method implementations
    """

    @classmethod
    def exhaustive_search(cls):
        """
        calculate the best values for toast and wait duration by searching all values exhaustively.
        """
        best_utility = float("-inf")
        best_solution = None

        for toast_duration in range(1, 101):
            for wait_duration in range(1, 101):
                utility = Optimization_Problem.utility(
                    toast_duration=toast_duration, wait_duration=wait_duration
                )

                if utility > best_utility:
                    best_utility = utility
                    best_solution = (toast_duration, wait_duration)
        return best_solution, best_utility

    @classmethod
    def hill_climbing(cls):
        """
        calculate the best values for toast and wait duration by implementing Hill Climbing
        """
        best_utility = float("-inf")
        best_solution = (50, 50)

        isRunning = True

        while isRunning:
            best_neighbour_utility = float("-inf")
            best_neighbour_solution = None

            # get neighbours

            neighbours = [
                (best_solution[0] + 1, best_solution[1]),
                (best_solution[0] - 1, best_solution[1]),
                (best_solution[0], best_solution[1] + 1),
                (best_solution[0], best_solution[1] - 1),
            ]

            # check if neighbours are in range

            for n in neighbours:
                if n[0] <= 0 or n[0] >= 101 or n[1] <= 0 or n[1] >= 101:
                    continue

                utility = Optimization_Problem.utility(
                    toast_duration=n[0], wait_duration=n[1]
                )

                if utility > best_neighbour_utility:
                    best_neighbour_utility = utility
                    best_neighbour_solution = n

            if best_neighbour_utility > best_utility:
                best_utility = best_neighbour_utility
                best_solution = best_neighbour_solution
            else:
                isRunning = False

        return best_solution, best_utility

    @classmethod
    def gradient_ascent(cls):
        best_utility = float("-inf")
        best_solution = [50, 50, 1.0]
        num_iterations = 600
        learning_rate = 0.1

        params = list(best_solution)

        for _ in range(num_iterations):
            slope_toast_duration = cls.numerical_gradient(params, 0, [0, 100], 1)
            slope_wait_duration = cls.numerical_gradient(params, 1, [0, 100], 1)
            slope_power = cls.numerical_gradient(params, 2, [0, 2], 0.01)

            params[0] = max(
                1, min(100, params[0] + learning_rate * slope_toast_duration)
            )
            params[1] = max(
                1, min(100, params[1] + learning_rate * slope_wait_duration)
            )
            params[2] = max(
                0.0001, min(1.9999, params[2] + learning_rate * slope_power)
            )

            utility = Optimization_Problem.utility(
                toast_duration=round(params[0]),
                wait_duration=round(params[1]),
                power=params[2],
            )
            if utility > best_utility:
                best_utility = utility
                best_solution = [round(params[0]), round(params[1]), params[2]]

        return best_solution, best_utility

    @classmethod
    def numerical_gradient(cls, params, pos, paramRange: List[int], h=1e-7):
        params_with_step_back = params.copy()
        params_with_step_front = params.copy()

        params_with_step_back[pos] = params_with_step_back[pos] - h
        params_with_step_front[pos] = params_with_step_front[pos] + h

        if params_with_step_back[pos] < paramRange[0]:
            return 0
        if params_with_step_front[pos] > paramRange[1]:
            return 0

        utility_with_step_back = Optimization_Problem.utility(
            toast_duration=round(params_with_step_back[0]),
            wait_duration=round(params_with_step_back[1]),
            power=params_with_step_back[2],
        )

        utility_with_step_front = Optimization_Problem.utility(
            toast_duration=round(params_with_step_front[0]),
            wait_duration=round(params_with_step_front[1]),
            power=params_with_step_front[2],
        )

        slope = (utility_with_step_front - utility_with_step_back) / (2 * h)

        return slope
