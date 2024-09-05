@startuml main
Title SIS Information Model
hide empty members
skinparam class {
    BackgroundColor<<enum>> #lightgreen
}

!startsub 1_2_Videregaaende_uddannelse
class VideregåendeUddannelse {
  fagbetegnelse: ? [[1..1]]
  /grad: Calculated [[1..1]]
  tilrettelæggelsesform: PicklistMulti [[1..2]]
  normeretStudietid: Number.1 [[1..*]]
  ECTS-point: Number.1 [[1..*]]
  optagelseskode: Text80 [[0..*]]
  aktivitetsgruppekode: Text80 [[1..*]]
  uddannelsesbetegnelseLatinHankøn: ? [[1..1]]
  uddannelsesbetegnelseDansk: ? [[1..1]]
  uddannelsesbetegnelseEngelsk: ? [[1..1]]
  uddannelsestype: PicklistMulti [[1..*]]
  uddannelsesKaldenavn: Text80 [[0..1]]
  uddannelsessystem: Picklist [[1..1]]
  uddannelsesbetegnelseLatinHunkøn: ? [[1..1]]
  sidsteStudiestartsdato: Date [[0..1]]
  /uddannelsesniveau: Calculated [[1..1]]
  /taxameterindplacering: Calculated [[1..*]]
  godkendtSprog: Picklist [[1..1]]
  læringsudbytte: ? [[1..1]]
  erElæringsuddannelse: Checkbox [[1..1]]
  <<BK>>
  uddannelsesId: AutoNum [[1..1]]
}

class Fagområde {
  videnskabeligtHovedområde: Picklist [[1..1]]
  fagområdenavn: Text80 [[1..1]]
  <<BK>>
  fagområdekode: AutoNum [[1..1]]
}

class UddannelsesansvarligEnhed {
  ansvarsfordeling: ? [[1..1]]
  <<BK>>
  orgEnhedAnsvarsrolle: Picklist [[1..1]]
  /orgEnhedId: IgnoreBK [[1..1]]
  /uddannelsesId: IgnoreBK [[1..1]]
}

class Censorkorps {
  censorkorpsNavn: Text80 [[1..1]]
}

class Uddannelse {
  uddannelseskode: Text80 [[1..1]]
  uddannelsesnavn: Text80 [[1..1]]
}

class UddannelsesansvarligPerson {
  orgPersonAnsvarsrolle: Picklist [[1..1]]
  <<BK>>
  /uddannelsesId: IgnoreBK [[1..1]]
  /orgPersonNavn: IgnoreBK [[1..1]]
  /medlemskabkode: IgnoreBK [[1..1]]
}

class InstitutionsRegister {
  registerNavn: Text80 [[1..1]]
}

class RegisterRegistrering {
  institutionsregisterKode: Text80 [[1..1]]
  institutionsregisterNavn: Text80 [[1..1]]
}

class DanskInstitutionsRegisterRegistrering {
  Institutionstype3kode: Text80 [[1..1]]
  Institutionstype3: ? [[1..1]]
  Enhedsart kode: Text80 [[1..1]]
  Enhedsart tekst: TekstLong [[1..1]]
  email: ? [[1..1]]
  cvr: ? [[1..1]]
}

enum UddannelsesniveauEnum <<enum>> {
  niveau8
  niveau5
  niveau6
  niveau7
  niveau4
}

enum UddannelsestypeEnum <<enum>> {
  akademiskOverbygningsuddannelse
  kandidatuddannelse
  masteruddannelse
  bacheloruddannelse
  kandidatuddannelseErasmusMundusJointMaster
  akademiuddannelse
  diplomuddannelse
  professionsbachelor-uddannelse
  erhvervsakademiuddannelse
  masteruddannelseFleksibel
  Ph.d.-uddannelse
  diplomuddannelseFleksibel
  kandidatuddannelseErhvervskandidat
  akademiuddannelseFleksibel
  akademiskOverbygningsuddannelse.akademiskErhvervsuddannelse
}

enum TilrettelæggelsesformEnum <<enum>> {
  påHeltid
  påDeltid
}

enum VidenskabeligtHovedområdeEnum <<enum>> {
  teologi
  naturvidenskab
  humaniora
  sundhedsvidenskab
  tekniskVidenskab
  samfundsvidenskab
}

enum UddannelsessystemEnum <<enum>> {
  ordinæreUddannelsessystem
  efter-OgVidereuddannelsessystemet
}

enum GradEnum <<enum>> {
  akademigrad
  akademiskOverbygningsgrad
  bachelorgrad
  diplomgrad
  erhvervsakademigrad
  kandidatgrad
  mastergrad
  professionsbachelorgrad
  ph.d.-grad
}

VideregåendeUddannelse "0..*" --  "1..*" Fagområde : hører under
UdbudtVideregåendeUddannelse "0..*" --  "1" VideregåendeUddannelse : udbud af
UddannelsesansvarligEnhed "0..*" --  "1" OrgEnhed : ansvarlig enhed
VideregåendeUddannelse "1" --  "1..*" Studieordning
VideregåendeUddannelse "0..*" --  "1..*" GodkendtUdbudssted : godkendt til udbud ved
UddannelsesansvarligEnhed "1..*" --  "1" VideregåendeUddannelse
StudieforløbFagelementgruppering "0..*" --  "0..1" Fagområde : henføres til
VideregåendeUddannelse "0..*" --  "1" Censorkorps : ansvarligt censorkorps
AdgangsgivendeUddannelse "0..*" --  "1" Uddannelse
Uddannelse "0..*" --  "0..*" Uddannelsesinstitution : samarbejdspartner
VideregåendeUddannelse "0..*" --  "1" Universitet : udbyder
Fagelement "0..*" --  "0..1" VideregåendeUddannelse : defineret i
UddannelsesansvarligPerson "0..*" --  "0..1" OrgPerson
UddannelsesansvarligPerson "0..*" --  "1" VideregåendeUddannelse
VideregåendeUddannelse "0..*" --  "0..*" Censorkorps : tværfakultært censorkorps
UddannelsesansvarligPerson "0..*" --  "0..1" Medlemskab
RegisterRegistrering "0..*" --  "1" InstitutionsRegister
Uddannelsesinstitution "1" --  "0..*" RegisterRegistrering
VideregåendeUddannelse "1" --  "0..*" TidligereOptag
DanskInstitutionsRegisterRegistrering "0..*" --  "0..1" DanskInstitutionsRegisterRegistrering : hovedinstitution
RegisterRegistrering "1" --  "0..1" GodkendtUdbudssted
DanskInstitutionsRegisterRegistrering "0..*" --  "0..1" DanskAdresse
VideregåendeUddannelse --|>  Uddannelse
GymnasialUddannelse --|>  Uddannelse
DanskInstitutionsRegisterRegistrering --|>  RegisterRegistrering
VideregåendeUddannelse .right.>  UddannelsestypeEnum
VideregåendeUddannelse .right.>  TilrettelæggelsesformEnum
Fagområde .right.>  VidenskabeligtHovedområdeEnum
VideregåendeUddannelse .right.>  UddannelsessystemEnum
UddannelsesansvarligEnhed .right.>  OrgEnhedAnsvarsrolleEnum
VideregåendeUddannelse .right.>  GradEnum
VideregåendeUddannelse .right.>  UddannelsesniveauEnum
VideregåendeUddannelse .right.>  SprogEnum
UddannelsesansvarligPerson .right.>  OrgPersonAnsvarsrolleEnum
!endsub

!startsub 1_3_1_Studieordning
class Studieordning {
  overgangsbestemmelse: ? [[1..1]]
  studieordningsikrafttrædelsesdato: Date [[1..1]]
  studieordningsophørsdato: Date [[0..1]]
  studieordningshjemmel: ? [[1..1]]
  adgangskrav: ? [[1..1]]
  studieordningsbeskrivelse: TekstLong [[1..1]]
  <<BK>>
  studieordningskode: AutoNum [[1..1]]
}

class Studieforløb {
  maksimalStudietid: Number.0 [[1..1]]
  ECTS-point: Number.1 [[1..1]]
  normeretStudietid: Number.1 [[1..1]]
  studieforløbsnavn: Text80 [[1..1]]
  studieforløbsbeskrivelse: TekstLong [[1..1]]
  studieforløbstype: Picklist [[1..1]]
  afsluttendeUddannelseskode: Text80 [[1..1]]
  fagprofilTitelEngelsk: Text80 [[0..1]]
  fagprofilTitelDansk: Text80 [[0..1]]
  kompetenceprofilDansk: ? [[1..1]]
  kompetenceprofilEngelsk: ? [[1..1]]
  sidsteUdbudsdato: Date [[0..1]]
  medPropædeutik: Checkbox [[1..1]]
  <<BK>>
  studieforløbskode: AutoNum [[1..1]]
}

class Studieordningsregel {
  studieordningsregeltype: Picklist [[1..1]]
  studieordningsregelbeskrivelse: TekstLong [[1..1]]
  <<BK>>
  /studieordningskode: IgnoreBK [[1..1]]
  studieordningsregelnr: ? [[1..1]]
}

class DiplomaSupplement {
  erhvervsmæssigStatus: Checkbox [[1..1]]
  karakterbeskrivelse: TekstLong [[1..1]]
  uddannelsesdetaljer: ? [[1..1]]
  uddannelsesinstitutionStatusOgAkkreditering: ? [[1..1]]
  undervisningsOgEksamenssprog: ? [[1..1]]
  videreuddannelseNiveau: ? [[1..1]]
  <<BK>>
  /studieforløbskode: IgnoreBK [[1..1]]
}

class Studieforløbsperiode {
  studieforløbsperiodenavn: Text80 [[1..1]]
  studieforløbsperiodeOmfang: Number.1 [[1..1]]
  <<BK>>
  studieforløbsperiodeRækkefølgeNr: ? [[1..1]]
  /studieforløbskode: IgnoreBK [[1..1]]
}

class AdgangsgivendeUddannelse {
  medRetskrav: Checkbox [[1..1]]
}

class Forløbsprøve {
  forløbsprøvetype: Picklist [[1..1]]
  beståelsesfrist: Date [[1..1]]
  <<BK>>
  /studieforløbskode: IgnoreBK [[1..1]]
  forløbsprøvenr: ? [[1..1]]
}

enum StudieforløbstypeEnum <<enum>> {
  delAfSidefag
  fællesuddannelse
  standardforløb
  delAfTilvalg
  to-fagliguddannelse
  akademiskErhvervsoverbygning
  deltidstilrettelagt
  erhvervskandidat
  fagprofilforløb
}

enum StudieordningsregeltypeEnum <<enum>> {
  tidsgrænseregel
  tilmeldingsregel
  prøveresultatregel
  optagelsesregel
  planlægningsregel
  beståregel
  forudsætningsregel
}

enum ForløbsprøvetypeEnum <<enum>> {
  førsteårsprøve
  studiestartsprøve
}

Studieordningsregel "1..*" --  "1" Studieordning
Studieforløb "1..*" --  "1" Studieordning
UdbudtVideregåendeUddannelse "0..*" --  "1" Studieordning : udbudt studieordning
VideregåendeUddannelse "1" --  "1..*" Studieordning
IndskrivningTilVideregåendeUddannelse "0..*" --  "1" Studieordning : indskrevet til
IndskrivningTilVideregåendeUddannelse "0..*" --  "0..1" Studieforløb : valgt forløb
Studieforløb "1" --  "0..*" StudieforløbFagelementgruppering
Studieforløb "0..1" --  "0..*" GrupperingAfFagelement : sidefag / tilvalg indlånt til
Studieforløb "1" --  "1..*" Studieforløbsperiode : opdelt i
Studieforløbsperiode "1" --  "0..*" FagelementgrupperingIStudieforløbsperiode
Studieforløbsperiode "1" --  "0..*" FagelementIStudieforløbsperiode
AdgangsgivendeUddannelse "0..*" --  "1" Uddannelse
Studieordning "1" --  "1..*" AdgangsgivendeUddannelse : giver adgang til 
StudieforløbFagelement "1..*" --  "1" Studieforløb
Studieforløb "1" --  "0..*" Forløbsprøve
PersonligForløbsprøve "0..*" --  "1" Forløbsprøve
Studieordningsregel "0..*" --  "0..*" Studiedispensation
Studieforløb "1" --  "1" DiplomaSupplement
Studieforløb "1" --  "0..*" UdbudtStudieforløb
Studieforløb .right.>  StudieforløbstypeEnum
Studieordningsregel .right.>  StudieordningsregeltypeEnum
Forløbsprøve .right.>  ForløbsprøvetypeEnum
!endsub

!startsub 1_4_1_Fagelement
class Fagelement {
  ECTS-point: Number.1 [[1..1]]
  læringsmål: ? [[1..1]]
  fagelementnavn: Text80 [[1..1]]
  udbudsfrekvens: ? [[1..1]]
  aktivitetsgruppekode: Text80 [[1..1]]
  uddannelsesniveau: Calculated [[0..1]]
  afviklingssprog: Picklist [[1..1]]
  erRessourceudløsende: Checkbox [[1..1]]
  sidsteUdbudsDato: Date [[0..1]]
  fagelementtype: Picklist [[1..1]]
  kontraktSkalUdarbejdes: ? [[1..1]]
  <<BK>>
  fagelementkode: AutoNum [[1..1]]
}

class Fagelementemne {
  fagelementemnenavn: Text80 [[1..1]]
  <<BK>>
  fagelementemnekode: AutoNum [[1..1]]
}

class FagelementansvarligEnhed {
  ansvarsfordeling: ? [[1..1]]
  <<BK>>
  orgEnhedAnsvarsRolle: Picklist [[1..1]]
  /orgEnhedId: IgnoreBK [[1..1]]
  /fagelementkode: IgnoreBK [[1..1]]
}

class FagelementansvarligPerson {
  <<BK>>
  orgPersonAnsvarsRolle: Picklist [[1..1]]
  /organisationskode: IgnoreBK [[1..1]]
  /personkode: IgnoreBK [[1..1]]
  /fagelementkode: IgnoreBK [[1..1]]
}

class ÆkvivalerendeFaglighed {
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
}

class OverlappendeFaglighed {
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
  /overlappendeFagelementkode: IgnoreBK [[1..1]]
}

enum AfsluttendeOpgavetypeEnum <<enum>> {
  kandidatspeciale
  masterprojekt
  bachelorprojekt
  afsluttendeprojekt
  diplomprojekt
  akademiskOverbygningsprojekt
}

enum FagelementTypeEnum <<enum>> {
  Projektopgave
  Praktik
  ProjektorienteretForløb
  FagspecifiktKursus
  KortKursus
  Kursus
  SærskiltModul
  IndtægtdækketVirksomhedskursus
  AfsluttendeOpgave
  SupplerendeECTS
}

Læringsaktivitet "0..*" --  "1" Fagelement
Prøve "1" --  "1" Fagelement
Fagelement "1" --  "0..*" UdbudtFagelement : udbudt som
Fagelement "1" --  "0..*" FagelementansvarligEnhed : rolle
FagelementansvarligPerson "0..*" --  "1" Fagelement : rolle
Fagelement "0..*" --  "0..*" Fagelementemne
FagelementansvarligPerson "0..*" --  "0..1" Ansat
FagelementansvarligEnhed "0..*" --  "1" OrgEnhed
ÆkvivalerendeFaglighed "0..1" --  "1" Fagelement : har 
Fagelement "1" --  "0..*" PersonligtFagelement
Fagelement "1" --  "0..*" FagelementIFagelementgruppering
Fagelement "1" --  "0..*" OverlappendeFaglighed : med 
StudieforløbFagelement "0..*" --  "1" Fagelement
Fagelement "0..*" --  "0..1" VideregåendeUddannelse : defineret i
OverlappendeFaglighed "0..*" --  "1" Fagelement : har
FagelementansvarligPerson "0..*" --  "0..1" Medlemskab
Fagelement .right.>  SprogEnum
FagelementansvarligPerson .right.>  OrgPersonAnsvarsrolleEnum
FagelementansvarligEnhed .right.>  OrgEnhedAnsvarsrolleEnum
Fagelement .right.>  UddannelsesniveauEnum
Fagelement .right.>  FagelementTypeEnum
!endsub

!startsub 1_5_Gruppering_af_fagelement
class GrupperingAfFagelement {
  fagelementgrupperingsformål: ? [[1..1]]
  fagelementgrupperingsnavn: Text80 [[1..1]]
  fagelementgrupperingstype: Picklist [[0..1]]
  prioriteringVedTilmelding: Number.0 [[1..1]]
  <<BK>>
  fagelementgrupperingskode: AutoNum [[1..1]]
}

class FagelementIFagelementgruppering {
  rækkefølgePåBevis: ? [[0..1]]
  medtagesPåBevis: Checkbox [[1..1]]
  <<BK>>
  /fagelementgrupperingskode: IgnoreBK [[1..1]]
  /fagelementkode: IgnoreBK [[1..1]]
}

enum FagelementgrupperingstypeEnum <<enum>> {
  centralfag
  sidefag
  tilvalgsfag
  fagpakke
  propædeutik
}

GrupperingAfFagelement "0..*" --  "0..*" GrupperingAfFagelement
GrupperingAfFagelement "1" --  "0..*" PersonligFagelementgruppering
GrupperingAfFagelement "1" --  "0..*" StudieforløbFagelementgruppering
GrupperingAfFagelement "1" --  "0..*" FagelementIFagelementgruppering
Fagelement "1" --  "0..*" FagelementIFagelementgruppering
Studieforløb "0..1" --  "0..*" GrupperingAfFagelement : sidefag / tilvalg indlånt til
StudieforløbFagelement "0..*" --  "0..1" FagelementIFagelementgruppering
GrupperingAfFagelement .right.>  FagelementgrupperingstypeEnum
!endsub

!startsub 3_1_1_Udbudt_fagelement
class UdbudtFagelement {
  kapacitetMinimum: Number.0 [[0..1]]
  fagelementvarighed: Number.1 [[1..1]]
  kapacitetMaximum: Number.0 [[0..1]]
  anbefaledeFagligeForudsætninger: ? [[0..1]]
  anbefaletLitteratur: ? [[0..1]]
  feedbackform: PicklistMulti [[0..*]]
  arbejdsbelastning: ? [[1..1]]
  fagligeKrav: ? [[0..1]]
  afviklingssprog: Picklist [[1..1]]
  udvælgelseskriterier: ? [[0..1]]
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
}

class Skemagruppe {
  skemagruppeNavn: Text80 [[1..1]]
  skemagruppeBeskrivelse: TekstLong [[1..1]]
  <<BK>>
  skemagruppekode: AutoNum [[1..1]]
}

class UdbudtFagelementansvarligEnhed {
  ansvarsfordeling: ? [[1..1]]
  <<BK>>
  orgEnhedAnsvarsrolle: Picklist [[1..1]]
  /fagelementkode: IgnoreBK [[1..1]]
  /udbudsperiode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
  /orgEnhedId: IgnoreBK [[1..1]]
}

class UdbudtFagelementansvarligPerson {
  <<BK>>
  orgPersonAnsvarsrolle: IgnoreBK [[1..1]]
  /fagelementkode: IgnoreBK [[1..1]]
  /udbudsperiode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
  /personkode: IgnoreBK [[1..1]]
  /organisationskode: IgnoreBK [[1..1]]
}

enum FeedbackformEnum <<enum>> {
  lokalt defineret liste
}

UdbudtFagelement "0..*" --  "1" Udbudssted
UdbudtLæringsaktivitet "0..*" --  "1" UdbudtFagelement
Fagelement "1" --  "0..*" UdbudtFagelement : udbudt som
UdbudtFagelement "1" --  "0..*" TilmeldingTilUdbudtFagelement : tilmeldt til
UdbudtEnkeltfag "0..*" --  "1..*" UdbudtFagelement : udbudt som
UdbudtFagelementansvarligEnhed "0..*" --  "1" UdbudtFagelement
UdbudtFagelement "1" --  "1..*" UdbudtPrøve
UdbudtFagelement "0..*" --  "0..1" Skemagruppe
UdbudtFagelement "1" --  "0..*" UdbudtFagelementansvarligPerson
UdbudtFagelementansvarligEnhed "0..*" --  "1" OrgEnhed
UdbudtFagelementansvarligPerson "0..*" --  "0..1" Ansat
UdbudtFagelement "0..*" --  "1" Udbudsperiode
UdbudtFagelementansvarligPerson "0..*" --  "0..1" Medlemskab
UdbudtFagelement .right.>  FeedbackformEnum
UdbudtFagelement .right.>  SprogEnum
UdbudtFagelementansvarligPerson .right.>  OrgPersonAnsvarsrolleEnum
UdbudtFagelementansvarligEnhed .right.>  OrgEnhedAnsvarsrolleEnum
!endsub

!startsub 3_2_1_Tilmelding_til_udbudt_fagelement
class TilmeldingTilUdbudtFagelement {
  afgjortAf: ? [[1..1]]
  afgørelsesdato: Date [[1..1]]
  tilmeldingsstatus: Picklist [[1..1]]
  tilmeldingsprioritet: Number.0 [[0..1]]
  tilmeldingsafvisningsårsag: Picklist [[0..1]]
  anmodningstidspunkt: Number.1 [[1..1]]
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
}

class FrameldingFraUdbudtFagelement {
  frameldingsdato: Date [[1..1]]
  frameldtAf: ? [[1..1]]
  frameldingsårsag: Picklist [[1..1]]
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
  /udbudsperiode: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
}

class Aftalegrundlag {
  opgaveformulering: ? [[0..1]]
  afleveringsfrist: Date [[0..1]]
  vejledningsplan: ? [[0..1]]
  aftaleperiode: ? [[0..1]]
  praktiskeForhold: TekstLong [[0..1]]
  lønnetPraktik: ? [[1..1]]
  fortrolighed: ? [[1..1]]
  aftaletype: Picklist [[1..1]]
  <<BK>>
  aftalegrundlagsnummer: AutoNum [[1..1]]
}

class TilmeldingTilUdbudtLæringsaktivitet {
  tilmeldingsstatus: Picklist [[1..1]]
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
  /udbudsstedskode: IgnoreBK [[1..1]]
  /læringsaktivitetsnummer: IgnoreBK [[1..1]]
  /læringsaktivitetsstartdato: IgnoreBK [[1..1]]
}

enum TilmeldingsstatusEnum <<enum>> {
  afventerBehandling
  tilmeldt
  frameldt
  påVenteliste
  tilmeldtBetinget
  afvist
  påVentelisteBetinget
  annulleret
}

enum TilmeldingsafvisningsårsagEnum <<enum>> {
  tabtLodtrækning
  kravIkkeOpfyldt
  ingenLedigePladser
  betalingIkkeModtaget
}

enum FagelementFrameldingsårsagEnum <<enum>> {
  aflysning
  dispensation
  merit
  udvekslingsophold
  karantæne
}

enum AftaletypeEnum <<enum>> {
  lokalt defineret liste
}

Prøvetilmelding "1..*" --  "1" TilmeldingTilUdbudtFagelement
UdbudtFagelement "1" --  "0..*" TilmeldingTilUdbudtFagelement : tilmeldt til
TilmeldingTilUdbudtFagelement "1" --  "0..1" FrameldingFraUdbudtFagelement
TilmeldingTilUdbudtFagelement "1" --  "0..*" Holdønske : tilmelding kan indeholde holdønsker
TilmeldingTilUdbudtFagelement "0..*" --  "1" PersonligtFagelement
TilmeldingTilUdbudtFagelement "0..*" --  "0..1" Aftalegrundlag
Aftalegrundlag "0..*" --  "0..1" EksternKontakt : ekstern vejleder
Aftalegrundlag "0..*" --  "1" Ansat : akademisk vejleder
Aftalegrundlag "0..*" --  "0..*" Ansat : akademisk medvejleder
Aftalegrundlag "0..*" --  "0..1" Eksamensgruppe : ønsket eksamensgruppe
Aftalegrundlag "0..1" --  "0..1" EksterntOphold
Aftalegrundlag "0..*" --  "0..*" Organisation
TilmeldingTilUdbudtFagelement "1" --  "0..*" TilmeldingTilUdbudtLæringsaktivitet
TilmeldingTilUdbudtLæringsaktivitet "0..*" --  "1..*" Hold : holdplacering
TilmeldingTilUdbudtLæringsaktivitet "0..*" --  "1" UdbudtLæringsaktivitet
TilmeldingTilUdbudtFagelement .right.>  TilmeldingsstatusEnum
TilmeldingTilUdbudtFagelement .right.>  TilmeldingsafvisningsårsagEnum
TilmeldingTilUdbudtLæringsaktivitet .right.>  TilmeldingsstatusEnum
FrameldingFraUdbudtFagelement .right.>  FagelementFrameldingsårsagEnum
Aftalegrundlag .right.>  AftaletypeEnum
!endsub

!startsub 1_4_3_Laeringsaktivitet
abstract Læringsaktivitet {
}

class Undervisning {
  undervisningsform: Picklist [[1..1]]
}

class Praktikophold {
}

class Projektarbejde {
}

class FagligVejledning {
}

class ProjektorienteretOphold {
}

enum UndervisningsformEnum <<enum>> {
  Lokalt defineret værdiliste
}

Undervisning --|>  Læringsaktivitet
Praktikophold --|>  Læringsaktivitet
ProjektorienteretOphold --|>  Læringsaktivitet
Projektarbejde --|>  Læringsaktivitet
FagligVejledning --|>  Læringsaktivitet
Undervisning .right.>  UndervisningsformEnum
!endsub

!startsub 1_4_2_Proeve
class Prøve {
  eksamensforudsætninger: ? [[0..*]]
  prøvetype: Picklist [[1..1]]
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
}

class Prøvevariant {
  eksamenssprog: Picklist [[1..1]]
  prøvevariantNavn: Text80 [[1..1]]
  censurform: Picklist [[1..1]]
  bedømmelsesform: Picklist [[1..1]]
  <<BK>>
  prøvevariantkode: AutoNum [[1..1]]
  /fagelementkode: IgnoreBK [[1..1]]
  /prøveaktivitetsnr: IgnoreBK [[1..1]]
}

class Prøveemne {
  prøveemnenavn: Text80 [[1..1]]
  <<BK>>
  prøveemnekode: AutoNum [[1..1]]
}

class Prøvebegivenhed {
  prøvebegivenhedsvarighed: Number.1 [[1..1]]
  prøvebegivenhedsform: Picklist [[1..1]]
  erGruppeprøve: Checkbox [[1..1]]
  forberedelsestid: Number.1 [[0..1]]
  eksamensspørgsmålstype: Picklist [[0..1]]
  særligePraktiskeForhold: TekstLong [[0..1]]
  hjælpemidlerVedPrøvebegivenhed: PicklistMulti [[0..*]]
  censornorm: ? [[1..1]]
  deltagelseskrav: ? [[0..1]]
  omfangskrav: Number.1 [[0..1]]
  afviklingsform: Picklist [[1..1]]
  bedømmelsesvægt: Percent [[0..1]]
  <<BK>>
  /prøvekode: IgnoreBK [[1..1]]
  /prøvevariantkode: IgnoreBK [[1..1]]
  prøvebegivenhedskode: AutoNum [[1..1]]
  /prøveaktivitetsnr: IgnoreBK [[1..1]]
}

class Prøveaktivitet {
  delprøverækkefølge: ? [[0..1]]
  delprøvekaraktervægt: Percent [[0..1]]
  prøveaktivitetsNavn: Text80 [[0..1]]
  prøveaktivitetstype: Picklist [[1..1]]
  eksamenspensum: ? [[0..1]]
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
  prøveaktivitetsnr: ? [[1..1]]
}

enum BedømmelsesformEnum <<enum>> {
  7-trinskala
  bestået/ikke-bestået
}

enum CensurformEnum <<enum>> {
  eksternCensur
  internBedømmelse
  udenCensur
}

enum PrøvebegivenhedsformEnum <<enum>> {
  skriftligStedprøve
  mundtligPrøve
  undervisningsdeltagelse
  praktiskprøve
  hjemmeopgave
}

enum PrøveTypeEnum <<enum>> {
  Fageksamen
  LøbendePrøve
  AfsluttendeEksamen
}

enum EksamensspørgsmålstypeEnum <<enum>> {
  bundetEksamensspørgsmål
  fritEksamensspørgsmål
}

enum AfviklingsformEnum <<enum>> {
  fremmøde
  virtuelPrøvebegivenhed
}

enum PrøveaktivitetstypeEnum <<enum>> {
  delprøve
  prøve
}

enum HjælpemidlerVedPrøvebegivenhedEnum <<enum>> {
  Lokalt defineret værdiliste
}

Prøve "1" --  "0..*" UdbudtPrøve : udbudt som
Prøve "1" --  "1" Fagelement
Prøvetilmelding "0..*" --  "0..1" Prøveemne : valgt emne
UdbudtPrøve "0..*" --  "0..*" Prøveemne : mulige emner
Prøvebegivenhed "1..*" --  "1" Prøvevariant
UdbudtPrøvevariant "0..*" --  "1" Prøvevariant
Prøve "0..*" --  "0..*" Prøveemne : mulige emner
Prøve "1" --  "1..*" Prøveaktivitet
Prøveaktivitet "1" --  "1..*" Prøvevariant
UdbudtPrøveaktivitet "0..*" --  "1" Prøveaktivitet
Prøvebegivenhed "1" --  "0..*" UdbudtPrøvebegivenhed
Prøvevariant .right.>  SprogEnum
Prøvebegivenhed .right.>  PrøvebegivenhedsformEnum
Prøve .right.>  PrøveTypeEnum
Prøvebegivenhed .right.>  EksamensspørgsmålstypeEnum
Prøvebegivenhed .right.>  AfviklingsformEnum
Prøveaktivitet .right.>  PrøveaktivitetstypeEnum
Prøvevariant .right.>  BedømmelsesformEnum
Prøvevariant .right.>  CensurformEnum
Prøvebegivenhed .right.>  HjælpemidlerVedPrøvebegivenhedEnum
!endsub

!startsub 3_1_2_Udbudt_proeve
class UdbudtPrøvevariant {
  eksamenssprog: Picklist [[1..1]]
  censurform: Picklist [[0..1]]
  bedømmelsesform: Picklist [[0..1]]
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
  /prøveaktivitetskode: IgnoreBK [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
  /prøveperiodestartdato: IgnoreBK [[1..1]]
  /prøvevariantkode: IgnoreBK [[1..1]]
}

class UdbudtPrøvebegivenhed {
  prøvebegivenhedsvarighed: Number.1 [[1..1]]
  erGruppeprøve: Checkbox [[1..1]]
  omfangskrav: Number.1 [[1..1]]
  forberedelsestid: Number.1 [[1..1]]
  særligePraktiskeForhold: TekstLong [[1..1]]
  anonymEksamensbesvarelse: ? [[0..1]]
  eksamensgruppeMaxStr: ? [[0..1]]
  gruppedannelsesprincip: Picklist [[0..1]]
  hjælpemidlerVedPrøvebegivenhed: PicklistMulti [[0..*]]
  afleveringsfrist: Date [[0..1]]
  afviklingsform: Picklist [[1..1]]
  eksamensgruppeMinStr: ? [[0..1]]
  eksamensopgave: ? [[0..1]]
  <<BK>>
  /prøveaktivitetskode: IgnoreBK [[1..1]]
  /fagelementkode: IgnoreBK [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
  /prøvebegivenhedskode: IgnoreBK [[1..1]]
  /prøvevariantkode: IgnoreBK [[1..1]]
  /prøveperiodestartdato: IgnoreBK [[1..1]]
}

class Sameksamination {
  sameksaminationsnavn: Text80 [[1..1]]
}

class UdbudtPrøveaktivitet {
  eksamenspensum: ? [[0..1]]
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
  /prøveaktivitetskode: IgnoreBK [[1..1]]
  /prøveperiodestartdato: IgnoreBK [[1..1]]
}

class UdbudtPrøve {
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
  /prøveperiodestartdato: IgnoreBK [[1..1]]
}

class TidOgSted {
  tidsrum: Number.1 [[1..1]]
  sted: ? [[1..1]]
}

enum GruppedannelsesprincipEnum <<enum>> {
  dannesAfStuderende
  dannesAfAdministration
}

Prøve "1" --  "0..*" UdbudtPrøve : udbudt som
UdbudtPrøve "1" --  "0..*" Prøvetilmelding
UdbudtPrøve "0..*" --  "0..*" Prøveemne : mulige emner
UdbudtPrøvevariant "1" --  "1..*" UdbudtPrøvebegivenhed
UdbudtPrøvevariant "0..*" --  "1" Prøvevariant
UdbudtFagelement "1" --  "1..*" UdbudtPrøve
Sameksamination "0..1" --  "0..*" UdbudtPrøvebegivenhed : del af
UdbudtPrøve "0..*" --  "1" Prøveperiode
UdbudtPrøveaktivitet "1" --  "1..*" UdbudtPrøvevariant
UdbudtPrøve "1" --  "1..*" UdbudtPrøveaktivitet
UdbudtPrøveaktivitet "0..*" --  "1" Prøveaktivitet
Prøveaktivitetstilmelding "0..*" --  "1" UdbudtPrøvevariant : prøvevarianttilmelding
Prøveaktivitetstilmelding "0..*" --  "1" UdbudtPrøveaktivitet
Prøvebegivenhed "1" --  "0..*" UdbudtPrøvebegivenhed
PersonligPrøvebegivenhed "0..*" --  "1" UdbudtPrøvebegivenhed
UdbudtPrøvebegivenhed "0..*" --  "0..*" TidOgSted
PersonligPrøvebegivenhed "0..*" --  "0..1" TidOgSted
UdbudtPrøvebegivenhed .right.>  GruppedannelsesprincipEnum
UdbudtPrøvevariant .right.>  SprogEnum
UdbudtPrøvebegivenhed .right.>  AfviklingsformEnum
UdbudtPrøvebegivenhed .right.>  HjælpemidlerVedPrøvebegivenhedEnum
UdbudtPrøvevariant .right.>  CensurformEnum
UdbudtPrøvevariant .right.>  BedømmelsesformEnum
!endsub

!startsub 3_1_3_Udbudt_laeringsaktivitet
abstract UdbudtLæringsaktivitet {
}

class UdbudtUndervisning {
}

class UdbudtFagligVejledning {
}

class UdbudtPraktikophold {
}

class UdbudtProjektarbejde {
}

class UdbudtProjektorienteretOphold {
}

class Samlæsning {
  samlæsningsnavn: Text80 [[1..1]]
}

class UdbudtLæringsaktivitetsansvarligPerson {
  orgPersonAnsvarsrolle: Picklist [[1..1]]
}

UdbudtUndervisning "0..*" --  "0..1" Samlæsning
UdbudtLæringsaktivitetsansvarligPerson "0..*" --  "1" UdbudtLæringsaktivitet
UdbudtLæringsaktivitetsansvarligPerson "0..*" --  "0..1" Ansat
UdbudtLæringsaktivitetsansvarligPerson "0..*" --  "0..1" Medlemskab
UdbudtUndervisning --|>  UdbudtLæringsaktivitet
UdbudtFagligVejledning --|>  UdbudtLæringsaktivitet
UdbudtPraktikophold --|>  UdbudtLæringsaktivitet
UdbudtProjektarbejde --|>  UdbudtLæringsaktivitet
UdbudtProjektorienteretOphold --|>  UdbudtLæringsaktivitet
UdbudtLæringsaktivitetsansvarligPerson .right.>  OrgPersonAnsvarsrolleEnum
!endsub

!startsub 2_3_Studerende
class Studerende {
  studiemail: ? [[1..1]]
  branche: ? [[0..1]]
  /studieforholdsstadie: Calculated [[1..1]]
  <<BK>>
  studienummer: AutoNum [[1..1]]
}

class Ansat {
}

class Ansøger {
}

class EuropeanStudentIdentifier {
}

enum StudieforholdsstadieEnum <<enum>> {
  AktivStuderende
  KommendeStuderende
  Dimittend
  MidlertidigtBortvist
  TidligereStuderende
  Orlov
  PermanentBortvist
}

Studerende "1" --  "1..*" Indskrivning
Prøvetilmelding "0..*" --  "0..1" Ansat : valgt vejleder
PrøveforsøgMedBedømmelse "0..*" --  "1..*" Ansat : eksaminator
PrøveforsøgMedBedømmelse "0..*" --  "0..*" Ansat : medbedømmer
FagelementansvarligPerson "0..*" --  "0..1" Ansat
UdbudtFagelementansvarligPerson "0..*" --  "0..1" Ansat
Ansøger "1" --  "1..*" AnsøgningOmOptagelse : ansøger
Studerende "0..1" --  "1" OrgPerson : er
Aftalegrundlag "0..*" --  "1" Ansat : akademisk vejleder
Aftalegrundlag "0..*" --  "0..*" Ansat : akademisk medvejleder
OrgPerson "1" --  "0..1" Ansat : er
UdbudtLæringsaktivitetsansvarligPerson "0..*" --  "0..1" Ansat
UdbudtVideregåendeUddannelseOgEnkeltfag "0..*" --  "0..*" Ansat : faglig bedømmer for
Ansøger "0..1" --  "1" OrgPerson : er
PermanentPrøvedispensation "0..*" --  "1" Studerende
EuropeanStudentIdentifier "0..1" --  "1" Studerende
Studerende .right.>  StudieforholdsstadieEnum
!endsub

!startsub 3_2_2_Proevetilmelding
class Prøvetilmelding {
  tilmeldingstidspunkt: Number.1 [[1..1]]
  tilmeldtAf: ? [[1..1]]
  /prøveforsøgnr: Calculated [[1..1]]
  eksamensforudsætningOpfyldt: ? [[1..1]]
  /erFrameldtFraUdbudtprøve: Calculated [[1..1]]
  <<BK>>
  /udbudsperiodekode: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /fagelementkode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
  /prøveperiodestartdato: IgnoreBK [[1..1]]
}

class FrameldingFraUdbudtPrøveaktivitet {
  frameldingsdato: Date [[1..1]]
  frameldtAf: ? [[1..1]]
  frameldingsårsag: Picklist [[1..1]]
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
  /prøvevariantkode: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
  /prøveforsøgnr: IgnoreBK [[1..1]]
  /udbudsperiodeStartdato: IgnoreBK [[1..1]]
}

class Eksamensgruppe {
  eksamensgruppeNavn: Text80 [[1..1]]
  <<BK>>
  eksamensgruppekode: AutoNum [[1..1]]
}

class Prøveaktivitetstilmelding {
  foreløbigOpgavetitel: Text80 [[0..1]]
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /prøveforsøgnr: IgnoreBK [[1..1]]
  /prøveperiodestartdato: IgnoreBK [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
  /prøveaktivitetskode: IgnoreBK [[1..1]]
}

class PersonligPrøvebegivenhed {
  særligeprøvevilkår: Picklist [[1..1]]
  personligPrøvebegivenhedsdato: Date [[1..1]]
  eksamensbesvarelse: ? [[0..1]]
  <<BK>>
  /prøveperiodestartdato: IgnoreBK [[1..1]]
  /fagelementkode: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /prøveforsøgnr: IgnoreBK [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
  /prøveaktivitetskode: IgnoreBK [[1..1]]
}

enum særligeprøvevilkårEnum <<enum>> {
  Lokalt defineret værdiliste
}

enum PrøveFrameldingsÅrsagEnum <<enum>> {
  sygdom
  aflyst
  dispensation
}

UdbudtPrøve "1" --  "0..*" Prøvetilmelding
Prøvetilmelding "1..*" --  "1" TilmeldingTilUdbudtFagelement
Prøveaktivitetstilmelding "1" --  "0..1" FrameldingFraUdbudtPrøveaktivitet
Prøvetilmelding "0..*" --  "0..1" Prøveemne : valgt emne
Prøvetilmelding "0..*" --  "0..1" Ansat : valgt vejleder
Prøvetilmelding "1..*" --  "0..1" Eksamensgruppe : valgt eksamensgruppe
Aftalegrundlag "0..*" --  "0..1" Eksamensgruppe : ønsket eksamensgruppe
Prøvetilmelding "1" --  "0..*" Prøvedispensation
Prøveaktivitetstilmelding "0..*" --  "1" UdbudtPrøvevariant : prøvevarianttilmelding
Prøveaktivitetstilmelding "0..*" --  "1" UdbudtPrøveaktivitet
Prøveaktivitetsforsøg "0..1" --  "1" Prøveaktivitetstilmelding
Prøvetilmelding "1" --  "1..*" Prøveaktivitetstilmelding
PersonligPrøveaktivitet "1" --  "1..*" Prøveaktivitetstilmelding
Prøveaktivitetstilmelding "1" --  "1..*" PersonligPrøvebegivenhed
PrøveforsøgUdenBedømmelse "0..1" --  "1" PersonligPrøvebegivenhed
PersonligPrøvebegivenhed "0..*" --  "1" UdbudtPrøvebegivenhed
PersonligPrøvebegivenhed "0..*" --  "0..1" TidOgSted
PersonligPrøvebegivenhed .right.>  særligeprøvevilkårEnum
FrameldingFraUdbudtPrøveaktivitet .right.>  PrøveFrameldingsÅrsagEnum
!endsub

!startsub 9_0_Universitetets_struktur
class Udbudssted {
  udbudsstedNavn: Text80 [[1..1]]
  <<BK>>
  udbudsstedkode: AutoNum [[1..1]]
}

class OrgEnhed {
  Enhedsnavn: Text80 [[1..1]]
  /organisationskode: Calculated [[1..1]]
  P-nummer: Number.0 [[0..1]]
  <<BK>>
  orgEnhedId: AutoNum [[1..1]]
}

class OrgPerson {
  navnIOrganisation: Text80 [[0..1]]
  kommunikationssprog: Picklist [[1..1]]
  nationalitet: Picklist [[1..1]]
  orgEmail: ? [[1..1]]
  orgTelefonnr: ? [[1..1]]
  privatEmail: ? [[1..1]]
  privattelefonnr: ? [[1..1]]
  identitetsvalidering: ? [[1..1]]
  <<BK>>
  orgPersonNavn: Text80 [[1..1]]
  /organisationskode: IgnoreBK [[1..1]]
}

class Uddannelsesinstitution {
  uddannelsesinstitutionLand: Picklist [[1..1]]
  uddannelsesinstitutionNavn: Text80 [[1..1]]
  <<BK>>
  /organisationskode: IgnoreBK [[1..1]]
}

class Person {
  addresseringsnavn: Text80 [[1..1]]
  efternavn: Text80 [[1..1]]
  fornavne: Text80 [[1..1]]
  mellemnavne: Text80 [[1..1]]
  id: ? [[1..1]]
  navneOgAdressebeskyttelse: Text80 [[1..1]]
  fødselsdato: Date [[1..1]]
  <<BK>>
  personnummer: AutoNum [[1..1]]
}

class DanskAdresse {
  husnummer: Number.0 [[1..1]]
  dør: ? [[1..1]]
  etage: ? [[1..1]]
  vejnavn: Text80 [[1..1]]
  postnummer: Number.0 [[1..1]]
  <<BK>>
  darId: AutoNum [[1..1]]
}

abstract Adresse {
}

class GodkendtUdbudssted {
  godkendtUdbudsstedNavn: Text80 [[1..1]]
  <<BK>>
  godkendtUdbudsstedKode: AutoNum [[1..1]]
}

class Universitet {
}

class Organisation {
  cvr: ? [[1..1]]
  organisationNavn: Text80 [[1..1]]
  <<BK>>
  organisationskode: AutoNum [[1..1]]
}

class Statsborgerskab {
  cprLandenavn: Picklist [[1..1]]
  cprLandekode: Text80 [[1..1]]
}

class UdenlandskAdresse {
  adresse: ? [[1..1]]
  land: Picklist [[1..1]]
}

class PersonUdenCpr {
  fødselsdato: Date [[1..1]]
  navn: Text80 [[1..1]]
  <<BK>>
  konstrueretPersonnummer: AutoNum [[1..1]]
}

abstract GeneriskPerson {
}

class CprAdresse {
  bygningsnummer: Number.0 [[1..1]]
  bynavn: Text80 [[1..1]]
  cprKommunekode: Text80 [[1..1]]
  cprKommunenavn: Text80 [[1..1]]
  cprVejkode: Text80 [[1..1]]
  cprAdreses: ? [[1..1]]
  etage: ? [[1..1]]
  husnummer: Number.0 [[1..1]]
  postdistrikt: ? [[1..1]]
  postnummer: Number.0 [[1..1]]
  sideDoer: ? [[1..1]]
  vejadresseringsnavn: Text80 [[1..1]]
  darAdresse: ? [[1..1]]
}

class Medlemskab {
  medlemskabRolle: Checkbox [[1..1]]
  <<BK>>
  medlemskabkode: AutoNum [[1..1]]
}

enum SprogEnum <<enum>> {
  jf. iso 639
}

enum OrgEnhedAnsvarsrolleEnum <<enum>> {
  økonomiskAnsvarlig
  uddannelsesAnsvarlig
  producerendeAnsvarlig
  alumneAnsvarlig
}

enum GodkendelsesstatusEnum <<enum>> {
  godkendt
  afvist
  delvistGodkendt
  betingetGodkendt
  henlagt
  annulleret
  imødekommet
  ikkeImødekommet
}

enum LandEnum <<enum>> {
  jf. ISO 3166-1
}

enum OrgPersonAnsvarsrolleEnum <<enum>> {
  underviser
  akademiskVejleder
  kursusansvarlig
  laboratorieansvarlig
  studievejleder
  bevisunderskriver
}

UdbudtFagelement "0..*" --  "1" Udbudssted
UddannelsesansvarligEnhed "0..*" --  "1" OrgEnhed : ansvarlig enhed
UdbudtVideregåendeUddannelseOgEnkeltfag "0..*" --  "1" Udbudssted : primære udbudssted
AdgangsgivendeEksamen "0..*" --  "1" Uddannelsesinstitution : adgangsgivende inst.
UdbudtLæringsaktivitet "0..*" --  "1" Udbudssted
VideregåendeUddannelse "0..*" --  "1..*" GodkendtUdbudssted : godkendt til udbud ved
Uddannelsesinstitution "1" --  "0..*" Udbudssted
EksterntFagelement "0..*" --  "1" Uddannelsesinstitution : fra
PrøveforsøgMedBedømmelse "0..*" --  "0..*" OrgPerson : censor
GeneriskPerson "1" --  "0..*" OrgPerson : repræsenterer
FagelementansvarligEnhed "0..*" --  "1" OrgEnhed
UdbudtFagelementansvarligEnhed "0..*" --  "1" OrgEnhed
Uddannelsesinstitution "1" --  "0..*" Udvekslingsaftale : partner institution
OrgPerson "1" --  "0..*" Organisation : tilhører
Studerende "0..1" --  "1" OrgPerson : er
Person "1" --  "1..2" Statsborgerskab
EksternKontakt "0..*" --  "1" Organisation
Virksomhedsbetaling "0..*" --  "1" Organisation : debitor
Indskrivning "0..*" --  "0..1" Organisation : relevant arbejdsplads
EksterntOphold "0..*" --  "0..1" Uddannelsesinstitution
Uddannelsesinstitution "1" --  "0..*" Udvekslingsansøgning : fra
OrgPerson "1" --  "0..1" Ansat : er
OrgEnhed "0..*" --  "1" Organisation : tilhører
Uddannelse "0..*" --  "0..*" Uddannelsesinstitution : samarbejdspartner
VideregåendeUddannelse "0..*" --  "1" Universitet : udbyder
Aftalegrundlag "0..*" --  "0..*" Organisation
Udbudssted "0..*" --  "1" Adresse
OrgEnhed "0..1" --  "0..*" OrgEnhed : overordnet
OrgEnhed "0..*" --  "0..*" Adresse : fysiskAdresse
OrgPerson "0..*" --  "0..*" UdbudtVideregåendeUddannelseOgEnkeltfag : ekstern faglig bedømmer
HoldBegivenhedPerson "0..*" --  "1" OrgPerson
EksterntOphold "0..1" --  "0..1" Organisation : hos
Ansøger "0..1" --  "1" OrgPerson : er
Udbudssted "0..*" --  "1" GodkendtUdbudssted : hører under
Uddannelsesinstitution "1" --  "1..*" GodkendtUdbudssted
Universitet "1" --  "0..*" OrgPerson : tilhører
Medlemskab "0..*" --  "0..1" OrgPerson
Medlemskab "0..*" --  "1..*" OrgEnhed
UddannelsesansvarligPerson "0..*" --  "0..1" OrgPerson
UddannelsesansvarligPerson "0..*" --  "0..1" Medlemskab
Udvekslingsansøgning "0..*" --  "0..1" OrgPerson : ekstern kontakt
UdbudtLæringsaktivitetsansvarligPerson "0..*" --  "0..1" Medlemskab
UdbudtFagelementansvarligPerson "0..*" --  "0..1" Medlemskab
FagelementansvarligPerson "0..*" --  "0..1" Medlemskab
Uddannelsesinstitution "1" --  "0..*" RegisterRegistrering
RegisterRegistrering "1" --  "0..1" GodkendtUdbudssted
DanskInstitutionsRegisterRegistrering "0..*" --  "0..1" DanskAdresse
DanskAdresse --|>  Adresse
Universitet --|>  Uddannelsesinstitution
Uddannelsesinstitution --|>  Organisation
UdenlandskAdresse --|>  Adresse
Person --|>  GeneriskPerson
PersonUdenCpr --|>  GeneriskPerson
CprAdresse --|>  Adresse
Statsborgerskab .right.>  LandEnum
OrgPerson .right.>  LandEnum
UdenlandskAdresse .right.>  LandEnum
Uddannelsesinstitution .right.>  LandEnum
OrgPerson .right.>  SprogEnum
!endsub

!startsub 1_7_1_Udbudt_videregaaende_uddannelse
class UdbudtVideregåendeUddannelse {
  tilrettelæggelsesform: Picklist [[1..1]]
  kræverValgAfStudieforløb: Checkbox [[1..1]]
  optagelseskode: Text80 [[1..1]]
  <<BK>>
  /optagelsesperiodekode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
  /uddannelsesId: IgnoreBK [[1..1]]
}

abstract UdbudtVideregåendeUddannelseOgEnkeltfag {
}

class Optagelsesperiode {
  ansøgningsstartdato: Date [[1..1]]
  optagelsesperiodenavn: Text80 [[1..1]]
  uddannelsestype: Picklist [[1..1]]
  <<BK>>
  optagelsesperiodekode: AutoNum [[1..1]]
}

class Udbudshjemmel {
  udbudsform: Picklist [[1..1]]
  uddannelsessystem: Picklist [[1..1]]
  <<BK>>
  udbudshjemmelkode: AutoNum [[1..1]]
}

class Bogføringsoplysninger {
  beløb: Currency [[1..1]]
  bogføringsandel: Percent [[1..1]]
  <<BK>>
  bogføringskonto: ? [[1..1]]
  /betalingsmålgruppe: IgnoreBK [[0..1]]
  /prisreference: IgnoreBK [[1..1]]
  /periodekode: IgnoreBK [[0..1]]
}

class Pris {
  pris: Currency [[1..1]]
  prisbeskrivelse: Currency [[1..1]]
  <<BK>>
  betalingsmålgruppe: ? [[0..1]]
  prisreference: IgnoreBK [[1..1]]
  periodekode: IgnoreBK [[0..1]]
}

class Ansøgningsfrist {
  ansøgningsfrist: Date [[1..1]]
  svarfrist: Date [[1..1]]
}

class Studiestart {
  studiestartsdato: Date [[1..1]]
}

class UdbudtStudieforløb {
}

enum UdbudsformEnum <<enum>> {
  deltidsuddannelse
  heltidPåDeltid
  heltidsuddannelse
}

UdbudtVideregåendeUddannelse "0..*" --  "1" VideregåendeUddannelse : udbud af
UdbudtVideregåendeUddannelse "0..*" --  "1" Studieordning : udbudt studieordning
IndskrivningTilVideregåendeUddannelse "0..*" --  "1" UdbudtVideregåendeUddannelse : indskrevet på
PrioriteretUddannelse "0..*" --  "1" UdbudtVideregåendeUddannelse
Uddannelsesansøgning "0..*" --  "0..1" UdbudtVideregåendeUddannelse : placeret på venteliste til
UdbudtVideregåendeUddannelse "1" --  "0..*" TilbudOmStudiepladsPåUddannelse
Optagelsesperiode "1" --  "0..*" UdbudtVideregåendeUddannelseOgEnkeltfag
UdbudtVideregåendeUddannelse "0..*" --  "1" Udbudshjemmel
UdbudtVideregåendeUddannelseOgEnkeltfag "0..*" --  "0..*" Pris : har ansøgningsgebyr
Pris "1" --  "1..*" Bogføringsoplysninger
UdbudtVideregåendeUddannelseOgEnkeltfag "0..*" --  "0..*" Pris : har pris for deltagelse
UdbudtVideregåendeUddannelseOgEnkeltfag "0..*" --  "0..*" Pris : har optagelsesgebyr
Optagelsesperiode "1" --  "1..*" Ansøgningsfrist
Optagelsesperiode "0..*" --  "1..*" Studiestart
TilbudOmStudiepladsPåUddannelse "0..*" --  "1" Studiestart
Studiepladskapacitet "0..1" --  "0..1" UdbudtStudieforløb : kan have begrænset kapacitet
Studieforløb "1" --  "0..*" UdbudtStudieforløb
UdbudtVideregåendeUddannelse "1" --  "1..*" UdbudtStudieforløb
UdbudtVideregåendeUddannelse --|>  UdbudtVideregåendeUddannelseOgEnkeltfag
UdbudtVideregåendeUddannelse .right.>  TilrettelæggelsesformEnum
Udbudshjemmel .right.>  UdbudsformEnum
Udbudshjemmel .right.>  UddannelsessystemEnum
Optagelsesperiode .right.>  UddannelsestypeEnum
!endsub

!startsub 2_1_3_Indskrivning
abstract Adgangsgrundlag {
}

abstract Indskrivning {
}

class IndskrivningTilEnkeltfag {
  enkeltfagsindskrivningstype: Picklist [[1..1]]
  <<BK>>
  /indskrivningsnummer: IgnoreBK [[1..1]]
}

class IndskrivningTilVideregåendeUddannelse {
  dispensationsindskrivning: ? [[1..1]]
  uddannelsesindskrivningstype: Picklist [[1..1]]
  <<BK>>
  /indskrivningsnummer: IgnoreBK [[1..1]]
}

class AdgangsgivendeErhvervserfaring {
  adgangsgivendeErhvervserfaringVarighed: Number.1 [[1..1]]
  branche: ? [[1..1]]
  erhvervserfaringNavn: Text80 [[1..1]]
}

enum IndskrivningsstatusEnum <<enum>> {
  kommende
  aktiv
  pauseBarsel
  pauseOrlov
  udmeldtAfbrudt
  udmeldtBestået
  udmeldtBortvist
  pauseBortvist
  nedsatStudieaktivitet
}

enum EnkeltfagsindskrivningstypeEnum <<enum>> {
  AdgangskursusIndskrivning
  DeltidsEnkeltfagsIndskrivning
  FagspecifikkeKurserIndskrivning
  KorteKurserIndskrivning
  MeritIndskrivning
  MeritSidefagsIndskrivning
  MeritTilvalgsIndskrivning
  SærskiltModulIndskrivning
  TompladsIndskrivning
  UdvekslingsIndskrivning
  SuppleringsIndskrivning
}

enum UddannelsesindskrivningstypeEnum <<enum>> {
  AdministrativGenindskrivning
  AdministrativOverflytning
  AdministrativStudieskift
  Genoptagelse
  Standardindskrivning
}

UdbudtEnkeltfag "1..*" --  "0..*" IndskrivningTilEnkeltfag : indskrevet på
IndskrivningTilVideregåendeUddannelse "0..*" --  "1" UdbudtVideregåendeUddannelse : indskrevet på
IndskrivningTilVideregåendeUddannelse "0..*" --  "1" Studieordning : indskrevet til
IndskrivningTilVideregåendeUddannelse "0..*" --  "0..1" Studieforløb : valgt forløb
IndskrivningTilVideregåendeUddannelse "1" --  "1" PersonligtStudieforløb
Eksamensbevis "0..1" --  "1" IndskrivningTilVideregåendeUddannelse
Enkeltfagsbevis "0..1" --  "1" IndskrivningTilEnkeltfag
IndskrivningTilVideregåendeUddannelse "1" --  "0..*" AnsøgningOmForhåndsgodkendelse : ansøger
Meritansøgning "0..*" --  "1" IndskrivningTilVideregåendeUddannelse : ansøger
TilbudOmStudiepladsPåUddannelse "1" --  "0..1" IndskrivningTilVideregåendeUddannelse : accept medfører
TilbudOmStudiepladsPåEnkeltfag "0..*" --  "0..1" IndskrivningTilEnkeltfag : accept medfører
IndskrivningTilEnkeltfag "1" --  "1" PersonligtEnkeltfagsforløb
IndskrivningTilVideregåendeUddannelse "1" --  "0..*" EksterntOpholdsansøgning
AdgangsgivendeErhvervserfaring "0..*" --  "1" Adgangsgrundlag
IndskrivningTilEnkeltfag "0..*" --  "0..1" Udvekslingsaftale : under 
IndskrivningTilVideregåendeUddannelse --|>  Indskrivning
IndskrivningTilEnkeltfag --|>  Indskrivning
IndskrivningTilEnkeltfag .right.>  EnkeltfagsindskrivningstypeEnum
IndskrivningTilVideregåendeUddannelse .right.>  UddannelsesindskrivningstypeEnum
!endsub

!startsub 1_7_2_Udbudt_enkeltfag
class UdbudtEnkeltfagSomTomplads {
}

class UdbudtEnkeltfagTilMeritstuderende {
}

abstract UdbudtEnkeltfag {
}

class UdbudtEnkeltfagTilUdvekslingsstuderende {
}

class UdbudtEnkeltfagFraDeltidsuddannelse {
}

class UdbudtEnkeltfagSomAdgangskursus {
}

class UdbudtEnkeltfagSomFagspecifiktKursus {
}

class UdbudtEnkeltfagSomKortKursus {
}

class UdbudtEnkeltfagSomSærskiltModul {
}

class UdbudtEnkeltfagSomSupplering {
}

UdbudtEnkeltfagSomTomplads --|>  UdbudtEnkeltfag
UdbudtEnkeltfagTilMeritstuderende --|>  UdbudtEnkeltfag
UdbudtEnkeltfagTilUdvekslingsstuderende --|>  UdbudtEnkeltfag
UdbudtEnkeltfagFraDeltidsuddannelse --|>  UdbudtEnkeltfag
UdbudtEnkeltfagSomAdgangskursus --|>  UdbudtEnkeltfag
UdbudtEnkeltfagSomFagspecifiktKursus --|>  UdbudtEnkeltfag
UdbudtEnkeltfagSomKortKursus --|>  UdbudtEnkeltfag
UdbudtEnkeltfagSomSærskiltModul --|>  UdbudtEnkeltfag
UdbudtEnkeltfagSomSupplering --|>  UdbudtEnkeltfag
!endsub

!startsub 2_1_5_Udmeldelse
abstract Udmeldelse {
}

class Selvudmeldelse {
  udmeldelsesårsag: Picklist [[1..1]]
}

class GennemførtUdbudtVideregåendeUddannelseOgEnkeltfag {
  /gennemførselstid: Calculated [[1..1]]
}

class AfbrudtIndskrivning {
  afbrydelsesårsag: Picklist [[1..1]]
  afbrydelsesbegrundelse: ? [[1..1]]
}

enum AfbrydelsesårsagEnum <<enum>> {
  død
  permanentbortvist
  studieaktivitetskravFørsteårsprøve
  opbrugtprøveforsøg
  betingelseIkkeOpfyldt
  ikkeBetalt
  studieaktivitetskravMaksimalstudietid
  studieaktivitetskravStudiestartsprøve
  studieaktivitetskravLøbendestudieaktivitet
  ikkeMødtOp
  studieskift
}

enum UdmeldelsesårsagEnum <<enum>> {
  Lokalt defineret værdiliste
}

Selvudmeldelse --|>  Udmeldelse
GennemførtUdbudtVideregåendeUddannelseOgEnkeltfag --|>  Udmeldelse
AfbrudtIndskrivning --|>  Udmeldelse
AfbrudtIndskrivning .right.>  AfbrydelsesårsagEnum
Selvudmeldelse .right.>  UdmeldelsesårsagEnum
!endsub

!startsub 3_3_Hold
class Holdbegivenhed {
  <<BK>>
  tidsrum: AutoNum [[1..1]]
  sted: ? [[1..1]]
  /holdkode: IgnoreBK [[1..1]]
}

class Holdønske {
  holdprioritet: Number.0 [[1..1]]
  <<BK>>
  /holdkode: IgnoreBK [[1..1]]
  /fagelementkode: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
}

class Hold {
  holdstørrelseMaximum: ? [[0..1]]
  holdstørrelseMinimum: Number.0 [[0..1]]
  holdnavn: Text80 [[1..1]]
  <<BK>>
  holdkode: AutoNum [[1..1]]
}

class HoldBegivenhedPerson {
  orgPersonAnsvarsrolle: ? [[1..1]]
}

TilmeldingTilUdbudtFagelement "1" --  "0..*" Holdønske : tilmelding kan indeholde holdønsker
Holdønske "0..*" --  "1" Hold
UdbudtLæringsaktivitet "1..*" --  "1..*" Hold
Holdbegivenhed "1..*" --  "1" Hold
TilmeldingTilUdbudtLæringsaktivitet "0..*" --  "1..*" Hold : holdplacering
Holdbegivenhed "1" --  "0..*" HoldBegivenhedPerson
HoldBegivenhedPerson "0..*" --  "1" OrgPerson
!endsub

!startsub 2_1_4_Uddannelsespause
abstract Uddannelsespause {
}

class Uddannelsesbarsel {
  uddannelsesbarselStartdato: Date [[1..1]]
  uddannelsesbarselSlutdato: Date [[1..1]]
}

class Uddannelsesorlov {
  orlovsårsag: Picklist [[1..1]]
}

class MidlertidigBortvisning {
  bortvisningsårsag: Picklist [[1..1]]
}

class AnsøgningOmUddannelsespause {
  godkendelsesstatus: Picklist [[1..1]]
  <<BK>>
  ansøgningsnummer: IgnoreBK [[1..1]]
}

enum OrlovsårsagEnum <<enum>> {
  egenSygdom
  barselAdoption
  værnepligt
  øvrigOrlov
  plejeorlov
  udsendelseVedForsvaret
  andreOffentligeHverv
  barsel
}

enum BortvisningsårsagEnum <<enum>> {
  Lokalt defineret værdiliste
}

Indskrivning "1" --  "0..*" AnsøgningOmUddannelsespause
AnsøgningOmUddannelsespause "1" --  "0..1" Uddannelsesorlov
Indskrivning "1" --  "0..*" Uddannelsesbarsel
Uddannelsesorlov --|>  Uddannelsespause
MidlertidigBortvisning --|>  Uddannelsespause
MidlertidigBortvisning .right.>  BortvisningsårsagEnum
Uddannelsesorlov .right.>  OrlovsårsagEnum
AnsøgningOmUddannelsespause .right.>  GodkendelsesstatusEnum
!endsub

!startsub 3_6_Bedoemmelse
class Prøveresultat {
  /bedømmelsesdato: Calculated [[1..1]]
  /prøveresultat: Calculated [[1..1]]
  /gældendeOpgavetitel: Calculated [[1..1]]
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
  /prøveforsøgnr: IgnoreBK [[1..1]]
  /prøveperiodestartdato: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
}

class PrøveforsøgMedBedømmelse {
  bedømmelsesnoter: ? [[1..1]]
  personligFeedback: ? [[0..1]]
}

class PrøveforsøgUdenBedømmelse {
  årsagTilManglendeBedømmelse: Picklist [[1..1]]
}

abstract Prøveaktivitetsforsøg {
}

class Prøveaktivitetsresultat {
  bedømmelsesdato: Date [[1..1]]
  gældendeOpgavetitel: Text80 [[0..1]]
  eksamenssprog: Picklist [[1..1]]
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /prøveaktivitetskode: IgnoreBK [[1..1]]
  /prøveforsøgsnr: IgnoreBK [[1..1]]
  /prøveperiodestartdato: IgnoreBK [[1..1]]
  /prøvevariantkode: IgnoreBK [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
}

class Resultat {
  skala: ? [[1..1]]
  karakter: ? [[1..1]]
}

enum årsagTilManglendeBedømmelseEnum <<enum>> {
  sygdom
  udeblivelse
  manglendeAflevering
  snyd
  forSentAflevering
}

PrøveforsøgMedBedømmelse "0..*" --  "1..*" Ansat : eksaminator
PrøveforsøgMedBedømmelse "0..*" --  "0..*" OrgPerson : censor
PrøveforsøgMedBedømmelse "0..*" --  "0..*" Ansat : medbedømmer
PersonligtFagelement "1" --  "0..*" Prøveresultat
PrøveforsøgMedBedømmelse "1" --  "1" Prøveaktivitetsresultat
Prøveresultat "1..*" --  "0..*" Prøveaktivitetsresultat : indgår i 
PrøveforsøgUdenBedømmelse "0..1" --  "1" PersonligPrøvebegivenhed
Prøveaktivitetsresultat "1" --  "1..*" Resultat
PrøveforsøgUdenBedømmelse --|>  Prøveaktivitetsforsøg
PrøveforsøgMedBedømmelse --|>  Prøveaktivitetsforsøg
PrøveforsøgUdenBedømmelse .right.>  årsagTilManglendeBedømmelseEnum
Prøveaktivitetsresultat .right.>  SprogEnum
!endsub

!startsub 4_1_Merit
abstract Merit {
}

class Meritansøgning {
  godkendelsesstatus: Picklist [[1..1]]
  dokumentationBeståelseAfEksterntFagelement: ? [[1..1]]
  afvisningsårsagsbegrundelse: ? [[1..1]]
  <<BK>>
  meritansøgningsnummer: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
}

class Omfangsmerit {
  omfangsmeritECTS-point: Number.1 [[1..1]]
  <<BK>>
  /ansøgningsnummer: IgnoreBK [[1..1]]
  /fagelementgrupperingskode: IgnoreBK [[1..1]]
  /periodekode: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
}

class Fagelementmerit {
  /meritECTS-point: Calculated [[1..1]]
  <<BK>>
  /ansøgningsnummer: IgnoreBK [[1..1]]
  /fagelementkode: IgnoreBK [[1..1]]
  /periodekode: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
  /uddannelseskode: IgnoreBK [[1..1]]
}

class Delmerit {
  delmeritECTS-point: Number.1 [[1..1]]
}

class SupplerendeECTS {
  /supplerendeECTS-point: Calculated [[1..1]]
}

class EksterntFagelement {
  eksterneCredits: ? [[0..1]]
  eksterntResultat: ? [[0..1]]
  eksterntFagelementNavn: Text80 [[1..1]]
  eksternBeståelsesdato: Date [[0..1]]
  beskrivelseAfEksternKarakterskala: TekstLong [[0..1]]
  beskrivelseAfEksterntCreditsystem: TekstLong [[0..1]]
  <<BK>>
  eksternFagelementkode: AutoNum [[1..1]]
  /organisationskode: IgnoreBK [[1..1]]
}

class Forhåndsgodkendelse {
  indløsningsstatus: Picklist [[1..1]]
  <<BK>>
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /ansøgningsnummer: IgnoreBK [[1..1]]
}

class AnsøgningOmForhåndsgodkendelse {
  godkendelsesstatus: Picklist [[1..1]]
  afvisningsårsagsbegrundelse: ? [[1..1]]
  <<BK>>
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /ansøgningsnummer: IgnoreBK [[1..1]]
}

class AnmodningOmIndløsning {
  dokumentationBeståelseAfEksterntFagelement: ? [[1..1]]
  <<BK>>
  /ansøgningsnummer: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
}

enum IndløsningsstatusEnum <<enum>> {
  indløst
  delvistIndløst
  ikkeIndløst
}

enum MerittypeEnum <<enum>> {
  førStartMerit
  regulærMerit
  tyvstartMerit
}

EksterntFagelement "0..*" --  "1" Uddannelsesinstitution : fra
Fagelementmerit "0..1" --  "1" PersonligtFagelement
Omfangsmerit "0..*" --  "1" PersonligFagelementgruppering : dækker en del af valgfri gruppering
Delmerit "1" --  "1" SupplerendeECTS
Merit "0..1" --  "1..*" EksterntFagelement
Meritansøgning "0..1" --  "0..*" Merit
AnsøgningOmForhåndsgodkendelse "1" --  "0..1" Forhåndsgodkendelse : kan medføre
Forhåndsgodkendelse "1" --  "0..*" AnmodningOmIndløsning
Merit "0..*" --  "0..1" AnmodningOmIndløsning
Meritansøgning "0..1" --  "0..*" EksterntFagelement
Forhåndsgodkendelse "0..1" --  "1..*" EksterntFagelement : gælder for
EksterntFagelement "1..*" --  "0..1" AnsøgningOmForhåndsgodkendelse : til
IndskrivningTilVideregåendeUddannelse "1" --  "0..*" AnsøgningOmForhåndsgodkendelse : ansøger
Meritansøgning "0..*" --  "1" IndskrivningTilVideregåendeUddannelse : ansøger
EksterntOphold "0..1" --  "1..*" EksterntFagelement : i forbindelse med
Forhåndsgodkendelse "0..1" --  "0..1" PersonligtFagelement
Forhåndsgodkendelse "0..1" --  "0..1" PersonligFagelementgruppering
AnmodningOmIndløsning "0..*" --  "1" EksterntFagelement
Omfangsmerit --|>  Merit
Fagelementmerit --|>  Merit
Delmerit --|>  Fagelementmerit
SupplerendeECTS --|>  PersonligtFagelement
Forhåndsgodkendelse .right.>  IndløsningsstatusEnum
Meritansøgning .right.>  GodkendelsesstatusEnum
AnsøgningOmForhåndsgodkendelse .right.>  GodkendelsesstatusEnum
!endsub

!startsub 3_1_4_Udbudsperiode
class Udbudsperiode {
  udbudsperiodenavn: Text80 [[1..1]]
  udbudsperiodeStartdato: Date [[1..1]]
  udbudsperiodeslutdato: Date [[1..1]]
  tilmeldingsperiode: ? [[1..1]]
  frameldingsperiode: ? [[1..1]]
  <<BK>>
  udbudsperiodekode: AutoNum [[1..1]]
}

class Læringsaktivitetsperiode {
  læringsaktivitetsPeriodeSlutdato: Date [[1..1]]
  <<BK>>
  læringsaktivitetsPeriodeStartdato: Date [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
}

class Prøveperiode {
  prøveperiodeslutdato: Date [[1..1]]
  tilmeldingsperiode: ? [[1..1]]
  frameldingsperiode: ? [[1..1]]
  <<BK>>
  prøveperiodestartdato: Date [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
}

PersonligtFagelement "0..*" --  "0..1" Udbudsperiode : planlagt til
PersonligFagelementgruppering "0..*" --  "0..*" Udbudsperiode : planlagt til
Læringsaktivitetsperiode "1..*" --  "1" Udbudsperiode
Prøveperiode "1..*" --  "1" Udbudsperiode
UdbudtFagelement "0..*" --  "1" Udbudsperiode
UdbudtLæringsaktivitet "0..*" --  "1" Læringsaktivitetsperiode
UdbudtPrøve "0..*" --  "1" Prøveperiode
!endsub

!startsub 3_7_Bevis
abstract Bevis {
}

class Eksamensbevis {
  dimissionsdato: Date [[1..1]]
  <<BK>>
  /indskrivningsnummer: IgnoreBK [[1..1]]
}

class Uddannelsescertifikat {
  <<BK>>
  /certifikatnummer: IgnoreBK [[1..1]]
}

class Enkeltfagsbevis {
  <<BK>>
  /indskrivningsnummer: IgnoreBK [[1..1]]
}

Eksamensbevis "0..1" --  "1" IndskrivningTilVideregåendeUddannelse
Enkeltfagsbevis "0..1" --  "1" IndskrivningTilEnkeltfag
Uddannelsescertifikat "0..*" --  "1" Bevis : vedlagt
Enkeltfagsbevis --|>  Bevis
Eksamensbevis --|>  Bevis
!endsub

!startsub 3_4_1_Personligt_studieforloeb
class PersonligtStudieforløb {
  /fortolketResultat: Calculated [[1..1]]
  /karaktergennemsnit: Calculated [[1..1]]
  <<BK>>
  /indskrivningsnummer: IgnoreBK [[1..1]]
}

class PersonligFagelementgruppering {
  /fortolketResultat: Calculated [[1..1]]
  /karaktergennemsnit: Calculated [[1..1]]
  /ECTS-point: Calculated [[1..1]]
  <<BK>>
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /fagelementgrupperingskode: IgnoreBK [[1..1]]
}

class Studiefremdrift {
  /opnåedeECTS-point: Calculated [[1..1]]
  /forventedeECTS-point: Calculated [[1..1]]
  /forventedeECTS-pointSU: Calculated [[1..1]]
  <<BK>>
  /indskrivningsnummer: IgnoreBK [[1..1]]
}

class PersonligtEnkeltfagsforløb {
  <<BK>>
  /indskrivningsnummer: IgnoreBK [[1..1]]
}

class PersonligForløbsprøve {
  erBestået: Checkbox [[1..1]]
  beståelsesdato: Date [[1..1]]
  <<BK>>
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /studieforløbskode: IgnoreBK [[1..1]]
  /forløbsprøvenr: IgnoreBK [[1..1]]
}

IndskrivningTilVideregåendeUddannelse "1" --  "1" PersonligtStudieforløb
GrupperingAfFagelement "1" --  "0..*" PersonligFagelementgruppering
PersonligtFagelement "1..*" --  "0..1" PersonligFagelementgruppering
PersonligFagelementgruppering "0..*" --  "0..1" PersonligtStudieforløb
Omfangsmerit "0..*" --  "1" PersonligFagelementgruppering : dækker en del af valgfri gruppering
PersonligtStudieforløb "1" --  "1" Studiefremdrift
Studieforløbsdispensation "0..*" --  "1" PersonligtStudieforløb
Fagelementdispensation "0..*" --  "0..1" PersonligFagelementgruppering
PersonligFagelementgruppering "0..*" --  "0..*" Udbudsperiode : planlagt til
PersonligtFagelement "0..*" --  "0..1" PersonligtStudieforløb
IndskrivningTilEnkeltfag "1" --  "1" PersonligtEnkeltfagsforløb
PersonligFagelementgruppering "0..*" --  "0..1" PersonligtEnkeltfagsforløb
PersonligtFagelement "0..*" --  "0..1" PersonligtEnkeltfagsforløb
PersonligtStudieforløb "1" --  "0..*" PersonligForløbsprøve
PersonligForløbsprøve "0..*" --  "1" Forløbsprøve
Forhåndsgodkendelse "0..1" --  "0..1" PersonligFagelementgruppering
!endsub

!startsub 3_4_2_Personligt_fagelement
abstract PersonligtFagelement {
}

class PersonligtProjektorienteretForløb {
}

class PersonligPraktik {
}

class PersonligAfsluttendeOpgave {
  afsluttendeOpgavetype: Picklist [[1..1]]
}

class PersonligProjektopgave {
}

class PersonligtKursus {
}

class EksterntOphold {
  opholdsperiodeSlutdato: Date [[1..1]]
  eksterntOpholdstype: Picklist [[1..1]]
  eksterntOpholdsform: Picklist [[1..1]]
  opholdsperiodeStartdato: Date [[1..1]]
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
}

class EksterntOpholdsansøgning {
  udvekslingsnomineret: ? [[0..1]]
  learningAgreement: ? [[0..1]]
  eksterntopholdssted: ? [[1..1]]
  grantAgreement: ? [[0..1]]
  <<BK>>
  /ansøgningsnummer: IgnoreBK [[1..1]]
}

class PersonligPrøveaktivitet {
  /antalBrugtePrøveaktivitetsforsøg: Calculated [[1..1]]
  <<BK>>
  /fagelementkode: IgnoreBK [[1..1]]
  /indskrivningsnummer: IgnoreBK [[1..1]]
  /prøveaktivitetskode: IgnoreBK [[1..1]]
}

enum PersonligtFagelementStatusEnum <<enum>> {
  anmodet
  planlagt
  tilmeldt
  bestået
  skalGennemføres
  ikkeBestået
  fritagelsePgaDispensation
}

enum EksterntOpholdstypeEnum <<enum>> {
  Udvekslingsophold
  UdlandsStudieopholdUdenUdvekslingsaftale
  PraktikIDanmark
  PraktikIUdlandet
  ProjektorienteretForløbIDanmark
  ProjektorienteretFOrløbIUdlandet
  StudieopholdIDanmark
}

enum EksterntOpholdsformEnum <<enum>> {
  fysiskOphold
  virtueltOphold
  hybridOphold
}

EksterntOphold "0..*" --  "0..1" Uddannelsesinstitution
EksterntOphold "0..1" --  "1..*" EksterntFagelement : i forbindelse med
Aftalegrundlag "0..1" --  "0..1" EksterntOphold
EksterntOphold "0..1" --  "0..1" EksterntOpholdsansøgning : medfører
EksterntOphold "0..*" --  "0..1" Program : hører under
IndskrivningTilVideregåendeUddannelse "1" --  "0..*" EksterntOpholdsansøgning
PersonligPrøveaktivitet "0..*" --  "1" PersonligtFagelement
PersonligPrøveaktivitet "1" --  "1..*" Prøveaktivitetstilmelding
PersonligPraktik "0..1" --  "1" EksterntOphold
PersonligtProjektorienteretForløb "0..1" --  "1" EksterntOphold
EksterntOphold "0..1" --  "0..1" Organisation : hos
PersonligtProjektorienteretForløb --|>  PersonligtFagelement
PersonligPraktik --|>  PersonligtFagelement
PersonligAfsluttendeOpgave --|>  PersonligtFagelement
PersonligProjektopgave --|>  PersonligtFagelement
PersonligtKursus --|>  PersonligtFagelement
PersonligAfsluttendeOpgave .right.>  AfsluttendeOpgavetypeEnum
EksterntOphold .right.>  EksterntOpholdstypeEnum
EksterntOphold .right.>  EksterntOpholdsformEnum
!endsub

!startsub 4_2_Udveksling
class Udvekslingsaftale {
  antalUdvekslingspladserIndrejse: Number.0 [[0..1]]
  antalUdvekslingspladserUdrejse: Number.0 [[0..1]]
  udvekslingsaftalePeriode: ? [[0..1]]
  udvekslingAftaletype: PicklistMulti [[1..2]]
  <<BK>>
  /programnavn: IgnoreBK [[1..1]]
  /organisationskode: IgnoreBK [[1..1]]
}

class Udvekslingsprogram {
}

class Udvekslingsansøgning {
  indrejsenominering: ? [[1..1]]
  learningAgreement: ? [[0..1]]
  praktiskeForhold: TekstLong [[0..1]]
  udvekslingsopholdStartdato: Date [[1..1]]
  udvekslingsopholdSlutdato: Date [[1..1]]
}

class Program {
  <<BK>>
  programnavn: Text80 [[1..1]]
}

class ProjektorienteretOpholdsprogram {
}

class Praktikprogram {
}

enum UdvekslingsaftaletypeEnum <<enum>> {
  programaftale
  institutionsaftale
}

Udvekslingsaftale "0..*" --  "0..1" Udvekslingsprogram : hører under
Uddannelsesinstitution "1" --  "0..*" Udvekslingsaftale : partner institution
Uddannelsesinstitution "1" --  "0..*" Udvekslingsansøgning : fra
EksterntOphold "0..*" --  "0..1" Program : hører under
Udvekslingsaftale "0..1" --  "0..*" Udvekslingsansøgning : under
Program "1" --  "0..1" Udvekslingsprogram
Program "1" --  "0..1" ProjektorienteretOpholdsprogram
Program "1" --  "0..1" Praktikprogram
IndskrivningTilEnkeltfag "0..*" --  "0..1" Udvekslingsaftale : under 
Udvekslingsansøgning "0..*" --  "0..1" OrgPerson : ekstern kontakt
Udvekslingsansøgning --|>  Enkeltfagsansøgning
Udvekslingsaftale .right.>  UdvekslingsaftaletypeEnum
!endsub

!startsub 2_1_1_Ansoegning_om_studieplads
abstract AnsøgningOmOptagelse {
}

class PrioriteretUddannelse {
  <<BK>>
  /ansøgningsnummer: IgnoreBK [[1..1]]
  /prioritering: IgnoreBK [[1..1]]
}

class FagligVurdering {
  ansøgningsrangering: Number.0 [[1..1]]
  afgørelsesbegrundelse: ? [[1..1]]
  ansøgningspoint: Number.1 [[1..1]]
  <<BK>>
  /ansøgningsnummer: IgnoreBK [[1..1]]
  /prioriteringsrangering: IgnoreBK [[1..1]]
}

class ErhvervsmæssigBaggrund {
  godkendt: Checkbox [[1..1]]
}

abstract Enkeltfagsansøgning {
}

class Uddannelsesansøgning {
  uddannelsestype: Picklist [[1..1]]
  <<BK>>
  /ansøgningsnummer: IgnoreBK [[1..1]]
}

class PrioriteretEnkeltfag {
  <<BK>>
  /ansøgningsnummer: IgnoreBK [[1..1]]
  /prioritering: IgnoreBK [[1..1]]
}

class MeritPladsAnsøgning {
}

class TompladsAnsøgning {
}

class EnkeltfagFraDeltidsuddannelsesansøgning {
}

class AndenBaggrund {
  godkendt: Checkbox [[1..1]]
}

class Optagelsesprøveresultat {
  bestået: ? [[1..1]]
}

abstract Ansøgningsrangering {
}

class Ansøgningsgebyr {
  beløb: Currency [[1..1]]
  betalingsdato: Date [[1..1]]
  betalingsstatus: Picklist [[1..1]]
}

class AdgangskursusAnsøgning {
}

class FagspecifiktKursusAnsøgning {
}

class KortKursusAnsøgning {
}

class SærskiltModulAnsøgning {
}

class Optagelsesdispensation {
  optagelsesdispensationstype: Picklist [[1..1]]
}

class Optagelsesdispensationsansøgning {
  godkendelsesstatus: Picklist [[1..1]]
}

class SuppleringsAnsøgning {
}

class KotAnsøgning {
  erStandby: Checkbox [[0..1]]
  ønskerUdskudtStart: ? [[0..1]]
  harBeståetKandidat: Checkbox [[0..1]]
  harFåetTIlsagn: Checkbox [[0..1]]
  Studieretning: ? [[0..1]]
  ToÅrsRegel: ? [[0..1]]
  iGangMedSuppleringskursus: ? [[0..1]]
  tilmeldtSuppleringskursus: ? [[0..1]]
  optagelsesDkAnsøgerId: ? [[1..1]]
  optagelsesDkAnsøgningsId: ? [[1..1]]
  erDigital: Checkbox [[1..1]]
  optagelseDkStatus: ? [[1..1]]
  optagelseDKSenesteÆndring: ? [[0..1]]
  underskriftTidspunkt: Number.1 [[0..1]]
  erTidligereOptaget: Number.1 [[0..1]]
  harSøgtGrønladskSærordning: Checkbox [[0..1]]
  udenlandskEksamenLand: ? [[0..1]]
  udenlandskEksamenÅr: ? [[0..1]]
  eksamensresultatGenberegnet: ? [[0..1]]
  resultatErGenberegnet: ? [[0..1]]
  bilag: ? [[0..*]]
}

enum OptagelsesstatusEnum <<enum>> {
  underFagligVurdering
  afventerPladsfordeling
  optaget
  afvist
  tilbudtOptagelse
  betingetOptaget
  tilbudtBetingetOptagelse
  afventerBehandling
  manglendeBetaling
  lukketPgaOptagPåHøjerePrioritet
  tilbudAfslået
  underAdministrativBehandling
  påventeliste
  annulleret
}

enum AnsøgningsstatusEnum <<enum>> {
  modtaget
  underbehandling
  afsluttet
  annulleret
}

enum AfvisningsårsagEnum <<enum>> {
  betingelserIkkeOpfyldt
  manglendeAnsøgningsgebyr
  manglendeDokumentation
  manglendeKvalifikationer
  manglendeStudieplads
  overskredetAnsøgningsfrist
  pgaAdgangsprøve
  pgaOptagelsesprøve
  pgaRegelbrud
}

enum OptagelsesdispensationstypeEnum <<enum>> {
  afvigelseAdgangskrav
  AfvigelseAnsøgningsfristOptagelse
}

Uddannelsesansøgning "1" --  "0..1" TilbudOmStudiepladsPåUddannelse : fremsendt tilbud
Uddannelsesansøgning "1" --  "1..*" PrioriteretUddannelse : ansøgning indeholder
PrioriteretUddannelse "0..*" --  "1" UdbudtVideregåendeUddannelse
Uddannelsesansøgning "0..*" --  "0..1" UdbudtVideregåendeUddannelse : placeret på venteliste til
ErhvervsmæssigBaggrund "0..1" --  "1" AnsøgningOmOptagelse : ansøgning indeholder
Enkeltfagsansøgning "1" --  "1..*" PrioriteretEnkeltfag : ansøgning indeholder
PrioriteretEnkeltfag "0..*" --  "1" UdbudtEnkeltfag
AnsøgningOmOptagelse "1" --  "0..1" AndenBaggrund
Optagelsesprøveresultat "0..*" --  "1" AnsøgningOmOptagelse
Ansøgningsrangering "1" --  "0..1" FagligVurdering
Ansøgningsgebyr "0..1" --  "1" AnsøgningOmOptagelse
Optagelsesdispensation "0..1" --  "1" AnsøgningOmOptagelse
AnsøgningOmOptagelse "0..1" --  "0..*" Optagelsesdispensationsansøgning
Optagelsesdispensationsansøgning "1" --  "0..*" Optagelsesdispensation
Uddannelsesansøgning --|>  AnsøgningOmOptagelse
PrioriteretUddannelse --|>  Ansøgningsrangering
PrioriteretEnkeltfag --|>  Ansøgningsrangering
SærskiltModulAnsøgning --|>  Enkeltfagsansøgning
FagspecifiktKursusAnsøgning --|>  Enkeltfagsansøgning
AdgangskursusAnsøgning --|>  Enkeltfagsansøgning
TompladsAnsøgning --|>  Enkeltfagsansøgning
MeritPladsAnsøgning --|>  Enkeltfagsansøgning
EnkeltfagFraDeltidsuddannelsesansøgning --|>  Enkeltfagsansøgning
KortKursusAnsøgning --|>  Enkeltfagsansøgning
SuppleringsAnsøgning --|>  Enkeltfagsansøgning
KotAnsøgning --|>  Uddannelsesansøgning
Uddannelsesansøgning .right.>  UddannelsestypeEnum
Optagelsesdispensation .right.>  OptagelsesdispensationstypeEnum
Optagelsesdispensationsansøgning .right.>  GodkendelsesstatusEnum
Ansøgningsgebyr .right.>  BetalingsstatusEnum
!endsub

!startsub 2_1_1_1_Uddannelsesbaggrund
class Uddannelsesbaggrund {
  godkendt: Checkbox [[1..1]]
  retskrav: ? [[1..1]]
}

class AdgangsgivendeEksamen {
  adgangsgivendeEksamenDS-kode: Text80 [[1..1]]
  adgangsgivendeEksamenNavn: Text80 [[1..1]]
  adgangsgivendeEksamenÅr: ? [[1..1]]
  retskrav: ? [[1..1]]
  adgangskvotient: ? [[1..1]]
  bedømmelsesform: Picklist [[1..1]]
  eksamensresultat: ? [[1..1]]
  eksamenstype: ? [[1..1]]
  eksamenstypeTekstbeskrivelse: TekstLong [[1..1]]
  eksamensår: ? [[1..1]]
  karaktergennemsnit: ? [[1..1]]
  udmeldelsesperiode: ? [[1..1]]
  udstedelsesår: ? [[1..1]]
  årskaraktergennemsnit: ? [[1..1]]
  adgangskvotient: ? [[1..1]]
  bedømmelsesform: ? [[1..1]]
  eksamensresultat: ? [[1..1]]
  eksamenstype: ? [[1..1]]
  eksamenstypeTekstbeskrivelse: TekstLong [[1..1]]
  eksamensår: ? [[1..1]]
  karaktergennemsnit: ? [[1..1]]
  udmeldelsesperiode: ? [[1..1]]
  udstedelsesår: ? [[1..1]]
  årskaraktergennemsnit: ? [[1..1]]
  adgangsgivendeEksamenNavn: Text80 [[1..1]]
  adgangsgivendeEksamensTerminAar: ? [[1..1]]
  <<BK>>
  adgangsgivendeEksamenskode: AutoNum [[1..1]]
  adgangsgivenddeEksamenkode: AutoNum [[1..1]]
}

class TidligereOptag {
  afbrudtÅr: ? [[0..1]]
  aktivIndskrivning: ? [[1..1]]
  ECTS-point: Number.1 [[0..1]]
  forventetBeståetÅr: ? [[1..1]]
  indskrivningsstartår: ? [[1..1]]
  optagelsesområde: ? [[1..1]]
}

class Fagniveau {
  bedømmelsesår: ? [[1..1]]
  fagkode: Text80 [[1..1]]
  fagnavn: Text80 [[1..1]]
  harMerit: Checkbox [[1..1]]
  karakter: ? [[1..1]]
  karaktertype: ? [[1..1]]
  karaktertypeForklaring: ? [[1..1]]
  karaktervægt: Percent [[1..1]]
  mundtligtNiveau: ? [[1..1]]
}

class AndenEksamenEllerPrøve {
  afbrudtÅr: ? [[0..1]]
  erStadigOptaget: Checkbox [[1..1]]
  fagnavn: Text80 [[1..1]]
  forventetBeståetMåned: ? [[0..1]]
  karakterMundtlig: ? [[0..1]]
  karakterSkriftlig: ? [[0..1]]
  kursusnavn: Text80 [[1..1]]
  startÅr: ? [[1..1]]
  uddannelsesniveau: Picklist [[1..1]]
}

class GymnasialUddannelse {
}

AdgangsgivendeEksamen "0..*" --  "1" Uddannelsesinstitution : adgangsgivende inst.
AnsøgningOmOptagelse "1" --  "0..1" Uddannelsesbaggrund : ansøgning indeholder
AdgangsgivendeEksamen "0..*" --  "0..1" Adgangsgrundlag
Uddannelsesbaggrund "1" --  "0..*" TidligereOptag
Uddannelsesbaggrund "1" --  "0..*" AdgangsgivendeEksamen
Uddannelsesbaggrund "1" --  "0..*" AndenEksamenEllerPrøve
AdgangsgivendeEksamen "1" --  "0..*" Fagniveau
VideregåendeUddannelse "1" --  "0..*" TidligereOptag
GymnasialUddannelse "1" --  "0..*" AdgangsgivendeEksamen
GymnasialUddannelse --|>  Uddannelse
AndenEksamenEllerPrøve .right.>  UddannelsesniveauEnum
AdgangsgivendeEksamen .right.>  BedømmelsesformEnum
!endsub

!startsub 2_1_2_Tilbud_om_studieplads
class AdgangsprøveResultat {
  bestået: ? [[1..1]]
  <<BK>>
  /ansøgningsnummer: IgnoreBK [[1..1]]
}

class TilbudOmStudiepladsPåUddannelse {
  svarfrist: Date [[1..1]]
  tilbudsstatus: Picklist [[1..1]]
  <<BK>>
  /ansøgningsnummer: IgnoreBK [[1..1]]
}

class TilbudOmStudiepladsPåEnkeltfag {
  svarfrist: Date [[1..1]]
  tilbudsstatus: Picklist [[1..1]]
  <<BK>>
  /ansøgningsnummer: IgnoreBK [[1..1]]
  /enkeltfagskode: IgnoreBK [[1..1]]
  /udbudsperiodekode: IgnoreBK [[1..1]]
  /udbudsstedkode: IgnoreBK [[1..1]]
}

enum TilbudsstatusEnum <<enum>> {
  afventerSvar
  afslået
  accepteret
  fortrudtAccepteret
}

Uddannelsesansøgning "1" --  "0..1" TilbudOmStudiepladsPåUddannelse : fremsendt tilbud
AdgangsprøveResultat "0..1" --  "1" TilbudOmStudiepladsPåUddannelse
TilbudOmStudiepladsPåUddannelse "1" --  "0..1" IndskrivningTilVideregåendeUddannelse : accept medfører
UdbudtVideregåendeUddannelse "1" --  "0..*" TilbudOmStudiepladsPåUddannelse
Enkeltfagsansøgning "1" --  "0..1" TilbudOmStudiepladsPåEnkeltfag : fremsendt tilbud
TilbudOmStudiepladsPåEnkeltfag "0..*" --  "1..*" UdbudtEnkeltfag
TilbudOmStudiepladsPåEnkeltfag "0..*" --  "0..1" IndskrivningTilEnkeltfag : accept medfører
TilbudOmStudiepladsPåUddannelse "0..*" --  "1" Studiestart
TilbudOmStudiepladsPåUddannelse .right.>  TilbudsstatusEnum
TilbudOmStudiepladsPåEnkeltfag .right.>  TilbudsstatusEnum
!endsub

!startsub 1_8_Finansiering
class EksternKontakt {
  kontaktNavn: Text80 [[1..1]]
  kontaktEmail: ? [[1..1]]
}

class Indskrivningsfinansiering {
  finansieringsform: Picklist [[1..1]]
  finansieringsperiode: ? [[1..1]]
  rekvirent: Picklist [[1..1]]
  <<BK>>
  /indskrivningsnummer: IgnoreBK [[1..1]]
}

class Deltagerfinansiering {
  beløb: Currency [[1..1]]
  personligAndel: Percent [[1..1]]
  virksomhedsandel: Percent [[1..1]]
  antalRater: Number.0 [[1..1]]
}

class Virksomhedsbetaling {
}

class PersonligBetaling {
}

class Faktureringsgrundlag {
  betalingsstatus: Picklist [[1..1]]
  betalingsfrist: Date [[1..1]]
  beløb: Currency [[1..1]]
  betalingsdato: Date [[0..1]]
}

enum FinansieringsformEnum <<enum>> {
  STÅ-finansieret
  udenlandskSelvfinansieret
  årselevfinansieret
  andenOffentligFinansiering
  friplads-ogStipendiefinansieret
  deltagerbetaling
  danskSelvfinansieret
}

enum BetalingsstatusEnum <<enum>> {
  opkrævet
  betalt
  krediteret
  annulleret
}

enum RekvirentEnum <<enum>> {
  AAKA
  AAKF
  AAKR
  AAST
  AFT
  AND
  ASO
  AUS
  FRB
  FRF
  FRU
  INNO
  KOMA
  KOMF
  KOMR
  SID1
  SJOB
  TALE
  UI
  UNI
  USB
  UVM
}

EksternKontakt "0..*" --  "1" Organisation
Aftalegrundlag "0..*" --  "0..1" EksternKontakt : ekstern vejleder
Indskrivningsfinansiering "1..*" --  "1" Indskrivning
Virksomhedsbetaling "0..*" --  "1" Organisation : debitor
Virksomhedsbetaling "0..*" --  "0..*" EksternKontakt : kontakt
Virksomhedsbetaling "0..1" --  "1..*" Faktureringsgrundlag
Faktureringsgrundlag "1..*" --  "0..1" PersonligBetaling
Virksomhedsbetaling "0..1" --  "1" Deltagerfinansiering
PersonligBetaling "0..1" --  "1" Deltagerfinansiering
Deltagerfinansiering --|>  Indskrivningsfinansiering
Indskrivningsfinansiering .right.>  FinansieringsformEnum
Faktureringsgrundlag .right.>  BetalingsstatusEnum
Indskrivningsfinansiering .right.>  RekvirentEnum
!endsub

!startsub 3_4_3_Studiedispensation
abstract Studiedispensation {
}

class Prøvedispensation {
  prøvedispensationstype: Picklist [[1..1]]
}

class Studieforløbsdispensation {
  studieforløbsdispensationstype: Picklist [[1..1]]
}

class PermanentPrøvedispensation {
  permanentprøvedispensationstype: Picklist [[1..1]]
}

class Fagelementdispensation {
  fagelementdispensationstype: Picklist [[1..1]]
}

class StudiedispensationsAnsøgning {
  godkendelsesstatus: Picklist [[1..1]]
  afvisningsårsagsbegrundelse: ? [[1..1]]
  dispensationsansøgningsbeskrivelse: TekstLong [[1..1]]
  <<BK>>
  /ansøgningsnummer: IgnoreBK [[1..1]]
}

class Indskrivningsdispensation {
}

enum FagelementdispensationstypeEnum <<enum>> {
  AfvigelseFagelementemne
  AfvigelseFagligeKrav
  FritagelseObligatoriskFagelement
  OverskredetFrameldingsfrist
  OverskredetTilmeldingsfrist
  FritagelseTilmeldingsbinding
}

enum PermanentPrøvedispensationstypeEnum <<enum>> {
  SærligeHjælpemidlerTilladt
  ÆndretForberedelsestid
  ÆndretPrøvebegivenhedsform
  ÆndretPrøvetid
  IndividuellePraktiskeForhold
  IndividuelPrøve
  Øvrige
}

enum StudieforløbsdispensationstypeEnum <<enum>> {
  ECTS-pointkrav
  ForlængelseStudieforløb
  FørsteårsprøveUdsættelse
  StudiestartsprøveUdsættelse
  SUaktivitetskrav
  TilladelseEkstraECTS-point
  Tilmeldingskrav
  TilmeldingTilKandidatfagelementer
}

enum PrøveDispensationstypeEnum <<enum>> {
  AfvigelseAfleveringsfrist
  AfvigelseEksamensforudsætning
  AfvigelseGruppestørrelse
  AfvigelsePrøveemne
  AfvigelseSprogkrav
  EkstraPrøveforsøg
  ÆndretPrøvetid
  IndividuelPrøve
  OverskredetFrameldingsfrist
  OverskredetTilmeldingsfrist
  SærligeHjælpemidlerTilladt
  ÆndretBedømmelsesform
  ÆndretCensurform
  ÆndretForberedelsestid
  ÆndretOpgavestørrelse
  ÆndretPrøvebegivenhedsform
  IndividuellePraktiskeForhold
  Øvrige
}

Studieforløbsdispensation "0..*" --  "1" PersonligtStudieforløb
Prøvetilmelding "1" --  "0..*" Prøvedispensation
Prøvedispensation "0..*" --  "0..1" PermanentPrøvedispensation : udmøntes i 
Fagelementdispensation "0..*" --  "0..1" PersonligtFagelement
Fagelementdispensation "0..*" --  "0..1" PersonligFagelementgruppering
StudiedispensationsAnsøgning "0..*" --  "1" Indskrivning
StudiedispensationsAnsøgning "1" --  "0..1" Studiedispensation
PermanentPrøvedispensation "0..*" --  "1" Studerende
Prøvedispensation --|>  Studiedispensation
Studieforløbsdispensation --|>  Studiedispensation
PermanentPrøvedispensation --|>  Studiedispensation
Fagelementdispensation --|>  Studiedispensation
Indskrivningsdispensation --|>  Studiedispensation
Fagelementdispensation .right.>  FagelementdispensationstypeEnum
PermanentPrøvedispensation .right.>  PermanentPrøvedispensationstypeEnum
Studieforløbsdispensation .right.>  StudieforløbsdispensationstypeEnum
Prøvedispensation .right.>  PrøveDispensationstypeEnum
StudiedispensationsAnsøgning .right.>  GodkendelsesstatusEnum
!endsub

!startsub 1_3_2_Studieforloebets_fagelementer
class StudieforløbFagelementgruppering {
  karaktervægt: Percent [[1..1]]
  erEtSammenvægtetResultat: Percent [[1..1]]
  medtagesPåBevis: Checkbox [[1..1]]
  rækkefølgePåBevis: ? [[0..1]]
  valgfrihedsgrad: Calculated [[1..1]]
  beståECTS-pointMaksimum: Number.0 [[1..1]]
  beståECTS-pointMinimum: Number.0 [[1..1]]
  anvendelsestype: Picklist [[0..1]]
  <<BK>>
  /studieforløbskode: IgnoreBK [[1..1]]
  /fagelementgrupperingskode: IgnoreBK [[1..1]]
  /parentFagelementgrupperingskode: IgnoreBK [[0..1]]
}

class FagelementIStudieforløbsperiode {
  erPrimærAnbefaletPlacering: Checkbox [[1..1]]
  <<BK>>
  /Fagelementgrupperingskode: IgnoreBK [[0..1]]
  /studieforløbskode: IgnoreBK [[1..1]]
  /fagelementkode: IgnoreBK [[1..1]]
  /studieforløbsperiodeRækkefølgeNr: IgnoreBK [[1..1]]
  /parentFagelementgrupperingskode: IgnoreBK [[0..1]]
}

class FagelementgrupperingIStudieforløbsperiode {
  placerbareECTS-pointMaksimum: Number.0 [[1..1]]
  placerbareECTS-pointMinimum: Number.0 [[1..1]]
  anbefaletOmfangPlacerbareECTS-point: Number.1 [[0..1]]
  <<BK>>
  /fagelementgrupperingskode: IgnoreBK [[1..1]]
  /studieforløbskode: IgnoreBK [[1..1]]
  /studieforløbsperiodeRækkefølgeNr: IgnoreBK [[1..1]]
  /parentFagelementgrupperingskode: IgnoreBK [[0..1]]
}

class StudieforløbFagelement {
  medtagesPåBevis: Checkbox [[1..1]]
  rækkefølgePåBevis: ? [[0..1]]
  karaktervægt: Percent [[1..1]]
  valgfrihedsgrad: Calculated [[1..1]]
  <<BK>>
  /Fagelementkode: IgnoreBK [[1..1]]
  /Fagelementgrupperingskode: IgnoreBK [[0..1]]
  /studieforløbskode: IgnoreBK [[1..1]]
  /parentFagelementgrupperingskode: IgnoreBK [[0..1]]
}

enum ValgfrihedsgradEnum <<enum>> {
  obligatorisk
  valgfrit
  afgrænsetValgfrit
}

enum AnvendelsestypeEnum <<enum>> {
  lokalt defineret værdiliste
}

Studieforløb "1" --  "0..*" StudieforløbFagelementgruppering
GrupperingAfFagelement "1" --  "0..*" StudieforløbFagelementgruppering
StudieforløbFagelementgruppering "0..*" --  "0..1" Fagområde : henføres til
Studieforløbsperiode "1" --  "0..*" FagelementgrupperingIStudieforløbsperiode
Studieforløbsperiode "1" --  "0..*" FagelementIStudieforløbsperiode
StudieforløbFagelementgruppering "1" --  "0..*" FagelementgrupperingIStudieforløbsperiode
StudieforløbFagelement "0..*" --  "0..1" StudieforløbFagelementgruppering
StudieforløbFagelement "0..*" --  "0..1" FagelementIFagelementgruppering
StudieforløbFagelement "0..*" --  "1" Fagelement
FagelementIStudieforløbsperiode "0..*" --  "1" StudieforløbFagelement
StudieforløbFagelement "1..*" --  "1" Studieforløb
PersonligtFagelement "0..*" --  "0..1" StudieforløbFagelement
StudieforløbFagelementgruppering .right.>  ValgfrihedsgradEnum
StudieforløbFagelement .right.>  ValgfrihedsgradEnum
StudieforløbFagelementgruppering .right.>  AnvendelsestypeEnum
!endsub

!startsub 1_7_3_Studiepladskapacitet
class Studiepladskapacitet {
  reelStudiepladskapacitet: Number.0 [[1..1]]
  efteroptagelseskapacitet: Number.0 [[1..1]]
  ventelistekapacitet: Number.0 [[1..1]]
  /optagelseskapcitet: Calculated [[1..1]]
  overbookingsantal: Number.0 [[1..1]]
}

class StudiepladskapacitetBachelor {
  /kvote2studiepladser: Calculated [[1..1]]
  kvote2procentdel: Percent [[1..1]]
  standbykapacitetKvote2: Number.0 [[1..1]]
  standbykapacitetKvote1: Number.0 [[1..1]]
}

Studiepladskapacitet "0..1" --  "0..1" UdbudtStudieforløb : kan have begrænset kapacitet
UdbudtVideregåendeUddannelseOgEnkeltfag "0..1" --  "0..1" Studiepladskapacitet : kan have begrænset kapacitet
StudiepladskapacitetBachelor --|>  Studiepladskapacitet
!endsub

@enduml
