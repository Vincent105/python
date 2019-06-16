from banks import Banks, Shilin_Banks


jamesbank = Banks('jAMES')
print("James's Bank= ", jamesbank.bank_title())
jamesbank.save_money(500)
jamesbank.get_balance()

huangbanks = Shilin_Banks('vin')
print(huangbanks.bank_title())