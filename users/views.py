from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from formtools.wizard.views import SessionWizardView
from .forms import UserForm, ProfileForm, NameForm
from main.models import Profile

FORMS = [("user", UserForm),
         ("name", NameForm),
         ("profile", ProfileForm)]

TEMPLATES = {"user": "registration/user_form.html",
             "name": "registration/user_form.html",
             "profile": "registration/profile_form.html"}

class RegistrationWizard(SessionWizardView):
    form_list = FORMS

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        user_form = form_list[0]
        name_form = form_list[1]
        profile_form = form_list[2]

        if User.objects.filter(username=user_form.cleaned_data['username']).exists():
            return self.render_revalidation_failure(form_list, 'User already exists.')

        user = User.objects.create_user(
            username=user_form.cleaned_data['username'],
            email=user_form.cleaned_data['email'],
            password=user_form.cleaned_data['password1'],
            first_name=name_form.cleaned_data['first_name'],
            last_name=name_form.cleaned_data['last_name'],
        )

        profile, created = Profile.objects.get_or_create(user=user)
        profile.bio = profile_form.cleaned_data['bio']
        profile.user_type = user_form.cleaned_data['user_type']
        profile.phone_number = profile_form.cleaned_data['phone_number']
        profile.faculty = profile_form.cleaned_data['faculty']
        profile.course = profile_form.cleaned_data['course']
        profile.semester = profile_form.cleaned_data['semester']
        profile.save()

        return redirect('login')

    def render_revalidation_failure(self, form_list, error_message):
        current_step_index = self.get_step_index(self.steps.current)
        form = form_list[current_step_index]
        context = self.get_context_data(form=form)
        context.update({
            'wizard_error': error_message,
        })
        return self.render_to_response(context)

    def get_step_index(self, step):
        return {step_name: index for index, (step_name, _) in enumerate(FORMS)}[step]


def login(request):
    return render(request, 'users/login.html')

def logout(request):
    return render(request, 'users/logout.html')
