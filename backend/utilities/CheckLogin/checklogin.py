from django.contrib.auth import authenticate, login


def CheckLogin(request,username, password):
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return True
    else:
        return False
