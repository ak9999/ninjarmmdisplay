import json
import random  # Only used for demo
import string  # Only used for demo

from flask import render_template, Response

from ninjadisplay import app
from ninjadisplay import client
from ninjadisplay import utils


Alert = utils.Alert

@app.route('/alerts')
def alerts():
    all_alerts_info = client.get_alerts()
    alerts = []
    for device in all_alerts_info:
        device_id = utils.safe_get(device, 'device', 'id')
        hostname = ''.join([random.choice(string.ascii_uppercase + string.digits) for n in range(10)])
        customer = ''.join([random.choice(string.ascii_uppercase) for n in range(15)])
        alerts.append(
            Alert(
                # hostname=utils.safe_get(device, 'device', 'system_name'),
                hostname=hostname,
                # customer=utils.safe_get(device, 'customer', 'name'),
                customer=customer,
                url=f'https://app.ninjarmm.com/#/deviceDashboard/{device_id}/overview',
                alert=utils.safe_get(device, 'message')
            )
        )
    return render_template('alerts.html', alerts=alerts)

# @app.route('/devices')
# def devices():
#     return Response(response=json.dumps(client.get_devices()), status=200, mimetype='application/json')


# @app.route('/servers')
# def servers():
#     return Response(response=json.dumps(utils.get_servers()), status=200, mimetype='application/json')


# @app.route('/virtual')
# def virtual_devices():
#     return Response(response=json.dumps(utils.get_virtual_devices()), status=200, mimetype='application/json')
