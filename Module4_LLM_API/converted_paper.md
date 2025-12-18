# Converted Academic Paper

> Automatically converted from PDF to Markdown

---



<!-- Chunk 1 -->

Multivariate Behavioral Research
ISSN: 0027-3171 (Print) 1532-7906 (Online) Journal homepage: www.tandfonline.com/journals/hmbr20
Small Sample Methods for Multilevel Modeling: A
Colloquial Elucidation of REML and the Kenward-
Roger Correction
Daniel McNeish
To cite this article: Daniel McNeish (2017) Small Sample Methods for Multilevel Modeling: A
Colloquial Elucidation of REML and the Kenward-Roger Correction, Multivariate Behavioral
Research, 52:5, 661-670, DOI: 10.1080/00273171.2017.1344538
To link to this article:  https://doi.org/10.1080/00273171.2017.1344538
Published online: 17 Jul 2017.
Submit your article to this journal 
Article views: 5096
View related articles 
View Crossmark data
Citing articles: 119 View citing articles 
Full Terms & Conditions of access and use can be found at
https://www.tandfonline.com/action/journalInformation?journalCode=hmbr20

---


<!-- Chunk 2 -->

MULTIVARIATEBEHAVIORALRESEARCH
,VOL.,NO.,–https://doi.org/./..
QUANTITATIVEMETHODSINPRACTICE:TUTORIAL
Small Sample Methods for Multilevel Modeling: A Colloquial Elucidation of REML
and the Kenward-Roger Correction
DanielMcNeish
UniversityofNorthCarolina,ChapelHill;ArizonaStateUniversity
KEYWORDS
Restrictedmaximum
likelihood;Kenward-Roger;
tutorial;explanation;mixed
modelABSTRACT
Studiesonsmallsamplepropertiesofmultilevelmodelshavebecomeincreasinglyprominentinthe
methodologicalliteratureinresponsetothefrequencywithwhichsmallsampledataappearinempir-ical studies. Simulation results generally recommend that empirical researchers employ restrictedmaximum likelihood estimation (REML) with a Kenward-Roger correction with small samples in fre-quentistcontextstominimizesmallsamplebiasinestimationandtopreventinflationofType-Ierrorrates.However,simulationstudiesfocusonrecommendationsforbestpractice,andthereislittletonoexplanationofwhytraditionalmaximumlikelihood(ML)breaksdownwithsmallersamples,whatdifferentiatesREMLfromML,orhowtheKenward-Rogercorrectionremedieslingeringsmallsampleissues.Duetothecomplexityofthesemethods,mostextantdescriptionsarehighlymathematicalandareintendedtoprovethatthemethodsimprovesmallsampleperformanceasintended.Thus,empir-
icalresearchershavedocumentationthatthesemethodsareadvantageousbutstilllackresourcesto
helpunderstandwhatthemethodsactuallydoandwhytheyareneeded.ThistutorialexplainswhyML falters with small samples, how REML circumvents some issues, and how Kenward-Roger works.We do so without equations or derivations to support more widespread understanding and use ofthesevaluablemethods.
In behavioral science studies, clustered data arise quite
frequentlyintheformofeithercross-sectionalclusteringor longitudinal clustering (Raudenbush & Bryk, 2002).
Cross-sectional clustering occurs when people belongto higher-level units, such as students clustered withinschools in education or employees clustered withincompanies in business. Longitudinal clustering occurswh e nth esa m ei n d i vi d ual sa r em ea s u r edr e pea t edl yo v e rtime such that observations are clustered within people.The clustered nature of such data violates the indepen-dence assumption posited by the general linear model;therefore, specialized statistical techniques are requiredtoappropriately model suchdata. In behavioral sciences,themostcommontechniqueis multilevelmodeling ,which
isalsocommonlyreferredtoas mixed effects modeling or
hierarchicallinearmodeling .
1
In multilevel models (MLMs), sample size issues tend
to be more prominent because the data feature multi-
ple levels. For instance, if students are cross sectionally
clustered within schools, there is a Level-1 sample sizethat refers to the number of students in the data and aLevel-2 sample size that refers to the number of schoolsinthedata.InMLMs,theLevel-2samplesizeisthemost
CONTACT DanielMcNeish dmcneish@asu.edu DepartmentofPsychology,ArizonaStateUniversity,P.O.Box,Tempe,AZ,USA.
Therearesomeminordiﬀerencesbetweenthesetypesofmodelsbut,forthepurposeofthismanuscript,weconsiderthemodelstobemoreorlessintercha ngeable.importantfactorfordeterminingwhetherthemodelwill
be afflicted by small sample issues (Snijders & Bosker,1993). In empirical studies, this tends to be problematic
b e c a u s et h eL e v e l - 2s a m p l es i z ei st h em o s td i ffi c u l ta n dfinancially costly to increase. Using the students withinschools as example, the number of students may be over1,000butiftheyareclusteredwithin20schools,thedata(perhaps unintuitively) fall under the “small sample”umbrella.
Withclustereddata,smallsamplesarequitecommon.
An informal review of behavioral science meta-analysesby McNeish ( 2016) reported that about 33% of growth
models,20%ofmultilevelmodels,40%ofmeta-analyses,and 30% of cluster randomized trials would be classifiedas small sample problems based on cutoffs suggested int h el i t e r a t u r e .S m a l ls a m p l ei s s u e sf o rM L M sh a v en o tgoneunnoticed,however.Infact,therehasbeenarecentincrease in methodological studies exploring small sam-
ple data and MLMs in the last decade beginning with
the seminal study by Maas and Hox ( 2005), which was
one of the first to explore sufficient sample sizes to usemultilevelmodels.Recentstudieshavebeenconductedtoexplorehowsmallresearcherscouldtakesamplesizesand
©Taylor&FrancisGroup,LLC

---


<!-- Chunk 3 -->

662 D.MCNEISH
still trust their estimates (Bell, Morgan, Schoeneberger,
Kromrey, &Ferron, 2014),acomparisonofsmallsample
corrections(McNeish&Stapleton, 2016a),acomparison
ofmultilevelbootstrappingandsmallsamplecorrections(Huang,2017), comparisons of Bayesian and frequentist
methods(Hox,vandeSchoot,&Matthijsse,2012),andareview of small sample methods for MLMs (McNeish &Stapleton, 2016b).
These studies generally find that Level-2 sample sizes
below 50 are susceptible to small sample biases, whichincludedownwardlybiasedestimatesofboththevariancecomponents and the fixed effect standard errors, result-ingininflatedType-Ierrorratesforinferenceaboutfixedeffects. Results show that data with Level-2 sample sizesbelow 25 will almost certainly encounter these issues ifprecautions are not taken. In the frequentist framework,restricted maximum likelihood (REML) estimation hasbeen shown to have much improved small sample prop-ertiesandcontinuestoperformwellwithLevel-2sample
sizes into the single digits (Ferron, Bell, Hess, Rendina-
Gobioff, & Hibbard, 2009; McNeish & Stapleton, 2016a).
REMLdoesnotcompletelysolveissuesrelatedtoinflatedType-Ierrorratesforfixedeffects,sotheKenward-Rogercorrection (Kenward & Roger, 1997) has been shown to
maintainnominalType-Ierrorratesandthereforeitsusehasbeenrecommendedasbestpractice(e.g.,McNeish&Stapleton, 2016b). This correction has also been recently
made available in SAS (PROC MIXED and PROCG L I M M I X ) ,S t a t a ,a n di nt h ep b k r t e s ta n dl m e r T e s tRpackages.
Thesestudies,alongwithpopulartextbooktreatments
ofthetopic,areundoubtedlyinformativeandtheytendtofocusonhowtomodelsmallsampledatabyproviding best
practicerecommendations.Thisgoalishelpfulforempir-
ical researchers who possess small sample data becausemaking informed modeling decisions is vital to improv-ingsmallsampleanalyses.However,thesesourcesallocatelittle to no space to explain whysmall sample issues are
a problem in the first place. For researchers looking tounderstand the mechanism underlying why MLMs fail
with smaller sample sizes with traditional methods and
whyalternativemethodsforsmallsamplesarenecessary,theexistingmethodologicalliteraturedoeslittletodelin-eatetheissuebeyondmentioningafewplatitudessuchasnotingthatmaximumlikelihood(ML)isasymptoticandt h e r e f o r eh a sfi n i t es a m p l eb i a so rp r e s e n t i n gt h eR E M Lformulas—the intuition behind the source of the biasis often left unaddressed. This is not intended to reflectnegatively on these sources as explaining the underlyingm e c h a n i s mi sa d m i t t e d l yn o tt h e i rf o c u s .C u r r e n t l y ,i fresearchers wish to understand the root cause of smalls a m p l ei s s u e s ,t h e ym u s tg od e e pi n t ot h em a t h e m a t i c a lstatistics literature where equations and Greek notationoutnumbers English text. Again, this is not a criticism as
mathematicsisthelanguageofnewlyproposedstatisticalmethods. However, a treatment of the tenets of smallsample issues that are accessible to empirical researchersencounteringtheseissuesanddecidingonhowtohandlethem has not yet appeared in the literature. Explainingthismechanismisthefocusofthecurrentmanuscript.
To outline the remainder of this manuscript, we first
i n t r o d u c eM L M sa n dt h eb a s i cn o t a t i o nt h a tw eu s e .W ea s s u m et h a tr e a d e r sh a v es o m eb a s e l i n ef a m i l i a r i t yw i t hMLMs and why they are used. We transition to standardfullMLforMLMsandexplainwhyissuesarisewithsmallLevel-2 sample sizes. Then, we show how REML differsfromMLandwhyREMLislesssusceptibletosmallLevel-2samplesizes.W econtinuebynotingthatREMLdoesnotcompletely solve problems when the Level-2 sample sizei ss m a l la n dw ed i s c u s st h el o g i co ft h eK e n w a r d - R o g e rcorrection and its antecedent from Kackar and Harville(1984). An example analysis is provided to demonstrate
how each successive small sample method reduces the
reliance on asymptotic assumptions and, in the pro-cess,improvesestimationandinferenceforsmallsampleanalyses.
Overviewofmultilevelmodels
ThoughweassumesomefamiliaritywithMLMs,theyareextensivelyusedacrossawidespanofdisciplines,somanydifferent sets of notation and terminology exist. In thispaper, we use the set provided by Raudenbush and Bryk(2002)t h a ti sc o m m o ni np s y c h o l o g ya n de d u c a t i o n .T o
clarify this notation, an MLM for a continuous outcomevariableandonepredictorateachlevelinthisnotationiswrittenas
Y
ij=β0j+β1jX1ij+rij
β0j=γ00+γ01W1j+u0j
β1j=γ10+γ11W1j+u1j(1)
whererYijis the outcome variable for the ith person in the
jthcluster;rβ0jisthecluster-specificinterceptforthe jthcluster;rβ1jisthecluster -specificslopeforthe jthcluster;rX1ijistheLevel-1predictorvariablevalueforthe ith
personinthe jthcluster;rrijistheLevel-1residualforthe ithpersoninthe jth
cluster;rγ00isthefixedeffectfortheintercept;rW1jistheLevel-2predictorvariablevalueforthe jth
cluster;rγ01isthefixedeffectcoefficientfortheeffectof W1j
onβ0j;rγ10isthefixedeffectfortheslopeof X1ij;

---


<!-- Chunk 4 -->

MULTIVARIATEBEHAVIORALRESEARCH 663
rγ11isthefixedeffectcoefficientfortheeffectof W1j
onβ1j;ru0jis the random effect for the intercept for the jth
cluster;ru1jis the random effect for the slope for the jth
cluster.
ThegeneralideaofanMLMisthatthereisaregression
line for the entire sample comprised by estimates of thefixed effects ( γ
00andγ10in Equation [ 1]) but that each
cluster has a unique regression line. The random effects(theuterms) capture the difference between aspects of
the cluster-specific intercept and slopes and the overallregressionlineformedbythefixedeffects.Forthisreason,t h er a n d o me ff e c tt e r m s uare sometimes called “Level-2
r e s i d u a l s . ”T h o u g hn o ts h o w ne x p l i c i t l yi nE q u a t i o n( 1),
am a i ni n t e r e s to fM L M si si na s se s s i n gh o wv a r i a b l et h ecluster-specific regression lines are (i.e., what is the vari-ance of the uparameters across clusters around the fixed
effects). These are referred to as variance components;
for the model in Equation ( 1), the variance components
would be written as u∼MVN([
0
0],[τ00τ01
τ10τ11]).T h a ti s ,t h e
vectorofrandomeffects uhasamultivariatenormaldis-
tributionwithameanvectorof 0(because,acrossclusters,
t h eb e s tr e g r e s s i o nl i n ei sc a p t u r e db yt h efi x e de ff e c t s )and a covariance matrix comprising tau estimates. Thediagonalsofthetau-matrixarethevariancecomponents;t h eo ff - d i a g o n a l sa r et h ec o v a r i a n c ec o m p o n e n t st h a tcapture the relation between the random intercept and
the random slope (e.g., a positive covariance indicates
that clusters with higher cluster-specific intercepts alsotend to have higher cluster-specific slopes). Level-2 pre-dictor variables can be included in the model to explainwhy cluster-specific regression lines are different fromthefixedeffectregressionline.
Maximumlikelihoodandassociatedproblems
When estimating an MLM with ML, variance compo-nents and fixed effects are estimated simultaneously.Estimating the parameters in this simultaneous fashionraises an important issue—namely that the variancecomponentsandthefixedeffects,toadegree,aredepen-dent upon one another. The variance components assessthe amount of variation in the cluster-specific regres-sion lines. To assess variation, it is necessary to have alocation around which observations vary. Consider thebasic formula for calculating the variance of a single
variableX,Var(X)=[σ(X
i−¯X)2]/N.I nt h i sf o r m u l a ,
the reference location is the mean such that the varianceis the average squared deviation of each observed valueofX(noted by the isubscript) from the mean. In an
MLM,thereferencelocationforavariancecomponentisthe respective fixed effect. However, the fixed effects areunknown aprioriandmustbeestimatedsothatthevari-
ance components can be calculated. Otherwise, it wouldnot be known around what the cluster-specific lines arevarying.
When estimating an MLM with ML, this dependency
of the parameters means that a closed-form solution isnot typically possible and iterative approaches such asthe Expectation-Maximization (EM) algorithm or itera-tivegeneralizedleastsquaresarenecessary(e.g.,Rauden-bush & Bryk, 2002,p .5 2 ) .T h ep r o c e s si si t e r a t i v es u c h
that the fixed effects are estimated initially, with the ran-dom effect being considered missing for all observationsin the EM algorithm, for example. The variance compo-nents are then estimated based on the fixed effect valuesin the first iteration and these variance components arethen used to update the fixed effect estimates in the nextiteration. The process continues until there is essentiallyno changebetween the iterations. Thus, even though theprocessisiterativeinnature,thefixedeffectsandvariance
components are estimated within the same algorithm in
sequentialsteps.
Byfirstestimatingthefixedeffects,theseestimatesend
u pbeingtr ea tedaskno wnwhencalcula tingthevariancecomponentsbecausethereferencepointinvariancecom-putationsisafixedpoint.Thisisproblematicfortworea-sons. First, all the variability in the fixed effect estimatesis ignored. Second, the degrees of freedom consumed toestimate the fixed effects is not accounted for. In largersamples,theseissuesdonothavemuchofaneffect:sam-plingvariabilityoffixedeffectsdecreaseswithsamplesizeand changes in degrees of freedom above about 50 haveonlytrivialeffects.However,insmallersamples,samplingvariability of fixed effects tends to be larger and smallchangesindegreesoffreedomhaveanoticeableimpact.
Asasimpleanalogy,consideragainthesimplevariance
formula for a single variable. Readers may have notedthat we presented the population version of this formulawithNinthedenominatorratherthanthesampleversion
withN−1. The sample version of the variance formula
reduces the denominator by 1 as a penalty for needing
to estimate the sample mean in the numerator. With
asymptotically large samples, the two formulas will yieldessentially equal results. However, with smaller samples,the population formula will yield estimates that are toosmall because the population formula overestimates theprecision in the data and does not account for the factthatthesamplemeanisestimatedandnotknown.
In the variance formula analogy, ML is related to the
population variance in that it does not account for thefact that fixed effects need to be estimated when esti-mating the variance components. Just like the popula-tion variance formula, the ML variance components areunderestimatedwithsmallersamples(Browne&Draper,

---


<!-- Chunk 5 -->

664 D.MCNEISH
2006; McNeish, 2016). In MLMs, this is an issue because
thevariancecomponentsareprominentlyfeaturedintheformula for calculating the standard errors for the fixedeffects(e.g.,Raudenbush&Bryk, 2002).Therefore,ifthe
variance components are too small, the standard errorsfor the fixed effects will also be too small. If the stan-darderrorestimateistoosmall,theinferential torZtest
statisticwillbetoolargemeaningthat p-valueswillbetoo
small.ThisendsupinflatingtheType-Ierrorratesforthefixed effects. Thus, estimating the fixed effects and vari-ance components simultaneously in ML leads to issueswhentheLevel-2samplesizeissmallwiththeresultbeingunderestimatedvariancecomponentsandinflatedType-Ierrorrates.
Restrictedmaximumlikelihood
REML isthe“ N−1” version of ML and has been known
to perform better than ML when the Level-2 samplesize is small (Browne & Draper, 2006;M a a s&H o x ,
2005; McNeish & Stapleton, 2016b). As mentioned in
the previous section, many of the issues that ML pos-sesses with small Level-2 sample sizes stem from thefact that fixed effects and variance components are esti-mated simultaneously (albeit in iterative steps). REMLaddresses this issue by separating the estimation of thefixedeffectsfromthevariancecomponents.Thisleadstoimprovedestimatesofvariancecomponentswithsmallersamples which, in turn, can improve the fixed effectsstandard error estimates. REML has the added benefito fb e i n ga s y m p t o t i c a l l ye q u i v a l e n tt oM La n di ti sn o t
computationallyintensiveaboveandbeyondML.
To demonstrate how REML separates the fixed effect
fromthevariance componentsintheestimationprocess,imagine a research question revolving around modelingMath Scores based on Hours Studied when students are
nested within classrooms. A model with no Level-2 pre-dictors and random effects for the intercept and slopewouldbewrittenoutas
MathScore
ij=β0j+β1jHoursStudied ij+rij
β0j=γ00+u0j
β1j=γ10+u1j(2)
T h efi r s ts t e po fR E M Li st oo b t a i nt h eo r d i n a r yl e a s t
square (OLS) residuals via a single-level model, ignoringclustering.
2Using the Math Score example,
MathScore i=β0+β1HoursStudied i+ei(3)
Technically, when implemented in software, this step is conducted with an
errorcontrastoftheoutcomevariableandtheprojectionmatrixratherthan
actually ﬁtting a single-level model with OLS and saving the residuals. Theresultoftheprocesshasthesameeﬀect,sowedescribetheprocessusingOLS
toincreasetheintuitionoftheprocessandminimizetherelianceonmathe-
maticalterminology.
Figure .Comparison of the relation between the outcome and
thepredictor(toppanel)andbetweentheOLSresidualsandthe
predictor(bottompanel).
T h er e s i d u a l sf r o mt h eO L Sfi t( ei) are then saved.
By definition, the OLS residuals ( ei) are independent of
the predictor variables. This means that the correlationbetweeneandHoursStudied isnecessarily0.TheMLMis
then fit using ML with the OLS residuals as the outcome
ratherthantheoriginaloutcomevariable.Thismayseemodd, but there is a rationale. The OLS residuals serve asa linear transformation of the original data that now areindependent of the predictor variables ( Hours Studied
in this example) but have the same amount of variance(conditionalonthepredictors).
This is demonstrated in Figure 1using a hypothetical
s i m u l a t e dd a tase tf o rth i se x a m p l e .T h et o pp a n e ls h o w stherelationfortheoriginal MathScore outcomeon Hours
Studiedand the bottom panel shows the relation for the
OLS residuals and Hours Studied. When using the OLS
residuals,thefixedeffectsnolongerneedtobeestimatedb e c a u s et h e ya r ek n o w nt ob ez e r ob yd e fi n i t i o n( v i athe properties of OLS) as illustrated by the horizontalline in the bottom panel of Figure 1 (i.e., the mean of
the OLS residuals is 0 by definition and the correlation
between eandHours Studied is also 0 by definition).
This essentially has the effect of rotating the relation ofMathScoreand Hours Studied sothefixedeffectsforthe
intercept and slope are necessarily equal to 0. That is, ifFigure 1is rotated about 60 °clockwise, the points in the
top panel essentially map onto the points in the bottom

---


<!-- Chunk 6 -->

MULTIVARIATEBEHAVIORALRESEARCH 665
panel—thedatapointsareessentiallyinthesamelocation
and have the same amount of variability, conditional onHours Studied . In fact, the conditional variance remains
identical whether the outcome is the OLS residualsor the original outcome variable. So, REML estimatesthe variance components of a model with no fixedeffects (i.e., the fixed effects are constrained to 0), whichserves simply to partition the variance into Level-1 andLevel-2 components—there is no simultaneous estima-tion because the focus of the first stage of REML liessolely on the variance components. Because REML doesn o th a v et od e a lw i t hi s s u e sr e l a t e dt os i m u l t a n e o u sestimation,thevariancecomponentestimatesare(appro-priately) higher than those estimated by ML with smallsamples. When samples sizes are large, the REML andMLvariancecomponentswillessentiallybeequal.
The first stage of REML leaves the fixed effects out,
s ot h en e x tq u e s t i o nn a t u r a l l yi s :h o wd o e so n eg e tfi x e deffects estimates with REML? Once the variance compo-
nentsareestimated,REMLthenestimatesthefixedeffects
in the second stage through generalized least squares
( G L S ) .G L Si ss i m i l a rt oO L Si nt h a tt h efi x e de ff e c te s t i -mates are calculated with matrix multiplication withouttheneedforiterativemethods.UnlikeOLS,GLSiscapa-b leo facco un tin gf o rc l us t er edda ta.Th eGLSfix edeff ectestimates are identical, on average, to ML estimates pro-videdthatthecovariancestructureofobservationswithinclustersisknown(e.g.,Goldstein, 1986).Thatis,GLSdoes
notestimatevariancecomponentsbutratherrequiresthatresearchers know these values ahead of time. In REML,t h ev a r i a n c ec o m p o n e n t sa r ee s t i m a t e dfi r s t ,s ot h eL e v e l - 1a n dL e v e l - 2v a r i a n c ec o m p o n e n te s t i m a t e sf r o mt h efi r s ts t a g ea r eu s e dt oc o m p o s et h ec o v a r i a n c es t r u c -ture for GLS.
3That is, rather than knowing the variance
c o m p o n e n t sa h e a do ft i m e ,t h eR E M Lv a r i a n c ec o m p o -nents are substituted into the GLS estimating equationas if they were known ahead of time and the GLS esti-matesareusedforthefixedeffects.Thus,REMLachievesimproved estimates of the variance components by sep-arating the estimation and also yields nearly equivalent
fixedeffectestimatesasML.
4Figure2conceptuallyshows
the difference between how ML and REML iterate to asolution.
In MLMs, the total variance Vis equal to V=ZτZT+Rwhere τis the
covariancematrixoftheLevel-randomeﬀects, Zistherandomeﬀectdesign
matrix,and RisthecovariancematrixoftheLevel-residuals.UsingtheREML
estimates of τandRto compute V,t h eG L Sﬁ x e de ﬀ e ct sa r ec o m p u t e db y
(XTV−1X)−1XTV−1ywhereXis the ﬁxed eﬀect design matrix and yis a
vectoroftheoutcomevariablevalues.Theadditionofthe Vtermaccounts
forthedependenceofobservationswithinclusterswhichisignoredbyOLS.TheOLSﬁxedeﬀectestimatesarecalculatedby (X
TX)−1XTy.
TheGLSandMLestimatesareequalonaveragebutarenotperfectlyidenti-
cal.Thatis,inthelongrun,GLSandMLareexpectedtoyieldthesamevalues
buttheremaybesmalldiﬀerenceswhenestimatesarecomparedforasingle
dataset.
Figure . Comparison of iterative process between ML (top) and
REML (bottom). ML uses simultaneous estimation and bounces
betweenﬁxedeﬀectsandvariancecomponentsuntilconvergenceis met. REML iterates to estimate the variance components until
convergence,thenestimatestheﬁxedeﬀectsastheﬁnalstepwith
GLS.
Fixedeffectstandarderrors
Though the use of REML improves fixed effect standard
error estimates because the variance components aremore accurately estimated, standard error estimates con-tinuetobeproblematicwithsmallerLevel-2samplesizes,even with REML. The issues related to standard errorestimationwithsmallLevel-2samplesizesstemfromthefrequentist definition of the standard error itself ratherthantheestimationissuesused.
Frequentist inferential p-values essentially ask, if the
studywereconductedinfinitelymanytimesbyrepeatedlydrawingrandomsamplesofidenticalsizefromthetargetpopulation,whatistheprobabilitythatonewouldobtainthe estimated value of the coefficient if the population
value were 0? In order to be able to discern information
a b o u tp r o b a b i l i t i e s ,i ti si m p o r t a n tt ok n o wt h e sampling
distribution of the estimates. However, because studies
are only conducted once, the distribution is unknown asresearchers end up with only a single estimate that theywanttocompareto0inthepopulation.
So then, how are p-values calculated? Using mathe-
maticsandbyrelyingonasymptotics,itcanbeshownviathecentral limit theorem that the sampling distribution
approaches a normal distribution asymptotically. Thenull sampling distribution should be centered around 0,but,tocalculateprobabilities,thevarianceofthedistribu-t i o ni sn e e d e d .F o r t u n a t e l y ,a g a i nu s i n ga s y m p t o t i c sa n dmathematics,itcanbeshownthat Fisherinformation can
approximate the variance of the sampling distribution,providedthatitissufficientlynormal.Fisherinformationis taken from the inverse of the Hessian matrix of thelikelihood function where the Hessian matrix consists ofthe second partial derivatives of the likelihood functionwith respect to each parameter in the model. Essentially,t h ec u r v a t u r eo ft h el i k e l i h o o df u n c t i o na tt h eM Le s t i -
mate is used to inform the variability of the sampling
d i s t r i b u t i o n .T h a ti s ,i ft h ec u r v a t u r eo ft h el i k e l i h o o dfunction is very sharp at the ML estimates, then changestotheparameterestimatesinanydirectiongreatlyreducethe likelihood, indicating that there is more certaintythat the ML estimates represent the best solution. If thecurvatureofthelikelihoodisgradualattheMLestimates,

---


<!-- Chunk 7 -->

666 D.MCNEISH
thenchangesin theparameterestimatesinanydirection
change the likelihood very little, indicating that thereare alternative solutions that are essentially as plausibleas the ML estimates. Put another way, if another samplewere taken, it would not be surprising to obtain differentML estimates when the likelihood curvature is gradual.ThesquarerootofthediagonalelementsofFisherinfor-mation provide standard error estimates with likelihoodestimation. Using asymptotics and advanced mathe-matics, the sampling distribution for parameters in themodel can be determined even from just a single sampleof data and properties of the likelihood function. For amore expansive and highly readable introduction to MLestimation, readers are referred to Chapter 3 of Enders(2010).
However, note that the previous paragraph used the
word “asymptotic” on a number of occasions. This isbecause these relations only hold when the sample sizeapproachesinfinityorisotherwisesufficientlylarge.Inthe
contextofclustereddatawithsmallLevel-2samplesizes,
this condition is highly unlikely to be met. In fact, withsmaller samples, the central limit theorem often fails totakeeffect,whichmakestheshapeofthesamplingdistri-butionmoreambiguous(vandeSchootetal., 2014).Fur-
thermore,Fisherinformationisagoodapproximationofthe sampling variability asymptotically, but the approxi-mationismuchpoorerwithsmallersamples,oftenbeingunderestimated(Efron&Hinkley, 1978).
Thus, with smaller samples, the statistical machin-
ery upon which frequentist inference is based breaksdown and p- v a l u e sa r en ol o n g e rt r u s t w o r t h ya sT y p e -
I error rates become highly inflated. Though somerecent studies use failings of the frequentist statisti-cal machinery as motivation to explore Bayesian meth-o d sw i t hs m a l l e rs a m p l e s( e . g . ,M u t h é n&A s p a r o u h o v ,2012;v a nd eS c h o o t ,B r o e r e ,P e r r y c k ,Z o n d e r v a n -
Zwijnenburg,&vanLoey, 2015),therearefrequentistcor-
rections that are also available that preclude researchersfrom necessarily having to resort to a Bayesian frame-work.McNeish( 2016)arguedthattheuseofthesesmall-
sample-corrected frequentist methods can sometimes
be preferable to Bayesian methods with small samples,especially when researchers lack strongly informativepriors.
Smallsamplestandarderrorcorrections
Kackar-Harville
In the 1980s, statistical research attempted to determine
the effect that violating asymptotic assumptions had onstandard error estimates. Kackar and Harville ( 1984)
posed the general conceptualization of the problem as(takenfromEquation[2.1]intheoriginalpaper),
Var(γ )=Var
REML(ˆγ)+SmallSampleBias (4)
or, in English, that the sampling variability of the fixed
effects is equal to the REML-estimated sampling vari-ability estimate plus some amount of small sample biasincurredbyviolatingasymptoticassumptions.ItisknownthatVar
REML(ˆγ)<Var(γ )with smaller samples, so the
“Small Sample Bias” term is a corrective inflation factor.Thus, the goal of this line of research was to discern amathematical function for the “Small Sample Bias” por-t i o no ft h ef u n c t i o ns ot h a tp r o p e rs t a n d a r de r r o re s t i -matescouldbeobtainedwithsmallersamples.
The mathematical details are intense to say the least
as this mechanism is quite complex; however, the basicfinding is that the Small Sample Bias portion doeshave a mathematical form but it requires that one havethe population values for the variance components (see,theleft-handcolumnofp.854inKackar&Harville, 1984
for full details). To work around this issue Kackar andHarville ( 1984)u seaTaylor series expansion whosebasic
premise is to approximate a complex nonlinear function(with potentially unknown values) with a simpler poly-
nomialfunction(consistingsolelyofknownvalues).The
function to represent the Small Sample Bias portion ofEquation( 4)isonesuchcomplexnonlinearfunction,and
Kackar and Harville ( 1984)d i s c u s st h a ti t sc o m p u t a t i o n
is infeasible without population values (p. 854) but itcan be approximated as a function of model estimates(Kackar&Harville, 1984,Equation[2.2]orEquation[ 1]
inKenward&Roger, 1997).
To elucidate the idea of Taylor series expansion in a
simplercontext,takethenonlinearfunction y=e
xwhere
eis base of the natural logarithm ( /22482.718). Perhaps the
value of eis unknown (like the population values in
aM L M )b u tt h a t xis known (like estimated values in
a MLM). Though we will not show the mathematics,a (second-order) Taylor series expansion of y=e
xis
y=1+x+x2
2+x3
6:n o ti c eth a tth eT a yl o rse ri e se x pa n -
sion is polynomial function only of xand that eis not
featured in the function. Figure 3compares the original
functiony=exinblackwiththeTaylorseriesexpansion
y=1+x+x2
2+x3
6ingray.Noticethatthetwofunctions
a r ea l m o s to nt o po fo n ea n o t h e r ,s h o w i n gt h a t y=ex
can be approximated solely by a polynomial function
ofx.
The Kackar-Harville correction works much in the
same way except that the original function (the equiv-alent of “ e”inFigure 3) is more complex and in mul-
tivariate space, while the equivalent of the “ x”input is
a vector of variance components estimates and their

---


<!-- Chunk 8 -->

MULTIVARIATEBEHAVIORALRESEARCH 667
Figure . Comparison of y=ex(black) and the Taylor series
expansion(gray).
REML-estimated covariance matrix.5The original idea
of Kackar and Harville ( 1984) has been refined and
extended by Prasad and Rao ( 1990)a n dH a r v i l l ea n d
Jeske(1992),sothecorrectionissometimesreferredtoas
the Prasad-Rao-Jeske-Kackar-Harville correction. Thisis how the correction is listed in the SAS software, forinstance, and this is how we refer to the correction inlatersectionsintheinterestoftechnicalaccuracy.
Kenward-Roger
Kenward and Roger ( 1997)u s e sK a c k a ra n dH a r v i l l e
(1984)a sas t a r t i n gp o i n tb u tn o t et h e Var
REML(ˆγ)term
in Equation ( 4) similarly has issues. Namely, REML uses
GLS to estimate the fixed effects after the variance com-ponentsareestimated.However,thevariancecomponentestimates are not known and have some associated sam-pling variability, which is not accounted for because theestimates ofthevariancecomponentsaresubstitutedinto
the GLS estimating equation where values are assumedto be known. This is the same issue that arises withint h e“ S m a l lS a m p l eB i a s ”a p p r o x i m a t i o no fK a c k a ra n dHarville ( 1984)inEquation( 4).
Therefore, in addition to the expansions in the
Prasad-Rao-Jeske-Kackar-Harville family of corrections,KenwardandRoger( 1997)performasecondTaylorseries
expansionto Var
REML(ˆγ)toaccountforthefactthatvari-
ancecomponentsareestimatedandnotknownwhenesti-matingfixedeffectsandtheirstandarderrorswithREML(Equation [ 2] in Kenward & Roger, 1997). These two
expansions together form the first step of the Kenward-Roger correction and provide more accurate fixed effectstandard error estimates that are robust to violations ofasymptotic assumptions (see Equation [ 3] in Kenward &
Roger,1997forthefullformulaicformofthecorrection).
ThefullmathematicalexpressioninEquation ismuchmorecomplexthan
thefunction y=exusedinFigure ,sow edonotwisht oimplytha tthea
TaylorseriesexpansionofEquation willnecessarilyresultintheremarkably
close approximation seen in Figure . The example in Figure was chosen
becauseitisatextbookexampleofhowaTaylorseriesexpansionoperates.
Asaresult,theTaylorseriesexpansionhappenstobequitegood.With smaller samples, inference should be conducted
witht-statistics rather than Z-statistics as with any other
statistical model.6t-statistics take the ratio of the esti-
matedvaluetoitsstandarderror( t=ˆγ/SEˆγ),sothefirst
step of the Kenward-Roger correction ensures that thet-statistic is calculated accurately—Kackar and Harville
(1981) show that the fixed effect point estimates, ˆγ,a r e
estimatedwithoutbiasinsmallsamplesandtheKenward-Roger correction ensures that SE
ˆγis estimated without
small sample bias. Therefore, t-statistics should be accu-
rate after employing appropriate corrections. To ensureproperp-valueswithsmallersamples,accurate t-statistics
a r en o ts u ffi c i e n t ,h o w e v e r .A d d i t i o n a l l y ,o n em u s th a v eaccuratedegreesoffreedom.Withsmallsamples,changesin degrees of freedom can lead to notable differences inp- v a l u e sb e c a u s et h ew e i g h to ft h et a i l so ft h en u l l t-
distribution will change. In MLMs, degrees of freedoma r en o t o r i o u s l yd i ffi c u l tt oc a l c u l a t ed u et ot h es a m -ple sizes at multiple levels and no fixed formulas exist
except for the most ideal situations (Schallje, McBride,
& Fellingham, 2002). Software defaults for calculatingdegreesoffreedomforfixedeffectsvaryfromprogramtoprogram
7andtypicallyrelyonapproximationsthattend
to perform undesirably with smaller samples (Keselman,Algina, Kowalchuk, & Wolfinger, 1999). Therefore, to
obtain more accurate p-values for inferential purposes,
t h es e c o n ds t e po ft h eK e n w a r d - R o g e rc o r r e c t i o ni st oapproximate the degrees of freedom with a method ofmomentsmatchingprocedure,aprocedurethatisessen-tially a scaled version of the Satterthwaite ( 1946)p r o c e -
dure. This procedure often results in fractional degreesoffreedominordertogivethemostpreciseresults.
Insummary,thegoaloftheKenward-Rogercorrection
istofirstcorrectthefixedeffectstandarderrorestimatesin order to reduce the reliance on asymptotics. Thisr e s u l t si ns t a n d a r de r r o re s t i m a t e st h a ta r el a r g e rt h a nthe asymptotic REML estimates. The first step leads tomore accurate t-statistics, but degrees of freedom are
still problematic. The second step of Kenward-Rogertherefore provides an alternative procedure for degree of
freedomcalculationinordertorefine p-valuestoimprove
inferentialdecisions.NotethatEquation( 4)r elieso nthe
REML estimate of the fixed effect sampling variability.Althoughtraditionaldegreeoffreedommethodssuchascontainment, between-within, or residual are available
Werefertounivariatetestshere,suchastestingasinglecoeﬃcient.Ifmul-
tiparameter tests are desired, the statement should be revised to say that
researchersshoulduse Ftestsratherthan χtestsbecausethe Fdistribution
is a ﬁnite sample version of the χdistribution (i.e., an Fdistribution with
inﬁnitedenominatordegreesoffreedomisequaltoa χdistributionifthe
numerator Fdegreesoffreedommatchthe χdegreesoffreedom).
Some software programs such as Stata and M plusreportZ-tests for ﬁxed
eﬀects which assume inﬁnitely large samples and therefore do not have
degreesoffreedom.Withsmallersamples, Z-testsarenotappropriate,gen-
erallyspeaking.

---


<!-- Chunk 9 -->

668 D.MCNEISH
with ML or REML estimation, the derivations of the
Kenward-Roger correction (and its antecedents) relyon REML estimation. That is, the Kenward-Roger is notapplicabletomodelsestimatedwithML.IfMLestimationis attempted along with a Kenward-Roger correction insoftwaresuchasSASPROCMIXED,anerrormessageisreturned.
Empirical example
To demonstrate the effect that different estimation and
c o r r e c t i o nm e t h o d sh a v eo nM L M sw i t hs m a l lL e v e l - 2samplesizes,considerdatapresentedinStapleton,Pituch,and Dion ( 2015). The data come from a cluster ran-
domized trial (a common source of small Level-2 sam-ple sizes) interested in whether a new socioemotionalcurriculum affects behavior for children at Head Start
sites(higherbehavior scoresindicatebetterbehavedstu-
dents). The data feature 14 sites (7 in the treatment con-dition, 7 in the control condition) each with 6 students(84studentstotal;Level-2samplesizeis14).Eachchild’sSocioemotional Knowledge is included as a Level-1 pre-
dictor and is group-mean centered. Level-2 predictorsincludetreatmentgroupstatus(variablelabel: Treatment )
andthesiteaveragefor SocioemotionalKnowledge (i.e.,the
model uses a between-within specification; Bell & Jones,2015). Random effects are included for the intercept and
Level-1slope.Themodelcanbewrittenas
Behavior
ij=β0j+β1j(SEKij−SEKj)+rij
β0j=γ00+γ01Treatj+γ02SEKj+u0j
β1j=γ10+u1j (5a)
u∼MVN/parenleftbigg/bracketleftbigg0
0/bracketrightbigg
,/bracketleftbiggτ00τ10
τ01τ11/bracketrightbigg/parenrightbigg
(5b)
T h em o d e li sfi tfi v ed i ff e r e n tw a y sw i t he a c hr e l y i n g
on asymptotic assumptions to varying degrees. The fivemethods are (in order of decreasing reliance on asymp-toticassumptions):
1. ML with inferential Z-tests, asymptotic standard
errors;
2. MLwithinferential ttests,containmentdegreesof
freedom,andasymptoticstandarderrors;
3. REMLwithinferential ttests,containmentdegrees
offreedom,andasymptoticstandarderrors;
4. REMLwithinferential ttests,containmentdegrees
offreedomandPrasad-Rao-Jeske-Kackar-Harvillestandarderrors
8;
The Prasad-Rao-Jeske-Kackar-Harville is not available as a formal option in
SAS though the relevant information can be pieced together. Using the
DDFM=KR(FIRSTORDER) option in the MODEL statement uses the Prasad-
Rao-Jeske-Kackar-Harville method for the standard error correction rather5. REML with inferential ttests, Kenward-Roger
degreesoffreedom,andKenward-Rogerstandarderrors.
All models are estimated in SAS 9.3 using PROC
MIXED. Containment degrees of freedom were selectedfor Model 1 through Model 4 because this is the SASdefaultforthemodel.
9
Table 1shows the estimates for the fixed effect coeffi-
cients,fixedeffect p-values,andvariancecomponentesti-
mates. Of particular note, focus on how the p-value for
the treatment effect changes across the table from left tori gh t( a n d ,t oal e s se re x t e n t , Socioemotional Knowledge ).
Using all asymptotic methods in Model 1, Treatment is
significant where p=.019. Changing the inferential test
fromaZ-testtoat-testwithcontainmentdegreesoffree-
dominModel2,the p-valueincreasesslightlyto p=.022.
If the estimation method is changed from ML to REMLin Model 3, Treatment is now on the border of signifi-
cance because REML variance components have (appro-
priately) inflated the variance component estimates (the
interceptvarianceincreasesfrom2.57to3.78,anincreaseof about 35%). When using Prasad-Rao-Jeske-Kackar-Harville standard errors (with containment degrees offreedom)ratherthanasymptoticstandarderrorsinModel4,Treatment isnonsignificantwith p=.068.Finally,using
theKenward-Rogercorrectionwithassociateddegreesoffreedom(relyingonnoasymptoticinformation)inModel5,Treatment has ap-value of .106. As can be seen, even
thoughthecoefficientestimatesareaboutequalacrossallfive methods, the inferential interpretation of the resultsvaries widely depending how strongly one (inappropri-ately)reliesonasymptoticassumptions.
Discussionandconcludingremarks
Though many resources exist to elucidate whenREML
and Kenward-Roger should be employed and when ML
than the Kenward-Roger correction. The output still contains the Kenward-
Rogerdegreesoffreedom,sowemanuallycalculatedthe p-valuesusingthe
containmentdegreesoffreedom.
Containmentdegreesoffreedomarecalculatedby N−rank(X,Z)where
Nistheoverallsamplesize, Xisadesignmatrixfortheﬁxedeﬀectsand Zisa
designmatrixfortherandomeﬀects.Inlinearalgebra,therankofamatrixis
thedimensionofthevectorspacespannedbythecolumns.Thecomputation
canbesimpliﬁedwitharandominterceptsmodelforbalanceddata(asisthecaseintheStapletonetal.data).Foraﬁxedeﬀectthatdoesnothavearan-
dom eﬀect, thecontainment degrees of freedom are equal to ( totalsample
size)minus(numberofpredictors )minus(numberofclustersminusLevel-pre-
dictors).Thismodelhastotalpeople,predictors,clusters,andLevel-
predictors,sothecontainmentdegreesoffreedomforanonvaryingﬁxed
eﬀect is84−3−(14−2)=69. For eﬀects that do have random eﬀects
(the intercept in this model), the containment degrees of freedom is equalto(numberofclusters )minus(numberofLevel-randomeﬀects )minus(num-
berofLevel-predictors ).In thisdata,there are  clusters,  Level-random
eﬀect,andLevel-predictors,sothedegreesoffreedomfortheinterceptis
14−1−2=11.Theseformulasarenotasstraightforwardforunbalanced
dataormodelswithrandomslopesbecausetheoutputfromtherankopera-torwillbedependentonaspectslikethedegreeofunbalancednessandthe
randomeﬀectcovariancestructure.

---


<!-- Chunk 10 -->

MULTIVARIATEBEHAVIORALRESEARCH 669
Table .Comparisonofestimatesusingmethodsthatdiﬀerbytheirrelianceonasymptoticassumptions.
ML,Z ML,t REML PRJKH KR
Est p Est p Est p Est p Est p
Treatment . . . . . . . . . .
SEK . <. . . . . . . . .
Level-SEK −. . −. . −. . −. . −. .
Var(Int) . . . . .
Var(SEK) . . . . .Cov(I,S) −. −. −. −. −.
Note:SEK,socioemotionalknowledge;ML,maximumlikelihood;Z,inferenceconductedwith Z-test;t,inferenceconductedwith t-test;REML,restrictedmaximum
likelihood;PRJKH,REMLwithPrasad-Rao-Jeske-Kackar-Harvillecorrectiontostandarderrorestimates;KR,REMLwithKenward-Rogercorrectiont ostandarderror
estimatesanddegreesoffreedombasedonascaledmethodofmoments.
should be avoided with multilevel models, there are far
fewer resources to elucidate whatthese methods do and
howthey improve model estimates and inferences for
multilevel models with smaller samples. We hope thispaperhelpstoprovidesomeinsightastowhatthesemeth-odsaredoingtocircumventsmallsampleissues.
ItisimportanttonoteoneprimarydrawbackofREML
whichliesinmodelcomparisons.BecauseREMLremovest h efi x e de ff e c t sf r o mt h ee s t i m a t i o n ,R E M Lu s e st h erestricted likelihood function that does not contain anyinformationaboutthefixedeffects(Raudenbush&Bryk,2002). Therefore, if comparing the fit of different mod-
elsusingREML,thefixedeffectsmustbeidenticalforthecomparisons of the restricted likelihood to be meaning-ful.Otherwise,MLmustbeusedformodelcomparisonsbecause the full likelihood includes information about
boththefixedeffectsandthevariancecomponents.After
competing models are compared using full ML, the finalmodel can be estimated with REML (and associated cor-rections, if necessary) to protect against bias in variancecomponentestimatesandinflatedType-Ierrorrates.
I nt e r m so fs o f t w a r ei m p l e m e n t a t i o n ,t h e r ea r es o m e
importantdifferencesthatmakesomesoftwareprogramsmore or less attractive for modeling multilevel data withsmall Level-2 sample sizes. SAS PROC MIXED and SASPROC GLIMMIX have included the Kenward-Roger forsometimeanditisquiteeasytoimplementthecorrection:oneonlyneedstospecifyDDFM =KRasanoptioninthe
MODEL statement. SAS also offers the Kenward-Roger2 correction via the DDFM =KR2 option. However,
this version of the correction is only required when thecovariance structure contains nonlinearities (Kenward& Roger, 2009) which is not commonplace in behavioral
science research. Stata uses asymptotic Z-tests by default
but beginning in version 14 (released April 2015) Statanow allows users to implement Kenward-Roger with theoption dfmethod(kroger) in the mixed procedure. The
pbkrtest R package does allow for Kenward-Roger to
be implemented but does so for model comparisonsratherthanfortheresultsofasinglemodel.SPSS does not allow users to implement Kenward-
Roger, but it does allow for the Satterthwaite degreesof freedom to be used with t-statistics for testing fixed
effects.TheSatterthwaiteproceduredoesnotincludethestandarderrorcorrectionfromeitherKackarandHarville(1984) or Kenward and Roger ( 1997), but it does pro-
videadegreeoffreedomadjustmentsimilartothesecondstepoftheKenward-Rogercorrection.TheHLMsoftwareusest-sta tisticstotestfixedeffectsbutdoesnotcurren tly
offer Kenward-Roger as of this writing. Finally, frequen-tistestimationinM plusofferslittleassistanceforhandling
small sample issues. REML is not available as an estima-tionmethod,therearenoavailablesmallsamplestandarderrorcorrections,andalleffectsaretestedwith Z-statistics
with no option to elicit t-statistics instead. On the other
hand, to their credit, M plusdoes have a user-friendly
interface for using Bayesian methods which can be use-
fulwithsmallersamples(e.g.,vandeSchootetal., 2015).
ResearchersshouldnotethattheM plusdefaultpriordis-
tributions in the Bayes module can produce some issueswith small sample analyses and they should be changedprior to running a small sample analysis (McNeish,2016).
Articleinformation
ConflictofInterestDisclosures : The author signed a form for
disclosure of potential conflicts of interest. The author did not
report any financial or other conflicts of interest in relation to
theworkdescribed.
Ethical Principles : The author affirms having followed pro-
fessional ethical guidelines in preparing this work. These
guidelines include obtaining informed consent from human
participants, maintaining ethical treatment and respect forthe rights of human or animal participants, and ensuring the
privacy of participants and their data, such as ensuring that
individual participants cannot be identified in reported resultsorfrompubliclyavailableoriginalorarchivaldata.
Funding: This work was not supported by any external
funding.

---


<!-- Chunk 11 -->

670 D.MCNEISH
Role of the Funders/Sponsors: None of the funders or spon-
sors of this research had any role in the design and conduct of
thestudy;collection,management,analysis,andinterpretationof data; preparation, review, or approval of the manuscript; or
decisiontosubmitthemanuscriptforpublication.
Acknowledgments: TheauthorwouldliketothankDanBauer,
PatrickCurran,andDaveThissenfortheircommentsonpriorversions of this manuscript. The ideas and opinions expressed
herein are those of the authors alone, and endorsement by the
author’sinstitutionisnotintendedandshouldnotbeinferred.
References
Bell, A., & Jones, K. (2015). Explaining fixed effects: Random
effects modeling of time-series cross-sectional and panel
data.Political Science Research and Methods ,3, 133–153.
doi:10.1017/psrm.2014.7
B e l l ,B .A . ,M o r g a n ,G .B . ,S c h o e n e b e r g e r ,J .A . ,K r o m r e y ,
J.D.,&Ferron,J.M.(2014).Howlowcanyougo?. Method-
ology,10,1–11.doi: 10.1027/1614-2241/a000062
Browne, W. J., & Draper, D. (2006). A comparison of Bayesian
andlikelihood-basedmethodsforfittingmultilevelmodels.BayesianAnalysis ,1,473–514.doi: 10.1214/06-BA117
Efron, B., & Hinkley, D. V. (1978). Assessing the accu-
racy of the maximum likelihood estimator: Observed ver-sus expected Fisher information. Biometrika ,65, 457–482.
doi:10.1093/biomet/65.3.457
Enders, C. K. (2010). Applied missing data analysis .N e wY o r k :
GuilfordPress.
Ferron, J. M., Bell, B. A., Hess, M. R., Rendina-Gobioff, G., &
Hibbard, S. T. (2009). Making treatment effect inferences
frommultiple-baselinedata:Theutilityofmultilevelmod-
eling approaches. Behavior Research Methods ,41, 372–384.
doi:10.3758/BRM.41.2.372
Goldstein, H. (1986). Multilevel mixed linear model analysis
using iterative generalized least squares. Biometrika ,73,
43–56.doi: 10.1093/biomet/73.1.43
Harville, D. A., & Jeske, D. R. (1992). Mean squared error
of estimation or prediction under a general linear model.JournaloftheA mericanStatisticalAssociation ,87,724–731.
doi:10.1080/01621459.1992.10475274
Hox, J. J., van de Schoot, R., & Matthijsse, S. (2012, July). How
few countries will do? Comparative survey analysis from a
Bayesianperspective. SurveyResearchMethods ,6,87–93.
Huang, F. L. (2017). Using cluster bootstrapping to ana-
lyze nested data with a few clusters. Educational and
Psychological Measurement . Advance online publication.
doi:10.1177/0013164416678980 .
Kackar, R. N., & Harville, D. A. (1981). Unbiased-
ness of two-stage estimation and prediction proce-
dures for mixed linear models. Communications in
Statistics-Theory and Methods ,10, 1249–1261. doi:
10.1080/03610928108828108
Kackar, R. N., & Harville, D. A. (1984). Approximations for
standard errors of estimators of fixed and random effects
in mixed linear models. Journal of the American Statistical
Association ,79,853–862.doi: 10.2307/2288715
Kenward, M. G., & Roger, J. H. (2009). An improved approxi-
mationtotheprecisionoffixedeffectsfromrestrictedmax-imumlikelihood. ComputationalStatisticsandDataAnaly-
sis,53,2583–2595.doi:
10.1016/j.csda.2008.12.013
Kenward, M. G., & Roger, J. H. (1997). Small sample inference
for fixed effects from restricted maximum likelihood. Bio-
metrics,53,983–997.doi: 10.2307/2533558
Keselman, H. J., Algina, J., Kowalchuk, R. K., & Wolfinger,
R. D. (1999). The analysis of repeated measurements: A
comparison of mixed-model Satterthwaite F tests and
a nonpooled adjusted degrees of freedom multivariatetest.Communications in Statistics-Theory and Methods ,28,
2967–2999.doi: 10.1080/03610929908832460
Maas, C. J., & Hox, J. J. (2005). Sufficient sample sizes
for multilevel modeling. Methodology ,1, 86–92. doi:
10.1027/1614-2241.1.3.86
McNeish, D. (2016). On using Bayesian methods to address
small sample problems. Structural Equation Modeling ,23,
750–773.doi: 10.1080/10705511.2016.1186549
McNeish, D., & Stapleton, L. M. (2016a). Modeling clus-
tered data with very few clusters. Multivariate Behavioral
Research,51,495–518.doi: 10.1080/00273171.2016.1167008
McNeish, D., & Stapleton, L. M. (2016b). The effect of small
sample size on two-level model estimates: A review and
illustration. E d u c a t i o n a lP s y c h o l o g yR e v i e w ,28, 295–314.
doi:10.1007/s10648-014-9287-x
Muthén, B., & Asparouhov, T. (2012). Bayesian structural
equation modeling: a more flexible representation of
substantive theory. Psychological Methods ,17, 313–335.
doi:10.1037/a0026802
Prasad, N. G. N., & Rao, J. N. (1990). The estimation of
the mean squared error of small-area estimators. Jour-
nal of the American Statistical Association ,85, 163–171.
doi:10.1080/01621459.1990.10475320
Raudenbush, S. W., & Bryk, A. S. (2002). Hierarchical linear
models: Applications and data analysis methods .T h o u s a n d
Oaks,CA:Sage.
Satterthwaite,F.E.(1946).Anapproximatedistributionofesti-
m a t e so fv a r i a n c ec o m po n e n t s . Biometrics Bulletin ,2, 110–
114.doi:10.2307/3002019
Schaalje, G. B., McBride, J. B., & Fellingham, G. W. (2002).
Adequacy of approximations to distributions of test statis-
tics in complex mixed linear models. Journal of Agricul-
tural, Biological, and Environmental Statistics ,7, 512–524.
doi:10.1198/108571102726
Snijders,T.A.,&Bosker,R.J.(1993).Standarderrorsandsam-
plesizesfortwo-levelresearch. JournalofEducationalStatis-
tics,18,237–259.doi: 10.2307/1165134
Stapleton, L. M., Pituch, K. A., & Dion, E. (2015). Standard-
ized effect size measures for mediation analysis in cluster-
randomized trials. The Journal of Experimental Education ,
83,547–582.doi: 10.1080/00220973.2014.919569
van de Schoot, R., Broere, J. J., Perryck, K. H., Zondervan-
Zwijnenburg,M.,&vanLoey,N.E.(2015).Analyzingsmall
data sets using Bayesian estimation: the case of posttrau-matic stress symptoms following mechanical ventilation in
burn survivors. European Journal of Psychotraumatology ,6.
doi:10.3402/ejpt.v6.25216
v a nd eS c h o o t ,R . ,K a p l a n ,D . ,D e n i s s e n ,J . ,A s e n d o r p f ,J .B . ,
Neyer,F.J.,&Aken,M.A.(2014).Agentleintroductionto
Bayesian analysis: Applications to developmental research.
ChildDevelopment ,85,842–860.doi: 10.1111/cdev.12169

---


<!-- Chunk 12 -->



---
