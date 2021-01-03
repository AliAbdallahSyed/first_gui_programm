import re
import time
import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


# Start

date = str(time.strftime("%d-%m-%Y"))


# To show the values in messagebox on click on (info) button


def counter():
	file = open("tobacco/{}.txt".format(date), "r", encoding="utf-8")
	line_reader = file.readlines()
	result = 0
	Total_price = 0
	for i in line_reader:
		search = re.search(r'- ([0-9]+)', i)
		if search:
			result = result + int(search.group(1))
	for x in line_reader:
		search = re.search(r'[0-9]+ ([0-9]+)', x)
		if search:
			Total_price = Total_price + int(search.group(1))
	messagebox.showinfo("Central Elgazera", """Total:{}
Total price:{}""".format(result, Total_price))
	file.close()

# To save the values in text file


def save():
	try:
		number = int(combobox_numbers_of_kinds.get())
	except ValueError:
		pass
	kinds = str(combobox_of_kinds.get())

	# Marlboro
	list_of_LM = [u"احمر  LM",u"ازرق  LM",u"ابيض  LM"]
	list_of_Marlboro = [u"احمر  Marlboro",u"ابيض  Marlboro"]
	list_of_Marlboro_medium = [u"Marlboro medium"]
	list_of_merit = [u"اصفر  Merit",u"ازرق  Merit"]
	list_of_next = [u"Next"]

	# Winston
	list_of_winston = [u"احمر  Winston",u"ازرق  Winston",u"ابيض  Winston"]
	list_of_LD = [u"احمر  LD",u"ازرق  LD"]
	list_of_camel = [u"اصفر  Camel",u"ازرق  Camel"]
	list_of_winston_blueberry = [u"توت  Winston"]

	# Roseman
	list_of_roseman = [u"ازرق  Roseman",u"احمر  Roseman",u"ابيض  Roseman"]
	list_of_roseman_red_small = [u"احمر صغير  Roseman"]
	list_of_viceroy = [u"احمر  Viceroy",u"ازرق  Viceroy"]
	list_of_pallmall = [u"احمر  Pallmall",u"ازرق  Pallmall"]
	list_of_kent = [u"Kent 1",u"kent 6",u"kent 9"]
	list_of_Dunhill = [u"احمر  Dunhill",u"ازرق  Dunhill"]
	list_of_luck_strike = [u"خفيف  lucky strike",u"تقيل lusky strike"]
	list_of_roseman_switch = [u"Roseman switch"]

	# Davidoff
	list_of_Davidoff = [u"Davidoff classic",u"Davidoff gold",u"Davidoff white",u"Davidoff slim"]
	list_of_target = [u"احمر  Target",u"ازرق  Target"]
	list_of_time = [u"احمر  Time",u"ازرق  Time",u"ابيض  Time"]

	# popular
	list_of_cleopatra = [u"كيلوبترا"]
	list_of_cleopatra_1 = [u"كيلوبترا  مقلوبة"]
	list_of_box = [u"بوكس"]
	list_of_super = [u"سوبر"]
	list_of_cleopatra_gold =[u"كيلوبترا جديدة"]

	# imported
	list_of_pine_blue = [u"ازرق  pine"]
	list_of_pine_red = [u"احمر  pine"]
	list_of_pine_change = [u"pine change"]
	list_of_Karelia_blue = [u"ازرق  Karelia"]
	list_of_Karelia_red = [u"احمر  Karelia"]
	list_of_capital = [u"capital"]
	list_of_kiss_apple = [u"تفاح kiss"]
	list_of_kiss_s = [u"فرولة kiss"]
	list_of_kiss_c = [u"شوكولاته kiss"]
	list_of_kiss_m = [u"مانجو kiss"]

	date = str(time.strftime("%d-%m-%Y"))
	try:
		file = open("tobacco/{}.txt".format(date), "r", encoding="utf-8")
	except FileNotFoundError:
		file = open("tobacco/{}.txt".format(date), "a+",encoding="utf-8")
	reader = file.readlines()
	file.close()
	file = open("tobacco/{}.txt".format(date), "a+",encoding="utf-8")
	if kinds in list_of_LM:
		save1 = 0
		file1 = open("price.txt","r")
		reader1 = file1.readlines()
		for price in reader1:
			result = re.search(r"price_of_LM:([0-9]+)",price)
			if result:
				save1 = save1 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines1 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines1,number,save1*number,kinds))
		else:
			number_of_lines1 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines1,number,save1*number,kinds))
		file1.close()
	elif kinds in list_of_Marlboro:
		save2 = 0
		file1 = open("price.txt","r")
		reader2 = file1.readlines()
		for price in reader2:
			result = re.search(r"price_of_Marlboro:([0-9]+)",price)
			if result:
				save2 = save2 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines2 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines2,number,save2*number,kinds))
		else:
			number_of_lines2 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines2,number,save2*number,kinds))
		file1.close()
	elif kinds in list_of_Marlboro_medium:
		save3 = 0
		file1 = open("price.txt","r")
		reader3 = file1.readlines()
		for price in reader3:
			result = re.search(r"price_of_Marlboro_medium:([0-9]+)",price)
			if result:
				save3 = save3 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines3 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines3,number,save3*number,kinds))
		else:
			number_of_lines3 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines3,number,save3*number,kinds))
		file1.close()
	elif kinds in list_of_next:
		save4 = 0
		file1 = open("price.txt","r")
		reader4 = file1.readlines()
		for price in reader4:
			result = re.search(r"price_of_Next:([0-9]+)",price)
			if result:
				save4 = save4 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines4 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines4,number,save4*number,kinds))
		else:
			number_of_lines4 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines4,number,save4*number,kinds))
		file1.close()
	elif kinds in list_of_merit:
		save5 = 0
		file1 = open("price.txt","r")
		reader5 = file1.readlines()
		for price in reader5:
			result = re.search(r"price_of_Merit:([0-9]+)",price)
			if result:
				save5 = save5 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines5 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines5,number,save5*number,kinds))
		else:
			number_of_lines5 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines5,number,save5*number,kinds))
		file1.close()
	elif kinds in list_of_winston:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_winston:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_LD:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_LD:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_camel:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_camel:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_winston_blueberry:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_winston_blueberry:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_roseman:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_Roseman:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_roseman_red_small:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_Roseman_small_red:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_viceroy:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_vicetory:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_pallmall:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_pallmall:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_kent:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_kent:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_Dunhill:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_Dunhill:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_luck_strike:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_luck_strike:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_roseman_switch:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_Roseman_switch:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_Davidoff:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_Davidoff:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_target:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_target:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_time:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_time:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_cleopatra:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_cleopatra:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_cleopatra_1:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_cleopatra_1:([0-9]+.\d)",price)
			if result:
				save6 = save6 + float(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_box:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_box:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_cleopatra_gold:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_cleopatra_Gold:([1-9]+.\d)",price)
			if result:
				save6 = save6 + float(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_super:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_super:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_pine_blue:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_pine_blue:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_pine_red:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_pine_red:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_pine_change:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_pine_change:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_Karelia_red:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_Karelia_red:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_Karelia_blue:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_Karelia_blue:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_capital:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_captal:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_kiss_apple:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_kiss_apple:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_kiss_s:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_kiss_s:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_kiss_c:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_kiss_c:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	elif kinds in list_of_kiss_m:
		save6 = 0
		file1 = open("price.txt","r")
		reader6 = file1.readlines()
		for price in reader6:
			result = re.search(r"price_of_kiss_m:([0-9]+)",price)
			if result:
				save6 = save6 + int(result.group(1))
		if len(reader) == 0:
			number_of_lines6 = len(reader)+1
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		else:
			number_of_lines6 = len(reader)
			file.write("\n")
			file.write(u"{}- {} {} {}".format(number_of_lines6,number,save6*number,kinds))
		file1.close()
	else:
		pass

	file = open("tobacco/{}.txt".format(date), "r",encoding="utf-8")
	line_reader = file.readlines()
	number_of_lines = 0
	Total_price = 0
	for i in line_reader:
		find = re.search(r'- ([0-9]+)', i)
		if find:
			number_of_lines = number_of_lines + int(find.group(1))
	for x in line_reader:
		search = re.search(r'[0-9]+ ([0-9]+)',x)
		if search:
			Total_price = Total_price + int(search.group(1))
	file.close()
	file = open("tobacco/{}.txt".format(date), "a+",encoding="utf-8")
	file.write("\n")
	file.write("Total:{}".format(number_of_lines))
	file.write("\n")
	file.write("Total price:{}".format(Total_price))
	file.close()


# exit function on exit (x) button


def on_closing_window():
	if messagebox.askyesno("Quit", "Are you sure that you want to exit?"):
		file = open("tobacco/{}.txt".format(date), "r",encoding="utf-8")
		line_reader = file.readlines()
		number_of_lines = 0
		Total_price = 0
		for i in line_reader:
			find = re.search(r'- ([0-9]+)', i)
			if find:
				number_of_lines = number_of_lines + int(find.group(1))
		for x in line_reader:
			search = re.search(r'[0-9]+ ([0-9]+)', x)
			if search:
				Total_price = Total_price + int(search.group(1))
		file.close()
		file = open("tobacco/{}.txt".format(date), "a+")
		file.write("\n")
		file.write("Total:{}".format(number_of_lines))
		file.write("\n")
		file.write("Total price:{}".format(Total_price))
		file.close()
		main.destroy()


def more_info_1():
	main1 = Tk()
	main1.title("More Info")
	w1 = 350
	h1 = 250
	sw1 = main1.winfo_screenwidth()
	sh1 = main1.winfo_screenheight()
	x1 = (sw1-w1)/2
	y1 = (sh1-h1)/2
	main1.geometry("%dx%d+%d+%d" % (w1,h1,x1,y1))
	main1.resizable(False,False)
	main1.configure(bg="#ff9933")
	main1.iconbitmap(default='central elgazera 2.ico')
	label_day = Label(main1,text="days").place(x=70,y=0)
	label_month = Label(main1,text="months").place(x=160,y=0)
	label_year = Label(main1,text="years").place(x=265,y=0)
	label_from = Label(main1,bg="#ff9933",text="From: ").place(x=0,y=17)
	lable_To = Label(main1,bg="#ff9933",text="To: ").place(x=0,y=68)

	# year
	combobox_year_var = StringVar()
	years = []
	combobox_year = ttk.Combobox(main1,width=12,textvariable=combobox_year_var)
	for c in range(2019,2101):
		years.append(c)
	combobox_year["values"] = years
	combobox_year.place(x=240,y=20)
	combobox_year.current(0)

	# year1
	combobox_year_var1 = StringVar()
	years1 = []
	combobox_year1 = ttk.Combobox(main1,width=12,textvariable=combobox_year_var1)
	for f in range(2019,2101):
		years1.append(f)
	combobox_year1["values"] = years1
	combobox_year1.place(x=240,y=70)
	combobox_year1.current(0)


	# month
	combobox_month_var = StringVar()
	combobox_month = ttk.Combobox(main1,width=12,textvariable=combobox_month_var)
	months = []
	for b in range(1,13):
		months.append(b)
	combobox_month["values"] = months
	combobox_month.place(x=140,y=20)
	combobox_month.current(0)

	# month1

	combobox_month_var1 = StringVar()
	combobox_month1 = ttk.Combobox(main1,width=12,textvariable=combobox_month_var1)
	months1 = []
	for e in range(1,13):
		months1.append(e)
	combobox_month1["values"] = months1
	combobox_month1.place(x=140,y=70)
	combobox_month1.current(0)

	# day
	combobox_day_var = StringVar()
	days = []
	for a in range(1,32):
		days.append(a)
	combobox_day = ttk.Combobox(main1,values=days,width=12,textvariable=combobox_day_var)
	combobox_day.place(x=40, y=20)
	combobox_day.current(0)

	# day1
	combobox_day_var1 = StringVar()
	days1 = []
	for d in range(1,32):
		days1.append(d)
	combobox_day1 = ttk.Combobox(main1,values=days1,width=12,textvariable=combobox_day_var1)
	combobox_day1.place(x=40, y=70)
	combobox_day1.current(0)


	# Ok
	def show():
		from datetime import date
		Total_price = 0
		count = 0
		try:
			days_var = int(combobox_day.get())
			days_var1 = int(combobox_day1.get())
			months_var = int(combobox_month.get())
			months_var1 = int(combobox_month1.get())
			years_var = int(combobox_year.get())
			years_var1 = int(combobox_year1.get())
		except ValueError:
			pass
		except UnboundLocalError:
			pass

		if months_var == months_var1:
			Total3 = 0
			for d in range(days_var,days_var1+1):
				if len(str(d)) < 2:
					days_str = "0{}".format(d)
					for m in range(months_var,months_var1+1):
						if len(str(m)) < 2:
							try:
								list_1 = []
								moths_str = "0{}".format(m)
								file = open("tobacco/{}-{}-{}.txt".format(days_str,moths_str,years_var),"r",encoding="utf-8")
								line_reader = file.readlines()
								for i1 in line_reader:
									list_1.append(i1)
								reuslt1 = re.search(r"Total price:([0-9]+)",list_1[-1])
								Total3 = Total3 + int(reuslt1.group(1))
							except FileNotFoundError:
								pass

						else:
							try:
								list_2 = []
								file = open("tobacco/{}-{}-{}.txt".format(days_str,m,years_var),"r",encoding="utf-8")
								line_reader = file.readlines()
								for i2 in line_reader:
									list_2.append(i2)
								result2 = re.search(r"Total price:([0-9]+)",list_2[-1])
								Total3 = Total3 + int(result2.group(1))
							except FileNotFoundError:
								pass
				else:
					for mo in range(months_var,months_var1+1):
						if len(str(mo)) < 2:
							try:
								list_3 = []
								mo_str = "0{}".format(mo)
								file = open("tobacco/{}-{}-{}.txt".format(d,mo_str,years_var),"r",encoding="utf-8")
								line_reader = file.readlines()
								for i3 in line_reader:
									list_3.append(i3)
								result3 = re.search(r"Total price:([0-9]+)",list_3[-1])
								if result3:
									Total3 = Total3 + int(result3.group(1))
							except FileNotFoundError:
								pass
						else:
							try:
								list_4 = []
								file = open("tobacco/{}-{}-{}.txt".format(d,mo_str,years_var),"r",encoding="utf-8")
								line_reader = file.readlines()
								for i4 in line_reader:
									list_4.append(i4)
								result4 = re.search(r"Total price:([0-9]+)",list_4[-1])
								if result4:
									Total3 = Total4 + int(result4.group(1))
							except FileNotFoundError:
								pass
			messagebox.showinfo("Total","Total:{}".format(Total3))
		else:
			Total1 = 0
			Total2 = 0
			Total = 0
			# First range
			for x in range(days_var,32):
				if len(str(x)) < 2:
					x_str =  "0{}".format(x)
					if len(str(months_var)) < 2:
						months_var_str = "0{}".format(months_var)
						try:
							file1 = open("tobacco/{}-{}-{}.txt".format(x_str,months_var_str,years_var),"r",encoding="utf-8")
							line_reader = file1.readlines()
							for i in line_reader:
								result1 = re.search(r"Total price:([0-9]+)",i)
							Total1 = Total1 + int(result1.group(1))
						except FileNotFoundError:
							pass
					else:
						try:
							file2 = open("tobacco/{}-{}-{}.txt".format(x_str,months_var,years_var),"r", encoding="utf-8")
							line_reader2 = file2.readlines()
							for i1 in line_reader2:
								result2 = re.search(r"Total price:([0-9]+)",i1)
							Total1 = Total1 + int(result2.group(1))
						except FileNotFoundError:
							pass
				else:
					if len(str(months_var)) < 2:
						months_var_str_2 = "0{}".format(months_var)
						try:
							file3 = open("tobacco/{}-{}-{}.txt".format(days_var,months_var_str_2,years_var),"r", encoding="utf-8")
							line_reader3 = file3.readlines()
							for i3 in line_reader3:
								result3 = re.search(r"Total price:([0-9]+)",i3)
							Total1 = Total1 + int(result3.group(1))
						except FileNotFoundError:
							pass
					else:
						try:
							file4 = open("tobacco/{}-{}-{}.txt".format(days_var,months_var,years_var),"r",encoding="utf-8")
							line_reader4 = file4.readlines()
							for i4 in line_reader4:
								result4 = re.search(r"Total price:([0-9]+)",i4)
							Total1 = Total1 + int(result4.group(1))
						except FileNotFoundError:
							pass
			# second range
			for x1 in range(1,days_var1+1):
				if len(str(x1)) < 2:
					x_str =  "0{}".format(x1)
					if len(str(months_var1)) < 2:
						months_var_str = "0{}".format(months_var1)
						try:
							file5 = open("tobacco/{}-{}-{}.txt".format(x_str,months_var_str,years_var1),"r",encoding="utf-8")
							line_reader5 = file5.readlines()
							for i5 in line_reader5:
								result5 = re.search(r"Total price:([0-9]+)",i5)
							Total2 = Total2 + int(result5.group(1))
						except FileNotFoundError:
							pass
					else:
						try:
							file6 = open("tobacco/{}-{}-{}.txt".format(x_str,months_var1,years_var1),"r",encoding="utf-8")
							line_reader6 = file6.readlines()
							for i6 in line_reader6:
								result6 = re.search(r"Total price:([0-9]+)",i6)
							Total2 = Total2 + int(result6.group(1))
						except FileNotFoundError:
							pass
				else:
					if len(str(months_var1)) < 2:
						months_var_str_2 = "0{}".format(months_var1)
						try:
							file7 = open("tobacco/{}-{}-{}.txt".format(days_var1,months_var_str_2,years_var1),"r",encoding="utf-8")
							line_reader7 = file7.readlines()
							for i7 in line_reader7:
								result7 = re.search(r"Total price:([0-9]+)",i7)
							Total2 = Total2 + int(result7.group(1))
						except FileNotFoundError:
							pass
					else:
						try:
							file8 = open("tobacco/{}-{}-{}.txt".format(days_var1,months_var1,years_var1),"r",encoding="utf-8")
							line_reader8 = file8.readlines()
							for i8 in line_reader8:
								result8 = re.search(r"Total price:([0-9]+)",i8)
							Total2 = Total2 + int(result8.group(1))
						except FileNotFoundError:
							pass
			Total = Total1 + Total2
			messagebox.showinfo("Total","Total:{}".format(Total))


	Ok = Button(main1,text="Ok",bg="#80bfff",command=show).place(x=320,y=220)
	main1.mainloop()

main = Tk()
w = 550
h = 600
sw = main.winfo_screenwidth()
sh = main.winfo_screenheight()
x = (sw-w)/2
y = (sh-h)/2
main.geometry("%dx%d+%d+%d" % (w,h,x,y))
main.resizable(False,False)
main.title("Central Elgazera")
main.configure(bg="#ff9933")
main.iconbitmap(default='central elgazera 2.ico')



lab = Label(main, text=u"سنترال الجزيرة", font=("italic", 30)).pack()

kinds_label = Label(main, text="الاصناف",font=("italic", 13)).place(x=35,y=60)
number_of_kinds_label = Label(main, text="عدد الاصناف",font=("italic", 13)).place(x=210, y=60)

# start conbobox for number of kinds

comboboxvar_number_of_kinds = StringVar()
combobox_numbers_of_kinds = ttk.Combobox(main, width=17, textvariable=comboboxvar_number_of_kinds,state="readonly",font=("italic", 13))
number_of_kinds = []
for i in range(1,51):
	number_of_kinds.append(i)
combobox_numbers_of_kinds['values'] = number_of_kinds
combobox_numbers_of_kinds.place(x=180, y=80)
combobox_numbers_of_kinds.current(0)

# end combobox for number of kinds

# start combobox for kinds

comboboxvar_of_kinds = StringVar()
combobox_of_kinds = ttk.Combobox(main, width=17, textvariable=comboboxvar_of_kinds,state="readonly",font=("italic", 13))
combobox_of_kinds["values"] = (u"احمر  LM",u"ازرق  LM",u"ابيض  LM",u"احمر  Marlboro",u"ابيض  Marlboro", u"Marlboro medium",u"اصفر  Merit",u"ازرق  Merit",u"Next",u"كيلوبترا",u"بوكس",u"سوبر",u"كيلوبترا جديدة",u"كيلوبترا  مقلوبة",u"احمر  Karelia",u"ازرق  Karelia",u"ازرق  pine",u"احمر  pine",u"pine change",u"Davidoff classic",u"Davidoff gold",u"Davidoff white",u"Davidoff slim",u"احمر  Target", u"ازرق  Target", u"احمر  Time", u"ازرق  Time", u"ابيض  Time", u"احمر  Winston",u"ازرق  Winston",u"ابيض  Winston",u"توت  Winston",u"اصفر  Camel",u"ازرق  Camel",u"احمر  LD",u"ازرق  LD",u"ازرق  Roseman",u"احمر  Roseman",u"ابيض  Roseman",u"احمر صغير  Roseman",u"Roseman switch",u"Kent 1",u"kent 6",u"kent 9",u"احمر  Viceroy",u"ازرق  Viceroy",u"احمر  Pallmall",u"ازرق  Pallmall",u"احمر  Dunhill",u"ازرق  Dunhill",u"خفيف  lucky strike",u"تقيل lusky strike",u"capital",u"تفاح kiss",u"فرولة kiss",u"شوكولاته kiss",u"مانجو kiss")
combobox_of_kinds.place(x=0, y=80)
combobox_of_kinds.current(0)

# end combobox for kinds

Counter = Button(main, text="معلومات", bg="#3399ff", command=counter,font=("italic", 13)).place(x=430, y=75)

save = Button(main, text="حفظ", bg="#d9d9d9", command=save,font=("italic", 13)).place(x=375, y=75)


# mobile accessories
accessories_var = StringVar()
price_accessories = StringVar()
label_mobile = Label(main,text="Mobile Accessories",font=("italic", 13)).place(x=0,y=450)
label_kinds = Label(main,text="الصنف",font=("italic", 13)).place(x=110,y=480)
label_price = Label(main,text="القيمة",font=("italic", 13)).place(x=240,y=480)
entry_accessories = Entry(main,textvariable=accessories_var,width=25,font=("italic", 13)).place(x=0,y=500)
entry_price_accessories = Entry(main,textvariable=price_accessories,width=5,font=("italic", 13)).place(x=235,y=500)


def save2():
	try:
		accessories_price = int(price_accessories.get())
		kinds_accessories = accessories_var.get()
		file_a = open("accessories/{}-accessories.txt".format(date),"a+",encoding="utf-8")
		file_a.write("\n")
		file_a.write("-{} {}".format(accessories_price,kinds_accessories))
		file_a.close()

	except ValueError:
		messagebox.showerror("Error","يجب ادخال ارقام فقط")


B_save_accessories = Button(main, text="حفظ", command=save2, bg="#d9d9d9",font=("italic", 13)).place(x=290,y=495)


def info2():
	try:
		Total5 = 0
		file_a_i = open("accessories/{}-accessories.txt".format(date),"r")
		line_reader_a = file_a_i.readlines()
		for areader in line_reader_a:
			aresult = re.search(r"-([0-9]+) ",areader)
			if aresult:
				Total5 = Total5 + int(aresult.group(1))
		messagebox.showinfo("Total","Total:{}".format(Total5))
	except FileNotFoundError:
		pass

info_numbers = Button(main,text="معلومات",command=info2,bg="#3399ff",font=("italic", 13)).place(x=345,y=495)


def back_back():
	accessories_list = []
	file_list = open("accessories/{}-accessories.txt".format(date),"r",encoding="utf-8")
	line_file_list = file_list.readlines()
	for flreader in line_file_list:
		accessories_list.append(flreader)
	file_list.close()
	main4 = Tk()
	w5 = 300
	h5 = 250
	sw5 = main4.winfo_screenwidth()
	sh5 = main4.winfo_screenheight()
	x5 = (sw5-w5)/2
	y5 = (sh5-h5)/2
	main4.geometry("%dx%d+%d+%d" % (w5,h5,x5,y5))
	main4.resizable(False,False)
	main4.title("Central Elgazera")
	main4.configure(bg="#ff9933")
	main4.iconbitmap(default='central elgazera 2.ico')
	l1 = Listbox(main4,selectmode=SINGLE,font=("italic", 13))
	for items in range(len(accessories_list)):
		l1.insert(items,accessories_list[items])
	l1.place(x=0,y=0)

	def back_1():
		ac = l1.curselection()
		accessories_list.remove(l1.get(ac))
		l1.delete(ac)
		file_ac = open("accessories/{}-accessories.txt".format(date),"w",encoding="utf-8")
		for remove_item in range(len(accessories_list)):
			file_ac.write(accessories_list[remove_item])
		file_ac.close()

	back_Button = Button(main4,text="حذف",command=back_1,font=("italic", 13)).place(x=200,y=140)

	main4.mainloop()

back = Button(main,text="تراجع",command=back_back,font=("italic", 13)).place(x=415,y=495)

#numbers



numbers = StringVar()
price_numbers = StringVar()
label_numbers = Label(main,text="تحويل رصيد",font=("italic", 13)).place(x=0,y=150)
label_mobile_number = Label(main,text="رقم الموبيل",font=("italic", 13)).place(x=80,y=180)
label_price = Label(main,text="القيمة",font=("italic", 13)).place(x=240,y=180)
place_charge = Label(main,text="المكان",font=("italic", 13)).place(x=310,y=180)
entry_number = Entry(main,textvariable=numbers,width=25,font=("italic", 13)).place(x=0,y=200)
entry_price = Entry(main,textvariable=price_numbers,width=5,font=("italic", 13)).place(x=235,y=200)


def info1():
	try:
		Total4 = 0
		file_n_p1 = open("numbers/{}-numbers.txt".format(date),"r",encoding="utf-8")
		line_reader_1 = file_n_p1.readlines()
		for ireader in line_reader_1:
			iresult = re.search(r"-([0-9]+|[0-9]+.[0-9]+) ",ireader)
			if iresult:
				Total4 = Total4 + float(iresult.group(1))
		messagebox.showinfo("Total","Total:{}".format(Total4))
	except FileNotFoundError:
		pass


info_numbers = Button(main, text="معلومات", command=info1, bg="#3399ff", font=("italic", 13)).place(x=455,y=195)

place_number_combobox_var = StringVar()
place_number_combobox = ttk.Combobox(main, width=8, textvariable=place_number_combobox_var, state="readonly",font=("italic", 13))
place_number_combobox["values"] = ["فوري","مصاري","سداد"]
place_number_combobox.place(x=290, y=200)
place_number_combobox.current(0)

def save1():
	try:
		now = datetime.datetime.now()
		now_1 = now.strftime("%I:%M:%S %p")
		num = int(numbers.get())
		price_1 = float(price_numbers.get())
		place_charge_var = place_number_combobox.get()
		if messagebox.askyesno("operation", "هل تمت العملية بنجاح"):
			file_n_p = open("numbers/{}-numbers.txt".format(date), "a+", encoding="utf-8")
			file_n_p.write("\n")
			file_n_p.write("-{} number:{} place:{} state:عملية ناجحة  time:{}".format(price_1,num,place_charge_var,now_1))
			file_n_p.close()

		Total11 = 0
		file_n_p = open("numbers/{}-numbers.txt".format(date),"r",encoding="utf-8")
		line_reader_1 = file_n_p.readlines()
		for ireader in line_reader_1:
			iresult = re.search(r"-([0-9]+.[0-9]+) ",ireader)
			if iresult:
				Total11 = Total11 + float(iresult.group(1))
		file_n_p.close()
		file_n_p = open("numbers/{}-numbers.txt".format(date),"a+",encoding="utf-8")
		file_n_p.write("\n")
		file_n_p.write("Total price:{}".format(Total11))
		file_n_p.close()
	except ValueError:
		messagebox.showerror("Error","يجب ادخال ارقام فقط")


B_save_numbers = Button(main, text="حفظ", command=save1, bg="#d9d9d9", font=("italic", 13)).place(x=400, y=195)


# more


def more_2():
	main5 = Tk()
	w5 = 205
	h5 = 105
	sw5 = main5.winfo_screenwidth()
	sh5 = main5.winfo_screenheight()
	x5 = (sw5-w5)/2
	y5 = (sh5-h5)/2
	main5.geometry("%dx%d+%d+%d" % (w5,h5,x5,y5))
	main5.resizable(False,False)
	main5.configure(bg="#ff9933")
	main5.iconbitmap(default='central elgazera 2.ico')
	main5.title("Central Elgazera")
	more_info = Button(main5,text="جرد السجائر" ,bg="#ffffff",command=more_info_1).pack()

	# more inforemation about tobaco
	def more_information():
		import re
		main26 = Tk()
		w9 = 600
		h9 = 750
		sw9 = main.winfo_screenwidth()
		sh9 = main.winfo_screenheight()
		x9 = (sw9-w9)/2
		y9 = (sh9-h9)/2
		main26.geometry("%dx%d+%d+%d" % (w9, h9, x9, y9))
		main26.resizable(False, False)
		main26.iconbitmap(default='central elgazera 2.ico')
		main26.title("Central Elgazera")

		paned1 = PanedWindow(main26, orient=VERTICAL, bg="#ff9933")
		paned2 = PanedWindow(main26, orient=VERTICAL, bg="#0099ff")
		paned2.config(height=550)
		paned1.pack(fill=BOTH, expand=1)
		paned2.pack(fill=BOTH, expand=1)

		Lab_space = Label(paned1, text="   ", bg="#ff9933")
		Lab_space1 = Label(paned1, text="   ", bg="#ff9933")
		Label_from = Label(paned1, text="From:", font=("italic", 13))
		Label_to = Label(paned1, text="To:", font=("italic", 13))
		Label_days = Label(paned1, text="days", font=("italic", 13))
		Label_months = Label(paned1, text="months", font=("italic", 13))
		Lable_years = Label(paned1, text="years", font=("italic", 13))


		# days
		days2 = []
		for a in range(1, 32):
			c = "{}".format(a)
			if len(c) < 2:
				c = "0{}".format(a)
				days2.append(c)
			else:
				days2.append(a)
		combobox_day2 = ttk.Combobox(paned1, values=days2, width=12, font=("italic", 13), state="readonly")

		combobox_day2.current(0)

		days3 = []
		for a in range(1, 32):
			c = "{}".format(a)
			if len(c) < 2:
				c = "0{}".format(a)
				days3.append(c)
			else:
				days3.append(a)
		combobox_day2_ = ttk.Combobox(paned1, values=days3, width=12, font=("italic", 13), state="readonly")

		combobox_day2_.current(0)


		# months
		month2 = []
		for a in range(1, 13):
			c = "{}".format(a)
			if len(c) < 2:
				c = "0{}".format(a)
				month2.append(c)
			else:
				month2.append(a)
		combobox_month2 = ttk.Combobox(paned1, values=month2, width=12, font=("italic", 13), state="readonly")

		combobox_month2.current(0)

		month_2 = []
		for a in range(1, 13):
			c = "{}".format(a)
			if len(c) < 2:
				c = "0{}".format(a)
				month_2.append(c)
			else:
				month_2.append(a)
		combobox_month2_ = ttk.Combobox(paned1, values=month_2, width=12, font=("italic", 13), state="readonly")

		combobox_month2_.current(0)

		# years
		year2 = []
		for a in range(2019, 2050):
			c = "{}".format(a)
			if len(c) < 2:
				c = "0{}".format(a)
				year2.append(c)
			else:
				year2.append(a)
		combobox_year2 = ttk.Combobox(paned1, values=year2, width=12, font=("italic", 13), state="readonly")

		combobox_year2.current(0)

		year_2 = []
		for a in range(2019, 2050):
			c = "{}".format(a)
			if len(c) < 2:
				c = "0{}".format(a)
				year_2.append(c)
			else:
				year_2.append(a)
		combobox_year2_ = ttk.Combobox(paned1, values=year_2, width=12, font=("italic", 13), state="readonly")

		combobox_year2_.current(0)

		# Labels
		Lm_Label_red = Label(paned2, text="احمر Lm", font=("italic", 13))
		Lm_var_red = StringVar()
		Label1 = Label(paned2, text="0", font=("italic", 13))

		lm_var_blue = StringVar()
		Lm_Label_blue = Label(paned2,text="ازرق Lm", font=("italic", 13))
		Label2 = Label(paned2, text="0", font=("italic", 13))


		Lm_Label_white = Label(paned2, text="ابيض Lm", font=("italic", 13))
		Lm_var_white = StringVar()
		Label3 = Label(paned2, text="0", font=("italic", 13))


		Label_Marl_red = Label(paned2, text="احمر  Marlboro", font=("italic", 13))
		Label_var_Marl_red = StringVar()
		label4 = Label(paned2, text="0", font=("italic", 13))


		Label_Marl_Gold = Label(paned2, text="ابيض  Marlboro", font=("italic", 13))
		var_Marl_Gold = StringVar()
		Label5 = Label(paned2, text="0", font=("italic", 13))


		Mar_md = Label(paned2, font=("italic",13), text="Marlboro medium")
		var_mar_md = StringVar()
		Label6 = Label(paned2, text="0", font=("italic", 13))


		Mert_Label = Label(paned2, text="اصفر  Merit", font=("italic", 13))
		mert_var = StringVar()
		Label7 = Label(paned2, text="0", font=("italic", 13))


		Mert_blue = Label(paned2, text="ازرق  Merit", font=("italic", 13))
		mert_blue_var = StringVar()
		Label8 = Label(paned2, text="0", font=("italic", 13))


		Next = Label(paned2, text="Next", font=("italic", 13))
		next_var = StringVar()
		Label9 = Label(paned2, text="0", font=("italic", 13))


		ke = Label(paned2, text="كيلوبترا", font=("italic", 13))
		ke_var = StringVar()
		Label10 = Label(paned2, text="0", font=("italic", 13))


		box = Label(paned2, text="بوكس",  font=("italic", 13))
		box_var = StringVar()
		Label11 = Label(paned2, text="0",font=("italic", 13))


		super_ = Label(paned2, text="سوبر", font=("italic", 13))
		super_var = StringVar()
		label12 = Label(paned2, text="0", font=("italic", 13))


		new_ke = Label(paned2, text="كيلوبترا جديدة", font=("italic", 13))
		new_ke_var = StringVar()
		label13 = Label(paned2, text="0", font=("italic", 13))


		other_ke = Label(paned2, text="كيلوبترا  مقلوبة", font=("italic", 13))
		other_ke_var = StringVar()
		label14 = Label(paned2, text="0", font=("italic", 13))


		ka_red = Label(paned2, text="احمر  Karelia", font=("italic", 13))
		ka_red_var = StringVar()
		Label15 = Label(paned2, text="0", font=("italic", 13))


		Ka_blue = Label(paned2, text=u"ازرق  Karelia", font=("italic", 13))
		ka_blue_var = StringVar()
		Label16 = Label(paned2, text="0", font=("italic", 13))


		pine_blue = Label(paned2, text=u"ازرق  pine", font=("italic", 13))
		pine_blue_var = StringVar()
		Label17 = Label(paned2, text="0",font=("italic", 13))


		pine_red = Label(paned2, text="احمر  pine", font=("italic", 13))
		pine_red_var = StringVar()
		Label18 = Label(paned2, text="0", font=("italic", 13))


		pine_change = Label(paned2, text="pine change", font=("italic", 13))
		pine_change_var = StringVar()
		Label19 = Label(paned2, text="0", font=("italic", 13))


		dv_c = Label(paned2, text="Davidoff classic", font=("italic", 13))
		dv_c_var = StringVar()
		Label20 = Label(paned2, text="0",  font=("italic", 13))


		dv_g = Label(paned2, text="Davidoff gold", font=("italic", 13))
		dv_g_var = StringVar()
		Label21 = Label(paned2, text="0", font=("italic", 13))


		dv_w = Label(paned2, text="Davidoff white", font=("italic", 13))
		dv_w_var = StringVar()
		Label22 = Label(paned2, text="0", font=("italic", 13))


		dv_s = Label(paned2, text="Davidoff slim", font=("italic", 13))
		dv_s_var = StringVar()
		Label23 = Label(paned2, text="0", font=("italic", 13))


		target_red = Label(paned2, text="احمر  Target", font=("italic", 13))
		target_red_var = StringVar()
		Label24 = Label(paned2, text="0", font=("italic", 13))


		target_blue = Label(paned2, text="ازرق  Target", font=("italic", 13))
		target_blue_var = StringVar()
		Label25 = Label(paned2, text="0", font=("italic", 13))


		time_red = Label(paned2, text="احمر  Time", font=("italic", 13))
		time_red_var = StringVar()
		Label26 = Label(paned2, text="0", font=("italic", 13))


		time_blue = Label(paned2, text="ازرق  Time", font=("italic", 13))
		time_blue_var = StringVar()
		Label27 = Label(paned2, text="0", font=("italic", 13))


		time_white = Label(paned2, text="ابيض  Time", font=("italic", 13))
		time_white_var = StringVar()
		Label28 = Label(paned2, text="0", font=("italic", 13))


		winston_red = Label(paned2, text="احمر  Winston", font=("italic", 13))
		winston_red_var = StringVar()
		Label29 = Label(paned2, text="0", font=("italic", 13))


		winston_blue = Label(paned2, text="ازرق  Winston", font=("italic", 13))
		winston_blue_var = StringVar()
		Label30 = Label(paned2, text="0", font=("italic", 13))


		winston_white = Label(paned2, text="ابيض  Winston", font=("italic", 13))
		winston_white_var = StringVar()
		Label31 = Label(paned2, text="0", font=("italic", 13))


		winston_t = Label(paned2, text="توت  Winston", font=("italic", 13))
		winston_t_var = StringVar()
		Label32 = Label(paned2, text="0", font=("italic", 13))


		camel_y = Label(paned2, text="اصفر  Camel", font=("italic", 13))
		camel_y_var = StringVar()
		Label33 = Label(paned2, text="0", font=("italic", 13))


		camel_b = Label(paned2, text="ازرق  Camel", font=("italic", 13))
		camel_b_var = StringVar()
		Label34 = Label(paned2, text="0", font=("italic", 13))


		ld_r = Label(paned2, text="احمر  LD", font=("italic", 13))
		ld_rv = StringVar()
		Label35 = Label(paned2, text="0", font=("italic", 13))


		ld_b = Label(paned2, text="ازرق  LD", font=("italic", 13))
		ld_bv = StringVar()
		Label36 = Label(paned2, text="0", font=("italic", 13))


		ros_b = Label(paned2, text="ازرق  Roseman", font=("italic", 13))
		ros_b_var = StringVar()
		Label37 = Label(paned2, text="0", font=("italic", 13))


		ros_r = Label(paned2, text="احمر  Roseman", font=("italic", 13))
		ros_r_var = StringVar()
		Label38 = Label(paned2, text="0", font=("italic", 13))


		ros_w = Label(paned2, text="ابيض  Roseman", font=("italic", 13))
		ros_w_var = StringVar()
		Label39 = Label(paned2, text="0", font=("italic", 13))


		ros_rs = Label(paned2, text="احمر صغير  Roseman", font=("italic", 13))
		ros_rs_var = StringVar()
		Label40 = Label(paned2, text="0",textvariable=ros_rs_var, font=("italic", 13))


		ros_c = Label(paned2, text="Roseman switch", font=("italic", 13))
		ros_c_var = StringVar()
		Label41 = Label(paned2, text="0", font=("italic", 13))


		kent1 = Label(paned2, text="Kent 1", font=("italic", 13))
		kent1_var = StringVar()
		LabeL42 = Label(paned2, text="0", font=("italic", 13))


		kent6 = Label(paned2, text="kent 6", font=("italic", 13))
		kent6_var = StringVar()
		Label43 = Label(paned2, text="0", font=("italic", 13))


		kent9 = Label(paned2, text="kent 9", font=("italic", 13))
		kent9_var = StringVar()
		Label44 = Label(paned2, text="0", font=("italic", 13))


		vc_r = Label(paned2, text="احمر  Viceroy", font=("italic", 13))
		vc_r_var = StringVar()
		Label45 = Label(paned2, text="0", font=("italic", 13))


		vc_b = Label(paned2, text="ازرق  Viceroy", font=("italic", 13))
		vc_b_var = StringVar()
		Label46 = Label(paned2, text="0", font=("italic", 13))


		pal_r = Label(paned2, text="احمر  Pallmall", font=("italic", 13))
		pal_r_var = StringVar()
		Label47 = Label(paned2, text="0", font=("italic", 13))


		pal_b = Label(paned2, text="ازرق  Pallmall", font=("italic", 13))
		pal_b_var = StringVar()
		Label48 = Label(paned2, text="0", font=("italic", 13))


		du_r = Label(paned2, text="احمر  Dunhill", font=("italic", 13))
		du_r_var = StringVar()
		Label49 = Label(paned2, text="0", font=("italic", 13))


		du_b = Label(paned2, text="ازرق  Dunhill", font=("italic", 13))
		du_b_var = StringVar()
		Label50 = Label(paned2, text="0", font=("italic", 13))


		luc_l = Label(paned2, text="خفيف  lucky strike", font=("italic", 13))
		luc_l_var = StringVar()
		Label51 = Label(paned2, text="0", font=("italic", 13))


		luc_h = Label(paned2, text="تقيل lusky strike", font=("italic", 13))
		luc_h_var = StringVar()
		Label52 = Label(paned2, text="0", font=("italic", 13))


		kiss_a = Label(paned2, text="تفاح kiss", font=("italic", 13))
		kiss_a_var = StringVar()
		Label53 = Label(paned2, text="0", font=("italic", 13))


		kiss_s = Label(paned2, text="فرولة kiss", font=("italic", 13))
		kiss_s_var = StringVar()
		Label54 = Label(paned2, text="0", font=("italic", 13))


		kiss_k = Label(paned2, text="شوكولاته kiss", font=("italic", 13))
		kiss_k_var = StringVar()
		Label55 = Label(paned2, text="0", font=("italic", 13))


		kiss_m = Label(paned2, text="مانجو kiss", font=("italic", 13))
		kiss_m_var = StringVar()
		Label56 = Label(paned2, text="0", font=("italic", 13))


		def ok_():
			lm_red = 0
			lm_blue = 0
			lm_white = 0
			marl_red = 0
			marl_white = 0
			marl_m = 0
			mert_y = 0
			mert_b = 0
			Next_ = 0
			K_ = 0
			box_ = 0
			super_1 = 0
			k_d = 0
			k_new = 0
			kr_red = 0
			kr_blue = 0
			p_b = 0
			p_r = 0
			p_c = 0
			d_c = 0
			d_g = 0
			d_w = 0
			d_s = 0
			t_r = 0
			t_b = 0
			ti_r = 0
			ti_b = 0
			ti_w = 0
			ws_r = 0
			ws_b = 0
			ws_w = 0
			ws_u = 0
			ca_y = 0
			ca_b = 0
			LD_red = 0
			LD_blue = 0
			rs_blue = 0
			rs_red = 0
			rs_white = 0
			rs_red_small = 0
			rs_switch = 0
			kn1 = 0
			kn6 = 0
			kn9 = 0
			vec_red = 0
			vec_blue = 0
			pl_red = 0
			pl_blue = 0
			dun_r = 0
			dun_b = 0
			luck_1 = 0
			luck_2 = 0

			try:
				days_var_ = int(combobox_day2.get())
				days_var1_ = int(combobox_day2_.get())
				months_var_ = int(combobox_month2.get())
				months_var1_ = int(combobox_month2_.get())
				years_var_ = int(combobox_year2.get())
				years_var1_ = int(combobox_year2_.get())
			except ValueError:
				pass
			except UnboundLocalError:
				pass

			if months_var1_ == months_var_ :
				for days in range(int(days_var_), int(days_var1_)+1):
					if len(str(days)) < 2:
						len_days = "0{}".format(days)
						file_t = open("tobacco/{}-{}-{}.txt".format(len_days, combobox_month2.get(), years_var1_), "r", encoding="utf-8")
						file_t_reader = file_t.readlines()
						for file_t_reader_ in file_t_reader:
							resutl_lmRed = re.search(r"- ([0-9]+) [0-9]+ احمر  LM", file_t_reader_)
							result_lmBlue = re.search(r"- ([0-9]+) [0-9]+ ازرق  LM", file_t_reader_)
							result_lmWhite = re.search(r"- ([0-9]+) [0-9]+ ابيض  LM", file_t_reader_)
							result_ma_red = re.search(r"- ([0-9]+) [0-9]+ احمر  Marlboro", file_t_reader_)
							result_ma_white = re.search(r"- ([0-9]+) [0-9]+ ابيض  Marlboro", file_t_reader_)
							result_ma_m = re.search(r"- ([0-9]+) [0-9]+ Marlboro medium", file_t_reader_)
							result_mer_y = re.search(r"- ([0-9]+) [0-9]+ اصفر  Merit", file_t_reader_)
							result_mert_b = re.search(r"- ([0-9]+) [0-9]+ ازرق  Merit", file_t_reader_)
							resutl_Next = re.search(r"- ([0-9]+) [0-9]+ Next", file_t_reader_)
							resutl_k = re.search(r"- ([0-9]+) [0-9]+ كيلوبترا", file_t_reader_)
							result_box = re.search(r"- ([0-9]+) [0-9]+ بوكس", file_t_reader_)
							result_super = re.search(r"- ([0-9]+) [0-9]+ سوبر", file_t_reader_)
							result_k_d = re.search(r"- ([0-9]+) [0-9]+.[0-9]+ كيلوبترا  مقلوبة", file_t_reader_)
							result_k_new = re.search(r"- ([0-9]+) [0-9]+.[0-9]+ كيلوبترا جديدة", file_t_reader_)
							result_kr_red = re.search(r"- ([0-9]+) [0-9]+ احمر  Karelia", file_t_reader_)
							resutl_kr_blue = re.search(r"- ([0-9]+) [0-9]+ ازرق  Karelia", file_t_reader_)
							result_p_b = re.search(r'- ([0-9]+) [0-9]+ ازرق  pine', file_t_reader_)
							result_p_r = re.search(r"- ([0-9]+) [0-9]+ احمر  pine", file_t_reader_)
							result_p_c = re.search(r"- ([0-9]+) [0-9]+ pine change", file_t_reader_)
							result_d_c = re.search(r"- ([0-9]+) [0-9]+ Davidoff classic", file_t_reader_)
							result_d_g = re.search(r"- ([0-9]+) [0-9]+ Davidoff gold", file_t_reader_)
							result_d_w = re.search(r"- ([0-9]+) [0-9]+ Davidoff white", file_t_reader_)
							result_d_s = re.search(r"- ([0-9]+) [0-9]+ Davidoff slim",file_t_reader_)
							result_t_r = re.search(r"- ([0-9]+) [0-9]+ احمر  Target", file_t_reader_)
							result_t_b = re.search(r"- ([0-9]+) [0-9]+ ازرق  Target", file_t_reader_)
							result_ti_r = re.search(r"- ([0-9]+) [0-9]+ احمر  Time", file_t_reader_)
							result_ti_b = re.search(r"- ([0-9]+) [0-9]+ ازرق  Time", file_t_reader_)
							result_ti_w = re.search(r"- ([0-9]+) [0-9]+ ابيض  Time", file_t_reader_)
							result_ws_r = re.search(r"- ([0-9]+) [0-9]+ احمر  Winston", file_t_reader_)
							result_ws_b = re.search(r"- ([0-9]+) [0-9]+ ازرق  Winston", file_t_reader_)
							result_ws_w = re.search(r"- ([0-9]+) [0-9]+ ابيض  Winston", file_t_reader_)
							result_ws_u = re.search(r"- ([0-9]+) [0-9]+ توت  Winston", file_t_reader_)
							result_ca_y = re.search(r"- ([0-9]+) [0-9]+ اصفر  Camel", file_t_reader_)
							result_ca_b = re.search(r"- ([0-9]+) [0-9]+ ازرق  Camel", file_t_reader_)
							result_LD_red = re.search(r"- ([0-9]+) [0-9]+ احمر  LD", file_t_reader_)
							result_LD_blue = re.search(r"- ([0-9]+) [0-9]+ ازرق  LD", file_t_reader_)
							result_rs_blue = re.search(r"- ([0-9]+) [0-9]+ ازرق  Roseman", file_t_reader_)
							result_rs_red = re.search(r"- ([0-9]+) [0-9]+ احمر  Roseman", file_t_reader_)
							result_rs_red_s = re.search(r"- ([0-9]+) [0-9]+ احمر صغير  Roseman", file_t_reader_)
							result_rs_w = re.search(r"- ([0-9]+) [0-9]+ ابيض  Roseman", file_t_reader_)
							result_rs_c = re.search(r"- ([0-9]+) [0-9]+ Roseman switch", file_t_reader_)
							result_kn1 = re.search(r"- ([0-9]+) [0-9]+ Kent 1", file_t_reader_)
							result_kn6 = re.search(r"- ([0-9]+) [0-9]+ kent 6", file_t_reader_)
							result_kn9 = re.search(r"- ([0-9]+) [0-9]+ kent 9", file_t_reader_)
							result_vec_r = re.search(r"- ([0-9]+) [0-9]+ احمر  Viceroy", file_t_reader_)
							result_vec_b = re.search(r"- ([0-9]+) [0-9]+ ازرق  Viceroy", file_t_reader_)
							result_pl_red = re.search(r"- ([0-9]+) [0-9]+ احمر  Pallmall", file_t_reader_)
							result_pl_blue = re.search(r"- ([0-9]+) [0-9]+ ازرق  Pallmall", file_t_reader_)
							result_dun_r = re.search(r"- ([0-9]+) [0-9]+ احمر  Dunhill", file_t_reader_)
							result_dun_b = re.search(r"- ([0-9]+) [0-9]+ ازرق  Dunhill", file_t_reader_)
							result_luck_1 = re.search(r"- ([0-9]+) [0-9]+ خفيف  lucky strike", file_t_reader_)
							result_luck_2 = re.search(r"- ([0-9]+) [0-9]+ تقيل lusky strike", file_t_reader_)

							if resutl_lmRed:
								lm_red = lm_red + int(resutl_lmRed.group(1))
							if result_lmBlue:
								lm_blue = lm_blue + int(result_lmBlue.group(1))
							if result_lmWhite:
								lm_white = lm_white + int(result_lmWhite.group(1))
							if result_ma_red:
								marl_red = marl_red + int(result_ma_red.group(1))
							if result_ma_white:
								marl_white = marl_white + int(result_ma_white.group(1))
							if result_ma_m:
								marl_m = marl_m + int(result_ma_m.group(1))
							if result_mer_y:
								mert_y = mert_y + int(result_mer_y.group(1))
							if result_mert_b:
								mert_b = mert_b + int(result_mert_b.group(1))
							if resutl_Next:
								Next_ = Next_ + int(resutl_Next.group(1))
							if resutl_k:
								K_ = K_ + int(resutl_k.group(1))
							if result_box:
								box_ = box_ + int(result_box.group(1))
							if result_super:
								super_1 = super_1 + int(result_super.group(1))
							if result_k_d:
								k_d = k_d + int(result_k_d.group(1))
							if result_k_new:
								k_new = k_new + int(result_k_new.group(1))
							if result_kr_red:
								kr_red = kr_red + int(result_kr_red.group(1))
							if resutl_kr_blue:
								kr_blue = kr_blue + int(resutl_kr_blue.group(1))
							if result_p_b:
								p_b = p_b + int(result_p_b.group(1))
							if result_p_r:
								p_r = p_r + int(result_p_r.group(1))
							if result_p_c:
								p_c = p_c + int(result_p_c.group(1))
							if result_d_c:
								d_c = d_c + int(result_d_c.group(1))
							if result_d_g:
								d_g = d_g + int(result_d_g.group(1))
							if result_d_w:
								d_w = d_w = int(result_d_w.group(1))
							if result_d_s:
								d_s = d_s + int(result_d_s.group(1))
							if result_t_r:
								t_r = t_r + int(result_t_r.group(1))
							if result_t_b:
								t_b = t_b + int(result_t_b.group(1))
							if result_ti_r:
								ti_r = ti_r + int(result_ti_r.group(1))
							if result_ti_b:
								ti_b = ti_b + int(result_ti_b.group(1))
							if result_ti_w:
								ti_w = ti_w + int(result_ti_w.group(1))
							if result_ws_r:
								ws_r = ws_r + int(result_ws_r.group(1))
							if result_ws_b:
								ws_b = ws_b + int(result_ws_b.group(1))
							if result_ws_w:
								ws_w = ws_w + int(result_ws_w.group(1))
							if result_ws_u:
								ws_u = ws_u + int(result_ws_u.group(1))
							if result_ca_b:
								ca_b = ca_b + int(result_ca_b.group(1))
							if result_ca_y:
								ca_y = ca_y + int(result_ca_y.group(1))
							if result_LD_red:
								LD_red = LD_red + int(result_LD_red.group(1))
							if result_LD_blue:
								LD_blue = LD_blue + int(result_LD_blue.group(1))
							if result_rs_blue:
								rs_blue = rs_blue + int(result_rs_blue.group(1))
							if result_rs_red:
								rs_red = rs_red + int(result_rs_red.group(1))
							if result_rs_red_s:
								rs_red_small = rs_red_small + int(result_rs_red_s.group(1))
							if result_rs_w:
								rs_white = rs_white + int(result_rs_w.group(1))
							if result_rs_c:
								rs_switch = rs_switch + int(result_rs_c.group(1))
							if result_kn1:
								kn1 = kn1 + int(result_kn1.group(1))
							if result_kn6:
								kn6 = kn6 + int(result_kn6.group(1))
							if result_kn9:
								kn9 = kn9 + int(result_kn9.group(1))
							if result_vec_r:
								vec_red = vec_red + int(result_vec_r.group(1))
							if result_vec_b:
								vec_blue = vec_blue + int(result_vec_b.group(1))
							if result_pl_red:
								pl_red = pl_red + int(result_pl_red.group(1))
							if result_pl_blue:
								pl_blue = pl_blue + int(result_pl_blue.group(1))
							if result_dun_r:
								dun_r = dun_r + int(result_dun_r.group(1))
							if result_dun_b:
								dun_b = dun_b + int(result_dun_b.group(1))
							if result_luck_1:
								luck_1 = luck_1 + int(result_luck_1.group(1))
							if result_luck_2:
								luck_2 = luck_2 + int(result_luck_2.group(1))
					else:
						file_t = open("tobacco/{}-{}-{}.txt".format(days, combobox_month2.get(), years_var1_), "r", encoding="utf-8")
						file_t_reader = file_t.readlines()
						for file_t_reader_ in file_t_reader:
							resutl_lmRed = re.search(r"- ([0-9]+) [0-9]+ احمر  LM", file_t_reader_)
							result_lmBlue = re.search(r"- ([0-9]+) [0-9]+ ازرق  LM", file_t_reader_)
							result_lmWhite = re.search(r"- ([0-9]+) [0-9]+ ابيض  LM", file_t_reader_)
							result_ma_red = re.search(r"- ([0-9]+) [0-9]+ احمر  Marlboro", file_t_reader_)
							result_ma_white = re.search(r"- ([0-9]+) [0-9]+ ابيض  Marlboro", file_t_reader_)
							result_ma_m = re.search(r"- ([0-9]+) [0-9]+ Marlboro medium", file_t_reader_)
							result_mer_y = re.search(r"- ([0-9]+) [0-9]+ اصفر  Merit", file_t_reader_)
							result_mert_b = re.search(r"- ([0-9]+) [0-9]+ ازرق  Merit", file_t_reader_)
							resutl_Next = re.search(r"- ([0-9]+) [0-9]+ Next", file_t_reader_)
							resutl_k = re.search(r"- ([0-9]+) [0-9]+ كيلوبترا", file_t_reader_)
							result_box = re.search(r"- ([0-9]+) [0-9]+  بوكس", file_t_reader_)
							result_super = re.search(r"- ([0-9]+) [0-9]+  سوبر", file_t_reader_)
							result_k_d = re.search(r"- ([0-9]+) [0-9]+.[0-9]+ كيلوبترا  مقلوبة", file_t_reader_, re.UNICODE)
							result_k_new = re.search(r"- ([0-9]+) [0-9]+.[0-9]+ كيلوبترا جديدة", file_t_reader_, re.UNICODE)
							result_kr_red = re.search(r"- ([0-9]+) [0-9]+ احمر  Karelia", file_t_reader_)
							resutl_kr_blue = re.search(r"- ([0-9]+) [0-9]+ ازرق  Karelia", file_t_reader_)
							result_p_b = re.search(r'- ([0-9]+) [0-9]+ ازرق  pine', file_t_reader_)
							result_p_r = re.search(r"- ([0-9]+) [0-9]+ احمر  pine", file_t_reader_)
							result_p_c = re.search(r"- ([0-9]+) [0-9]+ pine change", file_t_reader_)
							result_d_c = re.search(r"- ([0-9]+) [0-9]+ Davidoff classic", file_t_reader_)
							result_d_g = re.search(r"- ([0-9]+) [0-9]+ Davidoff gold", file_t_reader_)
							result_d_w = re.search(r"- ([0-9]+) [0-9]+ Davidoff white", file_t_reader_)
							result_p_s = re.search(r"- ([0-9]+) [0-9]+ Davidoff slim",file_t_reader_)
							result_t_r = re.search(r"- ([0-9]+) [0-9]+ احمر  Target", file_t_reader_)
							result_t_b = re.search(r"- ([0-9]+) [0-9]+ ازرق  Target", file_t_reader_)
							result_ti_r = re.search(r"- ([0-9]+) [0-9]+ احمر  Time", file_t_reader_)
							result_ti_b = re.search(r"- ([0-9]+) [0-9]+ ازرق  Time", file_t_reader_)
							result_ti_w = re.search(r"- ([0-9]+) [0-9]+ ابيض  Time", file_t_reader_)
							result_ws_r = re.search(r"- ([0-9]+) [0-9]+ احمر  Winston", file_t_reader_)
							result_ws_b = re.search(r"- ([0-9]+) [0-9]+ ازرق  Winston", file_t_reader_)
							result_ws_w = re.search(r"- ([0-9]+) [0-9]+ ابيض  Winston", file_t_reader_)
							result_ws_u = re.search(r"- ([0-9]+) [0-9]+ توت  Winston", file_t_reader_)
							result_ca_y = re.search(r"- ([0-9]+) [0-9]+ اصفر  Camel", file_t_reader_)
							result_ca_b = re.search(r"- ([0-9]+) [0-9]+ ازرق  Camel", file_t_reader_)
							result_LD_red = re.search(r"- ([0-9]+) [0-9]+ احمر  LD", file_t_reader_)
							result_LD_blue = re.search(r"- ([0-9]+) [0-9]+ ازرق  LD", file_t_reader_)
							result_rs_blue = re.search(r"- ([0-9]+) [0-9]+ ازرق  Roseman", file_t_reader_)
							result_rs_red = re.search(r"- ([0-9]+) [0-9]+ احمر  Roseman", file_t_reader_)
							result_rs_red_s = re.search(r"- ([0-9]+) [0-9]+ احمر صغير  Roseman", file_t_reader_)
							result_rs_w = re.search(r"- ([0-9]+) [0-9]+ ابيض  Roseman", file_t_reader_)
							result_rs_c = re.search(r"- ([0-9]+) [0-9]+ Roseman switch", file_t_reader_)
							result_kn1 = re.search(r"- ([0-9]+) [0-9]+ Kent 1", file_t_reader_)
							result_kn6 = re.search(r"- ([0-9]+) [0-9]+ kent 6", file_t_reader_)
							result_kn9 = re.search(r"- ([0-9]+) [0-9]+ kent 9", file_t_reader_)
							result_vec_r = re.search(r"- ([0-9]+) [0-9]+ احمر  Viceroy", file_t_reader_)
							result_vec_b = re.search(r"- ([0-9]+) [0-9]+ ازرق  Viceroy", file_t_reader_)
							result_pl_red = re.search(r"- ([0-9]+) [0-9]+ احمر  Pallmall", file_t_reader_)
							result_pl_blue = re.search(r"- ([0-9]+) [0-9]+ ازرق  Pallmall", file_t_reader_)
							result_dun_r = re.search(r"- ([0-9]+) [0-9]+ احمر  Dunhill", file_t_reader_)
							result_dun_b = re.search(r"- ([0-9]+) [0-9]+ ازرق  Dunhill", file_t_reader_)
							result_luck_1 = re.search(r"- ([0-9]+) [0-9]+ خفيف  lucky strike", file_t_reader_)
							result_luck_2 = re.search(r"- ([0-9]+) [0-9]+ تقيل lusky strike", file_t_reader_)

							if resutl_lmRed:
								lm_red = lm_red + int(resutl_lmRed.group(1))
							if result_lmBlue:
								lm_blue = lm_blue + int(result_lmBlue.group(1))
							if result_lmWhite:
								lm_white = lm_white + int(result_lmWhite.group(1))
							if result_ma_red:
								marl_red = marl_red + int(result_ma_red.group(1))
							if result_ma_white:
								marl_white = marl_white + int(result_ma_white.group(1))
							if result_ma_m:
								marl_m = marl_m + int(result_ma_m.group(1))
							if result_mer_y:
								mert_y = mert_y + int(result_mer_y.group(1))
							if result_mert_b:
								mert_b = mert_b + int(result_mert_b.group(1))
							if resutl_Next:
								Next_ = Next_ + int(resutl_Next.group(1))
							if resutl_k:
								K_ = K_ + int(resutl_k.group(1))
							if result_box:
								box_ = box_ + int(result_box.group(1))
							if result_super:
								super_1 = super_1 + int(result_super.group(1))
							if result_k_d:
								k_d = k_d + int(result_k_d.group(1))
							if result_k_new:
								k_new = k_new + int(result_k_new.group(1))
							if result_kr_red:
								kr_red = kr_red + int(result_kr_red.group(1))
							if resutl_kr_blue:
								kr_blue = kr_blue + int(resutl_kr_blue.group(1))
							if result_p_b:
								p_b = p_b + int(result_p_b.group(1))
							if result_p_r:
								p_r = p_r + int(result_p_r.group(1))
							if result_p_c:
								p_c = p_c + int(result_p_c.group(1))
							if result_d_c:
								d_c = d_c + int(result_d_c.group(1))
							if result_d_g:
								d_g = d_g + int(result_d_g.group(1))
							if result_d_w:
								d_w = d_w = int(result_d_w.group(1))
							if result_d_s:
								d_s = d_s + int(result_d_s.group(1))
							if result_t_r:
								t_r = t_r + int(result_t_r.group(1))
							if result_t_b:
								t_b = t_b + int(result_t_b.group(1))
							if result_ti_r:
								ti_r = ti_r + int(result_ti_r.group(1))
							if result_ti_b:
								ti_b = ti_b + int(result_ti_b.group(1))
							if result_ti_w:
								ti_w = ti_w + int(result_ti_w.group(1))
							if result_ws_r:
								ws_r = ws_r + int(result_ws_r.group(1))
							if result_ws_b:
								ws_b = ws_b + int(result_ws_b.group(1))
							if result_ws_w:
								ws_w = ws_w + int(result_ws_w.group(1))
							if result_ws_u:
								ws_u = ws_u + int(result_ws_u.group(1))
							if result_ca_b:
								ca_b = ca_b + int(result_ca_b.group(1))
							if result_ca_y:
								ca_y = ca_y + int(result_ca_y.group(1))
							if result_LD_red:
								LD_red = LD_red + int(result_LD_red.group(1))
							if result_LD_blue:
								LD_blue = LD_blue + int(result_LD_blue.group(1))
							if result_rs_blue:
								rs_blue = rs_blue + int(result_rs_blue.group(1))
							if result_rs_red:
								rs_red = rs_red + int(result_rs_red.group(1))
							if result_rs_red_s:
								rs_red_small = rs_red_small + int(result_rs_red_s.group(1))
							if result_rs_w:
								rs_white = rs_white + int(result_rs_w.group(1))
							if result_rs_c:
								rs_switch = rs_switch + int(result_rs_c.group(1))
							if result_kn1:
								kn1 = kn1 + int(result_kn1.group(1))
							if result_kn6:
								kn6 = kn6 + int(result_kn6.group(1))
							if result_kn9:
								kn9 = kn9 + int(result_kn9.group(1))
							if result_vec_r:
								vec_red = vec_red + int(result_vec_r.group(1))
							if result_vec_b:
								vec_blue = vec_blue + int(result_vec_b.group(1))
							if result_pl_red:
								pl_red = pl_red + int(result_pl_red.group(1))
							if result_pl_blue:
								pl_blue = pl_blue + int(result_pl_blue.group(1))
							if result_dun_r:
								dun_r = dun_r + int(result_dun_r.group(1))
							if result_dun_b:
								dun_b = dun_b + int(result_dun_b.group(1))
							if result_luck_1:
								luck_1 = luck_1 + int(result_luck_1.group(1))
							if result_luck_2:
								luck_2 = luck_2 + int(result_luck_2.group(1))

				Label1.config(text=lm_red)
				Label2.config(text=lm_blue)
				Label3.config(text=lm_white)
				label4.config(text=marl_red)
				Label5.config(text=marl_white)
				Label6.config(text=marl_m)
				Label7.config(text=mert_y)
				Label8.config(text=mert_b)
				Label9.config(text=Next_)
				Label10.config(text=K_)
				Label11.config(text=box_)
				label12.config(text=super_1)
				label13.config(text=k_d)
				label14.config(text=k_new)
				Label15.config(text=kr_red)
				Label16.config(text=kr_blue)
				Label17.config(text=p_b)
				Label18.config(text=p_r)
				Label19.config(text=p_c)
				Label20.config(text=d_c)
				Label21.config(text=d_g)
				Label22.config(text=d_w)
				Label23.config(text=d_s)
				Label24.config(text=t_r)
				Label25.config(text=t_b)
				Label26.config(text=ti_r)
				Label27.config(text=ti_b)
				Label28.config(text=ti_w)
				Label29.config(text=ws_r)
				Label30.config(text=ws_b)
				Label31.config(text=ws_w)
				Label32.config(text=ca_y)
				Label33.config(text=ca_b)
				Label34.config(text=LD_red)
				Label35.config(text=LD_blue)
				Label36.config(text=rs_blue)
				Label37.config(text=rs_red)
				Label38.config(text=rs_red_small)
				Label39.config(text=rs_switch)
				Label40.config(text=kn1)
				Label41.config(text=kn6)
				LabeL42.config(text=kn9)
				Label43.config(text=vec_red)
				Label44.config(text=vec_blue)
				Label45.config(text=pl_red)
				Label46.config(text=pl_blue)
				Label47.config(text=dun_r)
				Label48.config(text=dun_b)
				Label49.config(text=luck_1)
				Label50.config(text=luck_2)
			else:
				pass


		button_ok = Button(paned1, text="ok", command=ok_, font=("italic", 13))

		# place
		Lab_space.grid(column=1, row=0)
		Lab_space1.grid(column=1, row=1)
		Label_from.grid(column=0, row=1)
		Label_to.grid(column=0, row=2)

		Label_days.grid(column=2, row=0)
		Label_months.grid(column=3, row=0)
		Lable_years.grid(column=4, row=0)
		combobox_day2.grid(column=2, row=1)
		combobox_day2_.grid(column=2, row=2)
		combobox_month2.grid(column=3, row=1)
		combobox_month2_.grid(column=3, row=2)
		combobox_year2.grid(column=4, row=1)
		combobox_year2_.grid(column=4, row=2)


		Y = 30
		Y1 = 90
		Y2 = 60
		Y3 = 125
		Y4 = 155
		Y5 = 190
		Y6 = 220
		Y7 = 250
		Y8 = 280
		Y10 = 310
		Y11 = 340
		Y12 = 370
		Y13 = 400
		Y14 = 430
		Y15 = 460
		Y16 = 490
		Y17 = 520
		Y18 = 550
		Y19 = 580

		button_ok.place(x=460, y=77)
		du_r.place(x=480, y=0)
		Label49.place(x=500, y=30)
		du_b.place(x=480, y=60)
		Label50.place(x=520, y=90)
		Lm_Label_red.place(x=0, y=0)
		Label1.place(x=20, y=Y)
		Lm_Label_blue.place(x=80, y=0)
		Label2.place(x=100, y=Y)
		Lm_Label_white.place(x=160, y=0)
		Label3.place(x=180, y=Y)
		Label_Marl_red.place(x=240, y=0)
		label4.place(x=280, y=Y)
		Label_Marl_Gold.place(x=360, y=0)
		Label5.place(x=380, y=Y)
		Mar_md.place(x=0, y=Y2)
		Label6.place(x=50, y=Y1)
		Mert_Label.place(x=140, y=Y2)
		Label7.place(x=170, y=Y1)
		Mert_blue.place(x=230, y=Y2)
		Label8.place(x=260, y=Y1)
		Next.place(x=320, y=Y2)
		Label9.place(x=330, y=Y1)
		ke.place(x=370, y=Y2)
		Label10.place(x=390, y=Y1)
		box.place(x=430, y=Y2)
		Label11.place(x=440, y=Y1)
		super_.place(x=0, y=Y3)
		label12.place(x=10, y=Y4)
		new_ke.place(x=40, y=Y3)
		label13.place(x=70, y=Y4)
		other_ke.place(x=130, y=Y3)
		label14.place(x=165, y=Y4)
		ka_red.place(x=225, y=Y3)
		Label15.place(x=265, y=Y4)
		Ka_blue.place(x=325, y=Y3)
		Label16.place(x=365, y=Y4)
		pine_blue.place(x=0, y=Y5)
		Label17.place(x=20, y=Y6)
		pine_red.place(x=85, y=Y5)
		Label18.place(x=110, y=Y6)
		pine_change.place(x=170, y=Y5)
		Label19.place(x=210, y=Y6)
		dv_c.place(x=270, y=Y5)
		Label20.place(x=320, y=Y6)
		dv_g.place(x=395, y=Y5)
		Label21.place(x=435, y=Y6)
		dv_w.place(x=0, y=Y7)
		Label22.place(x=45, y=Y8)
		dv_s.place(x=115, y=Y7)
		Label23.place(x=155, y=Y8)
		target_red.place(x=220, y=Y7)
		Label24.place(x=250, y=Y8)
		target_blue.place(x=315, y=Y7)
		Label25.place(x=350, y=Y8)
		time_red.place(x=410, y=Y7)
		Label26.place(x=440, y=Y8)
		time_blue.place(x=0, y=Y10)
		Label27.place(x=20, y=Y11)
		time_white.place(x=85, y=Y10)
		Label28.place(x=120, y=Y11)
		winston_red.place(x=170, y=Y10)
		Label29.place(x=215, y=Y11)
		winston_blue.place(x=280, y=Y10)
		Label30.place(x=320, y=Y11)
		winston_white.place(x=390, y=Y10)
		Label31.place(x=430, y=Y11)
		winston_t.place(x=0, y=Y12)
		Label32.place(x=40, y=Y13)
		camel_y.place(x=105, y=Y12)
		Label33.place(x=140, y=Y13)
		camel_b.place(x=205, y=Y12)
		Label34.place(x=240, y=Y13)
		ld_r.place(x=305, y=Y12)
		Label35.place(x=330, y=Y13)
		ld_b.place(x=380, y=Y12)
		Label36.place(x=400, y=Y13)
		ros_b.place(x=0, y=Y14)
		Label37.place(x=50, y=Y15)
		ros_r.place(x=115, y=Y14)
		Label38.place(x=170, y=Y15)
		ros_w.place(x=230, y=Y14)
		Label39.place(x=290, y=Y15)
		ros_rs.place(x=350, y=Y14)
		Label40.place(x=400, y=Y15)
		ros_c.place(x=0, y=Y16)
		Label41.place(x=50, y=Y17)
		kent1.place(x=130, y=Y16)
		LabeL42.place(x=150, y=Y17)
		kent6.place(x=190, y=Y16)
		Label43.place(x=210, y=Y17)
		kent9.place(x=250, y=Y16)
		Label44.place(x=265, y=Y17)
		vc_r.place(x=310, y=Y16)
		Label45.place(x=350, y=Y17)
		vc_b.place(x=415, y=Y16)
		Label46.place(x=460, y=Y17)
		pal_r.place(x=0, y=550)
		Label47.place(x=40, y=580)
		pal_b.place(x=100, y=550)
		Label48.place(x=150, y=580)
		luc_l.place(x=430, y=125)
		Label51.place(x=490, y=155)
		luc_h.place(x=210, y=550)
		Label52.place(x=250, y=580)
		kiss_a.place(x=500, y=190)
		Label53.place(x=520, y=220)
		kiss_s.place(x=500, y=250)
		Label54.place(x=520, y=280)
		kiss_k.place(x=500, y=310)
		Label55.place(x=530, y=340)
		kiss_m.place(x=455, y=370)
		Label56.place(x=480, y=400)


		main26.mainloop()



	button_tobaco = Button(main5, text="جرد مفصل", command=more_information).pack()

	# search
	def search_on():
		main3 = Tk()
		w4 = 305
		h4 = 200
		sw4 = main3.winfo_screenwidth()
		sh4 = main3.winfo_screenheight()
		x4 = (sw4-w4)/2
		y4 = (sh4-h4)/2
		main3.geometry("%dx%d+%d+%d" % (w4,h4,x4,y4))
		main3.resizable(False,False)
		main3.configure(bg="#ff9933")
		main3.iconbitmap(default='central elgazera 2.ico')
		main3.title("Central Elgazera")
		# combobox
		# years
		combobox_year_var2 = StringVar()
		years2 = []
		combobox_year2 = ttk.Combobox(main3,width=12,textvariable=combobox_year_var2)
		for c2 in range(2000,2101):
			years2.append(c2)
		combobox_year2["values"] = years2
		combobox_year2.place(x=205,y=20)
		combobox_year2.current(0)

		# months
		combobox_month_var2 = StringVar()
		combobox_month2 = ttk.Combobox(main3,width=12,textvariable=combobox_month_var2)
		months2 = []
		for b2 in range(1,13):
			if len(str(b2)) < 2:
				b2_str = "0{}".format(b2)
				months2.append(b2_str)
			else:
				months2.append(b2)
		combobox_month2["values"] = months2
		combobox_month2.place(x=105,y=20)
		combobox_month2.current(0)

		# days
		combobox_day_var2 = StringVar()
		days2 = []
		for a2 in range(1,32):
			if len(str(a2)) < 2:
				a2_str = "0{}".format(a2)
				days2.append(a2_str)
			else:
				days2.append(a2)
		combobox_day2 = ttk.Combobox(main3,values=days2,width=12,textvariable=combobox_day_var2)
		combobox_day2.place(x=5, y=20)
		combobox_day2.current(0)

		search_n = Entry(main3)
		search_n.place(x=0,y=100)

		def search_numbers1():
			try:
				search_n_var = int(search_n.get())
				file_numbers = open("numbers/{}-{}-{}-numbers.txt".format(combobox_day2.get(), combobox_month2.get(), combobox_year2.get()), "r", encoding="utf-8")
				file_n_reader = file_numbers.readlines()
				for nreader in file_n_reader:
					nresult = re.search(r"-([0-9]+) number:({}) place:([\u0600-\u06FF]+) state:([\u0600-\u06FF]+ [\u0600-\u06FF]+)  time:([0-9]+:[0-9]+:[0-9]+ \w+)".format(search_n_var), nreader, re.UNICODE)
					nresult2 = re.search(r"-([0-9]+.[0-9]+) number:({}) place:([\u0600-\u06FF]+) state:([\u0600-\u06FF]+ [\u0600-\u06FF]+)  time:([0-9]+:[0-9]+:[0-9]+ \w+)".format(search_n_var), nreader, re.UNICODE)
					if nresult:
						messagebox.showinfo("central elgazera","""price:{}
							number:0{}
							place:{}
							state:{}
							time:{}""".format(nresult.group(1), nresult.group(2), nresult.group(3), nresult.group(4), nresult.group(5)))

					if nresult2:
						messagebox.showinfo("central elgazera","""price:{}
							number:0{}
							place:{}
							state:{}
							time:{}""".format(nresult2.group(1),nresult2.group(2),nresult2.group(3),nresult2.group(4),nresult2.group(5)))
			except ValueError:
				messagebox.showerror("Error","يجب ادخال ارقام فقط")
			except FileNotFoundError:
				messagebox.showerror("Error","الملف غير موجود")
		search_numbers_o = Button(main3,text="بحث",command=search_numbers1).place(x=130,y=95)
		main3.mainloop()


	def money():
		main6 = Tk()
		w7 = 300
		h7 = 100
		sw7 = main6.winfo_screenwidth()
		sh7 = main6.winfo_screenheight()
		x7 = (sw7-w7)/2
		y7 = (sh7-h7)/2
		main6.geometry("%dx%d+%d+%d" % (w7,h7,x7,y7))
		main6.resizable(False,False)
		main6.title("Central Elgazera")
		main6.configure(bg="#ff9933")
		main6.iconbitmap(default='central elgazera 2.ico')


		label_name = Label(main6,text="الاسم",font=("italic",13)).place(x=60,y=5)
		name_entry = Entry(main6,font=("italic",13),width=15)
		name_entry.place(x=0,y=25)


		price_label = Label(main6,text="القيمة",font=("italic",13)).place(x=160,y=5)
		price_entry = Entry(main6,font=("italic",13),width=5)
		price_entry.place(x=150,y=25)

		def save_n():
			try:
				price_2 = int(price_entry.get())
				file_p = open("people/{}-people.txt".format(date),"a+",encoding="utf-8")
				file_p.write("\n")
				file_p.write(u"المبلغ:{} الاسم:{} التاريخ:{}".format(price_2,name_entry.get(),date))
				file_p.close()
			except ValueError:
				messagebox.showerror("Error","يجب ادخال ارقام فقط")


		save_name = Button(main6,text="Save",font=("italic",13),bg="#d9d9d9",command=save_n).place(x=210,y=20)


		def back_n():
			main7 = Tk()
			w8 = 350
			h8 = 250
			sw8 = main7.winfo_screenwidth()
			sh8 = main7.winfo_screenheight()
			x8 = (sw8-w8)/2
			y8 = (sh8-h8)/2
			main7.geometry("%dx%d+%d+%d" % (w8,h8,x8,y8))
			main7.resizable(False,False)
			main7.title("Central Elgazera")
			main7.configure(bg="#ff9933")
			main7.iconbitmap(default='central elgazera 2.ico')

			accessories_list1 = []
			file_list1 = open("people/{}-people.txt".format(date),"r",encoding="utf-8")
			line_file_list1 = file_list1.readlines()
			for flreader1 in line_file_list1:
				accessories_list1.append(flreader1)
			file_list1.close()

			l2 = Listbox(main7,selectmode=SINGLE,font=("italic",13),width=30,height=30)
			for items2 in range(len(accessories_list1)):
				l2.insert(items2,accessories_list1[items2])
			l2.place(x=0,y=0)

			def del_n1():
				ac1 = l2.curselection()
				accessories_list1.remove(l2.get(ac1))
				l2.delete(ac1)
				file_ac1 = open("people/{}-people.txt".format(date),"w",encoding="utf-8")
				for remove_item1 in range(len(accessories_list1)):
					file_ac1.write(accessories_list1[remove_item1])
				file_ac1.close()

			del_n = Button(main7,text="حذف",command=del_n1,font=("italic",13)).place(x=310,y=220)
			main7.mainloop()
		more_n = Button(main6,text="تراجع",command=back_n,font=("italic",13)).place(x=0,y=66)

		main6.mainloop()

	money_b = Button(main5,text="مستحقات",command=money).pack()


	search_button = Button(main5,text="بحث عن عملية",command=search_on).pack()

	main5.mainloop()
more_more = Button(main,text="المزيد",command=more_2,font=("italic",13)).place(x=500,y=566)

# cards
cards_label = Label(main,text="كروت شحن",font=("italic",13)).place(x=0,y=250)
combobox_cards_kinds_var = StringVar()
combobox_cards_kinds = ttk.Combobox(main, width=13, textvariable=combobox_cards_kinds_var,state="readonly",font=("italic",13))
combobox_cards_kinds["values"] = [u"فودافون", u"اورنج", u"اتصالات", u"المصرية للاتصالات"]
combobox_cards_kinds.place(x=0, y=305)
combobox_cards_kinds.current(0)

# vodafone
vodafone_list = ["2","4","5","10","15","25","50","100"]
# orange
orange_list = ["2","4","5","10","15","20","25","50","100"]
# etisalat
etisalat_list = ["1.5","3.5","5","7","10","15","25","50","100"]
# we
we_list = ["5","10","15","25","30","40","50","60","75","100","150"]

list_vodafone = [u"فودافون"]
list_orange = [u"اورنج"]
list_etisalat = [u"اتصالات"]
list_we = [u"المصرية للاتصالات"]


num_cards = ttk.Combobox(main, width=5, font=("italic",13), state="readonly")
num_cards_list = []
for nums_cards in range(1,21):
	num_cards_list.append(nums_cards)
num_cards["values"] = num_cards_list
num_cards.place(x=280,y=310)
num_cards.current(0)


def next1():
	if combobox_cards_kinds.get() in list_vodafone:
		list_values = []
		for cards1 in vodafone_list:
			list_values.append(cards1)
		combobox_cards.configure(values=list_values)
		combobox_cards.current(0)
	elif combobox_cards_kinds.get() in list_orange:
		list_values = []
		for cards1 in orange_list:
			list_values.append(cards1)
		combobox_cards.configure(values=list_values)
		combobox_cards.current(0)
	elif combobox_cards_kinds.get() in list_etisalat:
		list_values = []
		for cards1 in etisalat_list:
			list_values.append(cards1)
		combobox_cards.configure(values=list_values)
		combobox_cards.current(0)
	elif combobox_cards_kinds.get() in list_we:
		list_values = []
		for cards1 in we_list:
			list_values.append(cards1)
		combobox_cards.configure(values=list_values)
		combobox_cards.current(0)
	else:
		pass


cards_button = Button(main,text="التالى",font=("italic",13),command=next1).place(x=150,y=305)


def cars_command():
	Total7 = 0
	Total8 = 0
	file_command = open("cards/{}-cards.txt".format(date),"r",encoding="utf-8")
	cards_linereader = file_command.readlines()
	for file_cards in cards_linereader:
		cards_result = re.search(r"-([0-9]+) ",file_cards)
		cards_result1 = re.search(r"-([0-9]+.[0-9]+) ",file_cards)
		if cards_result:
			Total7 = Total7 + int(cards_result.group(1))
		if cards_result1:
			Total8 = Total8 + float(cards_result1.group(1))


	messagebox.showinfo("Central Elgazera","Total:{}".format(Total7+Total8))


cards_info = Button(main,text="معلومات",font=("italic",13),command=cars_command,bg="#3399ff").place(x=410,y=305)

def save_cards():
	price_cards = float(combobox_cards.get())
	kinds_cards = str(combobox_cards_kinds.get())
	cards_file = open("cards/{}-cards.txt".format(date),"a+",encoding="utf-8")
	cards_file.write("\n")
	cards_file.write("-{} {}".format(price_cards*int(num_cards.get()),kinds_cards))
	cards_file.close()

	Total7 = 0
	Total8 = 0
	file_command = open("cards/{}-cards.txt".format(date), "r", encoding="utf-8")

	cards_linereader = file_command.readlines()
	file_command.close()
	file_command = open("cards/{}-cards.txt".format(date), "a+", encoding="utf-8")
	for file_cards in cards_linereader:
		cards_result = re.search(r"-([0-9]+) ", file_cards)
		cards_result1 = re.search(r"-([0-9]+.[0-9]+) ", file_cards)
		if cards_result:
			Total7 = Total7 + int(cards_result.group(1))
		if cards_result1:
			Total8 = Total8 + float(cards_result1.group(1))
	file_command.write("\n")
	file_command.write("Total:{}".format(Total8+Total7))
	file_command.close()

save_cards_button = Button(main, text="حفظ", command=save_cards, font=("italic", 13), bg="#d9d9d9").place(x=370, y=305)

combobox_cards_var = StringVar()
combobox_cards = ttk.Combobox(main, width=5, textvariable=combobox_cards_var, font=("italic", 13), state="readonly")
combobox_cards["values"] = []
combobox_cards.place(x=200,y=310)

# electricity

electricity_label = Label(main, text="كروت الكهربة", font=("italic", 13)).place(x=0, y=350)

electricity_entry_var = StringVar()
electricity_entry = Entry(main,textvariable=electricity_entry_var,width=5,font=("italic", 13)).place(x=0,y=385)

def save_electricity_cards():
	try:
		electricity_entry_float = int(electricity_entry_var.get())
		electricity_entry_file = open("electricity cards/{}-electricity.txt".format(date), "a+", encoding="utf-8")
		electricity_entry_file.write("\n")
		electricity_entry_file.write("-{}".format(electricity_entry_float))
		electricity_entry_file.close()
		electricity_entry_file = open("electricity cards/{}-electricity.txt".format(date), "r", encoding="utf-8")
		electricity_entry_file_r = electricity_entry_file.readlines()
		electricity_entry_file.close()
		Total21 = 0
		for f_reader in electricity_entry_file_r:
			result20 = re.search(r"-([0-9]+)", f_reader)
			if result20:
				Total21 = Total21 + int(result20.group(1))
		electricity_entry_file = open("electricity cards/{}-electricity.txt".format(date), "a+", encoding="utf-8")
		electricity_entry_file.write("\n")
		electricity_entry_file.write("Total:{}".format(Total21))
		electricity_entry_file.close()

	except ValueError:
		messagebox.showerror("Error","يجب ادخال ارقام فقط")

save_electricity_button = Button(main, text="حفظ", font=("italic", 13), command=save_electricity_cards ,bg="#d9d9d9").place(x=60, y=380)

def info_electricity_button():
	Total10 = 0
	file_electricity = open("electricity cards/{}-electricity.txt".format(date), "r", encoding="utf-8")
	file_electricity_reader = file_electricity.readlines()
	for file_electricity_reader1 in file_electricity_reader:
		fresult = re.search(r"-([0-9]+)", file_electricity_reader1)
		if fresult:
			Total10 = Total10 + int(fresult.group(1))
	messagebox.showinfo("Central Elgazera", "Total:{}".format(Total10))

info_electricity_button = Button(main, text="معلومات", font=("italic", 13),bg="#3399ff", command=info_electricity_button).place(x=120, y=380)
main.protocol("WM_DELETE_WINDOW", on_closing_window)
main.mainloop()

# End
