# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Note:
# In some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type.
# It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation.
# Therefore, in Example 3, the input represents the signed integer. -3.

def hammingWeight(number):
    count = 0

    while (number > 0):
        if(number % 10 == 1):
            count += 1

        number = number // 10

    return count

print(hammingWeight(00000000001011))