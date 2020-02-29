import json

from flask import render_template, Response, request

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
        alerts.append(
            Alert(
                hostname=utils.safe_get(device, 'device', 'system_name'),
                customer=utils.safe_get(device, 'customer', 'name'),
                url=f'https://app.ninjarmm.com/#/deviceDashboard/{device_id}/overview',
                alert=utils.safe_get(device, 'message')
            )
        )
    if request.args['csv']:
        from io import StringIO
        import csv
        csvfile = StringIO()
        writer = csv.writer(csvfile)
        writer.writerow(['customer', 'hostname', 'url', 'alert'])
        for a in alerts:
            writer.writerow([a.customer, a.hostname, a.url, a.alert])
        return Response(response=csvfile.getvalue(), status=200, mimetype='text/csv')
    else:
        return render_template('alerts.html', alerts=alerts)


@app.route('/devices')
def devices():
    return Response(response=json.dumps(client.get_devices()), status=200, mimetype='application/json')


@app.route('/servers')
def servers():
    return Response(response=json.dumps(utils.get_servers()), status=200, mimetype='application/json')


@app.route('/virtual')
def virtual_devices():
    return Response(response=json.dumps(utils.get_virtual_devices()), status=200, mimetype='application/json')
