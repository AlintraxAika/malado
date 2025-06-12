import streamlit as st
from datetime import date
import datetime
import math

bgmom = ""
rhmom = ""
momBlood = "XX"
bgnb = ""
rhnb = ""
nbBlood = "XX"
afu = 0
preec = False

def nDaysBetween (date1, date2):
	s1 = date1.split("/")
	s2 = date2.split("/")
	dateC1 = datetime.datetime(int(s1[2]),int(s1[1]),int(s1[0]))
	dateC2 = datetime.datetime(int(s2[2]),int(s2[1]),int(s2[0]))
	return abs((dateC2 - dateC1).days)

def igToDays (weeks, days):
	return days+weeks*7

def daysToIg (days):
	return [math.floor(days/7), days%7]

st.header("📝 EVOLUÇÃO DOM MALADO")
st.subheader("🐁exclusive 4 ratchex🐀")
st.write("<todo texto inserido será convertido para caixa alta>")

#QUESTIONAIRE
##ID + POINT-OF-CARE TESTS
name = st.text_input("NOME:")
c1, c2, c3, c4, c5, c6, c7, c8, c9 = st.columns([1.5,1,1,1,1,1.5,1.5,1.5,1.5])
with c1:
	age = st.text_input("IDADE:")
with c2:
	g = st.text_input("G:", value="1")
with c3:
	pv = st.text_input("PV:", value="0")
with c4:
	pc = st.text_input("PC:", value="0")
with c5:
	a = st.text_input("A:", value="0")
with c6:
	sif = st.checkbox("SÍFILIS")
with c7:
	hiv = st.checkbox("HIV")
with c8:
	hcv = st.checkbox("HCV")
with c9:
	hbs = st.checkbox("HbsAg")

##COMORBIDITIES
c1, c2, c3 = st.columns(3)
c4, c5 = st.columns(2)
with c1:
	dm = st.checkbox("DIABETES MELLITUS")
	if dm:
		with c4:
			dmType = st.radio("DM:", ["GESTACIONAL","TIPO 1", "TIPO 2"], key="radio0", horizontal=True)
with c2:
	crhyp = st.checkbox("HAS CRÔNICA")
with c3:
	gesthyp = st.checkbox("HAS GESTACIONAL")
if gesthyp:
	with c5:
		c6, c7 = st.columns(2)
		with c6:
			severePreec = st.checkbox("DETERIORAÇÃO")
		with c7:
			preec = st.checkbox("PRÉ-ECLÂMPSIA", value=severePreec)

##MOTHER BLOOD TYPE
if st.checkbox("TIPO SANGUÍNEO DA MÃE DISPONÍVEL?"):
	c1, c2 = st.columns(2)
	with c1:
		bgmom = st.radio("TIPO:", ["O", "A", "B", "AB"], key="radio1", horizontal=True)
	with c2:
		rhmom = st.radio("Rh:", ["POSITIVO", "NEGATIVO"], key="radio2", horizontal=True)
		if rhmom == "POSITIVO":
			rhmom = "+"
		else:
			rhmom = "-"
	momBlood = bgmom+rhmom

st.write("SE DUM INCERTA, DEIXAR A DATA DE HOJE")
#LAST MENSTRUAL PERIOD
c1, c2, c3, c4 = st.columns(4)
with c1:
	lmpDate = st.text_input("DUM:", value=date.today().strftime("%d/%m/%Y"))
with c2:
	admDate = st.text_input("DATA ADMISSÃO:", value=date.today().strftime("%d/%m/%Y"))
with c3:
	postPartum = st.checkbox("PUERPERA")
with c4:
	usg = st.checkbox("USG DISPONÍVEL")

#LMP GESTATIONAL AGE
gestAgeLmp = daysToIg( nDaysBetween( lmpDate, date.today().strftime("%d/%m/%Y") ) )

#USG
if usg:
	c1, c2, c3, c4, c5 = st.columns([2,1,1,1,2])
	with c1:
		usgDate = st.text_input("DATA USG:", value=date.today().strftime("%d/%m/%Y"))
	with c2:
		st.write("IG NA USG:")
	with c3:
		usgWeeks = st.text_input("SEMANAS:", value="0")
	with c4:
		usgDays = st.text_input("DIAS:", value="0")
	#USG GESTATIONAL AGE
	gestAgeUsg = daysToIg( nDaysBetween( usgDate, date.today().strftime("%d/%m/%Y") ) + igToDays( int(usgWeeks), int(usgDays) ) )

#DEFINES WHICH GESTATIONAL AGE TO USE
if usg:
	if int( usgWeeks ) < 13 and abs( igToDays (gestAgeUsg[0],gestAgeUsg[1]) - igToDays (gestAgeLmp[0],gestAgeLmp[1]) ) > 7:
		gestAge = gestAgeUsg
		modeChosen = "(USG 1º TRIMESTRE)"
	elif int( usgWeeks ) < 29 and abs( igToDays (gestAgeUsg[0],gestAgeUsg[1]) - igToDays (gestAgeLmp[0],gestAgeLmp[1]) ) > 14:
		gestAge = gestAgeUsg
		modeChosen = "(USG 2º TRIMESTRE)"
	elif abs( igToDays (gestAgeUsg[0],gestAgeUsg[1]) - igToDays (gestAgeLmp[0],gestAgeLmp[1]) ) > 21:
		gestAge = gestAgeUsg
		modeChosen = "(USG 3º TRIMESTRE)"
	else:
		gestAge = gestAgeLmp
		modeChosen = "(DUM)"
else:
	gestAge = gestAgeLmp
	modeChosen = "(DUM)"

#LABOR + NEWBORN BLOOD TYPE
if postPartum:
	c1, c2, c3 = st.columns([2,1,1])
	with c1:
		laborMode = st.radio("VIA:", ["VAGINAL", "CESÁREA"], key="radio3", horizontal=True)
	with c2:
		laborDate = st.text_input("DATA:", value=date.today().strftime("%d/%m/%Y"))
	with c3:
		laborTime = st.text_input("HORA:")
	if st.checkbox("TIPO SANGUÍNEO DO NEONATO DISPONÍVEL?"):
		c4, c5 = st.columns(2)
		with c4:
			bgnb = st.radio("TIPO:", ["O", "A", "B", "AB"], key="radio4", horizontal=True)
		with c5:
			rhnb = st.radio("Rh:", ["POSITIVO", "NEGATIVO"], key="radio5", horizontal=True)
			if rhnb == "POSITIVO":
				rhnb = "+"
			else:
				rhnb = "-"
		nbBlood = bgnb+rhnb

#DIURESIS
#mark: diu, svd, - bh, qt - sne, vm
c1, c2, c3, c4, c5, c6 = st.columns([1,1,1,1,1,1])
with c1:
	svd = st.checkbox("SVD")
with c2:
	diu = st.checkbox("DIURESE", value=svd)
if svd:
	with c3:
		diuQt = st.text_input("ML:")
	with c4:
		bh = st.text_input("BH:")
with c5:
	sne = st.checkbox("SNE")
with c6:
	vm = st.checkbox("VM")

#DIET + NAUSEA
c1, c2, c3 = st.columns([3,1,1])
with c1:
	diet = st.radio("ACEITAÇÃO DIETA:", ["SIM", "NÃO", "ZERO"], key="radioDiet", horizontal=True)
with c2:
	emesis = st.checkbox("ÊMESE")
with c3:
	nausea = st.checkbox("NAUSEA", value=emesis)

#BOWEL MOVEMENTS + OTHER
#ratio: dej: s, flat, n; sedação, deambulação
c1, c2, c3 = st.columns([3,1,1])
with c1:
	bowel = st.radio("DEJEÇÕES:", ["SIM", "FLATOS", "NÃO"], key="radioBowel", horizontal=True)
with c2:
	walk = st.checkbox("DEAMBULA")
with c3:
	sed = st.checkbox("SEDAÇÃO")

#VITAL SIGNS
#box: pa, fc, spo, fr, gcs, o2, dva
c1, c2, c3, c4, c5, c6, c7, c8, c9 = st.columns(9)
with c1:
	pa = st.text_input("PA:")
with c2:
	fc = st.text_input("FC:")
with c3:
	spo2 = st.text_input("SpO2:")
with c4:
	fr = st.text_input("FR:")
with c7:
	gcs = st.text_input("GCS:", value="15")
with c8:
	o2 = st.checkbox("O2", value=vm)
with c9:
	dva = st.checkbox("DVA")

st.write("EM CASO DE PÓS PARTO, COLOCAR VALORES NEGATIVOS NA AFU SE ABAIXO DA CICATRIZ UMBILICAL")

#FETAL VITAL SIGNS
#fetus: bcf, afu, du, mov. fetal
if not postPartum:
	c1, c2, c3, c4 = st.columns([1,1,1,4])
	with c1:
		afu = round(float(st.text_input("AFU:", value = "0")), 1)
	with c2:
		bcf = st.text_input("BCF:")
	with c3:
		du = st.checkbox("DU")
	with c4:
		movFet = st.checkbox("MOV. FETAL")
else:
	c1, c2, c3 = st.columns([1,2,4])
	with c1:
		afu = round(float(st.text_input("AFU:", value = "0")), 1)
	with c2:
		milk = st.checkbox("AMAMENTAÇÃO")

#box+: eminencia, >fio2, pinsp, peep,< ou >qtO2<
if preec:
	severitySigns = st.checkbox("SINAIS DE IMINÊNCIA DE ECLÂMPSIA")


#PHYSICAL EXAM
ect = st.text_input("ECTOSCOPIA:", value="EG BOM, CONSCIENTE E ORIENTADA, EUPNEICA, NORMOCORADA, HIDRATADA, ACIANÓTICA, ANICTÉRICA, AFEBRIL.")
mamas = st.text_input("MAMAS:", value="MAMAS FLÁCIDAS, SEM FISSURAS OU SINAIS FLOGÍSTICOS.")
cv = st.text_input("CARDIOVASCULAR:", value=f"RITMO CARDÍACO REGULAR EM 2 TEMPOS, BULHAS NORMOFONÉTICAS, SEM SOPROS, CLIQUES OU ESTALIDOS. PA: {pa} MMHG | FC: {fc} BPM")
ap = st.text_input("PULMONAR:", value=f"MURMÚRIO VESICULAR PRESENTE EM AMBOS HEMITÓRAX, SEM RUÍDOS ADVENTÍCIOS. SpO2: {spo2}% | FR: {fr} IRPM")
if postPartum:
	abdVal = f"SEMIGLOBOSO, RUÍDOS HIDROAÉREOS PRESENTES, DEPRESSÍVEL, DOLOROSO À PALPAÇÃO PROFUNDA EM REGIÃO SUPRAPÚBICA, SEM SINAIS DE IRRITAÇÃO PERITONEAL, ÚTERO CONTRAÍDO "
	if afu > 0:
		abdVal += f"{afu} CM ACIMA DA CICATRIZ UMBILICAL."
	elif afu < 0:
		afu *= -1
		abdVal += f"{afu} CM ABAIXO DA CICATRIZ UMBILICAL."
	else:
		abdVal += f"NO NÍVEL DA CICATRIZ UMBILICAL."
else:
	abdVal = f"GRAVÍDICO, RUÍDOS HIDROAÉREOS PRESENTES, SEM DOR À PALPAÇÃO, TÔNUS UTERINO FISIOLÓGICO, DINÂMICA UTERINA "
	abdVal += "PRESENTE. " if du else "AUSENTE. "
	abdVal += "MOVIMENTAÇÕES FETAIS "
	abdVal += "PRESENTES." if movFet else "AUSENTES."
	abdVal += f" BCF: {bcf} BPM | AFU: {afu} CM"
abd = st.text_input("ABDOME:", value=abdVal)
neur = st.text_input("NEUROLÓGICO:", value=f"GLASGOW {gcs}, SEM SINAIS DE DÉFICITS NEUROLÓGICOS FOCAIS.")
if postPartum:
	if laborMode == "CESÁREA":
		fo = st.text_input("FO:", value="FERIDA OPERATÓRIA LIMPA E SEM SINAIS FLOGÍSTICOS.")
	loq = st.text_input("LOQUIOS:", value="RUBROS, SEM ODOR, EM PEQUENA QUANTIDADE.")
else:
	tv = st.text_input("TV:", value="TOQUE VAGINAL NÃO REALIZADO.")
ext = st.text_input("EXTREMIDADES:", value="EDEMA (+1/+4) EM MMII. TEC <3S. SEM SINAIS DE TROMBOSE. PULSOS PRESENTES E SIMÉTRICOS.")

#HYPOTHESIS
if postPartum:
	hypothesis = f"1. PUERPÉRIO IMEDIATO DE PARTO {laborMode} REALIZADO DIA {laborDate} ÀS {laborTime}"
else:
	hypothesis = f"1. GESTAÇÃO ÚNICA TÓPICA"
	if gestAge[0] < 34:
		hypothesis += f" PRÉ-TERMO "
	elif gestAge[0] < 37:
		hypothesis += f" PRÉ-TERMO TARDIO "
	elif gestAge[0] < 41:
		hypothesis += f" TERMO "
	elif gestAge[0] < 42:
		hypothesis += f" TERMO TARDIO "
	else:
		hypothesis += f" PÓS-TERMO "
	hypothesis += f"COM {gestAge[0]}S {gestAge[1]}D {modeChosen}"
	
hypothesis += f"\n. INCOMPATIBILIDADE SANGUÍNEA MATERNO-FETAL" if (rhmom == "+" and rhnb == "-") else ""
if dm:	
	hypothesis += f"\n. DIABETES MELLITUS {dmType}"	
if crhyp:
	hypothesis += f"\n. HAS CRÔNICA"
if gesthyp:
	if preec:
		hypothesis += f"\n. PRÉ-ECLÂMPSIA"
		if crhyp:
			hypothesis += f" SOBREPOSTA"
		hypothesis += f" COM SINAIS DE DETERIORAÇÃO CLÍNICA" if severePreec else ""
	else:
		hypothesis += f"\n. HAS GESTACIONAL"
hypothesis += f"\n. TR SÍFILIS REAGENTE" if sif else ""
hypothesis += f"\n. TR HIV REAGENTE" if hiv else ""
hypothesis += f"\n. TR HCV REAGENTE" if hcv else ""
hypothesis += f"\n. TR HbsAg REAGENTE" if hbs else ""

#HISTORY
history = f"PACIENTE, G{g}P"
history += str(int(pv)+int(pc)-1) if postPartum else str(int(pv)+int(pc))
gestAgeAdm = daysToIg( igToDays(gestAge[0], gestAge[1]) - nDaysBetween( admDate, date.today().strftime("%d/%m/%Y") ) )
history += f"A{a}, EM CURSO DE IG: {gestAgeAdm[0]}S {gestAgeAdm[1]}D {modeChosen}, DEU ENTRADA NESTE SERVIÇO DIA {admDate}, DEVIDO ________.AO EXAME FISICO ADMISSIONAL, APRESENTAVA-SE COM ________. PACIENTE FOI INTERNADA PARA ________."
if postPartum:
	history += f"PARTO {laborMode} REALIZADO EM {laborDate} ÀS {laborTime} COM RETIRADA DE FETO VIVO, CEFALICO, _[SEXO]_, APGAR __, PESO ____G."
history += f"ENCAMINHADA PARA _[ALA]_. SEGUE AOS CUIDADOS DA EQUIPE."

#MEDICAL HISTORY
pHist = f"DIABETES MELLITUS {dmType}" if dm and dmType != "GESTACIONAL" else "NEGA DM PRÉ-GESTACIONAL"
pHist += f". HAS CRÔNICA." if crhyp else ". NEGA HAS CRÔNICA."
pHist += " NEGA TRANSFUSÕES. NEGA ETILISMO E TABAGISMO."

#PROGRESS SECTION
prog = "PACIENTE HEMODINAMICAMENTE ESTÁVEL, "
if vm:
	prog += "EM USO DE VENTILAÇÃO MECÂNICA (MODO: ; PINSP/VOL: ; FIO2: ; PEEP: )."
elif o2:
	prog += "EM USO DE ______ (__ L/MIN)."
else:
	prog += "RESPIRANDO EM AR AMBIENTE, SEM DESCONFORTO RESPIRATÓRIO. "
prog += "SEM USO DE DROGA VASOATIVA. " if not dva else "EM USO DE ____ (__/MIN). "
prog += "SEM SEDAÇÃO. " if not sed else "SEDADA COM ____. "
if svd:
	prog += f"DIURESE EM SVD ({diuQt} ML/24H; BH: {bh}). "
else:
	if diu:
		prog += f"DIURESE PRESENTE. "
	else:
		prog += f"DIURESE AUSENTE. "
if bowel == "SIM":
	prog += f"DEJEÇÕES E FLATOS PRESENTES. "
else:
	if bowel == "FLATOS":
		prog += f"DEJEÇÕES AUSENTES (FLATOS PRESENTES). "
	else:
		prog += f"DEJEÇÕES AUSENTES. "	
if sne:
	if diet == "ZERO":
		prog += f"EM USO DE SNE, DIETA ZERO. "
	elif diet == "SIM":
		prog += f"EM USO DE SNE, SEM RETORNOS. "
	else:
		prog += f"EM USO DE SNE, COM RETORNO DE ____ML. "
else:
	if diet == "ZERO":
		prog += f"EM DIETA ZERO. "
	elif diet == "SIM":
		prog += f"BOA ACEITAÇÃO DE DIETA VIA ORAL. "
	else:
		prog += f"ACEITAÇÃO RUIM DE DIETA VIA ORAL. "
if emesis:
	prog += f"APRESENTA ÊMESE (_ EPISÓDIOS). "
elif nausea:
	prog += f"APRESENTA NÁUSEAS. "
else:
	prog += f"NEGA NAUSEA E VÔMITOS. "
if walk:
	prog += f"DEAMBULA SEM DIFICULDADES. "
else:
	prog += f"SEM DEAMBULAR. "
if postPartum:
	if milk:
		prog += f"AMAMENTANDO. "
	else:
		prog += f"SEM AMAMENTAR, [MOTIVO]. "
else:
	prog += f"NEGA PERDA DE LÍQUIDO E SANGRAMENTO. NEGA SINTOMAS URINÁRIOS. "
prog += f"NEGA OUTRAS QUEIXAS. "
if preec:
	prog += " RELATA SINAIS DE IMINÊNCIA DE ECLÂMPSIA: [SINAL]." if severitySigns else " NEGA SINAIS DE IMINÊNCIA DE ECLÂMPSIA."

#PHYSICAL EXAM
exFis = "ECTOSCOPIA: "+ect+"\n"
exFis += "MAMAS: "+mamas+"\n"
exFis += "CV: "+cv+"\n"
exFis += "AP: "+ap+"\n"
exFis += "ABDOME: "+abd+"\n"
exFis += "NEUR: "+neur+"\n"
if postPartum:
	if laborMode == "CESÁREA":
		exFis += "FO: "+fo+"\n"
	exFis += "LOQUIOS: "+loq+"\n"
else:
	exFis += "TV: "+tv+"\n"
exFis += "EXTREMIDADES: "+ext+"\n"

#TEXT AREAS
hd = st.text_area("Hipóteses diagnósticas:", value=hypothesis)
hda = st.text_area("História da doença atual:", height=300, value=history)
ap = st.text_area("Antecedentes pessoais:", value=pHist)
evol = st.text_area("Evolução:", height = 200, value=prog)

string = f"ID: {name}, {age} ANOS, G{g} PV{pv} PC{pc} A{a}\nADM HDM: {admDate};\n"
if not postPartum:
	string += f"IG[DUM]: {gestAgeLmp[0]}S {gestAgeLmp[1]}D;" if igToDays (gestAgeLmp[0],gestAgeLmp[1]) > 0 else "IG[DUM]: NÃO SABE INFORMAR;"
	string += f" IG[USG]: {gestAgeUsg[0]}S {gestAgeUsg[1]}D;\n" if usg else "\n"
string += f"TS[MÃE]: {momBlood} | TS[NEONATO]: {nbBlood}\n(TESTES RÁPIDOS) SÍFILIS: "
string += "REAGENTE" if sif else "NR"
string += " |  HIV: "
string += "REAGENTE" if hiv else "NR"
string += " |  HCV: "
string += "REAGENTE" if hcv else "NR"
string += " |  HbsAg: "
string += "REAGENTE" if hbs else "NR"
string += ";\n\n"
string += "#HD:\n"
string += hd
string += "\n\n#HDA: "
string += hda
string += "\n\n#CPN: X CONSULTAS [SEM ALTERAÇÕES PRESSÓRICAS/COM ALTERAÇÕES PRESSÓRICAS A PARTIR DE XX SEMANAS]. GJ: ; TOTG: (JEJUM)| (1H)| (2H). SOROLOGIAS: NR."
string += "\n\n#AP: "
string += ap
string += "\n\n#EM USO:\n\n#FEZ USO:\n\n#DADOS DA ENFERMAGEM:\nPA: X | X | X | X MMHG\nTAX:  |  |  |  ºC\nFC:  |  |  |  BPM\nBCF:  |  |  |  BPM"
string += "\n\n#EVOLUÇÃO: "
string += evol
string += "\n\n#EXAME FÍSICO:\n"
string += exFis
string += "\n#EXAMES COMPLEMENTARES:\n-LABORATÓRIO:\n\n-IMAGEM:\n\n#PROGRAMAÇÃO:\n"
string += "\n#CONDUTA:\n"

string = string.upper()
st.subheader("🧾 EVOLUÇÃO:")
st.text_area("TEXTO:", height = 500, value = string)
