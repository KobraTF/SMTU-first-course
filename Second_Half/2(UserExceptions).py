from dataclasses import dataclass

def main():

    @dataclass
    class UserData:
        name:str
        email:str
        age:str
    
    class NamingError(Exception):
        def __init__(self, exc):
            self.data=exc
        def __repr__(self) -> str:
            return repr(self.data)
    class AgeError(Exception):
        def __init__(self, exc):
            self.data=exc
        def __repr__(self) -> str:
            return repr(self.data)
    class EmailError(Exception):
        def __init__(self, exc):
            self.data=exc
        def __repr__(self) -> str:
            return repr(self.data)

    def verify(user:UserData, verified_users:list[UserData])->bool:
        try:
            if user.name in (name.name for name in verified_users):
                raise NamingError('This username is already taken!')
            if int(user.age)<1:
                raise AgeError('Age supposed to be > 1')
            elif int(user.age)<16:
                raise AgeError('User is too young')
            if user.email[-1]=='@' or user.email.count('@')!=1 or user.email[0]=='@':
                raise EmailError('This email adress is definetly not correct')
        except NamingError as error:
            print(f"Error: {error}")
            return False
        except AgeError as error:
            print(f"Error: {error}")
            return False
        except EmailError as error:
            print(f"Error: {error}")
            return False
        except ValueError:
            print(f"Error: Age supposed to be an integer")
            return False
        else:
            return True

    verified_users=[]
    for n in range(int(input("Insert number of users: ").strip())):
        try:
            user=UserData(*[data.strip() for data in input(f"Insert {n+1}'s user unique username, email and age splited with ',': ").split(",")])
            #print(f'{user.age},{user.email},{user.name}')
            if verify(user,verified_users):
                verified_users.append(user)
        except TypeError:
            print('you suppused to use two "," inserting users data')
            break


if __name__=="__main__":
    main()