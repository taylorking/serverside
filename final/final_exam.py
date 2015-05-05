import re
def centered_average(data):
     if len(data) > 2:
        num_sum = 0 
        for i in range(1, (len(data) - 1)):
            num_sum+=data[i]
        return num_sum // (len(data) - 2)
     elif len(data) > 1:
        return data[0] + data[1] // 2
     elif len(data) > 0:
         return data
     else:
        raise ValueError

def xyz_there(data):
    result =  re.match("[^#]xyz$", data)
    if result == None: 
        return False
    else:
        return True

def word_count(*data):
    result = dict()
    current_word = ""
    for i in range(0, len(data)):
        current_word = ""
        string_data = data[i].lower()
        for j in range(0, len(string_data)):
            print(string_data[j])
            if str(string_data[j]) != ' ':
                current_word += str(string_data[j])
            else:
                if current_word not in result:
                    result[current_word] = 1
                else:
                    result[current_word]+= 1
                current_word = ""
        if current_word != "": 
            if current_word not in result: 
                result[current_word] = 1 
            else:
                result[current_word] += 1 
    return result

print(word_count("all cows eat grass", "everywhere all the time"))
