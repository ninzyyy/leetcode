
def isPalindrome(s:str) -> bool:

    s = s.lower()
    s = s.replace(" ", "")
    s_list = [letter for letter in s]
    s_list = [letter for letter in s_list if letter.isalnum()]

    for n in range(int(len(s_list)/2)):
        if s_list[n] != s_list[-abs(n+1)]:
            return False
    return True

s = 'ra#ce:ca^r'
answer = isPalindrome(s)
if answer == True:
    print('✅ The string is a palindrome.')
else:
    print('❌ The string is not a palindrome.')
