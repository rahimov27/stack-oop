# import null as null
#
#
# class myStack():
#     # initial variables
#     t = 0
#     arr = []
#
#     def __init__(self, maxSize):
#         self.maxSize = maxSize
#
#     # Push
#     def push(self, value):
#         if self.t == self.maxSize:
#             print("Stack over flow")
#         else:
#             self.arr.append(value)
#             self.t += 1
#
#     # isEmpty function
#     def isEmpty(self):
#         if self.t == 0:
#             return True
#         else:
#             return False
#
#     # Top Function
#     def top(self):
#         if self.t != 0:
#             return self.arr[self.t-1]
#         else:
#             return null
#
#     # pop function
#     def pop(self):
#         if self.t != 0:
#             temp = self.arr[self.t-1]
#             self.t -= 1
#             return temp
#         else:
#             return null
#
#     # Print the stack
#     def printStack(self):
#         if self.t == 0:
#             print("[]")
#         else:
#             print("[", end=" ")
#             for i in range(0, self.t):
#                 print(self.arr[i], end=" ")
#             print("]", end=" ")
#
#
# # Initialize mt stack
# mStack = myStack(10)
#
# # Push reveals
# mStack.push(20)
# mStack.push(40)
# mStack.push(110)
# mStack.push(21)
# mStack.push(45)
# mStack.push(1100)
# mStack.push(230)
# mStack.push(27)
# mStack.push(543)
# mStack.push(340)
#
#
#
# # Print the stack
# mStack.printStack()
#
# mStack.push(2708)
# mStack.printStack()

# # Checking is the Stack is empty
# print(mStack.isEmpty())
#
# # Pop the value
# mStack.pop()
# mStack.pop()
#
# # Checking is the Stack empty
# print(mStack.isEmpty())
# print(mStack.printStack())
#
# # Return the top value
# m = mStack.top()
#
# # Print stack
# mStack.printStack()
























