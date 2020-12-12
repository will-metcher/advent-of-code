import utils

batch = utils.read_file("day04").split("\n\n")

required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid_height_units = ["cm", "in"]
valid_eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def required_fields_passports():
    count = 0
    for i in batch:
        if has_all_fields(i):
            count += 1
    return count


def has_all_fields(doc):
    for f in required_fields:
        if f not in doc:
            return False
    return True


def valid_data(doc):
    fields = dict(i.split(":") for i in doc.split(" "))
    if len(fields["byr"]) != 4 or int(fields["byr"]) < 1920 or int(fields["byr"]) > 2002:
        return False
    if len(fields["iyr"]) != 4 or int(fields["iyr"]) < 2010 or int(fields["iyr"]) > 2020:
        return False
    if len(fields["eyr"]) != 4 or int(fields["eyr"]) < 2020 or int(fields["eyr"]) > 2030:
        return False
    unit = fields["hgt"][-2:]
    if unit not in valid_height_units:
        return False

    if unit == "cm":
        if int(fields["hgt"][:-2]) < 150 or int(fields["hgt"][:-2]) > 193:
            return False
    else:
        if int(fields["hgt"][:-2]) < 59 or int(fields["hgt"][:-2]) > 76:
            return False
    if fields["hcl"][0] != "#" or len(fields["hcl"]) != 7:
        return False
    if fields["ecl"] not in valid_eye_colors:
        return False
    if len(fields["pid"]) != 9 or not fields["pid"].isnumeric():
        return False

    return True


def valid_passports():
    count = 0
    for i in batch:
        if has_all_fields(i) and valid_data(i.replace("\n", " ")):
            count += 1
    return count


print(valid_passports())
