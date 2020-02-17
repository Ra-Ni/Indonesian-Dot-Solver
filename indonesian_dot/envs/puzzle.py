from envs import Env


class Puzzle(Env):

    def __init__(self, actions, state, space):
        self._space = space
        super().__init__(actions, state)

    def solved(self):
        return int(self._state, 2) == 0

    def sample(self):
        return self.state, self.actions

    def step(self, action):
        new_state = self._actions[action]
        i_st = int(new_state, 2)
        form = f'0{len(new_state)}b'

        act = [(k, f"{i_st ^ self._space[k]:{form}}")
               for k in self._actions.keys()]

        act.sort(key=lambda x: x[1])
        act = dict(act)
        del act[action]
        return Puzzle(act, new_state, self._space), i_st == 0

    def copy(self):
        return Puzzle(self._actions.copy(), self._state, self._space)
