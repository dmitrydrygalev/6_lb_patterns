from abc import ABC, abstractmethod


# Абстрактный пользователь
class User(ABC):
    pass


# Пользователь МТС - с номером телефона
class MtsUser(User):
    def __init__(self, phone):
        print(f"MtsUser is created:{phone}")


# Пользователь Gmail - с почтовым ящиком
class GmailUser(User):
    def __init__(self, email):
        print(f"GmailUser is created:{email}")


# Абстрактные аккаунты
class Accounts(ABC):
    pass


# Данные для входа в аккаунт Gmail
class GmailAccounts(Accounts):
    def __init__(self, email, password):
        self._email = email
        self._password = password

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password


# Данные для входа в акканут МТС
class MtsAccounts(Accounts):
    def __init__(self, phone, password):
        self._phone = phone
        self._password = password

    @property
    def phone(self):
        return self._phone

    @property
    def password(self):
        return self._password


# Абстрактный аутентификатор
class Authenticator(ABC):
    @abstractmethod
    def authenticate(self, accounts: Accounts) -> User:
        pass


# Аутентификатор Gmail
class GmailAuthenticator(Authenticator):
    def authenticate(self, accounts: GmailAccounts) -> GmailUser:
        print(f"Authenticated by email: {accounts.email}")
        return GmailUser(accounts.email)


# Аутентификатор МТС
class MtsAuthenticator(Authenticator):
    def authenticate(self, accounts: MtsAccounts) -> MtsUser:
        print(f"Authenticated by phone: {accounts.phone}")
        return MtsUser(accounts.phone)


# Метод аутентификации
def authenticate(authenticator: Authenticator, accounts: Accounts) -> User:
    return authenticator().authenticate(accounts)


# логин для МТС (phone + password)
phone = "+79169744318"
password = '***'
accounts = MtsAccounts(phone, password)
user: MtsUser = authenticate(MtsAuthenticator, accounts)

# логин для Gmail(email + password)
email = 'campermailru@mail.ru'
password = '***'
accounts = GmailAccounts(email, password)
user: GmailUser = authenticate(GmailAuthenticator, accounts)
