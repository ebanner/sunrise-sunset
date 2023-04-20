from lxml import etree


def get_num_days(table):
    selector = etree.XPath(f'//*[@id="as-monthsun"]/tbody')
    tbody = selector(table)[0]
    return len(list(tbody.iterchildren()))


def get_sunrises(table):
    def get_sunrise(day):
        selector = etree.XPath(f'//*[@id="as-monthsun"]/tbody/tr[{day}]/td[1]')
        td = selector(table)[0]
        return td.text.strip()
    
    num_days = get_num_days(table)
    sunrises = []
    for i in range(1, num_days+1):
        try:
            sunrise = get_sunrise(i)
            sunrises.append(sunrise)
        except Exception as e:
            print(f'BadSunriseRowError({i}):', e)
    return sunrises


def get_sunsets(table):
    def get_sunset(day):
        selector = etree.XPath(f'//*[@id="as-monthsun"]/tbody/tr[{day}]/td[2]')
        td = selector(table)[0]
        return td.text.strip()

    num_days = get_num_days(table)
    sunsets = []
    for i in range(1, num_days+1):
        try:
            sunset = get_sunset(i) 
            sunsets.append(sunset)
        except Exception as e:
            print(f'BadSunsetRowError({i}):', e)
    return sunsets
