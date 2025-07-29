import streamlit as st
from datetime import date
import datetime
import math

bgmom = ""
rhmom = ""
momBlood = "XX"
bgnb = ""
rhnb = ""
nbBlood = "AGUARDO"
afu = 0
preec = False
sne = False
laborDate = date.today().strftime("%d/%m/%Y")

def nDaysBetween (date1, date2):
	s1 = date1.split("/")
	s2 = date2.split("/")
	dateC1 = datetime.datetime(int(s1[2]),int(s1[1]),int(s1[0]))
	dateC2 = datetime.datetime(int(s2[2]),int(s2[1]),int(s2[0]))
	return (dateC2 - dateC1).days
	
def nDaysBetweenAbs (date1, date2):
	s1 = date1.split("/")
	s2 = date2.split("/")
	dateC1 = datetime.datetime(int(s1[2]),int(s1[1]),int(s1[0]))
	dateC2 = datetime.datetime(int(s2[2]),int(s2[1]),int(s2[0]))
	return abs((dateC2 - dateC1).days)

def igToDays (weeks, days):
	return days+weeks*7

def daysToIg (days):
	return [math.floor(days/7), days%7]

st.header("📝 EVOLUÇÃO DOM MALAN")
st.subheader("🐁🐀")
st.write("<todo texto inserido será convertido para caixa alta>")

#QUESTIONAIRE
##ID + POINT-OF-CARE TESTS
name = st.text_input("NOME:")
c1, c2, c3, c4, c5, c6, c7, c8, c9 = st.columns([1.5,1,1,1,1,1.7,1.5,1.5,1.5])
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
if gesthyp or crhyp:
	with c5:
		c6, c7 = st.columns(2)
		with c6:
			severePreec = st.checkbox("DETERIORAÇÃO")
		with c7:
			preec = st.checkbox("PRÉ-ECLÂMPSIA", value=severePreec)

##MOTHER BLOOD TYPE
c1, c2 = st.columns(2)
with c1:
	disp = st.checkbox("TIPO SANGUÍNEO DA MÃE DISPONÍVEL")
with c2:
	icu = st.checkbox("UTI")
if disp:
	c3, c4 = st.columns(2)
	with c3:
		bgmom = st.radio("TIPO:", ["O", "A", "B", "AB"], key="radio1", horizontal=True)
	with c4:
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
	postPartum = st.checkbox("PUÉRPERA")
with c4:
	usg = st.checkbox("USG DISPONÍVEL")

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

#LABOR + NEWBORN BLOOD TYPE
if postPartum:
	c1, c2, c3, c4, c5, c6 = st.columns([2.5,2.2,1.7,2.6,1.6,1.6])
	with c1:
		laborMode = st.radio("VIA:", ["VAGINAL", "CESÁREA"], key="radio3")
	with c2:
		laborDate = st.text_input("DATA:", value=date.today().strftime("%d/%m/%Y"))
	with c3:
		laborTime = st.text_input("HORA:")
	with c4:
		nbSex = st.radio("SEXO:", ["MASCULINO", "FEMININO"], key="nbSex")
	with c5:
		nbWeight = st.text_input("PESO:")
	with c6:
		nbApgar = st.text_input("APGAR:")
	
	if st.checkbox("TIPO SANGUÍNEO DO NEONATO DISPONÍVEL"):
		c7, c8 = st.columns(2)
		with c7:
			bgnb = st.radio("TIPO:", ["O", "A", "B", "AB"], key="radio4", horizontal=True)
		with c8:
			rhnb = st.radio("Rh:", ["POSITIVO", "NEGATIVO"], key="radio5", horizontal=True)
			if rhnb == "POSITIVO":
				rhnb = "+"
			else:
				rhnb = "-"
		nbBlood = bgnb+rhnb

if postPartum:
	#LMP GESTATIONAL AGE TO PARTUM
	gestAgeLmp = daysToIg( nDaysBetween ( lmpDate, laborDate ) )
	if usg:
		#USG GESTATIONAL AGE TO PARTUM
		gestAgeUsg = daysToIg( nDaysBetweenAbs( usgDate, laborDate ) + igToDays( int(usgWeeks), int(usgDays) ) )
else:
	#LMP GESTATIONAL AGE
	gestAgeLmp = daysToIg( nDaysBetweenAbs( lmpDate, date.today().strftime("%d/%m/%Y") ) )

	if usg:
		#USG GESTATIONAL AGE
		gestAgeUsg = daysToIg( nDaysBetweenAbs( usgDate, date.today().strftime("%d/%m/%Y") ) + igToDays( int(usgWeeks), int(usgDays) ) )

c1, c2 = st.columns(2)
with c1:
	if postPartum:
		st.write(f"IG NO PARTO:")
	st.write(f"IG DUM: {gestAgeLmp[0]}S {gestAgeLmp[1]}D ({lmpDate})" if igToDays (gestAgeLmp[0],gestAgeLmp[1]) > 0 else "IG DUM : NÃO SABE INFORMAR")
with c2:
	st.write(f"IG USG: {gestAgeUsg[0]}S {gestAgeUsg[1]}D ({usgDate}; {usgWeeks}D {usgDays}D)" if usg else "IG USG : INDISPONÍVEL")

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

#DIURESIS
#mark: diu, svd, - bh, qt - sne, vm
c1, c2, c3, c4, c5, c6 = st.columns([1,1,1,1,1,1])
with c1:
	svd = st.checkbox("SVD")
with c2:
	diu = st.checkbox("DIURESE", value=True)
if svd:
	with c3:
		diuQt = st.text_input("ML:")
	with c4:
		bh = st.text_input("BH:")
with c5:
	if icu:
		sne = st.checkbox("SNE")
with c6:
	if icu:
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
	walk = st.checkbox("DEAMBULA", value=True)
with c3:
	if icu:
		sed = st.checkbox("SEDAÇÃO")

#VITAL SIGNS
#box: pa, fc, spo, fr, gcs, o2, dva
c1, c2, c3, c4, c5, c6, c7, c8, c9 = st.columns(9)
with c1:
	pa = st.text_input("PA:")
with c2:
	fc = st.text_input("FC:", value="80")
with c3:
	spo2 = st.text_input("SpO2:", value="99")
with c4:
	fr = st.text_input("FR:", value="16")
with c7:
	gcs = st.text_input("GCS:", value="15")
with c8:
	if icu:
		o2 = st.checkbox("O2", value=vm)
with c9:
	if icu:
		dva = st.checkbox("DVA")

st.write("EM CASO DE PÓS PARTO, COLOCAR VALORES NEGATIVOS NA AFU SE ABAIXO DA CICATRIZ UMBILICAL")

#FETAL VITAL SIGNS
#fetus: bcf, afu, du, mov. fetal
if not postPartum:
	c1, c2, c3, c4, c5 = st.columns([1,1,1,3,1])
	with c1:
		afu = round(float(st.text_input("AFU:", value = "0")), 1)
	with c2:
		bcf = st.text_input("BCF:")
	with c3:
		du = st.checkbox("DU")
	with c4:
		movFet = st.checkbox("MOV. FETAL", value=True)
else:
	c1, c2, c3 = st.columns([1,2,4])
	with c1:
		afu = round(float(st.text_input("AFU:", value = "0")), 1)
	with c2:
		milk = st.checkbox("AMAMENTAÇÃO", value=True)
	with c3:
		if postPartum:
			ltb = st.checkbox("LAQUEADURA")

#box+: eminencia, >fio2, pinsp, peep,< ou >qtO2<
if crhyp or gesthyp:
	severitySigns = st.checkbox("SINAIS DE IMINÊNCIA DE ECLÂMPSIA")


#PHYSICAL EXAM
ect = st.text_input("ECTOSCOPIA:", value="EG BOM, CONSCIENTE E ORIENTADA, EUPNEICA, NORMOCORADA, HIDRATADA, ACIANÓTICA, ANICTÉRICA, AFEBRIL.")
mamas = st.text_input("MAMAS:", value="MAMAS FLÁCIDAS, SEM FISSURAS OU SINAIS FLOGÍSTICOS.")
cv = st.text_input("CARDIOVASCULAR:", value=f"RCR EM 2T, BNF, SEM SOPROS, CLIQUES OU ESTALIDOS. PA: {pa} MMHG | FC: {fc} BPM")
ap = st.text_input("AUSCULTA PULMONAR:", value=f"MV+ EM AHT, SEM RUÍDOS ADVENTÍCIOS. SpO2: {spo2}% | FR: {fr} IRPM")
if postPartum:
	abdVal = f"SEMIGLOBOSO, RUÍDOS HIDROAÉREOS PRESENTES, DEPRESSÍVEL, "
	abdVal += f"INDOLOR À PALPAÇÃO" if laborMode == "VAGINAL" else "DOLOROSO À PALPAÇÃO PROFUNDA EM REGIÃO SUPRAPÚBICA"
	abdVal += f", SEM SINAIS DE IRRITAÇÃO PERITONEAL, ÚTERO CONTRAÍDO "
	if afu > 0:
		abdVal += f"{afu} CM ACIMA DA CICATRIZ UMBILICAL."
	elif afu < 0:
		afu *= -1
		abdVal += f"{afu} CM ABAIXO DA CICATRIZ UMBILICAL."
	else:
		abdVal += f"NO NÍVEL DA CICATRIZ UMBILICAL."
else:
	abdVal = f"GRAVÍDICO, RUÍDOS HIDROAÉREOS PRESENTES, INDOLOR À PALPAÇÃO, TÔNUS UTERINO FISIOLÓGICO, DINÂMICA UTERINA "
	abdVal += "PRESENTE. " if du else "AUSENTE. "
	abdVal += "MOVIMENTAÇÕES FETAIS "
	abdVal += "PRESENTES." if movFet else "AUSENTES."
	abdVal += f" BCF: {bcf} BPM | AFU: {afu} CM"
abd = st.text_input("ABDOME:", value=abdVal)
neur = st.text_input("NEUROLÓGICO:", value=f"GLASGOW {gcs}, SEM SINAIS DE DÉFICITS NEUROLÓGICOS FOCAIS.")
if postPartum:
	if laborMode == "CESÁREA" or ltb:
		fo = st.text_input("FO:", value="FERIDA OPERATÓRIA LIMPA E SEM SINAIS FLOGÍSTICOS.")
	loq = st.text_input("LOQUIOS:", value="RUBROS, SEM ODOR, EM PEQUENA QUANTIDADE.")
else:
	tv = st.text_input("TOQUE VAGINAL:", value="TOQUE VAGINAL NÃO REALIZADO.")
ext = st.text_input("EXTREMIDADES:", value="EDEMA (+1/+4) EM MMII. TEC <3S. SEM SINAIS DE TROMBOSE. PULSOS PRESENTES E SIMÉTRICOS.")

#HYPOTHESIS
if postPartum:
	hypothesis = f"- PUERPÉRIO IMEDIATO DE PARTO {laborMode} REALIZADO DIA {laborDate} ÀS {laborTime} SEC. IG"
	hypothesis += f" {gestAgeLmp[0]}S {gestAgeLmp[1]}D (DUM: {lmpDate}) " if igToDays (gestAgeLmp[0],gestAgeLmp[1]) > 0 else ""
	hypothesis += f" {gestAgeUsg[0]}S {gestAgeUsg[1]}D (USG: {usgDate}; {usgWeeks}S {usgDays}D)\n" if usg else ""
	if ltb:
		hypothesis += f"\n- PO LAQUEADURA"
else:
	hypothesis = f"- GUT"
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
	hypothesis += f"COM"
	hypothesis += f" {gestAgeLmp[0]}S {gestAgeLmp[1]}D (DUM: {lmpDate}) " if igToDays (gestAgeLmp[0],gestAgeLmp[1]) > 0 else ""
	hypothesis += f" {gestAgeUsg[0]}S {gestAgeUsg[1]}D (USG: {usgDate}; {usgWeeks}S {usgDays}D)\n" if usg else ""
	
hypothesis += f"\n- INCOMPATIBILIDADE SANGUÍNEA MATERNO-FETAL" if (rhmom == "-" and rhnb == "+") else ""
if dm:	
	hypothesis += f"\n- DIABETES MELLITUS {dmType}"	
if crhyp:
	if preec:
		hypothesis += f"\n- PRÉ-ECLÂMPSIA SOBREPOSTA"
		hypothesis += f" COM SINAIS DE DETERIORAÇÃO CLÍNICA" if severePreec else ""
	else:
		hypothesis += f"\n- HAS CRÔNICA"
elif gesthyp:
	if preec:
		hypothesis += f"\n- PRÉ-ECLÂMPSIA"
		hypothesis += f" COM SINAIS DE DETERIORAÇÃO CLÍNICA" if severePreec else ""
	else:
		hypothesis += f"\n- HAS GESTACIONAL"
hypothesis += f"\n- TR SÍFILIS REAGENTE" if sif else ""
hypothesis += f"\n- TR HIV REAGENTE" if hiv else ""
hypothesis += f"\n- TR HCV REAGENTE" if hcv else ""
hypothesis += f"\n- TR HbsAg REAGENTE" if hbs else ""

#HISTORY
history = f"PACIENTE, G{g}P"
history += str(int(pv)+int(pc)-1) if postPartum and not nDaysBetween(laborDate, admDate) > 0 else str(int(pv)+int(pc))
if postPartum:
	gestAgeAdm = daysToIg( igToDays(gestAge[0], gestAge[1]) - nDaysBetweenAbs( admDate, laborDate ) )
else:
	gestAgeAdm = daysToIg( igToDays(gestAge[0], gestAge[1]) - nDaysBetweenAbs( admDate, date.today().strftime("%d/%m/%Y") ) )
history += f"A{a}, "
history += f"PUÉRPERA" if postPartum and nDaysBetween(laborDate, admDate) > 0 else f"EM CURSO DE IG: {gestAgeAdm[0]}S {gestAgeAdm[1]}D {modeChosen}"
history += f", DEU ENTRADA NESTE SERVIÇO DIA {admDate}, [MOTIVO]. AO EXAME FISICO ADMISSIONAL, APRESENTAVA-SE COM [EXAME FÍSICO ADMISSIONAL]. PACIENTE FOI INTERNADA PARA [OBJETIVO INTERNAMENTO]. "
if postPartum:
	history += f"PARTO {laborMode} REALIZADO EM {laborDate} ÀS {laborTime} COM RETIRADA DE FETO VIVO, CEFALICO, {nbSex}, APGAR {nbApgar}, PESO {nbWeight} GRAMAS. "
history += f"ENCAMINHADA PARA [ALA]. SEGUE AOS CUIDADOS DA EQUIPE."

#MEDICAL HISTORY
pHist = f"DIABETES MELLITUS {dmType}" if dm and dmType != "GESTACIONAL" else "NEGA DM PRÉ-GESTACIONAL"
pHist += f". HAS CRÔNICA." if crhyp else ". NEGA HAS CRÔNICA."
pHist += " NEGA TRANSFUSÕES. NEGA ETILISMO E TABAGISMO."

#PROGRESS SECTION
prog = "PACIENTE HEMODINAMICAMENTE ESTÁVEL, "
if icu:
	if vm:
		prog += "EM USO DE VENTILAÇÃO MECÂNICA (MODO: ; PINSP/VOL: ; FIO2: ; PEEP: )."
	elif o2:
		prog += "EM USO DE [APARELHO] ([QUANTIDADE] L/MIN)."
	else:
		prog += "RESPIRANDO EM AR AMBIENTE, SEM DESCONFORTO RESPIRATÓRIO. "
	prog += "SEM USO DE DROGA VASOATIVA. " if not dva else "EM USO DE [DVA] ([QUANTIDADE]). "
	prog += "SEM SEDAÇÃO. " if not sed else "SEDADA COM [SEDAÇÃO]. "
else:
	prog += "RESPIRANDO EM AR AMBIENTE, SEM DESCONFORTO RESPIRATÓRIO. "
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
		prog += f"EM USO DE SNE, COM RETORNO DE [QUANTIDADE] ML. "
else:
	if diet == "ZERO":
		prog += f"EM DIETA ZERO. "
	elif diet == "SIM":
		prog += f"BOA ACEITAÇÃO DE DIETA VIA ORAL. "
	else:
		prog += f"ACEITAÇÃO RUIM DE DIETA VIA ORAL. "
if emesis:
	prog += f"APRESENTA ÊMESE ([QUANTIDADE] EPISÓDIOS). "
elif nausea:
	prog += f"APRESENTA NÁUSEAS. "
else:
	prog += f"NEGA NÁUSEA E VÔMITOS. "
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
if crhyp or gesthyp:
	prog += " RELATA SINAIS DE IMINÊNCIA DE ECLÂMPSIA: [SINAL]." if severitySigns else " NEGA SINAIS DE IMINÊNCIA DE ECLÂMPSIA."

#PHYSICAL EXAM
exFis = "ECT: "+ect+"\n"
exFis += "MAMAS: "+mamas+"\n"
exFis += "CV: "+cv+"\n"
exFis += "AP: "+ap+"\n"
exFis += "ABD: "+abd+"\n"
exFis += "NEUR: "+neur+"\n"
if postPartum:
	if laborMode == "CESÁREA":
		exFis += "FO: "+fo+"\n"
	exFis += "LOQ: "+loq+"\n"
else:
	exFis += "TV: "+tv+"\n"
exFis += "EXT: "+ext+"\n"

#TEXT AREAS
hd = st.text_area("Hipóteses diagnósticas:", value=hypothesis)
hda = st.text_area("História da doença atual:", height=300, value=history)
cpn = st.text_area("Cartão pré-natal:", value="X CONSULTAS [SEM ALTERAÇÕES PRESSÓRICAS/COM ALTERAÇÕES PRESSÓRICAS A PARTIR DE XX SEMANAS]. GJ: ; TOTG: (JEJUM)| (1H)| (2H). SOROLOGIAS: NR.")
ap = st.text_area("Antecedentes pessoais:", value=pHist)
evol = st.text_area("Evolução:", height = 200, value=prog)

string = f"#ID: {name}, {age} ANOS, G{g} PV{pv} PC{pc} A{a}, ADM HDM: {admDate}\n"
#string += f"(NO PARTO) " if postPartum else ""
#string += f"IG DUM: {gestAgeLmp[0]}S {gestAgeLmp[1]}D ({lmpDate})" if igToDays (gestAgeLmp[0],gestAgeLmp[1]) > 0 else "IG DUM: INCERTA"
#string += f" | IG USG: {gestAgeUsg[0]}S {gestAgeUsg[1]}D ({usgDate}; {usgWeeks}D {usgDays}D)\n" if usg else "\n"
string += f"TS MÃE: {momBlood}"
string += f" | TS NEONATO: {nbBlood} | " if postPartum and rhmom == "-" else " | "
string += "(TESTES RÁPIDOS) SÍFILIS: "
string += "REAGENTE" if sif else "NR"
string += " |  HIV: "
string += "REAGENTE" if hiv else "NR"
string += " |  HCV: "
string += "REAGENTE" if hcv else "NR"
string += " |  HbsAg: "
string += "REAGENTE" if hbs else "NR"
string += "\n\n"
string += "#HD:\n"
string += hd
string += "\n\n#HDA: "
string += hda
string += "\n\n#CPN: "
string += cpn
string += "\n\n#AP: "
string += ap
string += "\n\n#EM USO:\n- DIETA LIVRE\n- SULFATO FERROSO PROFILÁTICO\n- SINTOMÁTICOS\n"
string += "\n#FEZ USO:\n\n#DADOS DA ENFERMAGEM:\nPA:  |  |  |  MMHG\nTAX: SEM DISTERMIAS (MAX º)\nFC: - BPM"
string += f"" if postPartum else "\nBCF:  |  |  |  BPM"
string += "\n\n#EVOLUÇÃO: "
string += evol
string += "\n\n#EXAME FÍSICO:\n"
string += exFis
string += "\n#EXAMES COMPLEMENTARES:\n-LABORATÓRIO:\n\n-IMAGEM:\n\n#MÉTODO CONTRACEPTIVO DE ESCOLHA:\n"
string += f"" if postPartum else "\n#PROGRAMAÇÃO:\n"
string += "\n#CONDUTA:\n- COMUNICAR INTERCORRÊNCIAS AO PLANTÃO\n\nCASO E CONDUTA DISCUTIDOS COM PRECEPTORIA | RESIDENTE | INTERNO MATEUS"

string = string.upper()
st.subheader("🧾 EVOLUÇÃO:")
st.write("Obs: todo texto abaixo será automaticamente apagado e reescrito caso haja alguma edição nos campos acima")
st.text_area("TEXTO:", height = 500, value = string)
