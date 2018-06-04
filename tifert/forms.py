from PIL import Image
from django import forms
from django.core.files import File
from .models import Photo



#from django import forms
from .models import Rj
from .models import Defaut_tabia

from decimal import Decimal

#from .models import Document,Defaut_tabia

#class DocumentForm(forms.ModelForm):
    # class Meta:
    #    model = Document
    #    fields = ('description', 'document', )

class NewRjForm(forms.ModelForm):
    #message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Rj
        fields = ['date', 'h_m_h2so4','fqh_p_h2so4','fqa_p_h2so4','p_acide_h2so4','sh_acide_h2so4','tk2_1','tk2_2',
        'titre_p_h2so4','sh_s','sa_s','s_c','p_s_liq','r_s_solid','tk1_1','tk1_2','fqd_t_h2so4',
        'fqf_t_h2so4','t_acide_h2so4','titre_t_h2so4','p_acide_h3po4','h_a_gypse']

    def clean(self):

        cleaned_data = super(NewRjForm, self).clean()
        fqh_p_h2so4 = cleaned_data.get("fqh_p_h2so4")
        fqa_p_h2so4 = cleaned_data.get("fqa_p_h2so4")


        if fqh_p_h2so4 > fqa_p_h2so4:
            msg = u"FQ(j) doit être plus élevé que FQ(j-1)"
            self._errors['fqh_p_h2so4'] = self.error_class([msg])

        return cleaned_data






########################################################
class ImageForm(forms.ModelForm):
     class Meta:
        model = Photo
        fields = ('description', 'file', )
##################################################
class NewtabiaForm(forms.ModelForm):
    class Meta:
        model = Defaut_tabia
        fields = ('defaut', 'h_a_tabia','message','jour','doc',)

########################################################
class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())

    class Meta:
        model = Photo
        fields = ('file', 'x', 'y', 'width', 'height', )

    def save(self):
        photo = super(PhotoForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        return photo
