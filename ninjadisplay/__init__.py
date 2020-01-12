from flask import Flask
from flask import render_template

from .api import create_client
from . import utils

api = create_client()
app = Flask(__name__)


@app.route('/')
def slash():
    return render_template('base.html')


@app.route('/alerts')
def alerts():
    all_alerts_info = api.get_alerts()
    alerts = []
    for device in all_alerts_info:
        device_id = utils.safe_get(device, 'device', 'id')
        alerts.append(
            utils.Alert(
                hostname=utils.safe_get(device, 'device', 'system_name'),
                customer=utils.safe_get(device, 'customer', 'name'),
                url=f'https://app.ninjarmm.com/#/deviceDashboard/{device_id}/overview',
                alert=utils.safe_get(device, 'message')
            )
        )
    return render_template('alerts.html', alerts=alerts)
