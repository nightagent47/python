# create a function that will create a palindrome of a string
def isPalindrome():
    test=str(input("Enter a string: "))
    if (test==test[::-1]):
        print("The word is palindrome")
    else:
        print("The word is not palindrome")
isPalindrome()
