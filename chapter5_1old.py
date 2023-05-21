digits = {1,2,3,4,5,6,7,8,9,0}
# print("digits[0]:", digits[0])
# print("digits[-1]:", digits[-1])

print("")
for your_digit_name in digits:
    print(your_digit_name)
print("End of digits,")


digits[-1] = 13
for your_digit_name in digits:
    print(your_digit_name)
print("End of digits,")

test_tuple = (1,2,3)
print("test_tuple:", test_tuple)

test_tuple[-1] = 13