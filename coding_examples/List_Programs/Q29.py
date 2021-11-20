# Break a list into list of lists with chunks of size N.
# solution:-

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list2 = ['geeks', 'for', 'geeks', 'like', 'geeky', 'nerdy', 'geek', 'love', 'questions', 'words', 'life']

n = 5
k = 4

def list_chunks_producer(lst, n):
    chunk_list = []
    for x in range(n):
        if lst == []:  # even we can write "if not lst", it means if lst is empty/non existing.
            break  # if we don't put this code, we get lot of empty lists, because loop will continue for n times.
        else:
            new_list = lst[:n]
            chunk_list.append(new_list)
            del lst[:n]
    return chunk_list


print(list_chunks_producer(my_list, k))
print(list_chunks_producer(my_list2, n))
# ----------------------------------------------------------------------------------------------------------------