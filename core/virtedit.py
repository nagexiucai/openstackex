#!/usr/bin/env python
#coding=utf-8

# virt-edit -d $domain $file
# then skip to vi(m) or other editors configured as default
# guestfs-python is alternative tool
# so, there are 3 ways
# 1, call virt-edit in shell
# 2, call virt-edit in python, especially using howtopython to interact with it
# 3, call guestfs python binding

# [root@centos ~]# df -h
# Filesystem      Size  Used Avail Use% Mounted on
# /dev/vda3        18G  944M   17G   6% /
# devtmpfs        912M     0  912M   0% /dev
# tmpfs           921M     0  921M   0% /dev/shm
# tmpfs           921M  8.3M  912M   1% /run
# tmpfs           921M     0  921M   0% /sys/fs/cgroup
# /dev/vda1       497M  116M  382M  24% /boot
# tmpfs           185M     0  185M   0% /run/user/0
# [root@centos ~]# ls /dev/vda*
# /dev/vda  /dev/vda1  /dev/vda2    /dev/vda3

IMAGE = '/home/bob/Test-CentOS7.qcow2'
LOCAL = '/home/bob/test'
REMOTE = '/home/bob/test'

# yum install libguestfs-devel
# pip install http://libguestfs.org/download/python/guestfs-1.32.10.tar.gz
# yum install python-libguestfs

import guestfs

g = guestfs.GuestFS(python_return_dict=True)
g.add_drive_opts(IMAGE, readonly=False)
g.launch()
g.inspect_os()
ROOT = g.inspect_get_roots() #['/dev/sda3']
g.inspect_get_montpoints(ROOT[0]) #{'/boot': '/dev/sda1', '/': '/dev/sda3'}
g.inspect_get_filesystems(ROOT[0]) #['/dev/sda3', '/dev/sda1', '/dev/sda2']
g.mount(ROOT[0], '/')
g.upload(LOCAL, REMOTE)
g.shutdown()
g.close()
