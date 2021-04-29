import csv, codecs

from datetime import datetime


date_list = [datetime(2002, 9, 1, 0, 0), datetime(2005, 8, 1, 0, 0), datetime(2013, 12, 1, 0, 0), datetime(2016, 1, 1, 0, 0),
             datetime(2016, 11, 1, 0, 0), datetime(2018, 2, 1, 0, 0), datetime(2019, 10, 1, 0, 0), datetime(2021, 3, 1, 0, 0)]

def making_file_name(date):
    file_name = "content" + str(date.year)+ "_" + str(date.month) + ".txt"
    return file_name



if __name__ == '__main__':

    standard_time1 = date_list.pop(0)
    file_name1 = making_file_name(standard_time1)
    f1 = open(file_name1, 'w')

    standard_time2 = date_list.pop(0)
    file_name2 = making_file_name(standard_time2)
    f2 = open(file_name2, 'w')

    standard_time3 = date_list.pop(0)
    file_name3 = making_file_name(standard_time3)
    f3 = open(file_name3, 'w')

    standard_time4 = date_list.pop(0)
    file_name4 = making_file_name(standard_time4)
    f4 = open(file_name4, 'w')

    standard_time5 = date_list.pop(0)
    file_name5 = making_file_name(standard_time5)
    f5 = open(file_name5, 'w')

    standard_time6 = date_list.pop(0)
    file_name6 = making_file_name(standard_time6)
    f6 = open(file_name6, 'w')

    standard_time7 = date_list.pop(0)
    file_name7 = making_file_name(standard_time7)
    f7 = open(file_name7, 'w')

    standard_time8 = date_list.pop(0)
    file_name8 = making_file_name(standard_time8)
    f8 = open(file_name8, 'w')

    with codecs.open('full_data.csv', 'r') as f:
        rdr = csv.reader(f)
        next(rdr)

        for line in rdr:
            date = datetime.strptime(line[2], '%Y.%m.%d.')
            data = line[5] + "\n"

            if date < standard_time4:
                if date < standard_time2:
                    if date < standard_time1:
                        f1.write(data)
                    else:
                        f2.write(data)
                else:
                    if date < standard_time3:
                        f3.write(data)
                    else:
                        f4.write(data)
            else:
                if date < standard_time6:
                    if date < standard_time5:
                        f5.write(data)
                    else:
                        f6.write(data)
                else:
                    if date < standard_time7:
                        f7.write(data)
                    else:
                        f8.write(data)

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()