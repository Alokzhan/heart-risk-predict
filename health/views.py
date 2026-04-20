import os
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import datetime

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split

from .forms import DoctorForm
from .models import *
from django.contrib.auth import authenticate, login, logout
import numpy as np
import pandas as pd


# Exact feature order the model was trained on — never change this
HEART_FEATURE_ORDER = [
    'age', 'sex', 'cp', 'trestbps', 'chol',
    'fbs', 'restecg', 'thalach', 'exang',
    'oldpeak', 'slope', 'ca', 'thal'
]


# ─────────────────────────────────────────────
# Public pages
# ─────────────────────────────────────────────

def Home(request):
    return render(request, 'carousel.html')


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Gallery(request):
    return render(request, 'gallery.html')


# ─────────────────────────────────────────────
# Auth
# ─────────────────────────────────────────────

def Login_User(request):
    error = ""
    if request.method == "POST":
        u = request.POST.get('uname', '').strip()
        p = request.POST.get('pwd', '')
        user = authenticate(username=u, password=p)
        if user:
            is_patient = Patient.objects.filter(user=user).exists()
            if is_patient:
                login(request, user)
                error = "pat1"
            else:
                is_approved_doctor = Doctor.objects.filter(status=1, user=user).exists()
                if is_approved_doctor:
                    login(request, user)
                    error = "pat2"
                else:
                    error = "notmember"
        else:
            error = "not"
    return render(request, 'login.html', {'error': error})


def Login_admin(request):
    error = ""
    if request.method == "POST":
        u = request.POST.get('uname', '').strip()
        p = request.POST.get('pwd', '')
        user = authenticate(username=u, password=p)
        if user is not None and user.is_staff:
            login(request, user)
            error = "pat"
        else:
            error = "not"
    return render(request, 'admin_login.html', {'error': error})


def Signup_User(request):
    error = ""
    if request.method == 'POST':
        f         = request.POST.get('fname', '').strip()
        l         = request.POST.get('lname', '').strip()
        u         = request.POST.get('uname', '').strip()
        e         = request.POST.get('email', '').strip()
        p         = request.POST.get('pwd', '')
        d         = request.POST.get('dob', '')
        con       = request.POST.get('contact', '')
        add       = request.POST.get('add', '')
        user_type = request.POST.get('type', '')
        im        = request.FILES.get('image')

        if User.objects.filter(username=u).exists():
            error = "username_exists"
        elif User.objects.filter(email=e).exists():
            error = "email_exists"
        else:
            try:
                user = User.objects.create_user(
                    email=e, username=u, password=p,
                    first_name=f, last_name=l
                )
                if user_type == "Patient":
                    Patient.objects.create(
                        user=user, contact=con, address=add, image=im, dob=d
                    )
                else:
                    Doctor.objects.create(
                        dob=d, image=im, user=user,
                        contact=con, address=add, status=2
                    )
                error = "create"
            except Exception:
                error = "error"
    return render(request, 'register.html', {'error': error})


def Logout(request):
    logout(request)
    return redirect('home')


# ─────────────────────────────────────────────
# Dashboard homes
# ─────────────────────────────────────────────

def Admin_Home(request):
    d = {
        'dis':  Search_Data.objects.count(),
        'pat':  Patient.objects.count(),
        'doc':  Doctor.objects.count(),
        'feed': Feedback.objects.count(),
    }
    return render(request, 'admin_home.html', d)


@login_required(login_url="login")
def User_Home(request):
    return render(request, 'patient_home.html')


@login_required(login_url="login")
def Doctor_Home(request):
    return render(request, 'doctor_home.html')


# ─────────────────────────────────────────────
# Doctor management
# ─────────────────────────────────────────────

@login_required(login_url="login")
def assign_status(request, pid):
    try:
        doctor = Doctor.objects.get(id=pid)
    except Doctor.DoesNotExist:
        messages.error(request, 'Doctor not found.')
        return redirect('view_doctor')

    if doctor.status == 1:
        doctor.status = 2
        messages.success(request, 'Doctor approval has been withdrawn.')
    else:
        doctor.status = 1
        messages.success(request, 'Doctor has been approved successfully.')
    doctor.save()
    return redirect('view_doctor')


@login_required(login_url="login")
def add_doctor(request, pid=None):
    doctor = None
    if pid:
        try:
            doctor = Doctor.objects.get(id=pid)
        except Doctor.DoesNotExist:
            messages.error(request, 'Doctor not found.')
            return redirect('view_doctor')

    if request.method == "POST":
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            new_doc = form.save(commit=False)
            new_doc.status = 1
            if not pid:
                user = User.objects.create_user(
                    password=request.POST['password'],
                    username=request.POST['username'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                )
                new_doc.user = user
            new_doc.save()
            return redirect('view_doctor')
    else:
        form = DoctorForm(instance=doctor)

    return render(request, 'add_doctor.html', {'doctor': doctor, 'form': form})


@login_required(login_url="login")
def View_Doctor(request):
    doc = Doctor.objects.all()
    return render(request, 'view_doctor.html', {'doc': doc})


@login_required(login_url="login")
def delete_doctor(request, pid):
    try:
        Doctor.objects.get(id=pid).delete()
    except Doctor.DoesNotExist:
        messages.error(request, 'Doctor not found.')
    return redirect('view_doctor')


@login_required(login_url="login")
def Edit_Doctor(request, pid):
    try:
        doc = Doctor.objects.get(id=pid)
    except Doctor.DoesNotExist:
        messages.error(request, 'Doctor not found.')
        return redirect('view_doctor')

    error = ""
    if request.method == 'POST':
        doc.user.first_name = request.POST.get('fname', '')
        doc.user.last_name  = request.POST.get('lname', '')
        doc.user.email      = request.POST.get('email', '')
        doc.contact         = request.POST.get('contact', '')
        doc.address         = request.POST.get('add', '')
        doc.category        = request.POST.get('type', '')
        if 'image' in request.FILES:
            doc.image = request.FILES['image']
        doc.user.save()
        doc.save()
        error = "create"

    return render(request, 'edit_doctor.html', {'error': error, 'doc': doc})


# ─────────────────────────────────────────────
# Patient management
# ─────────────────────────────────────────────

@login_required(login_url="login")
def View_Patient(request):
    patient = Patient.objects.all()
    return render(request, 'view_patient.html', {'patient': patient})


@login_required(login_url="login")
def delete_patient(request, pid):
    try:
        Patient.objects.get(id=pid).delete()
    except Patient.DoesNotExist:
        messages.error(request, 'Patient not found.')
    return redirect('view_patient')


# ─────────────────────────────────────────────
# Profile / account
# ─────────────────────────────────────────────

@login_required(login_url="login")
def Change_Password(request):
    user   = request.user
    error  = ""
    terror = ""

    if Patient.objects.filter(user=user).exists():
        sign = Patient.objects.get(user=user)
        error = "pat"
    elif Doctor.objects.filter(user=user).exists():
        sign = Doctor.objects.get(user=user)
    else:
        sign = None

    if request.method == "POST":
        old_pwd = request.POST.get('pwd3', '')
        new_pwd = request.POST.get('pwd1', '')
        confirm = request.POST.get('pwd2', '')
        if not user.check_password(old_pwd):
            terror = "wrong_old"
        elif new_pwd != confirm:
            terror = "not"
        else:
            user.set_password(new_pwd)
            user.save()
            terror = "yes"

    return render(request, 'change_password.html',
                  {'error': error, 'terror': terror, 'data': sign})


@login_required(login_url="login")
def View_My_Detail(request):
    user  = request.user
    error = ""
    if Patient.objects.filter(user=user).exists():
        sign = Patient.objects.get(user=user)
        error = "pat"
    else:
        sign = Doctor.objects.get(user=user)
    return render(request, 'profile_doctor.html', {'error': error, 'pro': sign})


@login_required(login_url="login")
def Edit_My_deatail(request):
    user   = request.user
    error  = ""
    terror = ""

    if Patient.objects.filter(user=user).exists():
        sign = Patient.objects.get(user=user)
        error = "pat"
    else:
        sign = Doctor.objects.get(user=user)

    if request.method == 'POST':
        sign.user.first_name = request.POST.get('fname', '')
        sign.user.last_name  = request.POST.get('lname', '')
        sign.user.email      = request.POST.get('email', '')
        sign.contact         = request.POST.get('contact', '')
        sign.address         = request.POST.get('add', '')
        if 'image' in request.FILES:
            sign.image = request.FILES['image']
        if error != "pat":
            sign.category = request.POST.get('type', '')
        sign.user.save()
        sign.save()
        terror = "create"

    return render(request, 'edit_profile.html',
                  {'error': error, 'terror': terror, 'doc': sign})


# ─────────────────────────────────────────────
# Heart disease prediction
# ─────────────────────────────────────────────

def prdict_heart_disease(list_data):
    """
    FIX 1: Admin CSV nahi hai toh Machine_Learning/heart.csv use karta hai.
    FIX 2: input DataFrame se predict — sklearn warning band hogi.
    FIX 3: HEART_FEATURE_ORDER se correct column order guaranteed.
    """
    csv_file_obj = Admin_Helath_CSV.objects.order_by('-id').first()

    if csv_file_obj:
        csv_path = csv_file_obj.csv_file.path
    else:
        # Fallback: Machine_Learning/heart.csv directly use karo
        csv_path = os.path.join(settings.BASE_DIR, 'Machine_Learning', 'heart.csv')
        if not os.path.exists(csv_path):
            raise ValueError(
                "heart.csv not found. Please upload CSV from admin panel."
            )

    df = pd.read_csv(csv_path)

    X = df[HEART_FEATURE_ORDER]
    y = df['target']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, train_size=0.8, random_state=0
    )

    model = GradientBoostingClassifier(
        n_estimators=100, learning_rate=1.0,
        max_depth=1, random_state=0
    )
    model.fit(X_train, y_train)

    # FIX: DataFrame use karo taaki sklearn warning na aaye
    input_array = [float(v) for v in list_data]
    input_df    = pd.DataFrame([input_array], columns=HEART_FEATURE_ORDER)
    pred        = model.predict(input_df)
    accuracy    = model.score(X_test, y_test) * 100

    return accuracy, pred


@login_required(login_url="login")
def add_heartdetail(request):
    if request.method == "POST":
        post      = request.POST
        list_data = []

        for field in HEART_FEATURE_ORDER:
            val = post.get(field, '').strip()
            if field == 'sex':
                list_data.append(0 if val.lower() in ('male', 'm') else 1)
            else:
                list_data.append(val)

        if len(list_data) != 13 or any(str(v) == '' for v in list_data):
            messages.error(request, 'Please fill in all fields before submitting.')
            return redirect('add_heartdetail')

        try:
            accuracy, pred = prdict_heart_disease(list_data)
        except ValueError as e:
            messages.error(request, str(e))
            return redirect('add_heartdetail')
        except Exception as e:
            messages.error(request, f'Prediction failed: {e}')
            return redirect('add_heartdetail')

        try:
            patient = Patient.objects.get(user=request.user)
        except Patient.DoesNotExist:
            messages.error(request, 'Patient profile not found.')
            return redirect('user_home')

        Search_Data.objects.create(
            patient=patient,
            prediction_accuracy=accuracy,
            result=pred[0],
            values_list=list_data,
        )

        rem = int(pred[0])
        return redirect('predict_desease', str(rem), str(round(accuracy, 2)))

    return render(request, 'add_heartdetail.html')


@login_required(login_url="login")
def predict_desease(request, pred, accuracy):
    try:
        patient = Patient.objects.get(user=request.user)
        doctor  = Doctor.objects.filter(
            address__icontains=patient.address, status=1
        )
    except Patient.DoesNotExist:
        doctor = Doctor.objects.none()

    # FIX: template naam 'predict_desease.html' — aapke folder mein yahi naam hoga
    return render(request, 'predict_desease.html',
                  {'pred': pred, 'accuracy': accuracy, 'doctor': doctor})


@login_required(login_url="login")
def view_search_pat(request):
    user = request.user
    if Doctor.objects.filter(user=user).exists():
        doc  = Doctor.objects.get(user=user)
        data = Search_Data.objects.filter(
            patient__address__icontains=doc.address
        ).order_by('-id')
    elif Patient.objects.filter(user=user).exists():
        pat  = Patient.objects.get(user=user)
        data = Search_Data.objects.filter(patient=pat).order_by('-id')
    else:
        data = Search_Data.objects.all().order_by('-id')

    return render(request, 'view_search_pat.html', {'data': data})


@login_required(login_url="login")
def delete_searched(request, pid):
    try:
        Search_Data.objects.get(id=pid).delete()
    except Search_Data.DoesNotExist:
        messages.error(request, 'Record not found.')
    return redirect('view_search_pat')


# ─────────────────────────────────────────────
# Feedback
# ─────────────────────────────────────────────

@login_required(login_url="login")
def View_Feedback(request):
    dis = Feedback.objects.all()
    return render(request, 'view_feedback.html', {'dis': dis})


@login_required(login_url="login")
def delete_feedback(request, pid):
    try:
        Feedback.objects.get(id=pid).delete()
    except Feedback.DoesNotExist:
        messages.error(request, 'Feedback not found.')
    return redirect('view_feedback')


@login_required(login_url='login')
def sent_feedback(request):
    terror = None
    if request.method == "POST":
        username = request.POST.get('uname', '').strip()
        message  = request.POST.get('msg', '').strip()
        try:
            user_obj = User.objects.get(username=username)
            Feedback.objects.create(user=user_obj, messages=message)
            terror = "create"
        except User.DoesNotExist:
            terror = "user_not_found"
    return render(request, 'sent_feedback.html', {'terror': terror})