class Netflix():
    def __init__(self, msg):
        self.msg = msg

    def watch_netflix(self):
        print(self.msg)


class NetflixPayProxy():
    def __init__(self, bank_balance, netflix):
        self.bank_balance =  bank_balance
        self.netflix = netflix

    def watch_netflix(self):
        if self.bank_balance > 0:
            self.netflix.watch_netflix()
        else:
            print("Sorry, please subscribe to view.")


net = Netflix("You are watching Netflix")
duzo = NetflixPayProxy(14141, net)
duzo.watch_netflix()
malo = NetflixPayProxy(0, net)
malo.watch_netflix()