## Review
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("digits[0]:", digits[0])
print("digits[-1]:", digits[-1])

# Print the digits list
print("")
for your_digit_name in digits:
    print(your_digit_name)
print("End of digits.")

# Set the last index to 13.
digits[-1] = 13

# Reprint the digits list
print("")
for your_digit_name in digits:
    print(your_digit_name)
print("End of digits.")

test_tuple = (1, 2, 3)
print("test_tuple:", test_tuple)

# Set the last index of test tuple to 13.
# test_tuple[-1] = 13 # EXPECT AN ERROR!!!

test_tuple = (4, 5, 6)
print("new test_tuple:", test_tuple)
