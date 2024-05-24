def get_coordinate(record):
    return record[1]


def convert_coordinate(coordinate):
    num = coordinate[0]
    let = coordinate[1]
    return (num, let)


def create_record(azara_record, rui_record):

    a, b = azara_record
    c, d, e = rui_record
    num = b[0]
    let = b[1]
    coor_az = (num, let)

    if coor_az == d:
        final = azara_record + rui_record
    else:
        final = "not a match"

    return final
