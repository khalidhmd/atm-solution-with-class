import atm_calss
baraka_bank_atm = atm_calss.ATM(5000, 'Baraka Bank')
smart_bank_atm= atm_calss.ATM(7000, 'Smart Bank')

baraka_bank_atm.withdraw(155)
baraka_bank_atm.withdraw(456)

#smart_bank_atm.withdraw(333)
baraka_bank_atm.show_withdrawals()

