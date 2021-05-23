from bottle import route, run, template, request, response
import here
import json


@route('/data/v1/route')
def index():
    options = []
    params = dict(request.query.decode())
    try:
        destination = params['destination']
        mylocation = params['location']
        koordinates = here.get_koordinates(destination)
        kilometers = here.get_km_car(mylocation, koordinates)[0]
        car = here.get_km_car(mylocation, koordinates)
        bike = here.get_route_bike(mylocation, koordinates)
        bus = here.get_route_bus(mylocation, koordinates)
        walk = here.get_route_walk(mylocation, koordinates)
        options.append({'name': 'car', 'kilometers': car[0], 'time': car[1],'trees':car[0]*122*10**(-3)/21})
        options.append({'name': 'bike', 'kilometers': bike[0], 'time': bike[1], 'trees':bike[0]*122*10**(-3)/21, 'cal': bike[0]*30})
        options.append({'name': 'walk', 'kilometers': walk[0], 'time': walk[1], 'trees':walk[0]*122*10**(-3)/21, 'cal': walk[0]*76})
        if bus:
            options.append({'name': 'bus',
                            'number': bus[0] + " " + bus[1],
                            'vstopna': bus[2],
                            'izstopna': bus[3],
                            'leaving_time': bus[4],
                            'arriving_time': bus[5],
                            'time': bus[6]})
        json_object = {'destination': destination,
                       'kilometers': kilometers,
                       'options': options}
        response.content_type = 'application/json'
        return json.dumps(json_object)
    except Exception as e:
        print(e)
        return 'Bad request'


run(host='localhost', port=8888)
