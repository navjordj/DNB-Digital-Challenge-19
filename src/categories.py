import random

"""def get_categories():
    possible = ['shopping', 'kindergarden', 'school', 'travel']
    return [random.choice(possible), random.choice(possible)]

"""
def get_categories(s):

    # Removing punctuations from sentence
    s = s.replace("'"," ").replace('"', ' ')
    s = s.lower()
    stop_words = ['?', ',', ':', '!', '.', ';', '-', '_', '{}', '[]', '()']
    for a in s:
        #print(a)
        if a in stop_words:
            s = s.replace(a, '')
            print(s)

    categories = ['sports', 'entertainment', 'culture', 'hospital', 
              'rights', 'transport', 'food']
    # getting word from sentence that is in our category
    cat = []
    for i in s.split():
        #print(i)
        if i in categories:
            cat.append(i)
    return cat



if __name__ == "__main__":
    print(get_categories("i like food"))