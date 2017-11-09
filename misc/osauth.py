#!/usr/bin/env python
#coding=utf-8
#by nagexiucai

auth_url = "http://host:35357/v2.0" # identify_service_url
username='admin'
password='secret'
tenant_name='admin'
compute_service_url = "http://host:8004/v1/tenant_id"

jo = {"auth": {
        "tenantName": tenant_name,
        "passwordCredentials": {
                "username": username,
                "password": password
            }
        }
    }
headers = {"Content-Type": "application/json"}

def get_token():
    r = requests.post(auth_url+"/tokens", headers=headers, data=json.dumps(jo))
    rjson = json.loads(r.text) # serviceCatalog[].type
    token = rjson.get("access").get("token").get("id")
    return token

from keystoneauth1.identity import v2
from keystoneauth1 import session
auth = v2.Password(auth_url=auth_url,
                   username=username,
                   password=password,
                   tenant_name=tenant_name)

def get_session():
    return session.Session(auth=auth)
