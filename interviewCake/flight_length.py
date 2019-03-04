# Build a feature for choosing two movies whose
# total runtimes will equal the exact flight length.
#
# Write a function that takes an integer flight_length (in minutes) and a list of
# integers movie_lengths (in minutes) and returns a boolean
# indicating whether there are two numbers in movie_lengths
# whose sum equals flight_length.

# // My solution
def can_two_movies_fill_flight(movie_lengths, flight_length):
    i = 0

    for movie in movie_lengths:
        check_for = flight_length - movie_lengths[i]

        if check_for in movie_lengths:
            return True
        else:
            i += 1
    return False

# IC solution
# def can_two_movies_fill_flight(movie_lengths, flight_length):
#     # Movie lengths we've seen so far
#     movie_lengths_seen = set()
#
#     for first_movie_length in movie_lengths:
#         matching_second_movie_length = flight_length - first_movie_length
#         if matching_second_movie_length in movie_lengths_seen:
#             return True
#         movie_lengths_seen.add(first_movie_length)
#
#     # We never found a match, so return False
#     return False
