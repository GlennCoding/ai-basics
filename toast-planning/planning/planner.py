import heapq
from itertools import count
import random
from planning.planning_problem import Planning_Problem


class Planner:
    """
    Planner class with different planning method implementations
    """

    @staticmethod
    def state_key(state):
        # For BFS by number of actions, ignore "time"
        return (
            state["toaster_has_power"],
            state["toaster_is_on"],
            state["bread_location"],
            state["bread_state"],
        )

    @classmethod
    def random_search(cls, start_state):
        """
        Implementation of random search.

        returns (path, step_count) where path is a list of actions to the goal and step_count is the number of states extended
        """

        open_list = [
            (start_state, [])
        ]  # this is a list of state,path. The path of the start state is empty.
        start_state["path"] = (
            []
        )  # small hack: we add paths to the state in order to remember the path we travelled.
        step_count = 0

        while len(open_list) > 0:
            state, path = random.choice(open_list)
            step_count += 1

            for action in Planning_Problem.actions:
                next_state = Planning_Problem.state_transition(state, action)
                next_path = path + [action]

                if Planning_Problem.goal(next_state):
                    return next_path, step_count
                else:
                    open_list.append((next_state, next_path))

        return None, step_count

    @classmethod
    def breadth_first_search(cls, start_state):
        """
        Implementation of Breadth First Search

        returns (path, step_count) where path is a list of actions to the goal and step_count is the number of states extended
        """
        step_count = 0
        frontier = [(start_state, [])]
        visited_keys = {cls.state_key(start_state)}

        while len(frontier) > 0:
            state, path = frontier.pop(0)
            step_count += 1

            for action in Planning_Problem.actions:
                next_state = Planning_Problem.state_transition(state, action)
                next_path = path + [action]

                if Planning_Problem.goal(next_state):
                    return next_path, step_count

                key = cls.state_key(next_state)
                if key in visited_keys:
                    continue

                visited_keys.add(key)
                frontier.append((next_state, next_path))

        return None, step_count

    @classmethod
    def shortest_toast_time_search(cls, start_state):
        """
        Implementation of a search algorithm that also optimized for the time it takes to toast a slice of bread.
        This time is measured within the state in attribute ["time"]

        returns (path, step_count) where path is a list of actions to the goal and step_count is the number of states extended
        """
        step_count = 0
        start_key = cls.state_key(start_state)

        dist = {start_key: 0}
        prev = {start_key: (None, None)}
        counter = count()  # Counter needed because can't order dicts on tie
        minHeap = [(0, next(counter), start_state)]

        while minHeap:
            d, _, u = heapq.heappop(minHeap)
            u_key = cls.state_key(u)

            if d != dist.get(u_key, float("inf")):
                continue

            step_count += 1

            if Planning_Problem.goal(u):
                return cls.get_path_iterative(prev, u_key, start_key), step_count
                # return cls.get_path_recursion(prev, u_key, start_key, []), step_count

            for action in Planning_Problem.actions:
                v = Planning_Problem.state_transition(u, action)
                v_key = cls.state_key(v)
                edge_d = v["time"] - u["time"]

                nd = d + edge_d

                if nd < dist.get(v_key, float("inf")):
                    dist[v_key] = nd
                    prev[v_key] = (u_key, action)
                    heapq.heappush(minHeap, (nd, next(counter), v))

        return None, step_count

    @staticmethod
    def get_path_recursion(prev, u_key, start_key, path):
        if u_key == start_key:
            return path

        prev_state_key, prev_action = prev[u_key]

        updated_path = [prev_action] + path

        return Planner.get_path_recursion(prev, prev_state_key, start_key, updated_path)

    @staticmethod
    def get_path_iterative(prev, end_state_key, start_key):
        path_from_end_to_start = []
        next_u_key = end_state_key

        while next_u_key != start_key:
            prev_state_key, prev_action = prev[next_u_key]

            path_from_end_to_start.append(prev_action)
            next_u_key = prev_state_key

        path_from_end_to_start.reverse()
        return path_from_end_to_start
