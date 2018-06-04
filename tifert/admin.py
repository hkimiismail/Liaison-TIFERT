from django.contrib import admin

# Register your models here.
from .models import Rj,Defaut_tabia,Fax,Photo
from decimal import Decimal
# Register your models here.
#from RjT.models import Tache, Rj
#,Defaut_tabia,Document


#class defAdmin(admin.ModelAdmin):
#    model = Defaut_tabia

    #list_display = ('journee', 'defau','h_a_tabia','message','document')

class ProductAdmin(admin.ModelAdmin):
    model = Rj

    list_display = ('date', 'h_m_h2so4','fqh_p_h2so4','fqa_p_h2so4','p_acide_h2so4', 'Prod','sh_acide_h2so4','tk2_1','tk2_2',
    'titre_p_h2so4','sh_s','sa_s','s_c','p_s_liq','r_s_solid','tk1_1','tk1_2','fqd_t_h2so4',
    'fqf_t_h2so4','t_acide_h2so4','titre_t_h2so4','p_acide_h3po4','h_a_gypse')

    def Prod(self, instance):
        return round((instance.fqa_p_h2so4 - instance.fqh_p_h2so4)*(instance.titre_p_h2so4)*Decimal(1.83),1)
    Prod.short_description = "Production"


admin.site.register(Rj,ProductAdmin)
#admin.site.register(Rj)
admin.site.register(Defaut_tabia)
admin.site.register(Fax)
admin.site.register(Photo)
