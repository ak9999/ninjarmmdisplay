# NinjaRMM Heads Up Display

Project to show information from NinjaRMM to see device health at a glance.

## Requirements
* Python 3.8
* Flask
* [py-ninjarmm-api-client](https://pypi.org/project/py-ninjarmm-api-client/)

## Configuration
1. Clone the repo
2. Run `pip install -r requirements.txt` to install the dependencies.
3. Set the `FLASK_APP` environment variable equal to `ninjadisplay`.
4. Export your NinjaRMM API ID and Secret to the environment variables `NRMM_KEY_ID` and `NRMM_SECRET`.

## Features
* Shows a page with every device that has an alert triggered.