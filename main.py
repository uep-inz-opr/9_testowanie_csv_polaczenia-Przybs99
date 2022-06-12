import csv 

class Polaczenie:
    def __init__(s, f_name):
        s.filename = f_name
        s.data_dict = s.read_data()


    def read_data(s)
        sum = dict()
        with open (s.filename, 'r') as f:
            r = csv.reader(f,delimiter = ',')
            h = next(r)

            for row in r:
                subsr = int(row[0])
                if subsr not in sum:
                    sum[subsr] = 0
                sum[subsr] +=1
            return sum

    def najczesciej_dzwoniacy(s):
        return max(s.data_dict.items(), key = lambda var: var[1])

if __name__ == "__main__":
    print(Polaczenie(input()).najczesciej_dzwoniacy())