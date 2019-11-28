import csv

def save_to_file(comm_info):
    file = open("comm.csv",mode="a+",encoding="euc-kr",newline='')
    writer = csv.writer(file)
    # writer.writerow(['title','score','genre','comment'])
    for comm in comm_info:
        writer.writerow(list(comm.values()))
    return