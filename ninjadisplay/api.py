import ninjarmm_api
import os

def create_client():
    # Read API Keys
    API_KEY_ID = os.environ['NRMM_KEY_ID']
    API_SECRET = os.environ['NRMM_SECRET']
    # Create NinjaRMM API Client
    api = ninjarmm_api.client(API_KEY_ID, API_SECRET)
    return api