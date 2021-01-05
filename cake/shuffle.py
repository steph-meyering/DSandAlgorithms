import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(the_list):
    # Shuffle the input in place
    for i in range(len(the_list)):
        next_i = get_random(0, len(the_list) - 1)
        the_list[i], the_list[next_i] = the_list[next_i], the_list[i]


sample_list = [1, 2, 3, 4, 5]
print('Sample list:', sample_list)

print('Shuffling sample list...')
shuffle(sample_list)
print(sample_list)
