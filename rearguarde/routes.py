from flask import current_app, g, Response, request
import json

from .model.crack import Song, Sheet, TrackTab


about_string = """
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras sed convallis elit. Aenean quam 
ipsum, condimentum eget laoreet vel, hendrerit eget lacus. Maecenas feugiat justo sit amet 
vestibulum viverra. Praesent molestie condimentum pretium. Phasellus gravida mi ipsum, sed 
tincidunt orci tincidunt eu. Quisque tempus dolor nibh, quis condimentum nisi porttitor eget. 
Nullam vestibulum ligula nec turpis finibus mollis. In cursus non mauris in tincidunt. Integer 
accumsan mattis enim, at tincidunt tortor sodales ac.</p>

<p>Nulla et libero semper, pellentesque enim ac, interdum nibh. Vivamus quis ultrices tortor, in 
aliquam justo. Duis ex nisl, eleifend et ex ut, ultricies commodo velit. Nunc faucibus diam eget 
augue vulputate, quis sagittis lacus sagittis. Suspendisse hendrerit enim nec elementum venenatis. 
Vivamus fermentum dapibus tellus vel fringilla. Nullam lacus mi, bibendum facilisis dolor a, 
fermentum cursus diam. Vivamus accumsan lorem a finibus accumsan. Donec sit amet consequat nisl, 
non feugiat augue.</p>

<p>Curabitur varius dui id dolor consequat, quis maximus leo accumsan. Sed pretium, purus et 
vulputate posuere, lectus risus tempor ante, ac tincidunt arcu ante elementum elit. Nam egestas 
bibendum nulla non mollis. Morbi at venenatis erat. Pellentesque id lorem ac dolor viverra commodo 
quis pretium justo. Pellentesque sit amet enim tincidunt ante porta rhoncus. Sed luctus feugiat 
augue quis congue. Phasellus accumsan sollicitudin ante, sed congue turpis ultricies sit amet. 
Praesent varius turpis sem, ut placerat dolor interdum sed. Mauris leo odio, luctus et accumsan 
vitae, scelerisque nec velit. Nam nec accumsan lectus.</p>
"""


def _to_json(obj_or_list):
    if not obj_or_list:
        return json.dumps([])
    if not isinstance(obj_or_list, list):
        return json.dumps([obj_or_list])
    return json.dumps(obj_or_list)


def json_response(obj_or_list):
    return Response(_to_json(obj_or_list), mimetype='application/json')


def register_routes(app):
    @app.route('/')
    def index():
        return 'Hola mundo!'

    @app.route('/status')
    def status():
        return f'Running application name is {current_app.name}'

    @app.route('/about')
    def about():
        return about_string

    @app.route('/songs')
    def songs():
        elements = [repr(x) for x in g.session.query(Song).all()]
        return json_response(elements)

    @app.route('/sheets')
    def sheets():
        elements = [repr(x) for x in g.session.query(Sheet).all()]
        return json_response(elements)

    @app.route('/tracktabs')
    def tracktabs():
        elements = [repr(x) for x in g.session.query(TrackTab).all()]
        return json_response(elements)

    @app.route('/easter-egg')
    def easter_egg():
        with open('data/easter-egg.txt') as fstream:
            return '<pre>{}</pre>'.format(''.join(fstream.readlines()))
