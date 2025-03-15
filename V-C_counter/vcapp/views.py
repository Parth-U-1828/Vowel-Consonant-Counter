from django.shortcuts import render

def home(request):
	if request.GET.get("txt"):
		txt = request.GET.get("txt")
		vc , cc = 0, 0 
		for t in txt:
			if t != " ":
				if t.isalpha():
					if t in "aeiouAEIOU":
						vc = vc + 1
					else:
						cc = cc + 1
		msg = "vc = " + str(vc) + "cc= " + str(cc)
		return render(request,"home.html",{"msg":msg,"txt":txt})
	else:
		return render(request,"home.html")
		