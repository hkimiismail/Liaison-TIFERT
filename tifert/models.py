from django.db import models

# Create your models here.


from django.utils import timezone
###################################################
from django.db import models
from django.utils.text import Truncator
from django.contrib.auth.models import User


DEFAUT_STATUS = (
    ('Mécanique', 'Mécanique'),
    ('Q_Gypse', 'Qualité de Gypse'),
    ('Eléctrique', 'Eléctrique'),
)

TYPE_OBGJET = (
    ('Vap', 'Vapeur'),
    ('Reclamtion', 'Reclamtion'),
    ('Transfert', 'Transfert'),
)



##############################Rapport journalier de Tifert vers GCT##########################################

class Rj(models.Model):
    date = models.DateTimeField(default=timezone.now,verbose_name="DATE")
###################################################################################
    h_m_h2so4 = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="heure de marche sulfurique")
    fqh_p_h2so4 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="FQ (j-1) production")
    fqa_p_h2so4 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="FQ (j) production")
    p_acide_h2so4 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Production H2SO4")
    sh_acide_h2so4 = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Stock H2SO4 (j-1)")
    tk2_1 =  models.DecimalField(max_digits=8, decimal_places=2, verbose_name="7560 TK2/1 (T)")
    tk2_2 =  models.DecimalField(max_digits=8, decimal_places=2, verbose_name="7560 TK2/2 (T)")
    titre_p_h2so4 = models.DecimalField(max_digits=4, decimal_places=4, verbose_name="Titre H2SO4 produit")


    sh_s = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Stock Soufre (j-1)")
    sa_s = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Stock Soufre (j)")
    s_c = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Soufre consommé")
    p_s_liq = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Prod soufre liquide")
    r_s_solid = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Reception soufre solide")
    tk1_1 =  models.DecimalField(max_digits=8, decimal_places=2, verbose_name="7530 TK1/1 (T)")
    tk1_2 =  models.DecimalField(max_digits=8, decimal_places=2, verbose_name="7530 TK1/2 (T)")

    fqd_t_h2so4 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="FQ tr(début)")
    fqf_t_h2so4 = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="FQ tr(fin)")
    t_acide_h2so4 = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="transfert H2SO4")
    titre_t_h2so4 = models.DecimalField(max_digits=4, decimal_places=4, verbose_name="Titre H2SO4 produit")


    p_acide_h3po4 = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Production H3PO4 (T)")
    h_a_gypse = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Arrêt tabia (heure,minute)")





    last_updated = models.DateTimeField(auto_now_add=True)
    starter = models.ForeignKey(User,on_delete=models.CASCADE, related_name='starters')
    class Meta:
        verbose_name = "Rj"
        ordering = ['-date']


    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        #return self.journee
        return "{0}".format(self.date)





#####################################################################################
################################Defaut_tabia#######################################################
  ##################################################################################
class Defaut_tabia(models.Model):


    defaut = models.CharField(max_length=10, choices=DEFAUT_STATUS)
    h_a_tabia = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Arrêt tabia(Heure,min)")
    message = models.TextField()
    jour = models.ForeignKey(Rj,on_delete=models.CASCADE, related_name='jours')
    doc = models.FileField(upload_to='Documents/tabia/%Y/%m/%d/')



    class Meta:
        verbose_name = "Defaut_tabia"
        ordering = ['-jour']




    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        #return self.journee
        return "{0}".format(self.defaut)



#####################################################################################
################################Defaut_tabia#######################################################
  ##################################################################################
class Fax(models.Model):



    date = models.DateTimeField(default=timezone.now,verbose_name="DATE")

    objet = models.CharField(max_length=10, choices=TYPE_OBGJET)
    text = models.CharField(max_length=200)

    fax = models.FileField(upload_to='Documents/fax/%Y/%m/%d/')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='users')




    class Meta:
        verbose_name = "Fax"
        ordering = ['-date']




    def __str__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que
        nous traiterons plus tard dans l'administration
        """
        #return self.journee
        return "{0}".format(self.text)


########################################""gallerie photo########################

class Photo(models.Model):
    description = models.CharField(max_length=255, blank=True)
    file = models.ImageField(upload_to='Documents/images/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'photo'
        verbose_name_plural = 'photos'
        ordering = ['-uploaded_at']
