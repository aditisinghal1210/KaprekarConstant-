def kaprekar_const(num):

    it = 0
    while num != 6174:

        digits = [int(d) for d in str(num)] #Converting the number into list


        while len(digits) < 4:        #Pad the list with zeroes if the number is less than 4
            digits.append(0)


        small_digits = sorted(digits)             #Making the smallest number
        large_digits = sorted(digits, reverse=True)  #Making the largest number


        smallest_num = int(''.join(map(str, small_digits)))   #Converting the list into digits and then numbers
        largest_num = int(''.join(map(str, large_digits)))


        num = largest_num - smallest_num   #calculate the difference

        # Increment the number of iterations
        it += 1

    return it


print("Enter the 4 digit number:")
number=input()
print(kaprekar_const(number))
# print(kaprekar_const(4356))
