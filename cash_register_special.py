class CashRegister:
    def __init__(self, ones, twos, fives, tens, twenties):
        self.ones = ones
        self.twos = twos
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def get_total(self):
        return self.ones + self.twos * 2 + self.fives * 5 + \
               self.tens * 10 + self.twenties * 20

    def add(self, count, denomination):
        if denomination == 'ones':
            self.ones += count
        elif denomination == 'twos':
            self.twos += count
        elif denomination == 'fives':
            self.fives += count
        elif denomination == 'tens':
            self.tens += count
        elif denomination == 'twenties':
            self.twenties += count

    def remove(self, count, denomination):
        if denomination == 'ones':
            self.ones -= count
        elif denomination == 'twos':
            self.twos -= count
        elif denomination == 'fives':
            self.fives -= count
        elif denomination == 'tens':
            self.tens -= count
        elif denomination == 'twenties':
            self.twenties -= count

    def __str__(self):
        """ (CashRegister) -> str
        Return a string representation of this CashRegister.
        >>> reg1 = CashRegister(1, 2, 3, 4, 5)
        >>> reg1.__str__()
        'CashRegister: $160 ($1x1, $2x2, $5x3, $10x4, $20x5)'
        """

        # return 'CashRegister: $' + self.get_total() + ' ($1x' + self.ones + \
        #        ', $2x' + self.twos + ', $5x' + self.fives + ', $10x' + \
        #        self.tens + ', $20x' + self.twenties + ')'

        # return 'CashRegister: $' + str(self.get_total()) + ' ($1x' + str(self.ones) + \
        #        ', $2x' + str(self.twos) + ', $5x' + str(self.fives) + ', $10x' + \
        #        str(self.tens) + ', $20x' + str(self.twenties) + ')'
        #
        return 'CashRegister: ' + \
               '${0} ($1x{1}, $2x{2}, $5x{3}, $10x{4}, $20x{5})'.format(
                   self.get_total(), self.ones, self.twos,
                   self.fives, self.tens, self.twenties)

    def __eq__(self, other):
        """ (CashRegister, CashRegister) -> bool
        Return True iff this CashRegister has the same amount of money as other.
        >>> reg1 = CashRegister(2, 0, 0, 0, 0)
        >>> reg2 = CashRegister(0, 1, 0, 0, 0)
        >>> reg1 == reg2
        True
        """

        return self.get_total() == other.get_total()

    def __add__(self, other):
        """ (CashRegister, CashRegister) -> CashRegister
        Return new CashRegister where the amount of money
        for each denomination is the sum of the corresponding
        amounts in self and other.
        >>> reg1 = CashRegister(2, 0, 3, 0, 0)
        >>> reg2 = CashRegister(0, 1, 1, 0, 0)
        >>> str (reg1 + reg2)
        'CashRegister: $24 ($1x2, $2x1, $5x4, $10x0, $20x0)'
        """
        result = CashRegister(0, 0, 0, 0, 0)
        result.ones = self.ones + other.ones
        result.twos = self.twos + other.twos
        result.fives = self.fives + other.fives
        result.tens = self.tens + other.tens
        result.twenties = self.twenties + other.twenties

        return result

    def __repr__(self):
        """ (CashRegister) -> str
        Return an unambiguous representation
         of an object for debugging
        >>> reg1 = CashRegister(1, 2, 3, 4, 5)
        >>> reg1.__repr__()
        'CashRegister: $160 ($1x1, $2x2, $5x3, $10x4, $20x5)'
        """

        return self.__str__()


if __name__ == '__main__':
    cr1 = CashRegister(2, 0, 0, 0, 0)
    cr2 = CashRegister(0, 1, 0, 0, 0)
    cr3 = CashRegister(1, 1, 0, 0, 0)

    print(cr1)
    print(cr3)

    print(cr1 == cr2)
    print(cr3 == cr2)

    reg1 = CashRegister(2, 0, 3, 0, 0)
    reg2 = CashRegister(0, 1, 1, 0, 0)
    print(reg1 + reg2)

    cr1 = CashRegister(2, 0, 0, 0, 0)
    cr2 = CashRegister(0, 1, 0, 0, 0)
    cr3 = CashRegister(1, 1, 0, 0, 0)
    crs = []
    crs.append(cr1)
    crs.append(cr2)
    crs.append(cr3)

    print(crs)

    print(dir(cr1))