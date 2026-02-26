from datetime import datetime, timedelta
from flask import redirect
from app import db 
from app.models.models import URL
from app.utils.response import error_response , success_response


def get_and_redirect_url(short_code):
    url = URL.query.filter_by(short_code=short_code).first()
    if url and url.expired_at > datetime.utcnow():

        url.count = url.count + 1
        url.expired_at = datetime.utcnow() + timedelta(seconds=30)
        db.session.commit()
        return redirect(url.long_url, code=302)
    
    return error_response(message="Short code not found", status_code=404)
    