from flask import Blueprint, request, g, request, redirect, session


langs = Blueprint('langs', __name__, template_folder='views')


@langs.route('/change_language', methods=['POST'], endpoint='change_language')
def change_language():
    language = request.form.get('language')  
    session['lang'] = language  
    return redirect(request.referrer) 