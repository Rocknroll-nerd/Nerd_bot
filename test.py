from kerykeion import KrInstance, MakeSvgInstance
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

#просто пробные запуски частей
def kk():
    first = KrInstance("Who", 1956, 1, 21, 7, 0, "Москва")
    
    # Set the type, it can be Natal, Composite or Transit
    name = MakeSvgInstance(first, chart_type="Natal")
    svg = name.makeSVG()
    
    print(len(name.aspects_list))
 
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
    kk()
    
if __name__ == '__main__':
    main()
    
