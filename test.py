times = ['day', 'month', 'year']
#dict_date = dict(zip(times, birthday.split(".")))


def tests(birthday, times = times):
    #try except для нанов пж
    dict_date = dict(zip(times, birthday.split(".")))
    if len(dict_date)<3:
        if len(dict_date)==1:
            print('введите месяц и год')
        else:
            print('введите год')
    else:
        print(birthday)

def main():
    tests('12.8.1999')
    tests('12.8')
    tests('12')
    

if __name__ == '__main__':
    main()