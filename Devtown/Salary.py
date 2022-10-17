# the amount of money in your bank account is 1.2e5

# money recieved every year in form of salary

# decrease the salary by 30% as tax paied to the government.

# Add the salary to the bank account amt variable

# increase the amt by 4% that you recieved from the bank as intrest

# substract 1.2e5 from amt as the rent paied

# print the new value of the amt variable

amt_bank = 1.2 * 10 **6

amt_sal = 9.3 * 10 ** 5

dec_sal = amt_sal - ( 0.3 * amt_sal )

tot_bal = amt_bank + dec_sal

totinterst_bal = tot_bal + ( 0.04 * tot_bal )

after_rent = totinterst_bal - (1.2 * 10 ** 5 )

print (after_rent)