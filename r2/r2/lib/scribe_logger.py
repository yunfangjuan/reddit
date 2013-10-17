# The contents of this file are subject to the Common Public Attribution
# License Version 1.0. (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://code.reddit.com/LICENSE. The License is based on the Mozilla Public
# License Version 1.1, but Sections 14 and 15 have been added to cover use of
# software over a computer network and provide for limited attribution for the
# Original Developer. In addition, Exhibit A has been modified to be consistent
# with Exhibit B.
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
# the specific language governing rights and limitations under the License.
#
# The Original Code is reddit.
#
# The Original Developer is the Initial Developer.  The Initial Developer of
# the Original Code is reddit Inc.
#
# All portions of the code written by reddit are Copyright (c) 2006-2013 reddit
# Inc. All Rights Reserved.
###############################################################################


import sys
from scribe import scribe
from thrift.transport import TTransport, TSocket
from thrift.protocol import TBinaryProtocol


class ScribeLogger:
    '''ScribeLogger: A simple wrapper for scribe client'''
    def __init__(self,
                 port = 1464,
                 host = 'localhost'):
        socket = TSocket.TSocket(host=host, port=port)
        self.transport = TTransport.TFramedTransport(socket)
        protocol = TBinaryProtocol.TBinaryProtocol(trans=self.transport, 
            strictRead=False, strictWrite=False)
        self.client = scribe.Client(iprot=protocol, oprot=protocol)
        self.transport.open()
    ''' log: Main Function'''
    def log(self, category, message):
        log_entry = scribe.LogEntry(category, message)                
        return self.client.Log(messages=[log_entry])    

    def __del__(self):
        if self.transport is not None:
            self.transport.close()
   
