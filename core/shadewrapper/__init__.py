#!/usr/bin/env python
#coding=utf-8

#how to make the image?
##disable selinux
##modify sshd port according to hostfwd and ssh authorize(pubkey & password, root allowed)
##chmod a+x on /etc/rc.d/rc.local and configure ostserver & ostsnitcher
##isolate test tenant(project) is recommendation
##using environment variables as configuration for openstack

#todo: why virsh console failed for vm launched by openstack using same image with kvm correctly?

from core.base import Base
import shade
import os

class Cloud(Base):
    @staticmethod
    def update_environment_variables(**kws):
        os.environ.update(kws)
    def __init__(self, *args, **kws):
        super(Cloud, self).__init__(*args, **kws)
    def create(self, *args, **kws):
        self.backend = shade.openstack_cloud()

class Net(Base):
    pass

class VM(Base):
    def __init__(self, platform):
        self.platform = platform
    def create(self, **kws):
        '''
        name, image, flavor, 
        auto_ip=True, ips=None, ip_pool=None, 
        root_volume=None, terminate_volume=False, 
        wait=False, timeout=180, reuse_ips=True, 
        network=None, boot_from_volume=False, volume_size='50', 
        boot_volume=None, volumes=None, nat_destination=None, 
        **kwargs
        '''
        self.platform.create_server(**kws)
    def _start(self):
        pass
    def _stop(self):
        pass
    def remove(self, which, **kws):
        '''
        name_or_id, wait=False, timeout=180, delete_ips=False, delete_ip_retry=1
        '''
        self.platform.delete_server(which, **kws)

if __name__ == '__main__':
    Cloud()
