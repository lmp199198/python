# -*- coding:utf-8 -*-
from requests_toolbelt import MultipartEncoder
import requests

m=MultipartEncoder(
    fields={'file1':'value1',
            'file2':'value2',
            'file3':('filename',open('file.py','rb'),'text/plain')

    }
)

m=MultipartEncoder(
    fields=[('source',('f1.ext',f1,'application/x-example-mimetype')),
            ('source',('f2.ext',f2,'application/x-example-mimetype'))

]

)
r=requests.post('http://www.baidu.com/',data=m,
                headers={'Content-type':m.content_type})

