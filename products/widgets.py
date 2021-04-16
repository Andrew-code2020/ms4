from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _

"""imported from Django Github copied from Boutique Ado project"""


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
