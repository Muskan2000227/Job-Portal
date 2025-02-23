from django.shortcuts import render,redirect

# Create your views here.
from .models import register_user,register_emp,Jobs,Experience,Education,Skills,Resume,Saved

def mainpage(request):
    return render(request,'mainpage.html')


def signup_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        confirm_password = request.POST.get('cpass')

        if password != confirm_password:
            return render(request, 'signup_user.html')

        if register_user.objects.filter(email=email).exists():
            return render(request, 'signup_user.html')

        # Create new user
        register_user.objects.create(username=username, email=email, passw=password)
        return redirect('login_user')  # Redirect to the login page

    return render(request, 'signup_user.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('passw')
        user = register_user.objects.get(email=email)
        request.session['user_email'] = email 
        if user.passw == password: 
            request.session['user_id'] = user.id 
            return redirect('afterlogin')
    return render(request, 'login_user.html')  
      
def afterlogin(request):
    return render(request,'afterlogin.html')

def logout_user(request):
     if not request.session.has_key('email'):
          return redirect('/login_user')
     del request.session['email']
     return redirect('/login_user')    

def signup_emp(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        confirm_password = request.POST.get('cpass')

        if password != confirm_password:
            return render(request, 'signup_emp.html')

        if register_emp.objects.filter(email=email).exists():
            return render(request, 'signup_emp.html')

        # Create new user
        register_emp.objects.create(username=username, email=email, passw=password)
        return redirect('login_emp')  # Redirect to the login page

    return render(request, 'signup_emp.html')

def login_emp(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('passw')
        user = register_emp.objects.get(email=email)
        request.session['user_email'] = email 
        if user.passw == password: 
            request.session['user_id'] = user.id 
            return redirect('afterlogine')
    return render(request, 'login_emp.html') 


def afterlogine(request):
    return render(request,'afterlogine.html')

def logout_emp(request):
     if not request.session.has_key('email'):
          return redirect('/login_emp')
     del request.session['email']
     return redirect('/login_emp')     

def Home(request):
    return render(request,'Home.html') 



def Home(request):
    categories = Jobs.objects.values_list('category', flat=True).distinct()
    locations = Jobs.objects.values_list('location', flat=True).distinct()

    return render(request, 'Home.html', {'categories': categories, 'locations': locations})


from django.shortcuts import render
from .models import Jobs

from django.shortcuts import render
from .models import Jobs

def job_search(request):
    category = request.GET.get('cat', '')  # Get category from request
    location = request.GET.get('ct', '')  # Get location from request

    # Filter only available jobs
    jobs = Jobs.objects.filter(status="available")

    if category:
        jobs = jobs.filter(category=category)  # ✅ Directly filter based on category field
    if location:
        jobs = jobs.filter(location=location)  # ✅ Directly filter based on location field

    return render(request, 'job_results.html', {'jobs': jobs})

def companyprf(request):
    return render(request,'companyprf.html')

def editcompprf(request):
    return render(request,'editcompprf.html')

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Jobs

def addjob(request):
    if request.method == "POST":
        # Retrieve data from the form
        title = request.POST.get('title')
        description = request.POST.get('description')
        budget_salary = request.POST.get('budget_salary')
        education_req = request.POST.get('education_req', '')
        experience_req = request.POST.get('experience_req', '')
        job_type = request.POST.get('job_type')
        category = request.POST.get('category')
        location = request.POST.get('location')
        jobtag = request.POST.get('jobtag')
        deadline = request.POST.get('deadline')
        vacancies = request.POST.get('vacancies', '')
        status = request.POST.get('status', 'available')
        employer = request.POST.get('employer', '')

        # Create a new job instance and save it to the database
        job = Jobs(
            title=title,
            description=description,
            budget_salary=budget_salary,
            education_req=education_req,
            experience_req=experience_req,
            job_type=job_type,
            category=category,
            location=location,
            jobtag=jobtag,
            deadline=deadline,
            vacancies=vacancies,
            status=status,
            employer=employer
        )
        job.save()

        return render(request,'addjob.html',{'msg':"Added successfully"})  # Redirect to a success page after saving the job

    return render(request, 'addjob.html')  # Render the job form if not a POST request




def jobshowcomp(request):
    email = request.session.get('user_email')  
    
    # Fetch the username associated with the logged-in user's email
    user = register_emp.objects.get(email=email)
    username = user.username  # Get the username from the register_emp model
        
        
    # Filter jobs where the employer matches the username
    jobs = Jobs.objects.filter(employer=username)

    # Check if no jobs are found
    message = "No jobs available for you." if not jobs else None
    
    return render(request, 'jobshowcomp.html', {'jobs': jobs, 'message': message})


def experienceuser(request):
    email = request.session.get('user_email')
    try:
        user_instance = register_user.objects.get(email=email)  # Fetch user instance
    except register_user.DoesNotExist:
        print(f"User does not exist: {email}")  # Debugging output
        user_instance = None

    data = Experience.objects.filter(user=user_instance) if user_instance else []  # Correct way to filter

    if request.method == 'POST' and user_instance:
        cpn = request.POST.get('cpn')
        jt = request.POST.get('jt')
        sp = request.POST.get('sp')
        ep = request.POST.get('ep')
        resp = request.POST.get('resp')

        Experience.objects.create(
            user=user_instance,
            company_name=cpn,
            role=jt,
            start_date=sp,
            end_date=ep,
            responsibility=resp
        )

    return render(request, 'experienceuser.html', {'data': data})


def educationuser(request):
    email = request.session.get('user_email')   
    user_instance = register_user.objects.get(email=email)  # Fetch user instance
    data = Education.objects.filter(user=user_instance) # Correct way to filter

    if request.method == 'POST':
        el=request.POST.get('el')
        mj=request.POST.get('mj')
        inst=request.POST.get('inst')
        rst=request.POST.get('rst')
        ep=request.POST.get('ep')
        sp=request.POST.get('sp')

        Education.objects.create(
            user=user_instance,
            title=el,
            stream=mj,
            college=inst,
            result=rst,
            endingperiod=ep,
            startingperiod=sp
        )

    return render(request, 'educationuser.html', {'data': data})

def skillsuser(request):
    email = request.session.get('user_email')   
    user_instance = register_user.objects.get(email=email)  # Fetch user instance
    data = Skills.objects.filter(user=user_instance)
    if request.method == 'POST':
        skill=request.POST.get('skill')
        Skills.objects.create(user=user_instance,skills=skill )   
    return render(request,'skillsuser.html',{'data':data})

# def resume(request):
#     return render(request,'resume.html')



from django.shortcuts import render, redirect
from .models import Resume, register_user

def resume(request):
    email = request.session.get('user_email')   
    user_instance = register_user.objects.get(email=email)  
    data = Resume.objects.filter(user=user_instance)  
    resume = Resume.objects.first()  # Fetch the first resume
    print(resume.resume.url) 
    if request.method == 'POST' and user_instance:
        resume_file = request.FILES.get('resume')  
        if resume_file:  # Only create resume if there's a file uploaded
            Resume.objects.create(user=user_instance, resume=resume_file)  # Save resume
        return redirect('resume')  # Reload the page to clear the input field

    return render(request, 'resume.html', {'data': data,'resume':resume})


from django.shortcuts import render, redirect
from .models import Saved, Jobs, register_user

def savedjobs(request):
    email = request.session.get('user_email')   
    user_instance = register_user.objects.get(email=email)  # Fetch user instance

    job_id = request.POST.get('job_id')  # Get job ID from POST request

    if job_id:
        job_instance = Jobs.objects.get(id=job_id)  # Fetch the job
        # Check if the job is already saved before creating a new entry
        if not Saved.objects.filter(seeker=user_instance, job=job_instance, status='Save').exists():
            Saved.objects.create(seeker=user_instance, job=job_instance, status='Save')

        return redirect('savedjobs')  # Redirect to prevent form resubmission

    data = Saved.objects.filter(seeker=user_instance, status='Save')  # Fetch saved jobs
    return render(request, 'savedjobs.html', {'data': data})







from django.shortcuts import render, redirect
from .models import Saved, Jobs, register_user

def appliedjobs(request):
    email = request.session.get('user_email')   
    user_instance = register_user.objects.get(email=email)  # Fetch user instance

    job_id = request.POST.get('job_id')  # Get job ID from POST request

    if job_id:
        job_instance = Jobs.objects.get(id=job_id)  # Fetch the job
        # Check if the job is already saved before creating a new entry
        if not Saved.objects.filter(seeker=user_instance, job=job_instance, status='Apply').exists():
            Saved.objects.create(seeker=user_instance, job=job_instance, status='Apply')

        return redirect('appliedjobs')  # Redirect to prevent form resubmission

    data = Saved.objects.filter(seeker=user_instance, status='Apply')  # Fetch saved jobs
    return render(request, 'appliedjobs.html', {'data': data})

    
   

from django.shortcuts import render, get_object_or_404
def jobresshow(request, job_id):
    job = get_object_or_404(Jobs, id=job_id)  # Fetch the job by ID
    return render(request, 'jobresshow.html', {'job': job})

def alljobs(request):
    jobs = Jobs.objects.all()  # Fetch the job by ID
    return render(request, 'alljobs.html', {'jobs': jobs})


def alljobsdetails(request, job_id):
    job = get_object_or_404(Jobs, id=job_id)  # Fetch the job by ID
    return render(request, 'alljobsdetails.html', {'job': job})


# def candidates(request):
#     email = request.session.get('user_email')  # Get employer's email from session
#     jobs_posted = Jobs.objects.filter(employer=email)  # Get jobs posted by this employer
    
#     # Fetch applications related to these jobs
#     applied_jobs = Saved.objects.filter(job__in=jobs_posted, status="Apply").select_related('seeker', 'job')

#     return render(request, 'candidates.html', {'applied_jobs': applied_jobs})

from django.shortcuts import render
from .models import Saved, Jobs, register_emp, register_user  # Import employer model

def candidates(request):
    email = request.session.get('user_email')  # Get logged-in employer's email

    if not email:
        return render(request, 'candidates.html', {'applied_jobs': [], 'error': 'Employer not logged in'})

    # Fetch the employer's username using email
    try:
        employer_instance = register_emp.objects.get(email=email)
        employer_username = employer_instance.username  # Get the employer's username
    except register_emp.DoesNotExist:
        return render(request, 'candidates.html', {'applied_jobs': [], 'error': 'Employer not found'})

    # Get jobs posted by the employer
    jobs_posted = Jobs.objects.filter(employer=employer_username)

    # Fetch candidates who applied for these jobs
    applied_jobs = Saved.objects.filter(job__in=jobs_posted, status="Apply").select_related('seeker', 'job')

    return render(request, 'candidates.html', {'applied_jobs': applied_jobs})



def resume(request):
    return render(request,'resume.html')

def resume2(request):
    return render(request,'resume2.html')
