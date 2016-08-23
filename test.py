# -*- coding: utf-8 -*-
# @Date    : 2016/8/20  0:04
# @Author  : 490949611@qq.com

import random

random.seed(1)
count = 0
while count<200:
	year = (random.randint(0,5)%4)+1
	harm = (random.randint(0,3)%4)+1
	if harm == 2 or harm == 3 or harm == 4:
		harm = (random.randint(0,3)%4)+1
		if harm == 2 or harm == 3 or harm == 4:
			if harm == 3 or harm == 4:
				harm = (random.randint(0,3)%4)+1
				if harm == 3 or harm == 4:
					harm = (random.randint(0,3)%4)+1
					if harm == 3 or harm == 4:
						harm = (random.randint(0,3)%4)+1
						print harm
					else:
						print harm
				else:
					print harm
			else:
				print harm
		else:
			print harm
	else:
		print harm
	# print year
	if year == 1:
		time = (random.randint(1,6)%4)+1
		know = (random.randint(0,2)%3)+1
		if know == 3:
			know = (random.randint(0,2)%3)+1
			if know == 3:
				know = (random.randint(0,2)%3)+1
				# print (random.randint(0,2)%3)+1
			else:
				pass
				# print (random.randint(0,2)%3)+1
		elif know == 2:
			know = (random.randint(1,2)%3)+1
			# print (random.randint(0,2)%3)+1
		else:
			pass
			# print (random.randint(0,2)%3)+1
		# print time
	elif year == 2:
		time =  (random.randint(0,3)%4)+1
		know = (random.randint(1,4)%3)+1
		# print (random.randint(1,4)%3)+1
		# print time
	elif year == 3:
		know = (random.randint(1,4)%3)+1
		# print (random.randint(1,4)%3)+1
		time = (random.randint(0,3)%4)+1
		if time == 1:
			time = (random.randint(0,3)%4)+1
			if time == 1:
				time = (random.randint(0,3)%4)+1
				# print time
			else:
				pass
				# print time
		elif time == 2 or time == 3:
			time = (random.randint(1,3)%4)+1
			# print time
		else:
			pass
			# print time
	else:
		time = (random.randint(0,5)%4)+1
		know = (random.randint(0,2)%3)+1
		if know == 1:
				know = (random.randint(0,2)%3)+1
				if know == 1:
					know = (random.randint(0,2)%3)+1
					if know == 1:
						know = (random.randint(0,2)%3)+1
						# print (random.randint(0,2)%3)+1
					else:
						pass
						# print (random.randint(0,2)%3)+1
				else:
					pass
					# print know
		elif know == 2:
			know = (random.randint(4,5)%3)+1
			# print (random.randint(4,5)%3)+1
		else:
			pass
			# print (random.randint(0,2)%3)+1
		# print time
	count+=1