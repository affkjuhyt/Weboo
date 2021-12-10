"""
Function status
"""


def funcSuccess(data=None, msg='success', **kwargs):
    """
    :param data:
    :param msg:
    :return:
    """
    return {
        "result": True,
        "msg": msg,
        "data": data,
    }


def funcError(data=None, msg='error', **kwargs):
    """
    :param data:
    :param msg:
    :return:
    """
    return {
        "result": False,
        "msg": msg,
        "data": data,
    }


def funcResult(result=True, data=None, msg='success', **kwargs):
    """
    :param result:
    :param data:
    :param msg:
    :return:
    """
    if result:
        return funcSuccess(data=data, msg=msg)
    return funcError(data=data, msg=msg)


def paginate(data=None, count=0, next=None, previous=None, msg='success', code=2000):
    """
    pagination()
    :param data: []
    :param count: len(data); data, count(*); count, count==len(data)
    :param next: None,
    :param previous: None,
    :param msg: success
    :param code: 2000,
    :return:
    """
    if not data:
        data = []
    if not count:
        count = len(data)
    return {
        "code": code,
        "data": {
            "count": count,
            "next": next,
            "previous": previous,
            "results": data
        },
        "msg": msg,
        "status": "success"
    }
