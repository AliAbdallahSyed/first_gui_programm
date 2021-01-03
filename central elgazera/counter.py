import re
from tkinter import *
from tkinter import ttk
main = Tk()
w9 = 600
h9 = 750
sw9 = main.winfo_screenwidth()
sh9 = main.winfo_screenheight()
x9 = (sw9-w9)/2
y9 = (sh9-h9)/2
main.geometry("%dx%d+%d+%d" % (w9, h9, x9, y9))
main.resizable(False, False)
main.iconbitmap(default='central elgazera 2.ico')
main.title("Central Elgazera")

paned1 = PanedWindow(main, orient=VERTICAL, bg="#ff9933")
paned2 = PanedWindow(main, orient=VERTICAL, bg="#0099ff")
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


main.mainloop()
