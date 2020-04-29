from flask import current_app
from flask_restx import Api, Resource


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


def register(api: Api):
    # this creates and assigns the namespace to the Api instance
    ns = api.namespace('common')

    @ns.route('/about')
    class About(Resource):
        def get(self):
            """Large text output test resource"""
            return about_string

    @ns.route('/status')
    class Status(Resource):
        def get(self):
            return f'Running application name is {current_app.name}'

    @ns.route('/easter-egg')
    class EasterEgg(Resource):
        def get(self):
            with open('data/easter-egg.txt') as fstream:
                return '<pre>{}</pre>'.format(''.join(fstream.readlines()))
