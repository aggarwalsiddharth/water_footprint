from django.db import models

# Create your models here.
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

import uuid

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Question(models.Model):
    id = models.BigIntegerField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=1000)
    order = models.PositiveSmallIntegerField()

    bg_desktop1 = models.CharField(max_length=1000,blank=True)
    bg_desktop2 = models.CharField(max_length=1000, blank=True)
    bg_desktop3 = models.CharField(max_length=1000, blank=True)
    bg_desktop4 = models.CharField(max_length=1000, blank=True)
    bg_desktop5 = models.CharField(max_length=1000, blank=True)
    bg_mobile1 = models.CharField(max_length=1000, blank=True)
    bg_mobile2 = models.CharField(max_length=1000, blank=True)
    bg_mobile3 = models.CharField(max_length=1000, blank=True)

    RADIO = 'CH'
    BUTTON = 'BU'
    RANGE_MINUTES = 'RA'
    RANGE_SIZE ='RA-S'
    RANGE_LITRES = 'RA-L'
    RANGE_LITRES_BIG = 'RA-LB'
    RANGE_NUMBER_OF_BUCKETS ='RA-B'
    RANGE_TIMES = 'RA-T'
    RANGE_AREA = 'RA-Area'
    RANGE_PETS = 'RA-Pets'
    TYPES_OF_CHOICES = [
        (RADIO, 'Radio'),
        (BUTTON, 'Button'),
        (RANGE_MINUTES, 'Range for minutes'),
        (RANGE_SIZE, 'Range for size of bucket'),
        (RANGE_LITRES,'Range for Litres(0-30)'),
        (RANGE_NUMBER_OF_BUCKETS,'Range for Number of Buckets'),
        (RANGE_TIMES, 'Range for number of times'),
        (RANGE_LITRES_BIG, 'Range for Litres big(0-100)'),
        (RANGE_AREA, 'Range for Area of garden'),
        (RANGE_PETS,'Range for number of pets')

    ]

    Option_type = models.CharField(max_length=100,choices=TYPES_OF_CHOICES)


    def __str__(self):
        return str(self.category) + '-'+ str(self.question)





class Options(models.Model):
    id = models.BigIntegerField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    option = models.CharField(max_length=100)
    order = models.PositiveSmallIntegerField()
    next_question = models.PositiveSmallIntegerField()
    water_used = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,help_text='Water used in litres')


    def __str__(self):
        return (str(self.question) + str(self.option))
#
#
#
# class Result(models.Model):
#     pincode = models.PositiveSmallIntegerField(help_text="Please enter your 6 digit pin code")
#     state = models.CharField(max_length=100,editable=False)
#     category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
#     question = models.ForeignKey(Question,on_delete=models.DO_NOTHING)
#     answer = models.ForeignKey(Options,on_delete=models.DO_NOTHING)
#     water_used = models.DecimalField(max_digits=10,decimal_places=2)
#
#
#
#
# #
# # class Submission(models.Model):
# #     pincode = models.PositiveSmallIntegerField()
# #     state = models.CharField(max_length=100,editable=False)
# #     # total_in_all_categories = models.DecimalField(decimal_places=2,max_digits=10)
# #
#     def define_state(self):
#         pincode = str(self.pincode)
#         if(pincode.startswith('11')):
#             self.state='Delhi'
#         elif(pincode.startswith('12') or pincode.startswith('13')):
#             self.state='Haryana'
#         elif (pincode.startswith('14') or pincode.startswith('15') or pincode.startswith('16')):
#             self.state = 'Punjab'
#         elif (pincode.startswith('17')):
#             self.state = 'Himachal Pradesh'
#         elif (pincode.startswith('18') or pincode.startswith('19')):
#             self.state = 'Jammu & Kashmir'
#         elif (pincode.startswith('20') or pincode.startswith('21') or pincode.startswith('22') or pincode.startswith('23') or pincode.startswith('24') or pincode.startswith('25') or pincode.startswith('26') or pincode.startswith('27') or pincode.startswith('28')):
#             self.state = 'Uttar Pradesh'
#         elif (pincode.startswith('30') or pincode.startswith('31') or pincode.startswith('32') or pincode.startswith('33') or pincode.startswith('34')):
#             self.state = 'Rajasthan'
#         elif (pincode.startswith('36') or pincode.startswith('37') or pincode.startswith('38') or pincode.startswith('39')):
#             self.state = 'Gujarat'
#         elif (pincode.startswith('40') or pincode.startswith('41') or pincode.startswith('42') or pincode.startswith('43') or pincode.startswith('44')):
#             self.state = 'Maharashtra'
#         elif (pincode.startswith('45') or pincode.startswith('46') or pincode.startswith('47') or pincode.startswith('48')):
#             self.state = 'Madhya Pradesh'
#         elif (pincode.startswith('49')):
#             self.state = 'Chattisgarh'
#         elif (pincode.startswith('50') or pincode.startswith('51') or pincode.startswith('52') or pincode.startswith('53')):
#             self.state = 'Andhra Pradesh'
#         elif (pincode.startswith('56') or pincode.startswith('57') or pincode.startswith('58') or pincode.startswith('59')):
#             self.state = 'Karnataka'
#         elif (pincode.startswith('60') or pincode.startswith('61') or pincode.startswith('62') or pincode.startswith('63') or pincode.startswith('64')):
#             self.state = 'Tamil Nadu'
#         elif (pincode.startswith('682')):
#             self.state = 'Lakshwadeep'
#         elif (pincode.startswith('67') or pincode.startswith('68') or pincode.startswith('69')):
#             self.state = 'Kerala'
#         elif (pincode.startswith('744')):
#             self.state = 'Andaman & Nicobar'
#         elif (pincode.startswith('70') or pincode.startswith('71') or pincode.startswith('72') or pincode.startswith('73') or pincode.startswith('74')):
#             self.state = 'West Bengal'
#         elif (pincode.startswith('75') or pincode.startswith('76') or pincode.startswith('77')):
#             self.state = 'Odisha'
#         elif (pincode.startswith('78')):
#             self.state = 'Assam'
#         elif (pincode.startswith('79')):
#             self.state = 'Arunachal Pradesh'
#         elif (pincode.startswith('80') or pincode.startswith('81') or pincode.startswith('82') or pincode.startswith('83') or pincode.startswith('84') or pincode.startswith('85')):
#             self.state = 'Bihar'
#         else:
#             self.state = 'Others'
#
#
#
#
#
#     def save(self):
#         self.define_state()
#         super(Result,self).save()
#


        # 79 - Arunachal
        # Pradesh
        # 79 - Manipur
        # 79 - Meghalaya
        # 79 - Mizoram
        # 79 - Nagaland
        # 79 - Tripura
        # 80 - 85
        # Bihar
        # 80 - 83, 92
        # Jharkhand

#
# class Question_category(models.Model):
#     user = models.ForeignKey(Submission, on_delete=models.CASCADE)
#     category = models.CharField(max_length=100,)
#     total_in_category = models.DecimalField(decimal_places=2, max_digits=10)
#
#
# class Question_answer(models.Model):
#     user = models.ForeignKey(Submission,default=4,on_delete=models.CASCADE)
#     category = models.ForeignKey(Question_category,on_delete=models.CASCADE)
#     question = models.CharField(max_length=100)
#     answer = models.CharField(max_length=100)
#     water_used = models.DecimalField(null=True,blank=True,decimal_places=2,max_digits=10)



# class Continent(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     code = models.CharField(max_length=2, unique=True, primary_key=False)
#
#     class Meta:
#         ordering = ["name"]
#
#
# class Country(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     capital = models.CharField(max_length=255)
#     code = models.CharField(max_length=2, unique=True, primary_key=False)
#     continent = models.ForeignKey('Continent', related_name='countries',on_delete=models.CASCADE)
#     population = models.PositiveIntegerField()
#     area = models.PositiveSmallIntegerField()
#     class Meta:
#         ordering = ["name"]



##### FINAL ACCEPTED CODE ######

class User(models.Model):

    pincode = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=False,auto_now_add=True)
    state = models.CharField(max_length=100, editable=False)
    total_water_usage = models.DecimalField(default=0,max_digits=10,decimal_places=2,editable=False)

    def define_state(self):
        pincode = str(self.pincode)
        if(pincode.startswith('11')):
            self.state='delhi'
        elif(pincode.startswith('12') or pincode.startswith('13')):
            self.state='haryana'
        elif (pincode.startswith('14') or pincode.startswith('15') or pincode.startswith('16')):
            self.state = 'punjab'
        elif (pincode.startswith('17')):
            self.state = 'himachalpradesh'
        elif (pincode.startswith('18') or pincode.startswith('19')):
            self.state = 'jammu&kashmir'
        elif (pincode.startswith('20') or pincode.startswith('21') or pincode.startswith('22') or pincode.startswith('23') or pincode.startswith('24') or pincode.startswith('25') or pincode.startswith('26') or pincode.startswith('27') or pincode.startswith('28')):
            self.state = 'uttarpradesh'
        elif (pincode.startswith('30') or pincode.startswith('31') or pincode.startswith('32') or pincode.startswith('33') or pincode.startswith('34')):
            self.state = 'rajasthan'
        elif (pincode.startswith('36') or pincode.startswith('37') or pincode.startswith('38') or pincode.startswith('39')):
            self.state = 'gujarat'
        elif (pincode.startswith('40') or pincode.startswith('41') or pincode.startswith('42') or pincode.startswith('43') or pincode.startswith('44')):
            self.state = 'maharashtra'
        elif (pincode.startswith('45') or pincode.startswith('46') or pincode.startswith('47') or pincode.startswith('48')):
            self.state = 'madhyaPradesh'
        elif (pincode.startswith('49')):
            self.state = 'chattisgarh'
        elif (pincode.startswith('50') or pincode.startswith('51') or pincode.startswith('52') or pincode.startswith('53')):
            self.state = 'andhrapradesh'
        elif (pincode.startswith('56') or pincode.startswith('57') or pincode.startswith('58') or pincode.startswith('59')):
            self.state = 'karnataka'
        elif (pincode.startswith('60') or pincode.startswith('61') or pincode.startswith('62') or pincode.startswith('63') or pincode.startswith('64')):
            self.state = 'tamilnadu'
        elif (pincode.startswith('682')):
            self.state = 'lakshwadeep'
        elif (pincode.startswith('67') or pincode.startswith('68') or pincode.startswith('69')):
            self.state = 'kerala'
        elif (pincode.startswith('744')):
            self.state = 'andamannicobar'
        elif (pincode.startswith('70') or pincode.startswith('71') or pincode.startswith('72') or pincode.startswith('73') or pincode.startswith('74')):
            self.state = 'westbengal'
        elif (pincode.startswith('75') or pincode.startswith('76') or pincode.startswith('77')):
            self.state = 'odisha'
        elif (pincode.startswith('78')):
            self.state = 'assam'
        elif (pincode.startswith('79')):
            self.state = 'arunachalpradesh'
        elif (pincode.startswith('80') or pincode.startswith('81') or pincode.startswith('82') or pincode.startswith('83') or pincode.startswith('84') or pincode.startswith('85')):
            self.state = 'bihar'
        else:
            self.state = 'others'





    def save(self):
        self.define_state()
        super(User,self).save()

class category_wise_result(models.Model):
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    category_usage = models.DecimalField(max_digits=10,decimal_places=2,editable=False,default=0)


class question_wise_result(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=1)
    question = models.ForeignKey(Question,on_delete=models.DO_NOTHING)
    answer = models.ForeignKey(Options,on_delete=models.DO_NOTHING,blank=True,null=True)
    water_used = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True,default=0)

    def find_water_used(self):

        if self.question.id==6:
            print(int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=2)[0].answer.water_used))
            print(int(self.answer.option.split()[0]))
            a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=2)[0].answer.water_used) * int(self.answer.option.split()[0])
            print(a)
            self.water_used=a

        elif self.question.id==5:
            a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=3)[0].answer.water_used) * int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=4)[0].answer.water_used) * int(self.answer.option.split()[0])
            print(a)
            self.water_used=a

        elif self.question.id==7:
            a =  int(self.answer.option.split()[0])*2.83
            print(a)
            self.water_used=a
        elif self.question.id==8:
            a =  int(self.answer.option.split()[0])*2.83
            print(a)
            self.water_used=a

        elif self.question.id==10:
            a =self.answer.water_used

            self.water_used=a

        elif self.question.id==12:
            a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=11)[0].answer.water_used) * int(self.answer.option.split()[0]) * 3 #using 3 as average no. of times a day a person goes to washroom
            self.water_used=a

        elif self.question.id==17:
            a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=14)[0].answer.water_used) * int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=15)[0].answer.water_used) * int(self.answer.option.split()[0])
            # print(a)
            self.water_used=a

        elif self.question.id==18:
            a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=16)[0].answer.water_used) * int(self.answer.option.split()[0])/7
            # print(a)
            self.water_used=a

        elif self.question.id==21:
            a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=20)[0].answer.water_used) * int(self.answer.option.split()[0])
            # print(a)
            self.water_used=a

        elif self.question.id==22:
            a = int(self.answer.option.split()[0])
            # print(a)
            self.water_used=a

        elif self.question.id==24:
            a = self.answer.water_used
            self.water_used=a

        elif self.question.id == 25:
            a = int(self.answer.water_used) *2 # 2 because on average 2 times utensils are washed
            # print('a')
            # print(a)
            self.water_used = a

        elif self.question.id == 26:
            a = self.answer.water_used
            # print('next a')
            # print(a)
            self.water_used = a

        elif self.question.id==28:
            a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=27)[0].answer.water_used) * int(self.answer.water_used)
            # print(a)
            self.water_used=a

        elif self.question.id==29:
            if self.answer.id==308:
                a=(int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=27)[0].answer.water_used)*3)*-1
                # print(a)
                self.water_used=a
            else:
                self.water_used = 0

        elif self.question.id==32:
            a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=31)[0].answer.water_used) * int(self.answer.water_used) /7
            # print(a)
            self.water_used=a

        elif self.question.id==35:
            a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=34)[0].answer.water_used) * int(self.answer.water_used) /7
            # print(a)
            self.water_used=a

        elif self.question.id==37:
            a = self.answer.water_used
            # print(a)
            self.water_used=a

        elif self.question.id==38:
            a = self.answer.water_used
            # print(a)
            self.water_used=a

        elif self.question.id==41:
            a = self.answer.water_used
            print(a)
            self.water_used=a

        elif self.question.id==43:
            a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=42)[0].answer.water_used) * int(self.answer.water_used) / 365
            print(a)
            self.water_used=a

        elif self.question.id==44:
            a = self.answer.water_used
            print(a)
            self.water_used=a

        elif self.question.id == 46:
            a = self.answer.water_used
            print(a)
            self.water_used = a*-1

        elif self.question.id == 47:
            if self.answer.id==549:
                a = ((90000/365)/4.5)
                self.water_used = a * -1
            else:
                self.water_used=0

        elif self.question.id == 46:
            a = self.answer.water_used
            print(a)
            self.water_used = a*-1

        # elif self.question.id ==12:
        #     a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=11)[0].answer.option.split()[0]*3) * int(self.answer.option.split()[0])
        #     self.water_used = a
        #
        # elif self.question.id ==18:
        #     a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=16)[0].answer.water_used) * int(self.answer.option.split()[0])
        #     self.water_used = a
        # elif self.question.id ==17:
        #     a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=14)[0].answer.water_used) * int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=15)[0].answer.water_used) * int(self.answer.option.split()[0])
        #     self.water_used = a
        #
        # elif self.question.id ==22:
        #     a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=21)[0].answer.water_used) * int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=20)[0].answer.water_used) * int(self.answer.option.split()[0])
        #     self.water_used = a
        #
        # elif self.question.id ==27:
        #     a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=26)[0].answer.water_used) * int(self.answer.option.split()[0])
        #     self.water_used = a
        #
        # elif self.question.id ==31 or self.question.id ==33:
        #     a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=29)[0].answer.water_used) * int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=30)[0].answer.water_used)
        #     self.water_used = a
        # # elif self.question.id ==45:
        # #     a = int(question_wise_result.objects.filter(user_id=self.user_id).filter(question_id=44)[0].answer.water_used) * int(self.answer.option.split()[0])
        # #     self.water_used = a
        #
        #
        # else:
        #     return

    def save(self,*args,**kwargs):
        self.find_water_used()
        super(question_wise_result,self).save(*args,**kwargs)





