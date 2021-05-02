# حل مستوى متقدم
# نلاحظ قلة الجمل الشرطية و التكرار
def gameLogic(i, divisor, text):
	return text if i % divisor == 0 else ""


for i in range(1, 20):
	text = ""
	text += gameLogic(i, 3, "قفص ")
	text += gameLogic(i, 5, "خشب")
	if text == "":
		text = i
	print(text)

"""
# حل مستوى مبتدئ 
# نلاحظ كثرة الجمل الشرطية و التكرار
for i in range(1,20): 
    if i%3==0 and i%5== 0: 
        print("قفص خشب")                                         
        continue

    elif i% 3 == 0:     
        print("قفص")                                         
        continue

    elif i % 5 == 0:         
        print("خشب")                                     
        continue

    print(i)
"""

"""
# حل مستوى متوسط
هنا عرّف المبرمج متغيراً نصياً في البداية وطبعهُ في النهاية،و ما بين البداية والنهاية أجرى عملياتٍ تحدد محتوى النص الذي سيُطبع
بهذه الطريقة أصبحت الخوارزمية أكثرْ رُقياً وتحضراً، كما غدا توسيعُ -Scalability-الحل كُلّما توسّعت المشكلة أسهل
ولكن لا يزال هناك أجزاء متشابهة!

for i in range(1,20): 
  text=""
  if i%3==0: 
     text+="قفص"

  if i%5==0:     
     text+="خشب"

  # if i%4==0:         
  #    text+="خشن"
   
  if text=="":
     text= i

  print(text)
"""
