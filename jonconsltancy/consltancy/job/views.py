from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage

# Create your views here.
def index(request):
    return render(request,'index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        status = request.POST.get('status')
        city = request.POST.get('city')
        email=request.POST.get('email')
        address = request.POST.get('address')
        position = request.POST.get('position')
        spcl = request.POST.get('spcl')
        qualification = request.POST.get('qualification')
        exp = request.POST.get('exp')
        year = request.POST.get('year')
        cv = request.FILES['cv']
        sp = request.POST.get('sp')
        industry = request.POST.get('industry')
        salary = request.POST.get('industry')
        area = request.POST.get('area')




        '''except MultiValueDictKeyError:
            phone = False
            message = False'''
        template = get_template('reg.txt')
        context = {'name': name, 'number':number,'dob':dob,'gender':gender,'city':city,'address':address,'status':status ,'email':email,'cv':cv,'year':year,'exp':exp,'qualification':qualification,'spcl':spcl,'position':position,'sp':sp,'salary':salary,'industry':industry,'area':area,}
        print(context)
        content = template.render(context)
        print(content)
        email = EmailMessage(
            "Contact form Recieved",
            content,
            "Contact Form" + '',
            ['envvumarketing3@gmail.com', 'envvumarketing6@gmail.com'],
            headers={'Reply To': email}
        )
        email.attach(cv.name,cv.read(),cv.content_type)
        email.send()
        # messages.success(request, f'Thank You For Contacting Us , Our Executive Will Contact You Soon')
        html = "<html><body></body></html> "
        return HttpResponse(html)
    return render(request, 'pages-contact-1.html')

def thank(request):
    return render(request,'thank.html')



