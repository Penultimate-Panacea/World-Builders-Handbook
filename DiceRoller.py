import random


class DiceRoller:
    """
    A class used to roll dice for use in the digital

    ...

    Attributes
    ----------
    unique_seed : str
        a string used to ensure that each die is reproducible.
        It is recommended to use the name of the world being generated.

    Methods
    -------
    roll_1d6()
        Rolls a d6 and returns the result

    roll_1d3()
        Rolls a d3 by the method determined in the MegaTraveller Rules and returns the result

    roll_2d6()
        Rolls 2d6 and returns the result

    roll_nd6(n)
        Rolls a d6 n times and adds the results together

    roll_d66()
        Rolls a d66 and returns the result as a list with two items


    """
    def __init__(self, unique_seed):
        random.seed(unique_seed, 2)

    def roll_1d6(self):
        roll = random.randint(1, 6)
        return roll

    def roll_1d3(self):
        roll = random.randint(1, 6) % 3
        return roll

    def roll_2d6(self):
        result1 = self.roll_1d6()
        result2 = self.roll_1d6()
        roll = result1 + result2
        return roll

    def roll_nd6(self, n):
        i = 0
        roll = 0
        while n > i:
            roll += self.roll_1d6()
            i += 1
        return roll

    def roll_d66(self):
        result1 = self.roll_1d6()
        result2 = self.roll_1d6()
        roll = [result1, result2]
        return roll

