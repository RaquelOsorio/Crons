from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from reglas.models import Crons
from reglas.forms import CronsForm

from reglas.forms import CronsFormulario
from django.conf import settings


def listado(request):

    crons=Crons.objects.all()
    return render_to_response('gestionCron.html',{'crons': crons }, context_instance=RequestContext(request))



def registrarCron(request):
    if request.method == "POST":
        formulario = CronsForm(request.POST, request.FILES)

        if formulario.is_valid():

            formulario.save()
            cron= formulario.instance.id
            c=Crons.objects.get(pk=cron)
            c.nombre= c.accion + "-" + c.dispositivo + "-" + str(c.hora)
            c.save()
            generateCronRulesFile('./cron.rules')
            return HttpResponseRedirect('/')

    else:
        formulario=CronsForm()

    return render(request, 'cron_form.html', {'form': formulario,})


def editarCrons(request, codigo):

    crons=Crons.objects.get(pk=codigo)
    if request.method == "POST":
        formulario = CronsForm(request.POST, request.FILES, instance = crons)
        if formulario.is_valid():
            formulario.save()
            cron= formulario.instance.id
            c=Crons.objects.get(pk=cron)
            c.nombre= c.accion + "-" + c.dispositivo + "-" + str(c.hora)
            c.save()

            generateCronRulesFile('./cron.rules')
            return HttpResponseRedirect('/')
    else:
        formulario=CronsFormulario(instance = crons)
    return render(request,'modificarCron.html', {'form': formulario})

def eliminarCron(request, codigo):

    cron=Crons.objects.get(pk=codigo)
    return render_to_response('eliminar.html',{'cron':cron}, context_instance=RequestContext(request))

def eliCron(request, codigo):
    cron= Crons.objects.get(pk=codigo)
    cron.delete()
    generateCronRulesFile('./cron.rules')
    return HttpResponseRedirect('/')



def generateCronRulesFile(path):
    crons= Crons.objects.all()
    buffr = '''import org.openhab.core.library.types.*
import org.openhab.core.library.items.*
import org.openhab.model.script.actions.*
    '''
    template = '''
rule '%s'
when
    Time cron "%s"
then
    sendCommand(%s, '%s')
end
    '''
    """
    Formato de Expresion Cron
------------------ minuto (0 - 59)
|  .------------- hora (0 - 23)
|  |  .---------- dia del mes (1 - 31)
|  |  |  .------- mes (1 - 12) O jan,feb,mar,apr ... (los meses en ingles)
|  |  |  |  .---- dia de la semana (0 - 6) (Domingo=0) )
|  |  |  |  |
*  *  *  *  * """
    for c in crons:
        cont=0
        for d in c.dia:
            if cont==0:
                dias= str(d)
                cont=cont+1
            else:
                dias=dias + "," + str(d)
        exp=  str(c.hora.minute) + " " + str(c.hora.hour) + " * * " + dias

        buffr += template % (c.nombre, exp, c.dispositivo, c.accion)
    with open(path, 'w') as f:
        f.write(buffr)


