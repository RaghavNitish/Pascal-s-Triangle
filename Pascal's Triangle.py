# =============================================================================
# Data Structures and Algorithms Nanodegree Udacity (Arrays Challenges)
# 
# Problem Statement:
# Find and return the nth row of Pascals triangle in the form a list. n is 0-based.
# 
# Here is an example:
# If n = 4, then output = [1, 4, 6, 4, 1]
# =============================================================================


#Write your code in this function
def nth_row_pascal(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        prev_row = [1, 1]
        current_row = []

        for i in range(2, n+1):
            current_row.append(1)
            count = 0
            count1 = 1

            f_e = prev_row[count]
            s_e = prev_row[count1]

            while s_e != None:
                current_row.append(s_e + f_e)
                count1 += 1
                count += 1
                
                if count1 >= len(prev_row):
                    s_e = None
                    f_e = None
                else:
                    s_e = prev_row[count1]
                    f_e = prev_row[count]

            current_row.append(1)
            prev_row = current_row
            current_row = []
        return prev_row
    
# helper function for testing purpose
def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = nth_row_pascal(n)
    if solution == output:
        print("Pass")
    else:
        print("Fail")


# =============================================================================
# Test 1
# 
# n = 0
# solution = [1]
# test_case = [n, solution]
# test_function(test_case)
# 
# Test 2
# 
# n = 1
# solution = [1, 1]
# test_case = [n, solution]
# test_function(test_case)
# 
# Test 3
# 
# n = 2
# solution = [1, 2, 1]
# test_case = [n, solution]
# test_function(test_case)
# 
# Test 4
# 
# n = 3
# solution = [1, 3, 3, 1]
# test_case = [n, solution]
# test_function(test_case)
# 
# Test 5
# 
# n = 4
# solution = [1, 4, 6, 4, 1]
# test_case = [n, solution]
# test_function(test_case)
# 
# =============================================================================
