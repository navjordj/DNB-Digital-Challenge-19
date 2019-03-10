from tinydb import TinyDB, Query

db = TinyDB('db/db.json')

"""kategori1 = "travel"
kategori2 = "kindergarden"
kategori3 = "school"
"""
Pain = Query()


def similar_categories(kategorier):
    """
    The worst function ever written.
    """
    antall1 = 0
    antall2 = 1
    antall3 = 1
    samme = 0

    for i in range(len(db.all())):
        for kat in db.all()[i]["category"]:
            if len(kategorier) == 0:
                kategorier.append("")
                kategorier.append("")
                kategorier.append("")
            if len(kategorier) == 1:
                kategorier.append("")
                kategorier.append("")
            if len(kategorier) == 2:
                kategorier.append("")

            if kategorier[0] in kat:
                antall1 += 1
            if kategorier[1] in kat:
                antall2 += 1
            if kategorier[2] in kat:
                antall3 += 1
            if kategorier[0] in kat and kategorier[1] in kat and kategorier[2] in kat:
                samme +=1
    return [antall1, antall2, antall3, samme]

if __name__ == "__main__":
    print(similar_categories(["travel", "kindergarden", "school"]))