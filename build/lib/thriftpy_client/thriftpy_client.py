#encoding:utf-8
'''
Created on 2018年8月24日

@author: qiuyan
'''

from logs import LOG
import thriftpy
from thriftpy.protocol import (
    TBinaryProtocolFactory,
    TMultiplexedProtocolFactory
    )

from thriftpy.rpc import make_client
logger = LOG('rpc_conn')

def get_client(thrift_file,thrift_name,url,port,service_name,is_multiplexer=False,timeout=20*1000):
    '''
    获取RPC client 链接
    :param thrift_file: thriftpy服务文件路径
    :param thrift_name:thritpy定义的类名称   # service 【CarsServices】
    :param url:rpc服务ip或域名
    :param port:服务端口
    :param service_name: 服务名称  
    :param is_multiplexer:是否是多服务
    :return:
    '''
    try:
        my_service = getattr(thriftpy.load(thrift_file, module_name=thrift_file.split('/')[-1].replace('.', '_')),
                             thrift_name)
        if is_multiplexer:
            binary_factory = TBinaryProtocolFactory()
            dd_factory = TMultiplexedProtocolFactory(binary_factory, service_name)
            client = make_client(my_service,url,port, proto_factory=dd_factory,timeout=timeout)
        else:
            client = make_client(my_service,url,port,timeout=timeout)
        return client
    except Exception as ex:
        logger.error()
        return None


def request_thrift(thrift_file,thrift_name,url,port,service_name,method,is_multiplexer=False,timeout=20*1000,**kwargs):
    '''

    :param thrift_file:thriftpy服务文件路径
    :param thrift_name:thritpy定义的类名称   # service 【CarsServices】
    :param url:rpc服务ip或域名
    :param port:服务端口
    :param service_name:服务名称
    :param method:调用服务的对应方法
    :param is_multiplexer:是否是多服务
    :param timeout:超时时间
    :param kwargs:
    :return:
    '''
    try:
        client = get_client(thrift_file,thrift_name,url,port,service_name,is_multiplexer=is_multiplexer,timeout=timeout)
        '''
        my_service = getattr(thriftpy.load(thrift_file, module_name=thrift_file.split('/')[-1].replace('.', '_')),
                             service_name)
        if is_multiplexer:
            binary_factory = TBinaryProtocolFactory()
            dd_factory = TMultiplexedProtocolFactory(binary_factory, service_name)
            client = make_client(my_service, url, port, proto_factory=dd_factory, timeout=timeout)
        else:
            client = make_client(my_service, url, port, timeout=timeout)
        '''
        msg = getattr(client, method)(**kwargs)
        return msg
    except Exception as ex:
        logger.error()
        return None
