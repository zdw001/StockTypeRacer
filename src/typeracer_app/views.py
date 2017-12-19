from django.shortcuts import render
import random
from .forms import ContactForm
from django.core.mail import EmailMessage, send_mail
from django.conf import settings

# Create your views here.
def index(request): 
	symbol_list = ['XXII','IAF','CH','ABE','FCO','IF','ISL','ACU','ATNM','AE','ADK',
	'ACY','AIRI','AXU','ALO','AAU','APT','AAMC','DIT','ALN','AMS','USAS','AMPE',
	'APHB','AXN','ARNC','AKG','AINC','ASB','AST','AUG','AWX','ASM','BTG','BTN',
	'BKJ','BCV','BAA','BHB','BRN','BGSF','BPMX','BTX','BGI','BZM','MHE','BLE',
	'BLJ','BFY','BHV','BDR','BRG','BVX','BWL','CMCL','CEI','CANF','ROX','CAW',
	'CVM','CEF','CET','LEU','CCF','CQH','CQP','LNG','CVR','CPHI','CISN','CKX',
	'GLV','GLQ','GLO','COHN','MOC','CIX','LODE','CDOR','CTO','MCF','CUO','CMT',
	'CVRS','CRMD','CRF','CLM','CVU','CIK','DHY','CRHM','CRVP','CTEK','DXR','VCF',
	'VFL','VMM','DLA','DNN','DGSE','DPW','DSS','DMF','GRF','EVM','EIA','CEV',
	'EVV','MAB','MMV','MIW','EMI','EIM','EIV','EMJ','EVJ','ENX','NYH','EVY',
	'EIO','EVO','EIP','EVP','ELMD','ELLO','ECF','EMAN','MSN','EMX','UUUU','ENRJ',
	'ENSV','ESNC','EGI','EVI','ERN','ESP','EVBN','EPM','FPP','FEN','BDL','FSI',
	'FTF','FSP','FRD','GGN','GST','JOB','GMO','GSB','GSAT','GLOW','GORO','GSV',
	'AUMN','GSS','GV','GDP','GTE','GPL','SIM','GVP','HEB','HCAC','HLM','HMG',
	'HUSA','IBIO','IBO','IEC','IMUC','IMH','IMO','IOR','IGC','INFU','IHT','NSPR',
	'IDN','INS','THM','INTT','INUV','VKI','ISR','ISDR','JRJR','KIQ','KLDX','LTS',
	'LTS','LAQ','LGL','LBY','LLEX','LIQT','MAG','MJCO','MHH','MTNB','MNI','IPB',
	'MXC','CCA','MICR','MLSS','MVF','MZA','MYO','NNVC','NHC','NAVB',
	'NTIP','NBW','NHS','NBH','NML','NBO','NRO','UWN','NSU','GBR','NEN','NGD',
	'NXE','HLTH','NAK','NOG','NBY','NG','NTN','NJV','NPN','OCX','OGEN','TIS',
	'ONP','ORM','PCG','PTN','PARR','PZG','TEUM','PRK','BTU','PED','PFNX','HNW',
	'PLG','PLYM','PLM','PW','PLX','RLGT','UTG','REED','RWC','RCG','RVP','RNN','REI',
	'RIF','SACH','SGA','SSN','SNMP','SAND','SEB','SENS','SVT','SMTS','SIF','SVM',
	'SKY','XPL','SCE','SGB','LOV','SRCI','SGY','STRP','SSY','SDPI','STS','SYN',
	'TKAT','TRX','TGB','TIK','TGC','GLU','GGO','TXMD','TMP','TAT','TRXC','TMQ',
	'TPHS','TRT','HTM','UFAB','UAMY','UUU','UQM','URG','UEC','VSR','VII','VHC',
	'VGZ','VNRX','VISI','EAD','ERC','ERH','SBI','WRN','WYY','WTT','XTNT','YUMA',
	'ZDGE']

	symbol_sample = random.sample(symbol_list, 50)

	# contact form
	form_class = ContactForm

	if request.method == 'POST':
		form = form_class(data=request.POST)

		if form.is_valid():
			form_content = form.cleaned_data['content']
			contact_email = form.cleaned_data['contact_email'] 
			subject = form.cleaned_data['subject']

			from_email = settings.EMAIL_HOST_USER
			to_email = [from_email]
			contact_message = "%s:\n via %s"%(
					form_content,
					contact_email)

			send_mail(subject,
					contact_message,
					contact_email,
					to_email,
					fail_silently=False)


	return render(request, 'home.html', {
				'symbol_list': symbol_list,
				'symbol_sample': symbol_sample,
				'form': form_class,
		})