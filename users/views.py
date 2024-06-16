from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from formtools.wizard.views import SessionWizardView
from .forms import UserForm, ProfileForm, NameForm, FirmForm
from main.models import Profile

FORMS = [
    ("user", UserForm),
    ("name", NameForm),
    ("profile", ProfileForm),
    ("firm", FirmForm),
]

TEMPLATES = {
    "user": "registration/user_form.html",
    "name": "registration/user_form.html",
    "profile": "registration/profile_form.html",
    "firm": "registration/firm_form.html"
}


class RegistrationWizard(SessionWizardView):
    form_list = FORMS

    def get_template_names(self):
        current_step = self.steps.current

        if current_step == 'user':
            return [TEMPLATES["user"]]

        cleaned_data = self.get_cleaned_data_for_step('user')
        user_type = cleaned_data['user_type']
        if user_type == 'student' and current_step in ['name', 'profile']:
            return [TEMPLATES[current_step]]
        if user_type == 'firm' and current_step == 'firm':
            return [TEMPLATES["firm"]]


        return super().get_template_names()



    def done(self, form_list, **kwargs):
        user_form = form_list[0]
        name_form = form_list[1]
        profile_form = form_list[2]
        firm_form = form_list[3]

        if User.objects.filter(username=user_form.cleaned_data['username']).exists():
            return self.render_revalidation_failure(form_list, 'User already exists.')

        user = User.objects.create_user(
            username=user_form.cleaned_data['username'],
            email=user_form.cleaned_data['email'],
            password=user_form.cleaned_data['password1'],
            first_name=name_form.cleaned_data['first_name'],
            last_name=name_form.cleaned_data['last_name'],
        )

        cleaned_data = self.get_cleaned_data_for_step('user')
        if cleaned_data and 'user_type' in cleaned_data:
            user_type = cleaned_data['user_type']
            if user_type == "student" and profile_form:
                profile = Profile.objects.create(
                    user=user,
                    phone_number=profile_form.cleaned_data['phone_number'],
                    faculty=profile_form.cleaned_data['faculty'],
                    course=profile_form.cleaned_data['course'],
                    semester=profile_form.cleaned_data['semester'],
                    bio=profile_form.cleaned_data['bio']
                )
            elif user_type == "firm" and firm_form:
                profile = Profile.objects.create(
                    user=user,
                    nameFirm=firm_form.cleaned_data['nameFirm'],
                    website=firm_form.cleaned_data['website'],
                    bio=firm_form.cleaned_data['bio']
                )

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