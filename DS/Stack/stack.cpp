#include <iostream>

template <typename T>
class Stack {
private:
    T* array;
    int capacity;
    int top;

public:
    // Constructor
    Stack(int size = 10) {
        capacity = size;
        array = new T[capacity];
        top = -1;
    }

    // Destructor
    ~Stack() {
        delete[] array;
    }

    // Function to check if the stack is empty
    bool isEmpty() {
        return top == -1;
    }

    // Function to check if the stack is full
    bool isFull() {
        return top == capacity - 1;
    }

    // Function to push an element onto the stack
    void push(T value) {
        if (isFull()) {
            std::cout << "Stack overflow!" << std::endl;
            return;
        }
        array[++top] = value;
    }

    // Function to pop an element from the stack
    T pop() {
        if (isEmpty()) {
            std::cout << "Stack underflow!" << std::endl;
            // Returning a default value; you might want to handle this differently in a real application
            return T();
        }
        return array[top--];
    }

    // Function to get the top element of the stack without removing it
    T peek() {
        if (isEmpty()) {
            std::cout << "Stack is empty!" << std::endl;
            // Returning a default value; you might want to handle this differently in a real application
            return T();
        }
        return array[top];
    }
};

int main() {
    // Example usage of the stack
    Stack<int> myStack(5);

    myStack.push(1);
    myStack.push(2);
    myStack.push(3);

    std::cout << "Top element: " << myStack.peek() << std::endl;

    myStack.pop();

    std::cout << "Top element after pop: " << myStack.peek() << std::endl;

    return 0;
}
