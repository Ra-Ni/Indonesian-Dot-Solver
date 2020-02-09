"""

agent dictionary function outlines the required variables for an agent to run.

"""


def agent_dict(**kwargs):
    key = {'size': None, 'max_depth': None, 'max_length': None, 'start': None}
    key.update(kwargs)
    return key