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

def get_client(thrift_file,thrift_name,url,port,service_name,is_multiplexer=False):
    '''
    获取RPC client 链接
    :param thrift_file:
    :param service_name:
    :param url:
    :param port:
    :param is_multiplexer:
    :param kwargs:
    :return:
    '''
    try:
        my_service = getattr(thriftpy.load(thrift_file, module_name=thrift_file.split('/')[-1].replace('.', '_')),
                             thrift_name)
        if is_multiplexer:
            binary_factory = TBinaryProtocolFactory()
            dd_factory = TMultiplexedProtocolFactory(binary_factory, service_name)
            client = make_client(my_service,url,port, proto_factory=dd_factory,timeout=20*1000)
        else:
            client = make_client(my_service,url,port,timeout=20*1000)
        return client
    except Exception as ex:
        logger.error(str(ex))


def request_thrift(thrift_file,service_name, method, url, port,is_multiplexer=False,**kwargs):
    try:
        my_service = getattr(thriftpy.load(thrift_file, module_name=thrift_file.split('/')[-1].replace('.', '_')),
                             service_name)
        if is_multiplexer:
            binary_factory = TBinaryProtocolFactory()
            dd_factory = TMultiplexedProtocolFactory(binary_factory, service_name)
            client = make_client(my_service, url, port, proto_factory=dd_factory)
        else:
            client = make_client(my_service, url, port)

        msg = getattr(client, method)(**kwargs)
        return msg
    except Exception as ex:
        logger.error(str(ex))
