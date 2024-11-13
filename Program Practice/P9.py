# While Loop

# Initialisation
i = 1
j = 566
# Condition Checking
while i <= 566:
    if i ==5 or i ==7:
        print(5, end="")
    elif i ==6:
        print(6, end="")
    i += 1

# num = 123
# temp = num
# rev = 0

# 123 > 0 --> true
# while num > 0:
#     # First iteration:
#     remainder = num % 10    # remainder = 123 % 10 = 3
#     rev = rev * 10 + remainder  # rev = 0 * 10 + 3 = 3
#     num = num // 10         # num = 123 // 10 = 12
#
#     # Second iteration:
#     # 12 > 0 --> true
#     remainder = num % 10    # remainder = 12 % 10 = 2
#     rev = rev * 10 + remainder  # rev = 3 * 10 + 2 = 32
#     num = num // 10         # num = 12 // 10 = 1
#
#     # Third iteration:
#     # 1 > 0 --> true
#     remainder = num % 10    # remainder = 1 % 10 = 1
#     rev = rev * 10 + remainder  # rev = 32 * 10 + 1 = 321
#     num = num // 10         # num = 1 // 10 = 0
#
#     # Fourth iteration:
#     # 0 > 0 --> false
#     # Loop ends