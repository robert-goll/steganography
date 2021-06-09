from app import app 
from app.models import *

@app.shell_context_processor
def make_shell_context():
# Update dictionary when we add more models
    return{
        "db": db,
        "User": User,
        "Post": Post
    }