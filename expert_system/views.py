from django.views import View
from django.shortcuts import render


class HomeView(View):
    def get(self, request):
        context = {
            "title": "Home",
            "nav_home": "active",
        }
        return render(request, "index.html", context)


class FormView(View):
    def get(self, request):
        context = {
            "title": "Form",
        }
        return render(request, "form.html", context)


class AboutView(View):
    def get(self, request):
        context = {
            "title": "Tentang",
            "nav_about": "active",
        }
        return render(request, "about.html", context)


class ResultView(View):
    def get(self, request):
        context = {
            "title": "Hasil",
        }
        return render(request, "result.html", context)

    def post(self, request):
        nama = request.POST.get("nama")
        bangun_pagi = request.POST.get("bangun_pagi")
        begadang = request.POST.get("begadang")
        fokus = request.POST.get("fokus")
        segar = request.POST.get("segar")
        jadwal_kuliah = request.POST.get("jadwal_kuliah")
        rutinitas = request.POST.get("rutinitas")
        result = None
        # Pagi Hari
        if bangun_pagi == "0":
            if begadang == "0":
                if fokus == "pagi":
                    if segar == "pagi":
                        if jadwal_kuliah == "pagi":
                            if rutinitas == "pagi":
                                result = "Pagi Hari"
        # Siang Hari
        if bangun_pagi == "1":
            if begadang == "0":
                if fokus == "siang":
                    if segar == "siang":
                        if jadwal_kuliah == "siang":
                            if rutinitas == "siang":
                                result = "Siang Hari"
        # Malam Hari
        if bangun_pagi == "1":
            if begadang == "1":
                if fokus == "malam":
                    if segar == "malam":
                        if jadwal_kuliah == "malam":
                            if rutinitas == "malam":
                                result = "Malam Hari"
        context = {
            "title": "Hasil",
            "nama": nama,
            "result": result,
        }
        return render(request, "result.html", context)
