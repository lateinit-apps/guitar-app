from flask import current_app, g
from app.model.crack import Song


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
        session = g.get('session')
        elements = [f'<li>{x.id}: "{x.name}" - {x.trivia}</li>' 
                    for x in session.query(Song).all()]
        return '<ul>{}</ul>'.format('\n'.join(elements))
