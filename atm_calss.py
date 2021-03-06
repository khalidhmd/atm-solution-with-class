# One comment to test .gitignore
class ATM():
    def __init__(self, balance, bank_name, bank_note_values = [200, 100, 50, 20, 10, 5, 1]):
        self.withdrawal_list = []
        self.balance = balance
        self.bank_name = bank_name
        self.bank_note_values = bank_note_values

    def is_valid_operation(self, request):
        result = False
        if request < 0:
            print "Request value must be greater than 0"
        elif self.balance >= request:
            result = True
        elif request > self.balance:
            print "Balance is not sufficient"
        return result

    def output_msg(self, msg):
        if msg > 0:
            print "Give {}".format(msg)

    def print_welcom(self):
        print "Welecom to {}".format(self.bank_name)
        print "Current balance is: {}".format(self.balance)
        print "==========================================="

    def show_withdrawals(self):
        self.print_welcom()
        print "Mini Statement"
        for withdrawal in self.withdrawal_list:
            print withdrawal

    def withdraw(self, request):
        self.print_welcom()
        if self.is_valid_operation(request):
            self.withdrawal_list.append(request)
            for value in self.bank_note_values:
                while request >= value:
                    self.output_msg(value)
                    request -= value
                    self.balance -= value
            self.balance -= request
        print "============================="