from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Explicit imports for init_db.py compatibility
from .contact import Contact
from .user import User
from .settings import SiteSettings, SeoSettings
from .forms import FounderRequest, StartupRequest, InvestorRequest
from .message import Message
from .portfolio import PortfolioProject
from .analytics import VisitAnalytics
from .security_logs import SecurityLog, BannedIP
from .testimonial import Testimonial
