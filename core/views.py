from django.shortcuts import render
from django import forms
from io import TextIOWrapper
from django.contrib import messages
import csv

def index(request):
    return render(request, "core/index.html")

def upload(request):
    class UploadCSVForm(forms.Form):
        csv_file = forms.FileField(label="Upload CSV File")

    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']

            # Use TextIOWrapper to handle different encodings
            decoded_file = TextIOWrapper(csv_file, encoding='utf-8')
            csv_reader = csv.DictReader(decoded_file)
            data = list(csv_reader) #Read all lines into a list of dictionaries.

            # Process the parsed CSV data (e.g., store it, display it)
            context = {'csv_data': data}
            messages.success(request, "CSV file uploaded and parsed successfully.")
            return render(request, 'csv_upload/csv_display.html', context)
        else:
            messages.error(request, "Form is invalid.")
            return render(request, 'csv_upload/upload_form.html', {'form': form})
    else:
        form = UploadCSVForm()

    return render(request, 'csv_upload/upload_form.html', {'form': form})
