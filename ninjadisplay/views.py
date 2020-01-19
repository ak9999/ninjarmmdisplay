from flask import render_template, Response

from ninjadisplay import app
from ninjadisplay import api
from ninjadisplay import utils


api = api.create_client()
Alert = utils.Alert

@app.route('/alerts')
def alerts():
    all_alerts_info = api.get_alerts()
    alerts = []
    for device in all_alerts_info:
        device_id = utils.safe_get(device, 'device', 'id')
        alerts.append(
            Alert(
                hostname=utils.safe_get(device, 'device', 'system_name'),
                customer=utils.safe_get(device, 'customer', 'name'),
                url=f'https://app.ninjarmm.com/#/deviceDashboard/{device_id}/overview',
                alert=utils.safe_get(device, 'message')
            )
        )
    return render_template('alerts.html', alerts=alerts)

@app.route('/devices')
def devices():
    from flask import Response
    import json
    return Response(response=json.dumps(api.get_devices()), status=200, mimetype='application/json')