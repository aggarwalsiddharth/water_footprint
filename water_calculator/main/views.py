from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,get_object_or_404,redirect

from .models import Category,Question,Options,User,question_wise_result,category_wise_result
from .forms import Pincode
from django.db.models import Avg


from rest_framework.views import APIView
from rest_framework.response import Response



from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw





user = 0


def home_view(request,*args,**kwargs):

    form = Pincode(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        global user
        user= instance.id
        return redirect("/question/1")
    else:
        return render(request,"front_page.html",{'form':form})


def question_view(request,id):

    obj1 = Question.objects.filter(order = id)
    obj2 = Options.objects.filter(order = id)
    obj3 = Question.objects.all()
    context={

        'question' : obj1[0],
        'option' : obj2,
        'total_ques':obj3
     }
    if request.method=="POST":
        data = request.POST
        user_object = User.objects.get(id=user)
        print(user_object)
        answer = obj2.get(option=data['answer'])
        print(answer)
        new_ques_id = answer.next_question + id
        print("user_object=")
        print(user_object)
        print("category")
        print(obj1[0].category)
        print("question")
        print(obj1[0])
        print("answer")
        print(answer)

        question_wise_result.objects.create(user_id=user_object,category=obj1[0].category,question=obj1[0],answer=answer)

        if new_ques_id==120:
            return redirect('/result/')
        else:
            return redirect('/question/'+str(new_ques_id))

    return render(request, "main/questions.html", context)

def result_view(request):
    user_object = User.objects.get(id=user)
    print('im in this func2')

    total = 0
    for i in Category.objects.all():
        a = question_wise_result.objects.filter(category_id=i.id, user_id=user_object.id)
        for x in a:
            total += x.water_used
    if total<=150:

        img = Image.open("static/main/less_img.png")
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype("static/main/sans-serif.ttf", 48)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((581, 204), "You daily consumption", (0, 0, 0), font=font)
        draw.text((565, 260), " of water is 40 Litres less ", (0, 0, 0), font=font)
        draw.text((580, 310), " than an averge Indian.", (0, 0, 0), font=font)
        draw.text((450, 390), " Your savings will go a long way", (0, 0, 0), font=font)
        draw.text((580, 440), " in sustaining the future.", (0, 0, 0), font=font)

        img.save('static/main/results/'+ str(user_object.id) +'.png')
    else:
        img = Image.open('static/main/more_img.png')
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype("static/main/sans-serif.ttf", 48)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((581, 204), "You daily consumption", (0, 0, 0), font=font)
        draw.text((565, 260), " of water is 40 Litres more ", (0, 0, 0), font=font)
        draw.text((580, 310), " than an averge Indian.", (0, 0, 0), font=font)
        draw.text((450, 390), " You should focus on saving water that will help", (0, 0, 0), font=font)
        draw.text((580, 440), " in sustaining the future.", (0, 0, 0), font=font)
        img.save('static/main/results/' + str(user_object.id) + '.png')



    context = {


        'current_user_total': 20,
        'uganda' : int(int(total)//7.5),
        'bangladesh': int(total)//50,
        'china':int(total)//80,
        'australia': (24/500)*(int(total)),
        'america': (24/580)*(int(total)),
        'result_image':str('/static/main/results/' + str(user_object.id) + '.png'),
        'result_video':str('/static/main/' + str(user_object.state) + '.mp4'),
        'user_state': str(user_object.state).capitalize(),
        }



    return render(request,'main/results.html',context)


class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        user_object = User.objects.get(id=user)
        print('im in this func')
        labels = []
        water = []
        total = 0
        for i in Category.objects.all():
            a = question_wise_result.objects.filter(category_id=i.id, user_id=user_object.id)
            water_use = 0
            for x in a:
                water_use += x.water_used
                total += x.water_used
            water.append(int(water_use))
            labels.append(i.name)
            category_wise_result.objects.create(user_id=user_object, category=i, category_usage=water_use)
        User.objects.get(id=user_object.id).total_water_usage = int(total)
        average = User.objects.aggregate(Avg('total_water_usage'))

        data = {
            'labels': labels,
            'default': water,
            'current_user_total':total,
            'average_total':average

        }

        return Response(data)