from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .contact import Contact
from .user import User
from .settings import SiteSettings, SeoSettings
from .forms import FounderRequest, StartupRequest, InvestorRequest
from .message import Message
