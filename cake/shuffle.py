import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

# Using the Fisher-Yates Shuffle (in place, O(n) time, constant space)
def shuffle(the_list):
    # Shuffle the input in place
    for i in range(len(the_list) - 1):
        j = get_random(i, len(the_list) - 1)
        the_list[i], the_list[j] = the_list[j], the_list[i]


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)
