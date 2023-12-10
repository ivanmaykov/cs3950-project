import os

# problem 0
def read_in_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text

# problem 1
def read_all_files(directory_string):
    file_list = os.listdir(directory_string)
    file_contents = []

    for file_name in file_list:
        file_path = os.path.join(directory_string, file_name)
        with open(file_path, 'r') as file_object:
            content = file_object.read()
            file_contents.append(content)
    
    return file_contents

# problem 2
def word_freq(content_list):
    freq_dict = {}
    for content in content_list:
        words = content.split()
        for word in words:
            word = word.lower()
            if word not in freq_dict:
                freq_dict[word] = 1
            else:
                freq_dict[word] += 1

    return freq_dict

#problem 3
def total_words(input_dict):
    total_count = 0 
    for value in input_dict.values():
        total_count += value
    return total_count

# problem 4
def classify_message(message, spam_dict, ham_dict):
    spam_score = 1.0
    ham_score = 1.0
    spam_total_words = total_words(spam_dict)
    ham_total_words = total_words(ham_dict)

    message_words = message.split()
    for word in message_words:
        word = word.lower()
        
        if word in spam_dict:
            spam_count = spam_dict[word]
        else:
            spam_count = 0

        spam_score *= (spam_count + 1) / spam_total_words

        if word in ham_dict:
            ham_count = ham_dict[word]
        else:
            ham_count = 0

        ham_score *= (ham_count + 1) / ham_total_words

    return spam_score > ham_score