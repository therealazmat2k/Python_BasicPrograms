class Stack:

    def __init__(self, max_size, *args):
        self.values = []
        self.max_size = max_size
        if max_size < len(args):
            raise ValueError("Error: received more values than size of the stack")
        else:
            for i in range(len(args)):
                self.values.append(args[i])

    # PUSH, POP and IS_EMPTY are required functions for stack

    def push(self, value):
        if len(self.values) == self.size:
            raise ValueError("Overflow: cannot push more values to stack")
        else:
            self.values.append(value)

    def pop(self):
        if len(self.values) == 0:
            raise ValueError("Underflow: cannot pop from an empty stack")
        else:
            return self.values.pop()

    def is_emtpy(self):
        return len(self.values) == 0

    # Following are complementary functions

    def print_values(self):
        for i in range(1, len(self.values) + 1):
            print(self.values[-i])

    def length(self):  # Returns current size of the stack
        return len(self.values)

    def size(self):  # Returns maximum size of the stack
        return self.max_size


stack = Stack(35, 1, 2, 3, 4, 5)                                      # Creates an instance of Stack class
print(f"The length of the stack is = {stack.length()}")               # Prints current length of the stack
print(f"The max size of the stack is = {stack.size()}")               # Prints limit of the stack
print(f"The stack is {'empty' if stack.is_emtpy() else 'not empty'}") # Prints if the stack is currently empty or not
stack.push(33)                                                        # Pushes value 33 on top of the stack
print("Stack values - ")
stack.print_values()                                                  # Prints all the values in the stack
print(f"popped element = {stack.pop()}")                              # Pops top of the stack
