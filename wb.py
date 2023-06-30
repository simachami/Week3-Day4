# Pair of Gloves

# Winter is approaching, and you are preparing for your ski holidays. Your task is to determine the number of pairs of gloves you can create from the gloves in your drawer.

# Given an array describing the color of each glove, your goal is to calculate the number of pairs you can make. Remember, only gloves of the same color can form pairs.

# Write a function that takes in the array of glove colors and returns the number of pairs that can be constituted.

# Examples:

# Input :
["red", "green", "red", "blue", "blue"]

# Output: 2
# **Explanation:**
# You can form 1 pair of red gloves and 1 pair of blue gloves.


# Input:
["red", "red", "red", "red", "red", "red"]

# Output: 3

# Explanation:
# You can form 3 pairs of red gloves.



def make_pairs(color_list):
    pair_list = {} #color: count
    pair_count = 0
    
    for item in color_list:
        if item not in pair_list:
            pair_list[item] = 1
        else:
            pair_list[item] += 1
    print(pair_list)
    for quant in pair_list.values():
        pair_count = int(quant/2)
    return pair_count

print(make_pairs(["red", "green", "red", "blue", "blue"]))

print(make_pairs(["red", "red", "red", "red", "red", "red"]))


