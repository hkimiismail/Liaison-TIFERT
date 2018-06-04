from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
##########################################################################

from django.shortcuts import get_object_or_404, render, redirect
from tifert.models import Rj,Defaut_tabia,Photo
from .forms import ImageForm,NewtabiaForm,NewRjForm,PhotoForm
from django.core.files import File

from django.urls import reverse_lazy

################################################
from django.views.generic import CreateView

from django.views.generic import UpdateView
from django.views import View

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

##################################################
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
###########################################################################
from django.db.models import Sum,Avg
##################################################"
from django.contrib.auth.models import User

from .filters import UserFilter,DefFilter,RjFilter
########################################################
from django.http import HttpResponse
from reportlab.pdfgen import canvas

#¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
#¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤
def home(request):
    fin_rj_list = Rj.objects.all()
    Rjsomme = Rj.objects.aggregate(Sum('p_acide_h2so4'))
    Rjsomme_s = Rj.objects.aggregate(Sum('s_c'))
    Rjsomme_s_c = Rj.objects.aggregate(Sum('r_s_solid'))



    Rj_filter = RjFilter(request.GET, queryset=fin_rj_list)




    page = request.GET.get('page', 1)

    paginator = Paginator(fin_rj_list, 5)
    try:
        fin_rj_list1 = paginator.page(page)
    except PageNotAnInteger:
        fin_rj_list1 = paginator.page(1)
    except EmptyPage:
        fin_rj_list1 = paginator.page(paginator.num_pages)

    return render(request, 'tifert/home.html', {'Rjsomme_s': Rjsomme_s,'Rjsomme_s_c': Rjsomme_s_c,'Rjsomme': Rjsomme,'fin_rj_list': fin_rj_list,'filter': Rj_filter,'fin_rj_list1': fin_rj_list1})

################################################################




##################################################################################
#####                     Rapport journalier de TIFERT                    #######
#####                           Debut                                     ######
##################################################################################
############################################################""

@login_required
def index_rj(request):
    fin_rj_list = Rj.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(fin_rj_list, 10)
    try:
        fin_rj_list = paginator.page(page)
    except PageNotAnInteger:
        fin_rj_list = paginator.page(1)
    except EmptyPage:
        fin_rj_list = paginator.page(paginator.num_pages)

    return render(request, 'tifert/rj_tifert/index_rj.html', {'fin_rj_list': fin_rj_list})
    ##################################
############################################################""

@login_required
def table_rj(request, pk):
    rjs=get_object_or_404(Rj, pk=pk)

    return render(request, 'tifert/rj_tifert/detail_rj.html', {'rjs': rjs})

class NewRjView(CreateView):
    model = Rj
    form_class = NewRjForm
    success_url = reverse_lazy('index_rj')
    template_name = 'tifert/rj_tifert/new_rj.html'


    def form_valid(self, form):
        rjs = form.save(commit=False)
        rjs.starter = self.request.user
        rjs.save()

        return redirect('index_rj')


##########################################
@method_decorator(login_required, name='dispatch')
########################################

class RjUpdateView(UpdateView):
    model = Rj
    fields = ('date', 'h_m_h2so4','fqh_p_h2so4','fqa_p_h2so4','p_acide_h2so4','sh_acide_h2so4','tk2_1','tk2_2',
    'titre_p_h2so4','sh_s','sa_s','s_c','p_s_liq','r_s_solid','tk1_1','tk1_2','fqd_t_h2so4',
    'fqf_t_h2so4','t_acide_h2so4','titre_t_h2so4','p_acide_h3po4','h_a_gypse', )
    template_name = 'tifert/rj_tifert/e_tifert.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'rjs'


    def form_valid(self, form):
        rjs = form.save(commit=False)

        rjs.save()

        return redirect('table_rj', pk=rjs.pk)




##################################################################################
#####                     Rapport journalier de TIFERT                    #######
#####                           Fin                                     ######
##################################################################################
##################################################################################
#####                     Rapport TABIA                                 #######
#####                          Debut                                     ######
##################################################################################

@login_required
def index_tabia(request):
    tabias = Defaut_tabia.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(tabias, 10)
    try:
        Defauttabias = paginator.page(page)
    except PageNotAnInteger:
        Defauttabias = paginator.page(1)
    except EmptyPage:
        Defauttabias = paginator.page(paginator.num_pages)

    return render(request, 'tifert/rj_tabia/index_tabia.html', {'Defauttabias': Defauttabias})

def table_tabia(request, pk):
    tabias=get_object_or_404(Defaut_tabia, pk=pk)
    tabias.save()
    return render(request, 'tifert/rj_tabia/detail_tabia.html', {'tabias': tabias})

class NewPostView(CreateView):
    model = Defaut_tabia

    form_class = NewtabiaForm
    success_url = reverse_lazy('index_tabia')
    template_name = 'tifert/rj_tabia/new_tabia.html'


##########################################
@method_decorator(login_required, name='dispatch')
########################################

class DefUpdateView(UpdateView):
    model = Defaut_tabia
    fields = ('defaut', 'h_a_tabia','message','jour','doc', )
    template_name = 'tifert/rj_tabia/e_tabia.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'tabias'

    def form_valid(self, form):
        tabias = form.save(commit=False)

        tabias.save()
        return redirect('table_tabia', pk=tabias.pk)


##################################################################################
#####                     Rapport TABIA                                 #######
#####                          fin                                     ######
##################################################################################
##################################################################################
#####                     Rapport note&fax                                #######
#####                          Debut                                     ######
##################################################################################















##################################################################################
#####                     Rapport note&fax                                 #######
#####                          fin                                     ######
##################################################################################
##################################################################################
#####                     Rapport Gallerie photos                                #######
#####                          Debut                                     ######
##################################################################################


@login_required
def image_upload(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = ImageForm()
    return render(request, 'tifert/image_upload.html', {'form': form, 'photos': photos})




##################################################################################
#####                     Rapport Gallerie photos                                 #######
#####                          fin                                     ######
##################################################################################
##################################################################################
#####                     Calcule et affiche                                 #######
#####                          Debut                                     ######
##################################################################################

def calcule(request):
    Rjsomme = Rj.objects.aggregate(Sum('p_acide_h2so4'))

    return render(request, 'calc.html', {'Rjsomme': Rjsomme})
##################################################################################
#####                     Calcule et affiche                                 #######
#####                          fin                                     ######
##################################################################################
##################################################################################
#####                     Filtre                                 #######
#####                         debut                                     ######
##################################################################################
def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'user_list.html', {'filter': user_filter})

def def_search(request):
    def_list = Defaut_tabia.objects.all()
    def_filter = DefFilter(request.GET, queryset=def_list)
    return render(request, 'def_list.html', {'filter': def_filter})

def Rj_search(request):
    Rj_list = Rj.objects.all()
    Rj_filter = RjFilter(request.GET, queryset=Rj_list)
    return render(request, 'Rj_list.html', {'filter': Rj_filter})
############################################################################



def photo_list(request):
    photos = Photo.objects.all()
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'photo_list.html', {'form': form, 'photos': photos})

##############################################################################
#########
######## PDF CREATEUR
##############################################################################
def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world ismail.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
############################################################################
