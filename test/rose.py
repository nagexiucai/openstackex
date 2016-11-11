#!/usr/bin/env python
#coding=utf-8

from core.shadewrapper import Cloud, VM

if __name__ == '__main__':
    CONFIG = {
    'OS_PROJECT_DOMAIN_ID': 'default',
    'OS_USER_DOMAIN_ID': 'default',
    'OS_PROJECT_NAME': 'admin',
    'OS_TENANT_NAME': 'admin',
    'OS_USERNAME': 'admin',
    'OS_PASSWORD': '1abf3c7c0ff241ea',
    'OS_AUTH_URL': 'http://192.168.10.190:5000',
    'OS_IDENTITY_API_VERSION': '3'
    }
    Cloud.update_environment_variables(**CONFIG)
    IMAGE = 'Test-CentOS7'
    FLAVOR = 'test-centos7'
    cloud = Cloud()
    cloud.create()
    vm = VM(cloud.backend)
    vm.create(name='rose', image=IMAGE, flavor=FLAVOR, network='bobnet', wait=True, timeout=300)

#todo: what is next?
##disable selinux
##modify sshd port to 3389 and ssh authorize(pubkey & password, root allowed)
##isolate test tenant(project)
##using environment variables as configuration for openstack
#todo: why virsh console failed for vm launched by openstack using same image with kvm correctly?
