class Account:
    def __init__(self, acno, acname, acntbal):
        self.acc_num = acno
        self.acc_name = acname
        self.acc_bal = acntbal
    
class AccountDemo:
    def __init__(self):
        pass

    def depositAmnt(self, acc, depamnt):
        acc.acc_bal += depamnt
        return acc.acc_bal

    def withdrawAmnt(self, acc, withamnt):
        if acc.acc_bal - withamnt < 1000:
            return "No Adequate balance"
        else:
            acc.acc_bal -= withamnt
            return acc.acc_bal


if __name__ == '__main__':
    acno=int(input())
    acname= input()
    acntbal=int(input())
    depamnt=int(input())
    withamnt=int(input())
    acnt=Account(acno,acname,acntbal)
    acntdemoobj=AccountDemo()
    print(acntdemoobj.depositAmnt(acnt,depamnt))
    print(acntdemoobj.withdrawAmnt(acnt,withamnt))