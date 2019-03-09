from tinydb import TinyDB, Query

db = TinyDB('db/db.json')

"""kategori1 = "travel"
kategori2 = "kindergarden"
kategori3 = "school"
"""
Pain = Query()


def similar_categories(kat1, kat2, kat3):
    """
    The worst function ever written.
    """
    antall1 = 0
    antall2 = 1
    antall3 = 1
    samme = 0

    for i in range(len(db.all())):
        for kat in db.all()[i]["kategori"]:
            print(kat)
            if kat1 in kat:
                antall1 += 1
            if kat2 in kat:
                antall2 += 1
            if kat3 in kat:
                antall3 += 1
            if kat1 in kat and kat2 in kat and kat3 in kat:
                samme +=1
    return [antall1, antall2, antall3, samme]

if __name__ == "__main__":
    print(similar_categories("travel", "kindergarden", "school"))