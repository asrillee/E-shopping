from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.views.generic import View
from . forms import UserForm, UserLoginForm

def index(request):
    # all_excelfiles = Cust_Feedback.objects.all()
    # context = {'all_excelfiles': all_excelfiles}
    #html = ''
    #for files in all_excelfiles:
     #   url = '/excelhandler/' + str(files.id) + '/'
      #  html += '<a href = "' + url + '">' + files.fileName + '</a><br>'
    #return HttpResponse(template.render(context, request))
    return render(request, 'login/index.html')

class UserFormView(View):
    form_class = UserForm
    template_name = 'login/registration.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            user.profile.email = form.cleaned_data['email']
            user.save()
            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    #print out their name --> request.user.username
                    return redirect('/upload')

        return render(request, self.template_name, {'form': form})

class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'login/index.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)
        dict = {'hello'}
        if form.is_valid():

            #user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #user.set_password(password)
            #user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    # print out their name --> request.user.username
                    return redirect('/upload')
            else:
                return render(request, self.template_name, {'error': 'Username and password do not match.'})
        #return HttpResponse("Hello")
        return render(request, self.template_name, {'form': form, 'dict': dict})