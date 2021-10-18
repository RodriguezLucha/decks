from api.app import app
from config import constants

if __name__ == "__main__":
    app.run(debug=constants.FLASK_DEBUG, host="0.0.0.0", port=5000)
