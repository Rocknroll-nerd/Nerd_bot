from kerykeion import KrInstance, MakeSvgInstance
#просто пробные запуски частей
def kk():
    first = KrInstance("Jack", 1990, 6, 15, 15, 15, "Roma")
    name = MakeSvgInstance(first, chart_type="Natal")
    
    #name.output_directory = Path.home() / "charts"
    
    print(first.pluto)
    name.makeSVG()

def new_func(name):
    b = name.planets_settings
    return b
    #print(template)
    

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
    
if __name__ == '__main__':
    kk()
    
