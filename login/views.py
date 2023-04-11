from django.shortcuts import render
import os
from django.http import HttpResponse

from flask import Flask, redirect, url_for, render_template, request
import mysql.connector as sql
em = ''
pwd = ''


def d_new(request):
    from website import Gesture_Controller
    exit()
    my_result = Gesture_Controller(request.GET.get(''))
    return render(request, 'index.html', {'result': my_result})


def loginaction(request):
    global em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root",
                        passwd="Mahesh@021011", database='website')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "email":
                em = value
            if key == "password":
                pwd = value

        c = "select * from users where email='{}' and password='{}'".format(
            em, pwd)
        cursor.execute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request, 'login_page.html')
        else:
            return render(request, "index.html")

    return render(request, 'login_page.html')
