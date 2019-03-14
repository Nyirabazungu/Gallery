from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Gallery')

def images_of_day(request):
    date = dt.date.today()
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Images for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)   

def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day   

# def images_of_day(request):
#     date = dt.date.today()

#     # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    
#     html = f'''
#         <html>
#             <body>
#                 <h1>imagesfor {day} {date.day}-{date.month}-{date.year}</h1>
#             </body>
#         </html>
#             '''
#     return HttpResponse(html) 

def past_days_images(request,past_date):

    try:
           editor = Editor.objects.get(email = 'example@gmail.com')
           print('Editor found')
    except DoesNotExist:
           print('Editor was not found'
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
        # Converts data from the string Url
        if date == dt.date.today():
             return redirect(images_of_day)
        return render(request, 'all-images/past-images.html', {"date": date})      

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>imagesfor {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def welcome(request):
    return render(request, 'welcome.html')

# def images_of_day(request):
#     date = dt.date.today()
#        return render(request, 'all-images/today-images.html', {"date": date,})               