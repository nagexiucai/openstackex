#!/usr/bin/env python
#coding=utf-8

from core.ossdk import OpenstackSDK

ossdk = OpenstackSDK(auth='http://keystone:35357/v3')
ossdk.create()
ossdk.update('launch_vm')
