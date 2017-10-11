class Underscore(object):
    def map(self, some_list, test_function):
        mapped_list = []
        for item in some_list:
            mapped_list.append(test_function(item))
        return mapped_list
    def reduce(self, some_list, test_function, initial_val=0):
        if len(some_list) == 1:
            if initial_val != 0:
                return initial_val + some_list[0]
            else:
                return some_list[0]
        elif initial_val != 0:
            reduced_val = initial_val + some_list[0]
        else:
            reduced_val = some_list[0]
        for item in some_list[1:]:
            reduced_val = test_function(reduced_val, item)
        return reduced_val
    def find(self, some_list, test_function):
        found_item = None
        for item in some_list:
            if test_function(item):
                found_item = item
                break
        return found_item
    def filter(self, some_list, test_function):
        filtered_list = []
        for item in some_list:
            if test_function(item):
                filtered_list.append(item)
        return filtered_list
    def reject(self, some_list, test_function):
        rejected_list = []
        for item in some_list:
            if not test_function(item):
                rejected_list.append(item)
        return rejected_list

if __name__ == "__main__":
    # you just created a library with 5 methods!
    # let's create an instance of our class
    _ = Underscore() # yes we are setting our instance to a variable that is an underscore
    test_list = [1, 2, 3, 4, 5, 6]
    # filter method - should return [2, 4, 6] after you finish implementing the code above
    evens = _.filter(test_list, lambda x: x % 2 == 0)
    print evens
    # reject method - expecting return [1, 3, 5]
    odds = _.reject(test_list, lambda x: x % 2 == 0)
    print odds
    # find method - expecting 2
    found = _.find(test_list, lambda x: x % 2 == 0)
    print found
    # reduce method - no initial value - expecting 6
    sum1 = _.reduce([1, 2, 3], lambda total, num: total + num)
    print sum1
    # reduce method - initial value - expecting 9
    sum2 = _.reduce([1, 2, 3], lambda total, num: total + num, 3)
    print sum2
    # reduce method - string - expecting asdf
    sum3 = _.reduce(["s", "d", "f"], lambda total, num: total + num, "a")
    print sum3
    # map method - expecting [1, 4, 9, 16, 25, 36]
    mapped = _.map(test_list, lambda x: x ** 2)
    print mapped