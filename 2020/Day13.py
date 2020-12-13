import utils


def get_index(n):
    a, b = n
    return int(a), int(b)


timetable = utils.read_file("day13").split("\n")
bus_ids = list(map(get_index, filter(lambda x: x[1] != 'x', enumerate(timetable[1].split(",")))))


def earliest_departure():
    depart_time = int(timetable[0])
    for i in range(depart_time, 10000000):
        for b in range(len(bus_ids)):
            bus = int(bus_ids[b])
            if i % bus == 0:
                return (i - depart_time) * bus


def earliest_offset_departures():
    for i, j in bus_ids:
        i = -i
        while i < 0:
            i += j
        print('x = {} mod {}'.format(i, j))


earliest_offset_departures()
# using https://www.dcode.fr/chinese-remainder
