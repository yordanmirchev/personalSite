def read_high_score_as_int():
    with open("data.txt") as data:
        return int(data.read())

def write_high_score(score):
    with open("data.txt", mode="w") as data:
        data.write(str(score))