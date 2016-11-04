#!/usr/bin/env python
#coding=utf-8

from core.base import Base
from core.fs import FS
from core.log import Log
from openstack import connection
from openstack import profile

class OpenstackSDK(Base): #todo: design is not so good
    ACTIONS = {
        None: lambda *_:_,
    }
    @staticmethod
    def action_register(func):
        assert callable(func)
        OpenstackSDK.ACTIONS[func.func_name] = func
    def __init__(self, *args, **kws):
        super(OpenstackSDK, self).__init__(*args, **kws)
        self.__region = kws.get('region', 'RegionOne')
        self.__auth_url = kws.get('auth', 'http://keystone:5000/v3')
        self.__project_name = kws.get('project_name', 'admin')
        self.__username = kws.get('username', 'admin')
        self.__password = kws.get('password', 'admin')
        self.__user_agent = kws.get('user_agent')
    def create(self):
        self.__profile = profile.Profile()
        self.__profile.set_region(profile.Profile.ALL, self.__region)
        self.__connect = connection.Connection(
            profile = self.__profile,
            auth_url = self.__auth_url,
            project_name = self.__project_name,
            username = self.__username,
            password = self.__password,
            user_agent = self.__user_agent
            )
    def update(self, action, *args):
        OpenstackSDK.ACTIONS.get(action)(self.__connect, *args)

@OpenstackSDK.action_register
def make_keypair(openstack, *args):
    keypair_name, ssh_key_folder = args
    assert FS.is_folder(ssh_key_folder) #todo: make sure that a real folder path has been given
    keypair = openstack.compute.create_keypair(name=keypair_name)
    with file(FS.join_path(ssh_key_folder, keypair_name), 'w') as private_key:
        private_key.write('%s' % keypair.private_key)
    return keypair

@OpenstackSDK.action_register
def launch_vm(openstack, *args): #todo: just apply to floating-ip
    image_name, flavor_name, network_name, keypair_name, ssh_key_folder, vm_name = args
    image = openstack.compute.find_image(image_name)
    flavor = openstack.compute.find_flavor(flavor_name)
    network = openstack.network.find_network(network_name)
    keypair = openstack.compute.find_keypair(keypair_name) or make_keypair(openstack, keypair_name, ssh_key_folder)
    vm = openstack.compute.create_server(
             name = vm_name,
             image_id = image.id,
             flavor_id = flavor.id,
             networks = [{'uuid': network.id}],
             key_name = keypair.name
             )
    vm = openstack.compute.wait_for_server(vm)
    Log._('ssh -i {key} root@{ip}'.format(key=FS.join_path(ssh_key_folder, keypair_name), ip=vm.access_ipv4))

@OpenstackSDK.action_register
def delete_vm(openstack, *args):
    pass

@OpenstackSDK.action_register
def upload_image(openstack, *args):
    pass

@OpenstackSDK.action_register
def make_flavor(openstack, *args):
    pass


if __name__ == '__main__':
    for k,v in OpenstackSDK.ACTIONS.iteritems():
        print k,v
