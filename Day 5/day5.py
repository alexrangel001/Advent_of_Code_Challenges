def main():
    
    # Read the text file
    infile = open('input.txt', 'r')

    # Initialize nice counter
    nice = 0

    # Read all the lines from the file
    for current_line in infile:
        # Evaluate the first condition
        first = condition_one(current_line)

        # Evaluate the second condition
        second = condition_two(current_line)

        # Evaluate the second condition
        third = condition_three(current_line)

        if first == True and second == True and third == True:
            nice += 1
        
    # Close the file
    infile.close()

    # Print value of nice
    print(nice)

# First Condition: At Least Three Vowels (aeiou)
def condition_one(line):

    # Initialize vowel counter
    vowel_count = 0
    
    # Access individual characters and test the condition
    for ch in line:
        if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
            vowel_count += 1

    # Are there at least three vowels?
    if vowel_count >= 3:
        return True
    else:
        return False



# Second Condition: At Least One Letter that Appears Twice in a Row (aa, bb)
def condition_two(line):

    # Initialize ch
    ch = 0
    
    # Access individual characters
    while ch < len(line):

        # Assigning first element to first
        first = line[ch]

        # If ch = len(test), then exit the loop,
        # otherwise, assign the next element to second
        if ch+1 == len(line):
            break
        else:
            second = line[ch+1]

        # If the first and second elements are equal, return True
        # Otherwise, assign the second element is now
        # the first in the next iteration and increment ch
        if first == second:
            return True
        else:
            first = second
            ch += 1

    # If the here, that means no letter appeared twice in a row, return False
    return False



# Third Conidtion: Does NOT have ab, cd, pq, xy        
def condition_three(line):
    
    # Initialize ch
    ch = 0
    
    # Access individual characters
    while ch < len(line):

        # Assigning first element to first
        first = line[ch]

        # If ch = len(test), then exit the loop,
        # otherwise, assign the next element to second
        if ch+1 == len(line):
            break
        else:
            second = line[ch+1]

        # Concatenate the two elements together
        two_elements = first + second

        # If two_elements is ab, cd, pq, or xy, return False
        # otherwise, next iteration
        if two_elements == 'ab' or two_elements == 'cd' or two_elements == 'pq' or two_elements == 'xy':
            return False
        else:
            first = second
            ch += 1

    # If the here, that means no two elements were ab, cd, pq, xy, return True
    return True


    
main()
