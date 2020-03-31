import logging, uuid
from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from . const import LANGUAGE_CHOICE, DEDICATE_HOURS_CHOICE, MEDICAL_QUAL_CHOICES, TIME_PREF_CHOICES
from . serializers import DoctorSerializer


class TMPartnerForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name', required=True)
    contact_number = forms.CharField(max_length=10, min_length=10, label='Phone Number', required=True)
    other_contact = forms.CharField(max_length=10, min_length=10, label='Alternate Phone Number', required=False)
    email = forms.EmailField(label='Email ID', required=True)
    mci = forms.IntegerField(label='MCI Registration Number', required=True)
    state_authority = forms.CharField(max_length=100, label='Name of the State Authority (Ex. Karnataka Medical Council)', required=True)
    organisation_name = forms.CharField(max_length=100, label='Name of organisation', required=True)
    language = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=list(zip(range(len(LANGUAGE_CHOICE)), LANGUAGE_CHOICE)))
    duty_hours = forms.ChoiceField(widget=forms.Select, choices=list(zip(DEDICATE_HOURS_CHOICE, DEDICATE_HOURS_CHOICE)), help_text="")


def tm_partner_form_request(request):
    submitted = False
    if request.method == "POST":
        curr_form = TMPartnerForm(request.POST)
        if curr_form.is_valid():
            cleaned_data = curr_form.cleaned_data
            cleaned_data['id'] = uuid.uuid4().__str__()
            serializer = DoctorSerializer(data=cleaned_data)
            if serializer.is_valid():
                serializer.save()
            else:
                logging.error("error in saving doctor to model: %s", serializer.errors)
            # TODO - shubhra assert false
            return HttpResponseRedirect('/tmpartner?submitted=True')
    else:
        curr_form = TMPartnerForm()
        if submitted in request.GET:
            submitted = True

    return render(request, 'tmforms/tmpartner.html', {'form': curr_form,
                                                      'submitted': submitted})


class TMVolunteerForm(forms.Form):
    name = forms.CharField(max_length=100, label='Full Name', required=True)
    contact_number = forms.CharField(max_length=10, min_length=10, label='Phone Number', required=True)
    other_contact = forms.CharField(max_length=10, min_length=10, label='Alternate Phone Number', required=False)
    email = forms.EmailField(label='Email ID', required=True)
    medical_qual = forms.ChoiceField(widget=forms.Select, choices=list(zip(range(len(MEDICAL_QUAL_CHOICES)), MEDICAL_QUAL_CHOICES)))
    mci = forms.IntegerField(label='Please enter the registration no. given by MCI or State Authority', required=True)
    state_authority = forms.CharField(max_length=100,
                                      label='Name of the State Authority (Ex. Karnataka Medical Council)',
                                      required=True)
    language = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=list(zip(range(len(LANGUAGE_CHOICE)), LANGUAGE_CHOICE)))
    time_pref = forms.ChoiceField(widget=forms.Select,
                             choices=list(zip(range(len(TIME_PREF_CHOICES)), TIME_PREF_CHOICES)), help_text="")
    comment = forms.CharField(max_length=500, label='Please feel free to add other comments or questions', widget=forms.Textarea, required=False)


def tm_volunteer_form_request(request):
    submitted = False
    if request.method == "POST":
        curr_form = TMVolunteerForm(request.POST)
        if curr_form.is_valid():
            cleaned_data = curr_form.cleaned_data
            cleaned_data['id'] = uuid.uuid4()
            serializer = DoctorSerializer(data=cleaned_data)
            if serializer.is_valid():
                serializer.save()
            else:
                logging.error("error in saving doctor to model: %s", serializer.errors)
            return HttpResponseRedirect('/tmvolunteer?submitted=True')
    else:
        curr_form = TMVolunteerForm()
        if submitted in request.GET:
            submitted = True

    return render(request, 'tmforms/tmvolunteer.html', {'form': curr_form,
                                                        'submitted': submitted})
