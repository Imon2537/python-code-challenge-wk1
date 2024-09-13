# function for adding numbers
# def add(num1, num2):
#     return num1 + num2

# sumation = add(23, 65)
# print(sumation)
def intersperse_list_with_token(output_list, token):
    result = []
    token_index = 0

    # Convert the list of numbers to a single string with spaces
    output_str = ' '.join(map(str, output_list))

    for char in output_str:
        if char != ' ':
            result.append(char)
            if token_index < len(token):
                result.append(token[token_index])
                token_index += 1
        else:
            result.append(char)

    # Append any remaining token characters if they exist
    if token_index < len(token):
        result.append(' ')
        result.extend(token[token_index:])

    return ''.join(result)

# Example usage
output_list = [90, 4]
token = 'cp7wqnlj580'
final_output = intersperse_list_with_token(output_list, token)
print(final_output)  # Output: 9c0p 74w2qnlj580
























