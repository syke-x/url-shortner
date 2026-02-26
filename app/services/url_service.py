from app import db 
import logging
from app.models.models import URL
from app.utils.utils import generate_short_code , is_valid_url
from app.utils.response import success_response , error_response
from datetime import datetime , timedelta

def create_short_url(long_url, ttl_seconds):
    logger = logging.getLogger(__name__)
    logger.info(f"Attempting to create short URL for long URL: {long_url}")

    try : 
        logger.debug("Generating short code")
        short_code = generate_short_code()

        while URL.query.filter_by(short_code=short_code).first():
            short_code = generate_short_code() # generate until we get a unique code
        
        new_url = URL(
            long_url = long_url,
            short_code = short_code,
            count = 0,
            expired_at = datetime.utcnow() + timedelta(seconds=ttl_seconds) 
        )

        db.session.add(new_url)
        db.session.commit()

        return success_response(data={"short_code": short_code}, message="Short URL created successfully", status_code=201)
    
    except Exception as e:
        logger.error(f"Error creating short URL: {str(e)}")
        return error_response("An error occurred while creating the short URL", 500)

    


def create_custom_short_url(long_url , custom_short_code , ttl_seconds):

    if not is_valid_url(custom_short_code):
        return error_response("Invalid custom short code. It should be 3-20 characters long and can only contain letters, numbers, underscores, or hyphens.", 400)

    if URL.query.filter_by(short_code=custom_short_code).first():
        return error_response("Custom short code already exists", 400)
    
    new_url = URL(
        long_url = long_url,
        short_code = custom_short_code,
        count= 0,
        expired_at = datetime.utcnow() + timedelta(seconds=ttl_seconds)
    )

    db.session.add(new_url)
    db.session.commit()

    return success_response(data={"short_code": custom_short_code}, message="Custom short URL created successfully", status_code=201)
