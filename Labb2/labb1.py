#Skapa en list med Hockyspelare.

#
#alphabet = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Z")


# def bubble_sort(arr):
#     n = len(arr)
#     swapped = False
#     for i in range (n-1):
#         for j in range (0,n-i-1):
#             current_numb = arr[j]
#             next_numb = arr[j + 1]
#             if current_numb > next_numb:
#                 swapped = True
#                 arr[j] = next_numb
#                 arr[j + 1] = current_numb
#                 #arr [j], arr[j +1] = arr [j -1], arr[j]
#         if not swapped:
#             return
# arr = [5, 10, 52, 32, 14,18,40]

# bubble_sort(arr)
# print(arr)
#for i in range(len(arr)):
    #print("% d" % arr[i], end=" ")



def bubble_sort_string(arr):
    n = len(arr)
    for i in range(n -1):
        for j in range(0,n -i -1):
            current_word = arr[j]
            next_word = arr[j +1]
            if ord(current_word[0]) >  ord(next_word[0]):
                arr[j] = current_word
                arr[j +1] = next_word


elden_arr = ("Gordrc", "Daddy", "Tere","Afff","Corg")

bubble_sort_string(elden_arr)
print(elden_arr)


def bubble_sort_strings(arr):
    n = len(arr)
    
    for i in range(n):
        # Last i elements are already sorted, so we reduce the inner loop range
        for j in range(0, n-i-1):
            # Compare characters at index 0 using their Unicode values
            if ord(arr[j][0]) > ord(arr[j+1][0]):
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements
                
# Example usage
string_list = ["apple", "banana", "grape", "orange", "pear"]
bubble_sort_strings(string_list)
print(string_list)