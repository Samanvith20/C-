# Used to create a generator, a special kind of iterator.
# When yield is used, the function doesn’t execute entirely at once. Instead, it "pauses" and "resumes" between calls, emitting values one at a time.
# Suitable for large datasets or streaming data where storing all results in memory is impractical.


def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i


# even_generator(10)
# print(even_generator(10))   it returns a generator object that can be iterated over to retrieve values one at a time 

for num in even_generator(10):
    print(num)