from user import User


class UserSystem(object):

    def __init__(self):
        self.users = []

    @staticmethod
    def print_hint():
        print('=' * 20)
        print('请选择系统功能:')
        print('1. 添加用户')
        print('2. 删除用户')
        print('3. 修改用户信息')
        print('4. 查询用户信息')
        print('5. 显示所有用户信息')
        print('6. 保存学员信息')
        print('7. 退出系统')
        print('-' * 20)

    def run(self):
        self.load_users()

        while True:
            self.print_hint()
            in_str = input('请输入您需要的功能序号:')

            if in_str.isdigit():
                choice = int(in_str)
                print(choice)

                if choice == 1:
                    self.add_user()
                elif choice == 2:
                    self.del_user()
                elif choice == 3:
                    self.edit_user()
                elif choice == 4:
                    self.search_user()
                elif choice == 5:
                    self.print_all()
                elif choice == 6:
                    self.save_user()
                elif choice == 7:
                    break
                else:
                    print('输入错误请重新输入')
            else:
                print('输入错误请重新输入')

    def find_user(self, phone):
        for user in self.users:
            if user.is_this(phone):
                return user

        return False

    def add_user(self):
        phone = input('请输入手机号:')
        name = input('请输入用户名:')

        if self.find_user(phone):
            print('该手机号已存在')
        else:
            user = User(phone, name)
            self.users.append(user)
            print('添加用户成功')

    def del_user(self):
        phone = input('请输入手机号:')

        user = self.find_user(phone)
        if user:
            self.users.remove(user)
            print('删除用户成功')
        else:
            print('该用户不存在')

    def edit_user(self):
        phone = input('请输入手机号:')

        user = self.find_user(phone)
        if user:
            name = input('请输入用户名:')
            user.name = name
            print(user)
            print('修改用户成功')
        else:
            print('该用户不存在')

    def search_user(self):
        phone = input('请输入手机号:')

        user = self.find_user(phone)
        if user:
            print(user)
        else:
            print('该用户不存在')

    def save_user(self):
        f = open('users.data', 'w')
        users_list = [i.__dict__ for i in self.users]
        f.write(str(users_list))
        f.close()

    def load_users(self):
        try:
            f = open('users.data', 'r')
        except:
            f = open('users.data', 'w')
        else:
            data = f.read()
            users_list = eval(data)
            self.users = [User(i['phone'], i['name']) for i in users_list]
        finally:
            f.close()

    def print_all(self):
        for user in self.users:
            print(user)