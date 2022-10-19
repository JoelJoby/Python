#Is Mumbai more dense than Delhi

mum_popu, mum_area = 20411000, 4355
del_popu, del_area = 30291000, 1484

mum_pop_den = mum_popu/mum_area
del_pop_den = del_popu/del_area

print ('Is the population density is greater')
a = mum_pop_den == del_pop_den
print (a)