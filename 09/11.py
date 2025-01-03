from copy import deepcopy
class Selfie:
    instances = []

    def __init__(self):
        self.n_states_value = 0

    def save_state(self):
        self.instances.append(deepcopy(self))
        self.n_states_value +=1

    def recover_state(self, num=-1):
        if 0 <= num < len(self.instances):
            return deepcopy(self.instances[num])
        else:
            return deepcopy(self)

    def n_states(self):
        return self.n_states_value