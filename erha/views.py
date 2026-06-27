from django.shortcuts import render

def char_erha(request):
    if request.method == 'GET':
        chars = {
            'title': "Erha's characters",
            'characters':[
                {
            'name':"Chu Wanning",
            'age': 32,
            'element': ["Metal", "Wood"],
            'weapon': ["Tianwen", "Jiuge", "Huaisha"],
            'organization': "Sisheng Peak"
                },
                {
            'name':"Mo Ran",
            'age': 37,
            'element': ["Fire", "Wood"],
            'weapon': ["Jiangui", "Bugui"],
            'organization': "Sisheng Peak"
                },
            ]
        }
    return render(request, 'char1.html', chars )

def info(request):
    if request.method == "GET":
            me1 = {
            'full_name': "Kirkeeva Amina",
            'age': 18,
            'nationality': 'kyrgyz, uighur',
            'height': '175',
            'hobby': ['reading', 'drawing', 'academics', 'gaming']
        }
    return render(request, 'me1.html', me1)