from django import forms
from .models import Producer,Production

LOCATION=[
('IndiaGate','India Gate and Raj path'),
('SansadBhavan','Sansad Bhavan'),
('RashtrapatiBhawan','Rashtrapati Bhawan'),
('ConnaughtPlace','Connaught Place (Rajiv Chowk)'),
('LodhiGardens','Lodhi Gardens'),
('HumayunTomb','Humayun Tomb'),
('PuranaQila ','Purana Qila'),
('RedFort','Red Fort'),
('ChandniChowk','Chandni Chowk'),
("SafdarjungTomb"," Safdarjung's Tomb"),
('QutubMinar','Qutub Minar'),
('Tughlaqabad','Tughlaqabad'),
('LaxminarayanTemple','Laxminarayan Temple'),
('GurudwaraBanglaSahib','Gurudwara Bangla Sahib'),
('JamaMasjid','Jama Masjid'),
('JantarMantar','Jantar Mantar'),
('NizamuddinDargah','Nizamuddin Dargah'),
('RajGhat','Raj Ghat'),
('BuddhaJayantiPark','Buddha Jayanti Park'),
('DilliHaat','Dilli Haat'),
('HauzKhasVillageFORT','Hauz Khas Village & FORT '),
('KhanMarket','Khan Market'),
('AzadHindGram','Azad Hind Gram'),
('DelhiGate',' Delhi Gate'),
('ISBT','ISBT'),
('DelhiMalls','Delhi Malls'),
('NorthCampus','North Campus'),
('SouthCampus','South Campus'),
('JNU','Jawahar Lal Nehru University (JNU)'),
('DelhiMarkets','Delhi Markets'),
('GyarahMurt','Gyarah  Murt'),
('JamaliKamaliMosqueandTomb','Jamali Kamali Mosque and Tomb'),
('AgrasenkiBaoli','Agrasen ki Baoli'),
('GardenofFiveSenses','Garden of Five Senses'),
('DelhiMetro','Delhi Metro'),
('DelhiRoads','Delhi Roads'),
('GuruTegBahadurMemorial','Guru Teg Bahadur Memorial'),
('DilliHaatJanakpuri','Dilli Haat, Janakpuri')
]

class ApplicationForm(forms.ModelForm):
	"""Application Form"""
	class Meta:
		model=Production
		fields=['producer','production_house','production_house_address','contact','local_line_producer','local_line_producer_address','film','director','cinematographer','art_director','script','shoot_timing','shoot_start_date','shoot_end_date','location','undertaking']
		widgets = {
		    'producer':forms.TextInput(attrs={'style':'width: 100%;padding: 12px;border: 1px solid #ccc;border-radius: 4px;box-sizing: border-box;resize: vertical;'}),
		    'shoot_start_date':forms.SelectDateWidget(), # change to date picker
		    'shoot_end_date':forms.SelectDateWidget(), # change to date picker
		    'shoot_timing':forms.TimeInput(), #change to better time field.
		    'production_house':forms.TextInput(attrs={'style':'width: 100%;padding: 12px;border: 1px solid #ccc;border-radius: 4px;box-sizing: border-box;resize: vertical;'}),
		    'production_house_address':forms.Textarea(attrs={'style':'width: 100%;padding: 12px;border: 1px solid #ccc;border-radius: 4px;box-sizing: border-box;resize: vertical;'}),
		    'contact':forms.TextInput(attrs={'style':'width: 100%;padding: 12px;border: 1px solid #ccc;border-radius: 4px;box-sizing: border-box;resize: vertical;'}),
		    'local_line_producer':forms.TextInput(attrs={'style':'width: 100%;padding: 12px;border: 1px solid #ccc;border-radius: 4px;box-sizing: border-box;resize: vertical;'}),
		    'local_line_producer_address':forms.Textarea(attrs={'style':'width: 100%;padding: 12px;border: 1px solid #ccc;border-radius: 4px;box-sizing: border-box;resize: vertical;'}),
		    'location':forms.Select(choices=LOCATION,attrs={'style':'width: 100%;padding: 12px;border: 1px solid #ccc;border-radius: 4px;box-sizing: border-box;resize: vertical;'}),
		    'film':forms.TextInput(attrs={'style':'width: 100%;padding: 12px;border: 1px solid #ccc;border-radius: 4px;box-sizing: border-box;resize: vertical;'}),
		    'director':forms.TextInput(attrs={'style':'width: 100%;padding: 12px;border: 1px solid #ccc;border-radius: 4px;box-sizing: border-box;resize: vertical;'}),
		    'cinematographer':forms.TextInput(attrs={'style':'width: 100%;padding: 12px;border: 1px solid #ccc;border-radius: 4px;box-sizing: border-box;resize: vertical;'}),
		    'art_director':forms.TextInput(attrs={'style':'width: 100%;padding: 12px;border: 1px solid #ccc;border-radius: 4px;box-sizing: border-box;resize: vertical;'}),
		    'script':forms.FileInput(),
		    'undertaking':forms.FileInput(),
		}
		
		
			