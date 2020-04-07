from django.contrib.auth import authenticate, login, get_user_model
# for user authentication
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm


# Create your views here.
def getIndexPage(request):
    return render(request, "eapp/index.html")


def getLoginPage(request):
    form = LoginForm(request.POST or None)
    context = {'form': form}
    print("user logged in")
    # print(request.user.is_authenticated())
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        # print(request.user.is_authenticated())
        if user is not None:
            # print(request.user.is_authenticated())
            login(request, user)
            # return to successfull page
            # context['forms'] = LoginForm()
            return redirect('')
            # return redirect('/login')
        else:
            print("error")

    return render(request, "eapp/login.html", context)


User = get_user_model()


def getRegisterPage(request):
    form = RegisterForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        pass
        # print(form.cleaned_data)
        # username = form.cleaned_data.get('username')
        # email = form.cleaned_data.get('email')
        # dob = form.cleaned_data.get('dob')
        # address = form.cleaned_data.get('address')
        # new_user = User.objects.create_user(username, email, dob, address)
        # print(new_user)
    return render(request, "eapp/register.html", context)


