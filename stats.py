def num_words(text):
    text_list = text.split()
    text_length = len(text_list)
    return text_length

def chars(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def report(dict):
    report_list = []
    for entry in dict:
        count = dict[entry]
        report_dict = {"char": entry, "num": count}
        report_list.append(report_dict)
    
    report_list.sort(reverse=True, key=sort_on)
    return report_list

def sort_on(dict):
    return dict["num"]