import logging
import logging.handlers
import os
import sys
from datetime import datetime

def setup_logging(app):
    """
    Configure structured logging with JSON format and file rotation.
    """
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    log_format = os.getenv('LOG_FORMAT', 'json').lower()
    
    # Remove default Flask logger
    app.logger.handlers.clear()
    
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Set up root logger
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, log_level))
    
    # File handler with rotation
    file_handler = logging.handlers.RotatingFileHandler(
        'logs/app.log',
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=5
    )
    file_handler.setLevel(getattr(logging, log_level))
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, log_level))
    
    # Formatter
    if log_format == 'json':
        formatter = JsonFormatter()
    else:
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
    
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    app.logger = logger
    return logger


class JsonFormatter(logging.Formatter):
    """
    Custom formatter that outputs logs as JSON.
    """
    def format(self, record):
        import json
        log_data = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno,
        }
        
        if record.exc_info:
            log_data['exception'] = self.formatException(record.exc_info)
        
        return json.dumps(log_data, ensure_ascii=False)
