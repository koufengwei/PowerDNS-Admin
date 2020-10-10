class StructuredException(Exception):
    status_code = 0

    def __init__(self, name=None, message="You want override this error!"):
        Exception.__init__(self)
        self.message = message
        self.name = name

    def to_dict(self):
        rv = dict()
        msg = ''
        if self.name:
            msg = '{0} {1}'.format(self.message, self.name)
        else:
            msg = self.message

        rv['msg'] = msg
        return rv


class DomainNotExists(StructuredException):
    status_code = 404

    def __init__(self, name=None, message="域名不存在"):
        StructuredException.__init__(self)
        self.message = message
        self.name = name


class DomainAlreadyExists(StructuredException):
    status_code = 409

    def __init__(self, name=None, message="域名已经存在"):
        StructuredException.__init__(self)
        self.message = message
        self.name = name


class DomainAccessForbidden(StructuredException):
    status_code = 403

    def __init__(self, name=None, message="域名不允许访问"):
        StructuredException.__init__(self)
        self.message = message
        self.name = name


class ApiKeyCreateFail(StructuredException):
    status_code = 500

    def __init__(self, name=None, message="创建ApiKey失败"):
        StructuredException.__init__(self)
        self.message = message
        self.name = name


class ApiKeyNotUsable(StructuredException):
    status_code = 400

    def __init__(
        self,
        name=None,
        message="Api key must have domains or have administrative role"):
        StructuredException.__init__(self)
        self.message = message
        self.name = name


class NotEnoughPrivileges(StructuredException):
    status_code = 401

    def __init__(self, name=None, message="权限不够"):
        StructuredException.__init__(self)
        self.message = message
        self.name = name


class RequestIsNotJSON(StructuredException):
    status_code = 400

    def __init__(self, name=None, message="请求不是json格式"):
        StructuredException.__init__(self)
        self.message = message
        self.name = name


class AccountCreateFail(StructuredException):
    status_code = 500

    def __init__(self, name=None, message="创建账号失败"):
        StructuredException.__init__(self)
        self.message = message
        self.name = name


class AccountUpdateFail(StructuredException):
    status_code = 500

    def __init__(self, name=None, message="账号更新失败"):
        StructuredException.__init__(self)
        self.message = message
        self.name = name


class AccountDeleteFail(StructuredException):
    status_code = 500

    def __init__(self, name=None, message="删除账号失败"):
        StructuredException.__init__(self)
        self.message = message
        self.name = name


class UserCreateFail(StructuredException):
    status_code = 500

    def __init__(self, name=None, message="创建用户失败"):
        StructuredException.__init__(self)
        self.message = message
        self.name = name


class UserUpdateFail(StructuredException):
    status_code = 500

    def __init__(self, name=None, message="用户更新失败"):
        StructuredException.__init__(self)
        self.message = message
        self.name = name


class UserDeleteFail(StructuredException):
    status_code = 500

    def __init__(self, name=None, message="删除用户失败"):
        StructuredException.__init__(self)
        self.message = message
        self.name = name
