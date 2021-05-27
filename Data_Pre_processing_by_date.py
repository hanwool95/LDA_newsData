import csv, codecs

from datetime import datetime


date_list = [datetime(2002, 7, 1, 0, 0), datetime(2005, 11, 1, 0, 0), datetime(2009, 3, 1, 0, 0), datetime(2013, 10, 1, 0, 0),
             datetime(2015, 11, 1, 0, 0), datetime(2016, 4, 1, 0, 0), datetime(2016, 9, 1, 0, 0),
             datetime(2017, 12, 1, 0, 0), datetime(2020, 1, 1, 0, 0)]

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

    standard_time9 = date_list.pop(0)
    file_name9 = making_file_name(standard_time9)
    f9 = open(file_name9, 'w')

    with codecs.open('full_data_rev3.csv', 'r') as f:
        rdr = csv.reader(f)
        next(rdr)

        for line in rdr:
            date = datetime.strptime(line[2], '%Y-%m-%d')
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
                        if date < standard_time8:
                            f8.write(data)
                        else:
                            f9.write(data)

    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    f9.close()