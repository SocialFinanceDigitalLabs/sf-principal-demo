from django.shortcuts import render
from django import forms
from io import TextIOWrapper
from django.contrib import messages
from core.models import Person, Gender
from datetime import datetime
import csv
import logging

logger = logging.getLogger(__name__)

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
            logger.debug("Decoding CSV upload:")
            csv_reader = csv.DictReader(decoded_file)
            data = list(csv_reader)
            context = {'csv_data': data}

            for row in data:
                first_name = row['first_name'].strip()
                last_name = row['last_name'].strip()
                dob_str = row['dob'].strip()
                start_date_str = row['start_date'].strip()
                end_date_str = row['end_date'].strip()
                gender_str = row['gender'].strip()

                dob = None
                start_date = None
                end_date = None
                gender = None

                if dob_str:
                    try:
                        dob = datetime.strptime(dob_str, '%Y-%m-%d').date()
                    except (ValueError, TypeError):
                        messages.error(request, f"Invalid DOB format: {dob_str}. Row skipped.")
                        logger.error(f"Could not parse DOB: {dob_str}")
                        continue

                if start_date_str:
                    try:
                        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
                    except (ValueError, TypeError):
                        messages.error(request, f"Invalid Start Date format: {start_date_str}. Row skipped.")
                        logger.error(f"Could not parse Start Date: {start_date_str}")
                        continue

                if end_date_str:
                    try:
                        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
                    except (ValueError, TypeError):
                        messages.error(request, f"Invalid End Date format: {end_date_str}. Row skipped.")
                        logger.error(f"Could not parse End Date: {end_date_str}")
                        continue

                if gender_str:
                    gender_str = gender_str.upper()  # make gender string uppercase.
                    if gender_str == 'M':
                        gender = Gender.MALE
                    elif gender_str == 'F':
                        gender = Gender.FEMALE
                    else:
                        messages.error(request, f"Invalid Gender format: {gender_str}. Row skipped.")
                        logger.error(f"Could not parse Gender: {gender_str}")
                        continue

                try:
                    Person.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        dob=dob,
                        start_date=start_date,
                        end_date=end_date,
                        gender=gender,
                    )
                except Exception as err:
                    print(f"Could not save record: {err}")

            messages.success(request, "CSV file uploaded and data saved successfully.")
            return render(request, 'csv_upload/csv_display.html', context)
        else:
            messages.error(request, "Form is invalid.")
            return render(request, 'csv_upload/upload_form.html', {'form': form})
    else:
        form = UploadCSVForm()

    return render(request, 'csv_upload/upload_form.html', {'form': form})
