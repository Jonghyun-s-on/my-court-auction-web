class User:
    def __init__(self, user_id, username, password):
        self.__user_id = user_id
        self.__username = username
        self.__password = password

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    def to_dict(self):
        return {
            "user_id": self.__user_id,
            "username": self.__username,
            "password": self.__password  # 필요시 마스킹 가능
        }
