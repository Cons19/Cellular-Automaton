class CA:
    """Elementary Cellular Automaton - by cons0343 Constantin Razvan Tarau

    Represents a range 1, 3-cell neighbourhood elementary cellular automaton."""
    # the constructor where I initialize the given rule and the initial state and also other different variables


    def __init__(self, rule, init_state='0' * 20 + '1' + '0' * 20):
        """Initialize the CA with the given rule and initial state."""
        self.rule = rule  # the rule that covers 256 possibilities
        self.init_state = init_state  # the initial state which is the first state
        self.number = f'{rule:08b}'  # the number variable converts the rule into binary
        self.dict = {  # dictionary used to make the rule of cellular automata and used to make the states
            "111": self.number[0],
            "110": self.number[1],
            "101": self.number[2],
            "100": self.number[3],
            "011": self.number[4],
            "010": self.number[5],
            "001": self.number[6],
            "000": self.number[7]
        }
        self.current_state = self.init_state
        self.next_state = ""

        # returns the current state


    def state(self):
        """Returns the current state."""
        return self.current_state

        # progress to the next state


    def next(self):
        """Progress one step and then return the current state."""
        three_elem = ""  # take three elements at a time and is used to take the value as a key from the dictionary
        # adding two virtual zeroes one at beginning and one at the end of the current state,
        # in order to be able to calculate the first and the last element
        self.current_state = '0' + self.current_state + '0'
        # the first for start from 1 because it skips the first virtual zero and until 42 ,
        # it doesn't go through the last two elements but the skipped elements will be covered
        # by the second for
        for i in range(1, len(self.current_state) - 1):
            # the second for goes through three elements at a time,
            # covering all the elements including the virtual zeroes
            for j in range(i - 1, i + 2):
                three_elem += self.current_state[j]  # the variable takes the value of three elements at a time
            # the next state gets the value from the key in the dictionary
            self.next_state += self.dict[three_elem]
            three_elem = ""

        # prints the next state, replacing the zeroes with a space and the ones with a star

        self.current_state = self.next_state  # the current state gets the value of the next state in order to progress
        self.next_state = ""
        # prints the states and the number of rows is given by the num parameter
        return self.current_state

    def run(self, num=18):
        """Progress and print num states.
        0s are replaced by spaces, and 1s are replaced by * for pretty printing."""
        # prints the current state, replacing the zeroes with a space and the ones with a star
        print(self.state().replace('0', ' ').replace('1', '*'))
        # while loop going until the num becomes 0
        while num != 0:
            print(self.next().replace('0', ' ').replace('1', '*'))
            num -= 1  # decreasing num variable after each iteration

