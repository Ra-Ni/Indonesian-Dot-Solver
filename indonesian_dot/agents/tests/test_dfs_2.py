import unittest

from agents.agent import Agent
from envs.puzzle import Puzzle


class MyTestCase(unittest.TestCase):
    def test_something(self):
        e = Puzzle("111111111")
        a = Agent.make('dfs')
        sea, sol = a.run(max_d=3, environment=e)
        print(sea)
        print()
        print(sol)


if __name__ == '__main__':
    unittest.main()
