import streamlit as st
from datetime import date

bgmom = ""
rhmom = ""
momBlood = "XX"
bgnb = ""
rhnb = ""
nbBlood = "XX"
afu = 0
preec = False

st.header("📝 EVOLUÇÃO DOM MALADO")
st.subheader("🐁exclusive 4 ratchex🐀")
st.write("<todo texto digitado será convertido para caixa alta>")

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
c4, c5 = st.columns([3,2])
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
			preec = st.checkbox("PRÉ-ECLÂMPSIA")
		with c7:
			severePreec = st.checkbox("SEVERA")

##MOTHER INFO
if st.checkbox("TS[MÃE] DISPONÍVEL?"):
	c1, c2 = st.columns(2)
	with c1:
		bgmom = st.radio("Tipo:", ["O", "A", "B", "AB"], key="radio1", horizontal=True)
	with c2:
		rhmom = st.radio("Rh:", ["POSITIVO", "NEGATIVO"], key="radio2", horizontal=True)
		if rhmom == "POSITIVO":
			rhmom = "+"
		else:
			rhmom = "-"
	momBlood = bgmom+rhmom	

c1, c2, c3 = st.columns([3,1,3])
with c1:
	weeks = st.text_input("IG(HOJE/PARTO) SEMANAS:")
with c2:
	days = st.text_input("DIAS:")
with c3:
	admDate = st.text_input("DATA ADMISSÃO:", value=date.today().strftime("%d/%m/%Y"))

#LABOR + NEWBORN INFO
postPartum = st.checkbox("PÓS PARTO?")
if postPartum:
	c1, c2, c3 = st.columns([2,1,1])
	with c1:
		laborMode = st.radio("VIA:", ["VAGINAL", "CESÁREA"], key="radio3", horizontal=True)
	with c2:
		laborDate = st.text_input("DATA:", value=date.today().strftime("%d/%m/%Y"))
	with c3:
		laborTime = st.text_input("HORA:")
	if st.checkbox("TS[RN] DISPONÍVEL?"):
		c4, c5 = st.columns(2)
		with c4:
			bgnb = st.radio("Tipo:", ["O", "A", "B", "AB"], key="radio4", horizontal=True)
		with c5:
			rhnb = st.radio("Rh:", ["POSITIVO", "NEGATIVO"], key="radio5", horizontal=True)
			if rhnb == "POSITIVO":
				rhnb = "+"
			else:
				rhnb = "-"
		nbBlood = bgnb+rhnb

#DIURESIS
c1, c2, c3, c4, c5, c6 = st.columns([4,2,1,1,1,1])
with c1:
	diu = st.checkbox("DIURESE")
with c2:
	svd = st.checkbox("SVD")
if svd:
	with c3:
		diuQt = st.text_input("ML:")
	with c4:
		bh = st.text_input("BH:")
with c5:
	sne = st.checkbox("SNE")
with c6:
	vm = st.checkbox("VM")

#BOWEL MOVEMENTS
bowel = st.radio("DEJEÇÕES:", ["SIM", "FLATOS", "NÃO"], key="radioBowel", horizontal=True)

#VITAL SIGNS
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
	o2 = st.checkbox("O2")
with c9:
	dva = st.checkbox("DVA")

st.write("EM CASO DE PÓS PARTO, COLOCAR VALORES NEGATIVOS NA AFU SE ABAIXO DA CIC. UMBILICAL")
c1, c2, c3, c4 = st.columns([1,1,1,4])
with c1:
	afu = int(st.text_input("AFU:", value = "0"))
if not postPartum:
	with c2:
		bcf = st.text_input("BCF:")
	with c3:
		du = st.checkbox("DU")
	with c4:
		movFet = st.checkbox("MOV. FETAL")
else:
	with c2:
		milk = st.checkbox("AMAMENTAÇÃO")

if preec:
	severitySigns = st.checkbox("SINAIS DE IMINÊNCIA DE ECLÂMPSIA")

#mark: diu, svd, - bh, qt - sne, vm,
#ratio: dej: s, flat, n
#fetus: bcf, afu, du, mov. fetal
#box: pa, fc, spo, fr, gcs, o2, dva, >sedação<, >deambulação<
#box+: eminencia, >fio2, pinsp, peep,<

#PHYSICAL EXAM
ect = st.text_input("ECTOSCOPIA:", value="EG BOM, CONSCIENTE E ORIENTADA, EUPNEICA, NORMOCORADA, HIDRATADA, ACIANÓTICA, ANICTÉRICA, AFEBRIL")
mamas = st.text_input("MAMAS:", value="MAMAS FLASCIDAS, SEM FISSURAS OU SINAIS FLOGÍSTICOS")
cv = st.text_input("CARDIOVASCULAR:", value=f"RITMO CARDÍACO REGULAR EM 2 TEMPOS, BULHAS NORMOFONÉTICAS, SEM SOPROS, CLIQUES OU ESTALIDOS; PA: {pa} MMHG | FC: {fc} BPM")
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
	abdVal = f"GRAVÍDICO, SEM DOR À PALPAÇÃO, TÔNUS UTERINO FISIOLÓGICO, DINÂMICA UTERINA "
	abdVal += "PRESENTE. " if du else "AUSENTE. "
	abdVal += "MOVIMENTAÇÕES FETAIS "
	abdVal += "PRESENTES." if du else "AUSENTES."
	abdVal += f"BCF: {bcf} BPM | AFU: {afu} CM"
abd = st.text_input("ABDOME:", value=abdVal)
neur = st.text_input("NEUROLÓGICO:", value=f"GLASGOW {gcs}, SEM SINAIS DE DÉFICITS NEUROLÓGICOS FOCAIS.")
if postPartum:
	fo = st.text_input("FO:", value="FERIDA OPERATÓRIA LIMPA E SEM SINAIS FLOGÍSTICOS.")
else:
	tv = st.text_input("TV:", value="TOQUE VAGINAL NÃO REALIZADO.")
ext = st.text_input("EXTREMIDADES:", value="SEM EDEMA OU SINAIS DE TROMBOSE, PULSOS PRESENTES E SIMÉTRICOS.")

#HYPOTHESIS
hypothesis = f"1. PUERPÉRIO IMEDIATO DE PARTO {laborMode} REALIZADO DIA {laborDate} ÀS {laborTime}\n" if postPartum else ""
hypothesis += f"2. INCOMPATIBILIDADE SANGUÍNEA MATERNO-FETAL\n" if (rhmom == "+" and rhnb == "-") else ""
if dm:	
	hypothesis += f". DIABETES MELLITUS {dmType}\n"	
if crhyp:
	hypothesis += f". HAS CRÔNICA\n"
if gesthyp:
	if preec:
		hypothesis += f". PRÉ-ECLÂMPSIA"
		hypothesis += f" COM SINAIS DE DETERIORAÇÃO CLÍNICA\n" if severePreec else "\n"
	else:
		hypothesis += f". HAS GESTACIONAL\n"
hypothesis += f". TR SÍFILIS REAGENTE\n" if sif else ""
hypothesis += f". TR HIV REAGENTE\n" if hiv else ""
hypothesis += f". TR HCV REAGENTE\n" if hcv else ""
hypothesis += f". TR HbsAg REAGENTE\n" if hbs else ""

#HISTORY
history = f"PACIENTE, G{g}P"
history += str(int(pv)+int(pc)-1) if postPartum else str(int(pv)+int(pc))
history += f"A{a}, EM CURSO DE IG: _[IG ADM]_, DEU ENTRADA NESTE SERVIÇO DIA {admDate}, DEVIDO ________.AO EXAME FISICO ADMISSIONAL, APRESENTAVA-SE COM ________. PACIENTE FOI INTERNADA PARA ________."
if postPartum:
	history += f"PARTO {laborMode} REALIZADO EM {laborDate} ÀS {laborTime} COM RETIRADA DE FETO VIVO, CEFALICO, _[SEXO]_, APGAR __, PESO ____G."
history += f"ENCAMINHADA PARA _[ALA]_. SEGUE AOS CUIDADOS DA EQUIPE."

#MEDICAL HISTORY
pHist = f"DIABETES MELLITUS {dmType}" if dm and dmType != "GESTACIONAL" else "NEGA DM"
pHist += f". HAS CRÔNICA." if crhyp else " NEGA HAS."
pHist += " NEGA CIRURGIAS E INTERNAMENTOS PRÉVIOS. NEGA TRANSFUSÕES. NEGA ETILISMO E TABAGISMO."

#PROGRESS SECTION
#TEMP.!
prog = "PACIENTE HEMODINAMICAMENTE ESTÁVEL, RESPIRANDO EM AR AMBIENTE, SEM USO DE DROGA VASOATIVA OU SEDAÇÃO. DIURESE (__ML/24H EM SVD, BH: __) E DEJEÇÕES AUSENTES (FLATOS PRESENTES). BOA ACEITAÇÃO DE DIETA VIA ORAL. DEAMBULANDO E AMAMENTANDO SEM DIFICULDADES. SEM QUEIXAS."
if preec:
	prog += " RELATA SINAIS DE IMINÊNCIA DE ECLÂMPSIA." if severitySigns else " NEGA SINAIS DE IMINÊNCIA DE ECLÂMPSIA."
#prog = "PACIENTE HEMODINAMICAMENTE ESTÁVEL, "
#prog += "EM O2 SUPLEMENTAR" if o2 else "RESPIRANDO EM AR AMBIENTE"
#prog += "EM USO DE DVA." if dva else " SEM DROGA VASOATIVA."
#prog += "DIURESE PRESENTE" if diu else "SEM DIURESE"
#prog += "USO DE O2 ("+o2+" L/MIN)" if int(o2)>0 else "RESPIRANDO EM AR AMBIENTE"
#prog += "USO DE O2 ("+o2+" L/MIN)" if int(o2)>0 else "RESPIRANDO EM AR AMBIENTE"

#PHYSICAL EXAM
exFis = "ECTOSCOPIA: "+ect+"\n"
exFis += "MAMAS: "+mamas+"\n"
exFis += "CV: "+cv+"\n"
exFis += "AP: "+ap+"\n"
exFis += "ABDOME: "+abd+"\n"
exFis += "NEUR: "+neur+"\n"
exFis += "FO: "+fo+"\n" if postPartum else "TV: "+tv+"\n"
exFis += "EXTREMIDADES: "+ext+"\n"

#TEXT AREAS
hd = st.text_area("Hipóteses diagnósticas:", value=hypothesis)
hda = st.text_area("História da doença atual:", height=300, value=history)
ap = st.text_area("Antecedentes pessoais:", value=pHist)
evol = st.text_area("Evolução:", height = 200, value=prog)

string = f"ID: {name}, {age} ANOS, G{g} PV{pv} PC{pc} A{a}\nTS[MÃE]: {momBlood} | TS[NEONATO]: {nbBlood}\n(TESTES RÁPIDOS) SÍFILIS: "
string += "REAGENTE" if sif else "NR"
string += " |  HIV: "
string += "REAGENTE" if hiv else "NR"
string += " |  HCV: "
string += "REAGENTE" if hcv else "NR"
string += " |  HbsAg: "
string += "REAGENTE" if hbs else "NR"
string += ";\n"
string += "#HD:\n"
string += hd
string += "\n#HDA: "
string += hda
string += "\n\n#CPN: "
string += "\n\n#AP: "
string += ap
string += "\n\n#EVOLUÇÃO: "
string += evol
string += "\n\n#EXAME FÍSICO:\n"
string += exFis

string = string.upper()
st.subheader("🧾 EVOLUÇÃO:")
st.text_area("TEXTO:", height = 500, value = string)
