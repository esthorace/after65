from django.shortcuts import redirect, render

from . import forms, models


def index(request):
    return render(request, "Coder/index.html")


def profesor_list(request):
    consulta = models.Profesor.objects.all()
    contexto = {"profesores": consulta}
    return render(request, "Coder/profesor_list.html", contexto)


def profesor_form(request):
    if request.method == "POST":
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profesor_list")
    else:
        form = forms.ProfesorForm()
    return render(request, "Coder/profesor_form.html", {"form": form})
