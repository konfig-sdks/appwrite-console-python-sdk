from appwrite_console_python_sdk.paths.account.get import ApiForget
from appwrite_console_python_sdk.paths.account.post import ApiForpost
from appwrite_console_python_sdk.paths.account.delete import ApiFordelete


class Account(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
