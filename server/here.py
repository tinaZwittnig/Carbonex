import datetime
import requests

def get_koordinates(city):
    r = requests.get('https://geocode.search.hereapi.com/v1/geocode?q={}&apiKey=(YOUR API KEY)'.format(city))
    data = r.json()
    lok = data['items'][0]['position']
    return str(lok['lat'])+","+str(lok['lng'])

def get_km_car(origin, destination):
    '''
    :input: origin,destination - koordinates of origin and final destination
    :return km, time'''
    r = requests.get('https://router.hereapi.com/v8/routes?transportMode=car&return=summary&origin={}&destination={}&apiKey=(YOUR API KEY)'.format(origin,destination))
    data = r.json()
    print(data)
    km = (data['routes'][0]['sections'][0]['summary']['length']) / 1000
    time = (data['routes'][0]['sections'][0]['summary']['duration']) / 60
    return (km,time)

def get_route_bike(origin,destination):
    '''
    :input: origin,destination - koordinates of origin and final destination
    :return km, time'''
    r = requests.get('https://router.hereapi.com/v8/routes?transportMode=bicycle&return=summary&origin={}&destination={}&apiKey=(YOUR API KEY)'.format(origin,destination))
    data = r.json()
    print('https://router.hereapi.com/v8/routes?transportMode=bicycle&return=summary&origin={}&destination={}&apiKey=(YOUR API KEY)'.format(origin,destination))
    km = (data['routes'][0]['sections'][-1]['summary']['length']) / 1000
    time = (data['routes'][0]['sections'][-1]['summary']['duration']) / 60
    return (km,time)

def get_route_walk(origin,destination):
    '''
    :input: origin,destination - koordinates of origin and final destination
    :return km, time'''
    r = requests.get('https://router.hereapi.com/v8/routes?transportMode=pedestrian&return=summary&origin={}&destination={}&apiKey=(YOUR API KEY)'.format(origin,destination))
    data = dict(r.json())
    km = (data['routes'][0]['sections'][0]['summary']['length']) / 1000
    time = (data['routes'][0]['sections'][0]['summary']['duration']) /60
    return (km,time)

def get_route_bus(origin, destination):
    ''':return (stevilka, koncna, vstopna, izstopna, cas odhoda busa, cas prihoda, cas potovanja)'''
    r = requests.get('https://transit.router.hereapi.com/v8/routes?apiKey=(YOUR API KEY)&origin={}&destination={}'.format(origin,destination))
    data = dict(r.json())
    try:
        for path in data['routes'][0]['sections']:
            transport = path['transport']
            if transport['mode']=='bus':
                print(path)
                busna = path['departure']['place']['name']
                busna2 = path['arrival']['place']['name']
                time1 = datetime.datetime.strptime((path['departure']['time'][:-6]), '%Y-%m-%dT%H:%M:%S')
                time2 = datetime.datetime.strptime(path['arrival']['time'][:-6], '%Y-%m-%dT%H:%M:%S')
                deltat = (time2-time1) / 60
                return transport['name'],transport['headsign'], busna,busna2, str(time1.time()),str(time2.time()), str(deltat)
    except Exception as e:
        print(e)
        return False


def CO2_emitions_reduced(km):
    ''':returns CO2 in kg saved if we use bike/if we walk'''
    factor = 122 #per km
    return factor*km*10**-3


#start ='46.05142,14.49211'
#cilj = '46.04587,14.51845'
#print(get_km_car('46.05142,14.49211', cilj))
#print(get_route_bike('46.05142,14.49211', cilj))
#print(get_route_walk('46.05142,14.49211', cilj))
#print(get_route_bus(start,cilj))
#print(get_koordinates('Ljubljana'))
#print(CO2_emitions_reduced(100))
