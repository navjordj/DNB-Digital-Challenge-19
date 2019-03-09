import random

def get_categories():
    possible = ['shopping', 'kindergarden', 'school', 'travel']
    return [random.choice(possible), random.choice(possible)]

if __name__ == "__main__":
    print(get_categories())