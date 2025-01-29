cd /var/www-fastapi
date > forecast_lastrun
source venv/bin/activate
python3 getforecast.py
