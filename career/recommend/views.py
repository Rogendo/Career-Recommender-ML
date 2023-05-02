from django.shortcuts import render
import pickle

# loading the model
pickle_in=open('recommend/saved_model/trained_model.pkl','rb')
model=pickle.load(pickle_in)

# Create your views here.

def index(request):
    return render(request,'recommend/main.html')

def Forminfo(request):
    grade=request.GET['grade']
    percentage=request.GET['percentage']
    careercategory=request.GET['careercategory']
    talent=request.GET['talent']
    y_pred = model.predict([[grade,percentage,careercategory,talent]])
    print(y_pred)
    if y_pred==0:
        y_pred='is Science Engineering and Technology'
    elif y_pred==1:
        
        y_pred="is Social Sciences"
    elif y_pred==2:
        y_pred="is Sports Science"
    
    else:
        y_pred="Failed To recommend"
    print(y_pred)
    return render(request,'recommend/results.html',{'result':y_pred})