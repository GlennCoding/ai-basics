from optimization.optimization_problem import Optimization_Problem


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

            if n[0] <= 0 or n[0] >= 101 or n[1] <= 0 or n[1] >= 101:
                isRunning = False

        return best_solution, best_utility

    @classmethod
    def gradient_ascent(cls):
        """
        Calculate the best values for toast_duration, wait_duration and power.
        This will require a mixture of hill climbing and Gradient Ascent
        """
        # TODO: implement me
        start = [0.0, 0.0, 0.0]

        return None, float("-inf")
