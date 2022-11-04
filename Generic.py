# Generic.py
# Show the concept of generic programming using Python

# module to help with generic programming
from typing import TypeVar, Generic, List

# Create a generic type
T = TypeVar('T')
# Generic type accepting int and float only
U = TypeVar('U', int, float)


# Define a generic stack class
class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items


# Another generic stack class, this time for numbers only
class NumStack(Generic[U]):
    def __init__(self) -> None:
        # Create an empty list with items of type U
        self.items: List[U] = []

    def push(self, item: U) -> None:
        self.items.append(item)

    def pop(self) -> U:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items


# Main function
def main():
    # Create a Stack
    stack = Stack[int]()
    # Push 5 items to the stack
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    # This will raise an error in the IDE, but not at runtime, since it's only hinted at
    stack.push("Hello")
    print(stack.items)

    # Another method, create a NumStack
    num_stack = NumStack()
    # Push 5 items to the stack
    num_stack.push(6)
    num_stack.push(7)
    num_stack.push(8.5)
    num_stack.push(9)
    num_stack.push(10)

    # This will raise an error in the IDE, but not at runtime, since it's only hinted at
    num_stack.push("World")
    print(num_stack.items)


# Call the main function
main()
