import traceback

try:
    from api.server import app
    print("SUCCESS: api.server imported successfully")
except Exception:
    print(traceback.format_exc())
    raise
