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
    return render_template('alerts.html', alerts=alerts)


@app.route('/alerts/csv')
def alerts_csv():
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
    from io import StringIO
    import csv
    with StringIO() as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['customer', 'hostname', 'url', 'alert'])
        for a in alerts:
            writer.writerow([a.customer, a.hostname, a.url, a.alert])
        return Response(response=csvfile.getvalue(), status=200, mimetype='text/csv')

@app.route('/devices')
def devices():
    return Response(response=json.dumps(client.get_devices()), status=200, mimetype='application/json')


@app.route('/devices/csv')
def devices_csv():
    from io import StringIO 
    from csv import DictWriter
    devices = client.get_devices()
    customers = client.get_customers()
    with StringIO() as csvfile:
        fieldnames = ['customer', 'hostname', 'dns_name', 'last_user', 'last_online', 'last_update', 'last_boot_time', 'role', 'os', 'buildNumber', 'releaseId', 'ninja_url']
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for d in devices:
            customer_id = utils.safe_get(d, 'customer_id')
            customer_name = None
            for customer in customers:
                if customer_id == utils.safe_get(customer, 'id'):
                    customer_name = utils.safe_get(customer, 'name')
                    break
            writer.writerow(
                {
                    'customer': customer_name,
                    'hostname': utils.safe_get(d, 'system_name'),
                    'dns_name': d['dns_name'],
                    'last_user': utils.safe_get(d, 'last_logged_in_user'),
                    'last_online': utils.safe_get(d, 'last_online'),
                    'last_update': utils.safe_get(d, 'last_update'),
                    'last_boot_time': utils.safe_get(d, 'os', 'last_boot_time'),
                    'role': d['role'],
                    'os': utils.safe_get(d, 'os', 'name'),
                    'buildNumber': utils.safe_get(d, 'os', 'buildNumber'),
                    'releaseId': utils.safe_get(d, 'os', 'releaseId'),
                    'ninja_url': utils.safe_get(d, 'ninja_url'),
                }
            )
        return Response(response=csvfile.getvalue(), status=200, mimetype='text/csv')


@app.route('/customers')
def customers():
    return Response(response=json.dumps(client.get_customers()), status=200, mimetype='application/json')

@app.route('/servers')
def servers():
    return Response(response=json.dumps(utils.get_servers()), status=200, mimetype='application/json')


@app.route('/virtual')
def virtual_devices():
    return Response(response=json.dumps(utils.get_virtual_devices()), status=200, mimetype='application/json')
