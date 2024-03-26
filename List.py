# creating a student_info list to store the information about the student roll no,name, course and marks scored
Student_info = [21, 'Rose', "CSE", 30, 40, 50]
print(Student_info)



Student_info = [21, 'Rose', "CSE", 30, 40, 50, 120]
print("Student_roll :", Student_info[0], end=' , ')
print("Student_name :", Student_info[1], end=', ')
print("Student_totalMarks :", Student_info[-1], end=' ')



Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
Student_info[2] = "ME"
print(Student_info)


Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
Student_info.append(50)
print(Student_info)


Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
Student_info.remove(50)
print(Student_info)



Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
Student2_info = [22, "John", "ME", 40, 40, 50, 130]
print(Student_info + Student2_info)


Student_info = [21, "Rose", "CSE", 20, 30, 50, 120]
print(Student_info * 2)



List = [2.0, 24.1, 3.6, 12.0, 4.5]
print(len(List))
List.sort()
print(List)
List.reverse()
print(List)




# Problem Statement - Count Occurrences of each unique word in a Sentence


def count_word_occurrences(sentence):
    word_list = sentence.split()
    unique_words = []
    word_counts = []

    for word in word_list:
        # Check if the word is already in the unique_words list
        if word in unique_words:
            index = unique_words.index(word)
            word_counts[index] += 1
        else:
            # Add the word to the unique_words list and initialize its count to 1
            unique_words.append(word)
            word_counts.append(1)

    return unique_words, word_counts

# User input
user_sentence = input("Enter a sentence: ")

unique_words, word_counts = count_word_occurrences(user_sentence)
print("Word occurrences in the sentence:")
for word, count in zip(unique_words, word_counts):
    print(f"{word}: {count}")
