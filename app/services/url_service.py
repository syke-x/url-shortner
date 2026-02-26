from app import db 
import logging
from sqlalchemy.exc import SQLAlchemyError
from app.models.models import URL
from app.utils.utils import generate_short_code , is_valid_url
from app.utils.response import success_response , error_response
from datetime import datetime , timedelta

logger = logging.getLogger(__name__)

def create_short_url(long_url, ttl_seconds):
    
    logger.info(f"Attempting to create short URL for long URL")

    try : 
        max_attempts = 5
        attempt = 0

        while attempt < max_attempts:

            logger.debug("Generating short code")
            short_code = generate_short_code()

            exists = URL.query.filter_by(short_code=short_code).first()
            if not exists:
                break 
            
            attempt += 1 
            logger.warning(f"collision detected for short_code:{short_code} , retrying...")
            

        if attempt == max_attempts:
            logger.error("Max attempt reached for generating unique short code")
            return error_response("Failed to generate a unique short code", 500)
        
        new_url = URL(
            long_url = long_url,
            short_code = short_code,
            count= 0,
            expired_at = datetime.utcnow() + timedelta(seconds=ttl_seconds)
        )

        db.session.add(new_url)
        db.session.commit()

        logger.info(f"Short URL created successfully with short_code:{short_code}")
        return success_response(data={"short_code": short_code}, message="Short URL created successfully", status_code=201)
        
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.error(f"Database error while creating short URL: " , exc_info=True)
        return error_response("Database error occurred", 500)
    
    except Exception as e:
        db.session.rollback()
        logger.critical(f"Unexpected error while creating short URL: " , exc_info=True)
        return error_response("An unexpected server error occurred", 500)

    


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
