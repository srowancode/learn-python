def using_classes():
    """Understanding python classes."""

    # classes allow the creation of 'objects' an object can comprise
    # of any amount of member variables and member functions

    # example we define an object Soldier
    # we initialize a Solider by giving providing a name and rank
    # we can give the soldier a promotion via give_promotion() function
    # or we can give the soldier a demotion via give_demotion() function
    ## note the use of 'self' as member function arguments
    class Soldier:
        ranks = ['Private',
                 'Private First Class',
                 'Corporal',
                 'Sergeant',
                 'Staff Sergeant']

        def __init__(self, name, rank):
            self.name = name
            self.rank = rank
        
        def give_promotion(self):
            if self.rank == 'Staff Sergeant':
                print('Cannot be promoted further')
            else:
                current_rank = self.ranks.index(self.rank)
                self.rank = self.ranks[current_rank + 1]

        def give_demotion(self):
            if self.rank == 'Private':
                print('Cannot be demoted further')
            else:
                current_rank = self.ranks.index(self.rank)
                self.rank = self.ranks[current_rank - 1]

    # To use the class we must first create an 'instance' of the class
    # with a specific name
    soldier_1 = Soldier('Jane Doe', 'Corporal')
    soldier_2 = Soldier('John Doe', 'Private')

    # To access member variables and member functions, simply use the '.' operator
    print('name: ' + soldier_1.name)
    print('rank: ' + soldier_1.rank)
    print('name: ' + soldier_2.name)
    print('rank: ' + soldier_2.rank)

    # lets try promoting soldier_2 once and soldier_1 twice
    soldier_2.give_promotion()
    soldier_1.give_promotion()
    soldier_1.give_promotion()
    print('name: ' + soldier_1.name)
    print('rank: ' + soldier_1.rank)
    print('name: ' + soldier_2.name)
    print('rank: ' + soldier_2.rank)

    # lets try demoting soldier_2 twice, should only be demoted once as Private
    # is the lowest
    soldier_2.give_demotion()
    soldier_2.give_demotion()
    print('name: ' + soldier_2.name)
    print('rank: ' + soldier_2.rank)


if __name__ == '__main__':
    using_classes()