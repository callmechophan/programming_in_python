def is_palindrome(string: str):
    start_index = 0
    end_index = len(string) - 1

    while (start_index < end_index):
        if string[start_index] != string[end_index]:
            return False

        start_index += 1
        end_index -= 1
    
    return True

print(is_palindrome("raceccr"))
