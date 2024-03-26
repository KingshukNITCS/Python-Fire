multidimensional_dict = {
        'first_level': {
             'second_level_1': {
                     'third_level_1': 1,
                     'third_level_2': 2
               },
        'second_level_2': {
                    'third_level_3': 3,
                    'third_level_4': 4
                   }
              },
 'another_first_level': {
                'second_level_3': {
                             'third_level_5': 5,
                             'third_level_6': 6
                             },
              'second_level_4': {
                            'third_level_7': 7,
                            'third_level_8': 8
                    }
             }
}




#taking above example dictionary 
value = multidimensional_dict['first_level']['second_level_1']['third_level_2']
print(value) 


#Adding new level to existing Dictionary
#We can add new level in the multidimensional dictionary in the following way:
multidimensional_dict['new_first_level'] = {'new_second_level': {'new_third_level': 100}}
print(multidimensional_dict)



#Iterating over multidimensional Dictionary
#To iterate over multidimensional Dictionary you can use nested loops.
for first_level_key, second_level_dict in multidimensional_dict.items():
    print(f"First Level Key: {first_level_key}")
    
    for second_level_key, third_level_dict in second_level_dict.items():
        print(f"  Second Level Key: {second_level_key}")
        
        for third_level_key, value in third_level_dict.items():
            print(f"    Third Level Key: {third_level_key}, Value: {value}")



#Problem Statement- Counting Word Frequencies in text corpus

def count_word_frequencies(corpus):
    word_freq = {}  # Multidimensional dictionary to store word frequencies

    for document in corpus:
        words = document.split()

        for word in words:
            if word not in word_freq:
                word_freq[word] = {'total_count': 1, 'documents': {document: 1}}
            else:
                word_freq[word]['total_count'] += 1
                if document in word_freq[word]['documents']:
                    word_freq[word]['documents'][document] += 1
                else:
                    word_freq[word]['documents'][document] = 1
    return word_freq

corpus = [
    "This is the multidimensional dictionary.",
    "This dictionary stores the sub dictionary.",
    "And this is the third containing the word and count.",
    "Is this the first level of dictionary?"
]

word_frequencies = count_word_frequencies(corpus)

# Displaying word frequencies
for word, info in word_frequencies.items():
    print(f"Word: {word}")
    print(f"  Total Count: {info['total_count']}")
    print("  Document Occurrences:")
    for document, count in info['documents'].items():
        print(f"    {document}: {count}")
    print()
