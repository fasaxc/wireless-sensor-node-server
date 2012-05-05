import os

def ensure_dir_exists(d):
    """
    Creates the directory d if it doesn't exist.  Raises an exception iff the
    directory can't be created and didn't already exist.
    """
    try:
        os.makedirs(d)
    except Exception:
        pass
    if not os.path.isdir(d):
        raise RuntimeError("Failed to create dir %s" % dir)

# Calculate useful directories relative to the project.
_MY_DIR = os.path.dirname(__file__)
STATIC_DIR = os.path.join(_MY_DIR, "static")
PROJECT_DIR = os.path.abspath(os.path.join(_MY_DIR, ".."))
DATA_DIR = os.path.join(PROJECT_DIR, "data")
ensure_dir_exists(DATA_DIR)

DATABASE = 'sqlite:///%s/db.sqlite' % DATA_DIR
DATABASE_DEBUG = False
TORNADO_DEBUG = False
