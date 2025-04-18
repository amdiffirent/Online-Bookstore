class User:
    def __init__(self, user_id, name, email, password, role="customer"):
        self.__user_id = user_id
        self.__name = name
        self.__email = email
        self.__password = password
        self.__role = role

    def register(self):
        print(f"User {self.__name} registered successfully.")

    def login(self):
        print(f"User {self.__email} logged in.")

    def update_profile(self, name=None, email=None, password=None):
        if name:
            self.__name = name
        if email:
            self.__email = email
        if password:
            self.__password = password
        print("Profile updated successfully.")

    # Getters
    def get_user_id(self):
        return self.__user_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_role(self):
        return self.__role
    

    