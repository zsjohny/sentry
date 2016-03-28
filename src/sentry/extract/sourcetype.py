#coding:utf-8
import string 
import math
import random
import re
ignored_model_keywords = '''splunk sun mon tue tues wed thurs fri sat sunday monday tuesday wednesday thursday friday saturday jan feb mar apr may jun jul aug sep oct nov dec january february march april may june july august september october november december 2003 2004 2005 2006 2007 2008 2009 am pm ut utc gmt cet cest cetdst met mest metdst mez mesz eet eest eetdst wet west wetdst msk msd ist jst kst hkt ast adt est edt cst cdt mst mdt pst pdt cast cadt east eadt wast wadt aaron abbey abbie abby abdul abe abel abigail abraham abram adah adalberto adaline adam adan addie adela adelaida adelaide adele adelia adelina adeline adell adella adelle adena adina adria adrian adriana adriane adrianna adrianne adrien adriene adrienne afton agatha agnes agnus agripina agueda agustin agustina ahmad ahmed aida aide aiko aileen ailene aimee aisha aja akiko akilah al alaina alaine alan alana alane alanna alayna alba albert alberta albertha albertina albertine alberto albina alda alden aldo alease alec alecia aleen aleida aleisha alejandra alejandrina alejandro alena alene alesha aleshia alesia alessandra aleta aletha alethea alethia alex alexa alexander alexandra alexandria alexia alexis alfonso alfonzo alfred alfreda alfredia alfredo ali alia alica alice alicia alida alina aline alisa alise alisha alishia alisia alison alissa alita alix aliza alla allan alleen allegra allen allena allene allie alline allison allyn allyson alma almeda almeta alona alonso alonzo alpha alphonse alphonso alta altagracia altha althea alton alva alvaro alvera alverta alvin alvina alyce alycia alysa alyse alysha alysia alyson alyssa amada amado amal amalia amanda amber amberly ambrose amee amelia america ami amie amiee amina amira ammie amos amparo amy ana anabel analisa anamaria anastacia anastasia andera anderson andra andre andrea andreas andree andres andrew andria andy anette angel angela angele angelena angeles angelia angelic angelica angelika angelina angeline angelique angelita angella angelo angelyn angie angila angla angle anglea anh anibal anika anisa anisha anissa anita anitra anja anjanette anjelica ann anna annabel annabell annabelle annalee annalisa annamae annamaria annamarie anne anneliese annelle annemarie annett annetta annette annice annie annika annis annita annmarie anthony antione antionette antoine antoinette anton antone antonetta antonette antonia antonietta antonina antonio antony antwan anya apolonia april apryl ara araceli aracelis aracely arcelia archie ardath ardelia ardell ardella ardelle arden ardis ardith aretha argelia argentina ariana ariane arianna arianne arica arie ariel arielle arla arlean arleen arlen arlena arlene arletha arletta arlette arlie arlinda arline arlyne armand armanda armandina armando armida arminda arnetta arnette arnita arnold arnoldo arnulfo aron arron art arthur artie arturo arvilla asa asha ashanti ashely ashlea ashlee ashleigh ashley ashli ashlie ashly ashlyn ashton asia asley assunta astrid asuncion athena aubrey audie audra audrea audrey audria audrie audry august augusta augustina augustine augustus aundrea aurea aurelia aurelio aurora aurore austin autumn ava avelina avery avis avril awilda ayako ayana ayanna ayesha azalee azucena azzie babara babette bailey bambi bao barabara barb barbar barbara barbera barbie barbra bari barney barrett barrie barry bart barton basil basilia beata beatrice beatris beatriz beau beaulah bebe becki beckie becky bee belen belia belinda belkis bella belle belva ben benedict benita benito benjamin bennett bennie benny benton berenice berna bernadette bernadine bernard bernarda bernardina bernardine bernardo berneice bernetta bernice bernie berniece bernita berry bert berta bertha bertie bertram beryl bess bessie beth bethanie bethann bethany bethel betsey betsy bette bettie bettina betty bettyann bettye beula beulah bev beverlee beverley beverly bianca bibi billi billie billy billye birdie birgit blaine blair blake blanca blanch blanche blondell blossom blythe bo bob bobbi bobbie bobby bobbye bobette bok bong bonita bonnie bonny booker boris boyce boyd brad bradford bradley bradly brady brain branda brande brandee branden brandi brandie brandon brandy brant breana breann breanna breanne bree brenda brendan brendon brenna brent brenton bret brett brian briana brianna brianne brice bridget bridgett bridgette brigette brigid brigida brigitte brinda britany britney britni britt britta brittaney brittani brittanie brittany britteny brittney brittni brittny brock broderick bronwyn brook brooke brooks bruce bruna brunilda bruno bryan bryanna bryant bryce brynn bryon buddy buena buffy buford bula bulah bunny burl burma burt burton buster byron caitlin caitlyn calandra caleb calista callie calvin camelia camellia cameron cami camie camila camilla camille cammie cammy candace candance candelaria candi candice candida candie candis candra candy candyce caprice cara caren carey cari caridad carie carin carina carisa carissa carita carl carla carlee carleen carlena carlene carletta carley carli carlie carline carlita carlo carlos carlota carlotta carlton carly carlyn carma carman carmel carmela carmelia carmelina carmelita carmella carmelo carmen carmina carmine carmon carol carola carolann carole carolee carolin carolina caroline caroll carolyn carolyne carolynn caron caroyln carri carrie carrol carroll carry carson carter cary caryl carylon caryn casandra casey casie casimira cassandra cassaundra cassey cassi cassidy cassie cassondra cassy catalina catarina caterina catharine catherin catherina catherine cathern catheryn cathey cathi cathie cathleen cathrine cathryn cathy catina catrice catrina cayla cecelia cecil cecila cecile cecilia cecille cecily cedric cedrick celena celesta celeste celestina celestine celia celina celinda celine celsa ceola cesar chad chadwick chae chan chana chance chanda chandra chanel chanell chanelle chang chantal chantay chante chantel chantell chantelle chara charis charise charissa charisse charita charity charla charleen charlena charlene charles charlesetta charlette charley charlie charline charlott charlotte charlsie charlyn charmain charmaine charolette chas chase chasidy chasity chassidy chastity chau chauncey chaya chelsea chelsey chelsie cher chere cheree cherelle cheri cherie cherilyn cherise cherish cherly cherlyn cherri cherrie cherry cherryl chery cheryl cheryle cheryll chester chet cheyenne chi chia chieko chin ching chiquita chloe chong chris chrissy christa christal christeen christel christen christena christene christi christia christian christiana christiane christie christin christina christine christinia christoper christopher christy chrystal chu chun chung ciara cicely ciera cierra cinda cinderella cindi cindie cindy cinthia cira clair claire clara clare clarence claretha claretta claribel clarice clarinda clarine claris clarisa clarissa clarita clark classie claud claude claudette claudia claudie claudine claudio clay clayton clelia clemencia clement clemente clementina clementine clemmie cleo cleopatra cleora cleotilde cleta cletus cleveland cliff clifford clifton clint clinton clora clorinda clotilde clyde codi cody colby cole coleen coleman colene coletta colette colin colleen collen collene collette collin colton columbus concepcion conception concetta concha conchita connie conrad constance consuela consuelo contessa cora coral coralee coralie corazon cordelia cordell cordia cordie coreen corene coretta corey cori corie corina corine corinna corinne corliss cornelia cornelius cornell corrie corrin corrina corrine corrinne cortez cortney cory courtney coy craig creola cris criselda crissy crista cristal cristen cristi cristie cristin cristina cristine cristobal cristopher cristy cruz crysta crystal crystle cuc curt curtis cyndi cyndy cynthia cyril cyrstal cyrus cythia dacia dagmar dagny dahlia daina daine daisey daisy dakota dale dalene dalia dalila dallas dalton damaris damian damien damion damon dan dana danae dane danelle danette dani dania danial danica daniel daniela daniele daniell daniella danielle danika danille danilo danita dann danna dannette dannie dannielle danny dante danuta danyel danyell danyelle daphine daphne dara darby darcel darcey darci darcie darcy darell daren daria darin dario darius darla darleen darlena darlene darline darnell daron darrel darrell darren darrick darrin darron darryl daryl dave david davida davina davis dawn dawna dawne dayle dayna daysi deadra dean deana deandra deandre deandrea deane deangelo deann deanna deanne deb debbi debbie debbra debby debera debi debora deborah debra debrah debroah dede dedra dee deeann deeanna deedee deedra deena deetta deidra deidre deirdre deja delaine delana delbert delcie delena delfina delia delicia delila delilah delinda delisa dell della delma delmar delmer delmy delois deloise delora deloras delores deloris delorse delpha delphia delphine delsie delta demarcus demetra demetria demetrice demetrius dena denae deneen denese denice denis denise denisha denisse denita denna dennis dennise denny denver denyse deon deonna derek derick derrick deshawn desirae desire desiree desmond despina dessie destiny detra devin devon devona devora devorah dewayne dewey dewitt dexter dia diamond dian diana diane diann dianna dianne dick diedra diedre diego dierdre digna dillon dimple dina dinah dino dinorah dion dione dionna dionne dirk divina dixie dodie dollie dolly dolores doloris domenic domenica dominga domingo dominic dominica dominick dominique dominque domitila domonique don dona donald donella donetta donette dong donita donn donna donnell donnetta donnette donnie donny donovan donte donya dora dorathy dorcas doreatha doreen dorene doretha dorethea doretta dori doria dorian dorie dorinda dorine doris dorla dorotha dorothea dorothy dorris dorsey dortha dorthea dorthey dorthy dottie dotty doug douglas douglass dovie doyle dreama drema drew drucilla drusilla duane dudley dulce dulcie duncan dung dusti dustin dusty dwain dwana dwayne dwight dyan earl earle earlean earleen earlene earlie earline earnest earnestine eartha easter eboni ebonie ebony eda edda eddie eddy edelmira eden edgar edgardo edie edison edith edmond edmund edmundo edna edra edris eduardo edward edwardo edwin edwina edyth edythe effie efrain efren ehtel eileen eilene ela eladia elaina elaine elana elane elanor elayne elba elbert elda elden eldon eldora eldridge eleanor eleanora eleanore elease elena elene eleni elenor elenora elenore eleonor eleonora eleonore elfreda elfrieda elfriede eli elia eliana elias elicia elida elidia elijah elin elina elinor elinore elisa elisabeth elise eliseo elisha elissa eliz eliza elizabet elizabeth elizbeth elizebeth elke ella ellamae ellan ellen ellena elli ellie elliot elliott ellis ellsworth elly ellyn elma elmer elmira elmo elna elnora elodia elois eloisa eloise elouise eloy elroy elsa elsie elsy elton elva elvera elvia elvie elvin elvina elvira elvis elwanda elwood elyse elza ema emanuel emelda emelia emelina emeline emely emerald emerita emerson emery emiko emil emile emilee emilia emilie emilio emily emma emmaline emmanuel emmett emmie emmitt emmy emogene emory ena enda enedina eneida enid enoch enola enrique enriqueta epifania erasmo eric erica erich erick ericka erik erika erin erinn erlene erlinda erline erma ermelinda erminia erna ernest ernestina ernestine ernesto ernie errol ervin erwin eryn esmeralda esperanza essie esta esteban estefana estela estell estella estelle ester esther estrella etha ethan ethel ethelene ethelyn ethyl etsuko etta ettie eufemia eugena eugene eugenia eugenie eugenio eulah eulalia eun euna eunice eura eusebia eusebio eustolia eva evalyn evan evangelina evangeline evelia evelin evelina eveline evelyn evelyne evelynn everett everette evette evia evie evita evon evonne ewa exie ezekiel ezequiel ezra fabian fabiola fae fairy faith fallon fannie fanny farah farrah fatima fatimah faustina faustino fausto faviola fawn fay faye fe federico felecia felica felice felicia felicidad felicita felicitas felipa felipe felisa felisha felix felton ferdinand fermin fermina fern fernanda fernande fernando ferne fidel fidela fidelia filiberto filomena fiona flavia fleta fletcher flo flor flora florance florence florencia florencio florene florentina florentino floretta floria florida florinda florine florrie flossie floy floyd fonda forest forrest foster fran france francene frances francesca francesco franchesca francie francina francine francis francisca francisco francoise frank frankie franklin franklyn fransisca fred freda fredda freddie freddy frederic frederica frederick fredericka fredia fredric fredrick fredricka freeda freeman freida frida frieda fritz fumiko gabriel gabriela gabriele gabriella gabrielle gail gala gale galen galina garfield garland garnet garnett garret garrett garry garth gary gaston gavin gay gaye gayla gayle gaylene gaylord gaynell gaynelle gearldine gema gemma gena genaro gene genesis geneva genevie genevieve genevive genia genie genna gennie genny genoveva geoffrey georgann george georgeann georgeanna georgene georgetta georgette georgia georgiana georgiann georgianna georgianne georgie georgina georgine gerald geraldine geraldo geralyn gerard gerardo gerda geri germaine german gerri gerry gertha gertie gertrud gertrude gertrudis gertude ghislaine gia gianna gidget gigi gil gilbert gilberte gilberto gilda gillian gilma gina ginette ginger ginny gino giovanna giovanni gisela gisele giselle gita giuseppe giuseppina gladis glady gladys glayds glen glenda glendora glenn glenna glennie glennis glinda gloria glory glynda glynis golda golden goldie gonzalo gordon grace gracia gracie graciela grady graham graig grant granville grayce grazyna greg gregg gregoria gregorio gregory greta gretchen gretta gricelda grisel griselda grover guadalupe gudrun guillermina guillermo gus gussie gustavo guy gwen gwenda gwendolyn gwenn gwyn gwyneth ha hae hai hailey hal haley halina halley hallie han hana hanh hank hanna hannah hannelore hans harlan harland harley harmony harold harriet harriett harriette harris harrison harry harvey hassan hassie hattie haydee hayden hayley haywood hazel heath heather hector hedwig hedy hee heide heidi heidy heike helaine helen helena helene helga hellen henrietta henriette henry herb herbert heriberto herlinda herma herman hermelinda hermila hermina hermine herminia herschel hershel herta hertha hester hettie hiedi hien hilaria hilario hilary hilda hilde hildegard hildegarde hildred hillary hilma hilton hipolito hiram hiroko hisako hoa hobert holley holli hollie hollis holly homer honey hong hope horace horacio hortencia hortense hortensia hosea houston howard hoyt hsiu hubert huey hugh hugo hui hulda humberto hung hunter huong hwa hyacinth hye hyman hyo hyon hyun ian ida idalia idell idella iesha ignacia ignacio ike ila ilana ilda ileana ileen ilene iliana illa ilona ilse iluminada ima imelda imogene ina india indira inell ines inez inga inge ingeborg inger ingrid inocencia iola iona ione ira iraida irena irene irina iris irish irma irmgard irvin irving irwin isaac isabel isabell isabella isabelle isadora isaiah isaias isaura isela isiah isidra isidro isis ismael isobel israel isreal issac iva ivan ivana ivelisse ivette ivey ivonne ivory ivy izetta izola ja jacalyn jacelyn jacinda jacinta jacinto jackeline jackelyn jacki jackie jacklyn jackqueline jackson jaclyn jacob jacqualine jacque jacquelin jacqueline jacquelyn jacquelyne jacquelynn jacques jacquetta jacqui jacquie jacquiline jacquline jacqulyn jada jade jadwiga jae jaime jaimee jaimie jake jaleesa jalisa jama jamaal jamal jamar jame jamee jamel james jamey jami jamie jamika jamila jamison jammie jan jana janae janay jane janean janee janeen janel janell janella janelle janene janessa janet janeth janett janetta janette janey jani janice janie janiece janina janine janis janise janita jann janna jannet jannette jannie january janyce jaqueline jaquelyn jared jarod jarred jarrett jarrod jarvis jasmin jasmine jason jasper jaunita javier jay jaye jayme jaymie jayna jayne jayson jazmin jazmine jc jean jeana jeane jeanelle jeanene jeanett jeanetta jeanette jeanice jeanie jeanine jeanmarie jeanna jeanne jeannetta jeannette jeannie jeannine jed jeff jefferey jefferson jeffery jeffie jeffrey jeffry jen jena jenae jene jenee jenell jenelle jenette jeneva jeni jenice jenifer jeniffer jenine jenise jenna jennefer jennell jennette jenni jennie jennifer jenniffer jennine jenny jerald jeraldine jeramy jere jeremiah jeremy jeri jerica jerilyn jerlene jermaine jerold jerome jeromy jerrell jerri jerrica jerrie jerrod jerrold jerry jesenia jesica jess jesse jessenia jessi jessia jessica jessie jessika jestine jesus jesusa jesusita jetta jettie jewel jewell ji jill jillian jim jimmie jimmy jin jina jinny jo joan joana joane joanie joann joanna joanne joannie joaquin joaquina jocelyn jodee jodi jodie jody joe joeann joel joella joelle joellen joesph joetta joette joey johana johanna johanne john johna johnathan johnathon johnetta johnette johnie johnna johnnie johnny johnsie johnson joi joie jolanda joleen jolene jolie joline jolyn jolynn jon jona jonah jonas jonathan jonathon jone jonell jonelle jong joni jonie jonna jonnie jordan jordon jorge jose josef josefa josefina josefine joselyn joseph josephina josephine josette josh joshua josiah josie joslyn jospeh josphine josue jovan jovita joy joya joyce joycelyn joye juan juana juanita jude judi judie judith judson judy jule julee julene jules juli julia julian juliana juliane juliann julianna julianne julie julieann julienne juliet julieta julietta juliette julio julissa julius june jung junie junior junita junko justa justin justina justine jutta ka kacey kaci kacie kacy kai kaila kaitlin kaitlyn kala kaleigh kaley kali kallie kalyn kam kamala kami kamilah kandace kandi kandice kandis kandra kandy kanesha kanisha kara karan kareem kareen karen karena karey kari karie karima karin karina karine karisa karissa karl karla karleen karlene karly karlyn karma karmen karol karole karoline karolyn karon karren karri karrie karry kary karyl karyn kasandra kasey kasha kasi kasie kassandra kassie kate katelin katelyn katelynn katerine kathaleen katharina katharine katharyn kathe katheleen katherin katherina katherine kathern katheryn kathey kathi kathie kathleen kathlene kathline kathlyn kathrin kathrine kathryn kathryne kathy kathyrn kati katia katie katina katlyn katrice katrina kattie katy kay kayce kaycee kaye kayla kaylee kayleen kayleigh kaylene kazuko kecia keeley keely keena keenan keesha keiko keila keira keisha keith keitha keli kelle kellee kelley kelli kellie kelly kellye kelsey kelsi kelsie kelvin kemberly ken kena kenda kendal kendall kendra kendrick keneth kenia kenisha kenna kenneth kennith kenny kent kenton kenya kenyatta kenyetta kera keren keri kermit kerri kerrie kerry kerstin kesha keshia keturah keva keven kevin khadijah khalilah kia kiana kiara kiera kiersten kiesha kieth kiley kim kimber kimberely kimberlee kimberley kimberli kimberlie kimberly kimbery kimbra kimi kimiko kina kindra king kip kira kirby kirk kirsten kirstie kirstin kisha kittie kitty kiyoko kizzie kizzy klara korey kori kortney kory kourtney kraig kris krishna krissy krista kristal kristan kristeen kristel kristen kristi kristian kristie kristin kristina kristine kristle kristofer kristopher kristy kristyn krysta krystal krysten krystin krystina krystle krystyna kum kurt kurtis kyla kyle kylee kylie kym kymberly kyoko kyong kyra kyung lacey lachelle laci lacie lacresha lacy ladawn ladonna lael lahoma lai laila laine lajuana lakeesha lakeisha lakendra lakenya lakesha lakeshia lakia lakiesha lakisha lakita lala lamar lamonica lamont lana lance landon lane lanell lanelle lanette lani lanie lanita lannie lanny lanora laquanda laquita lara larae laraine laree larhonda larisa larissa larita laronda larraine larry larue lasandra lashanda lashandra lashaun lashaunda lashawn lashawna lashawnda lashay lashell lashon lashonda lashunda lasonya latanya latarsha latasha latashia latesha latia laticia latina latisha latonia latonya latoria latosha latoya latoyia latrice latricia latrina latrisha launa laura lauralee lauran laure laureen laurel lauren laurena laurence laurene lauretta laurette lauri laurice laurie laurinda laurine lauryn lavada lavelle lavenia lavera lavern laverna laverne laveta lavette lavina lavinia lavon lavona lavonda lavone lavonia lavonna lavonne lawana lawanda lawanna lawerence lawrence layla layne lazaro lea leah lean leana leandra leandro leann leanna leanne leanora leatha leatrice lecia leda lee leeann leeanna leeanne leena leesa leia leida leif leigh leigha leighann leila leilani leisa leisha lekisha lela lelah leland lelia lemuel lena lenard lenita lenna lennie lenny lenora lenore leo leola leoma leon leona leonard leonarda leonardo leone leonel leonia leonida leonie leonila leonor leonora leonore leontine leopoldo leora leota lera leroy les lesa lesha lesia leslee lesley lesli leslie lessie lester leta letha leticia letisha letitia lettie letty levi lewis lexie lezlie lia liana liane lianne libbie libby liberty librada lida lidia lien lieselotte ligia lila lili lilia lilian liliana lilla lilli lillia lilliam lillian lilliana lillie lilly lily lin lina lincoln linda lindsay lindsey lindsy lindy linette ling linh linn linnea linnie lino linsey linwood lionel lisa lisabeth lisandra lisbeth lise lisette lisha lissa lissette lita livia liz liza lizabeth lizbeth lizeth lizette lizzette lizzie lloyd loan logan loida lois loise lola lolita loma lon lona londa loni lonna lonnie lonny lora loraine loralee lore lorean loree loreen lorelei loren lorena lorene lorenza lorenzo loreta loretta lorette lori loria loriann lorie lorilee lorina lorinda lorine loris lorita lorna lorraine lorretta lorri lorriane lorrie lorrine lory lottie lou louann louanne louella louetta louie louis louisa louise loura lourdes lourie louvenia lovella lovetta lovie lowell loyce loyd luana luann luanna luanne luba lucas luci lucia luciana luciano lucie lucien lucienne lucila lucile lucilla lucille lucina lucinda lucio lucius lucrecia lucretia lucy ludie ludivina lue luella luetta luigi luis luisa luise luke lula lulu luna lupe lupita lura lurlene lurline luther luvenia luz lyda lydia lyla lyle lyman lyn lynda lyndia lyndon lyndsay lyndsey lynell lynelle lynetta lynette lynn lynna lynne lynnette lynsey lynwood mabel mabelle mable machelle macie mack mackenzie macy madalene madaline madalyn maddie madelaine madeleine madelene madeline madelyn madge madie madison madlyn madonna mae maegan mafalda magali magaly magan magaret magda magdalen magdalena magdalene magen maggie magnolia mahalia mai maia maida maile maira maire maisha maisie majorie makeda malcolm malcom malena malia malik malika malinda malisa malissa malka mallie mallory malorie malvina mamie mammie mana manda mandi mandie mandy manie manual manuel manuela maple mara maragaret maragret maranda marc marcel marcela marcelene marcelina marceline marcelino marcell marcella marcelle marcellus marcelo marcene marchelle marci marcia marcie marco marcos marcus marcy mardell maren marg margaret margareta margarete margarett margaretta margarette margarita margarite margarito margart marge margene margeret margert margery marget margherita margie margit margo margorie margot margret margrett marguerita marguerite margurite margy marhta mari maria mariah mariam marian mariana marianela mariann marianna marianne mariano maribel maribeth marica maricela maricruz marie mariel mariela mariella marielle marietta mariette mariko marilee marilou marilu marilyn marilynn marin marina marinda marine mario marion maris marisa marisela marisha marisol marissa marita maritza marivel marjorie marjory marketta markita markus marla marlana marleen marlen marlena marlene marlin marline marlo marlon marlyn marlys marna marni marnie marquerite marquetta marquis marquita marquitta marsha marshall marta marth martha marti martin martina martine marty marva marvel marvella marvin marvis marx mary marya maryalice maryam maryann maryanna maryanne marybelle marybeth maryellen maryetta maryjane maryjo maryland marylee marylin maryln marylou marylouise marylyn marylynn maryrose masako mason matha mathew mathilda mathilde matilda matilde matt matthew mattie maud maude maudie maura maureen maurice mauricio maurine maurita mauro mavis maxie maxima maximina maximo maxine maxwell may maya maybell maybelle maye mayme maynard mayola mayra mazie mckenzie mckinley meagan meaghan mechelle meda mee megan meggan meghan meghann mei mel melaine melani melania melanie melany melba melda melia melida melina melinda melisa melissa melissia melita mellie mellisa mellissa melodee melodi melodie melody melonie melony melva melvin melvina melynda mendy mercedes mercedez mercy meredith meri merideth meridith merilyn merissa merle merlene merlin merlyn merna merri merrie merrilee merrill merry mertie mervin meryl mica micaela micah micha michael michaela michaele michal michale micheal michel michele michelina micheline michell michelle michiko mickey micki mickie miesha migdalia mignon miguel miguelina mika mikaela mike mikel miki mikki mila milagro milagros milan milda mildred miles milford milissa millard millicent millie milly milo milton mimi mina minda mindi mindy minerva ming minh minna minnie minta miquel mira miranda mireille mirella mireya miriam mirian mirna mirta mirtha misha missy misti mistie misty mitch mitchel mitchell mitsue mitsuko mittie mitzi mitzie miyoko modesta modesto mohamed mohammad mohammed moira moises mollie molly mona monet monica monika monique monnie monroe monserrate monte monty moon mora morgan moriah morris morton mose moses moshe mozell mozella mozelle mui muoi muriel murray myesha myles myong myra myriam myrl myrle myrna myron myrta myrtice myrtie myrtis myrtle myung nada nadene nadia nadine naida nakesha nakia nakisha nakita nana nancee nancey nanci nancie nancy nanette nannette nannie naoma naomi napoleon narcisa natacha natalia natalie natalya natasha natashia nathalie nathan nathanael nathanial nathaniel natisha natividad natosha neal necole ned neda nedra neely neida neil nelda nelia nelida nell nella nelle nellie nelly nelson nena nenita neoma neomi nereida nerissa nery nestor neta nettie neva nevada neville newton nga ngan ngoc nguyet nia nichelle nichol nicholas nichole nicholle nick nicki nickie nickolas nickole nicky nicol nicola nicolas nicolasa nicole nicolette nicolle nida nidia niesha nieves nigel niki nikia nikita nikki nikole nila nilda nilsa nina ninfa nisha nita noah noble nobuko noe noel noelia noella noelle noemi nohemi nola nolan noma nona nora norah norbert norberto noreen norene noriko norine norma norman normand norris nova novella nubia numbers nydia nyla obdulia ocie octavia octavio oda odelia odell odessa odette odilia odis ofelia ola olen olene oleta olevia olga olimpia olin olinda oliva olive oliver olivia ollie olympia oma omar omer ona oneida onie onita opal ophelia ora oralee oralia oren oretha orlando orpha orval orville oscar ossie osvaldo oswaldo otelia otha otilia otis otto ouida owen ozell ozella ozie pablo paige palma palmer palmira pamala pamela pamelia pamella pamila pamula pandora pansy paola paris parker parthenia particia pasquale pasty patience patria patrica patrice patricia patrick patrina patsy patti pattie patty paul paula paulene pauletta paulette paulina pauline paulita paz pearl pearle pearlene pearlie pearline pearly pedro peggie peggy pei penelope penney penni pennie penny percy perla perry pete peter petra petrina petronila phebe phil philip phillip phillis philomena phoebe phung phuong phylicia phylis phyliss phyllis pia piedad pierre pilar pinkie piper polly porfirio porsche porsha porter portia precious preston pricilla prince princess priscila priscilla providencia prudence pura qiana queen queenie quentin quiana quincy quinn quintin quinton quyen rachael rachal racheal rachel rachele rachell rachelle racquel rae raeann raelene rafael rafaela raguel raina raisa raleigh ralph ramiro ramon ramona ramonita rana ranae randa randal randall randee randell randi randolph randy ranee raphael raquel rashad rasheeda rashida raul raven raye rayford raylene raymon raymond raymonde raymundo rayna rea reagan reanna reatha reba rebbeca rebbecca rebeca rebecca rebecka rebekah reda reed reena refugia refugio regan regena regenia reggie regina reginald regine reginia reid reiko reina reinaldo reita rema remedios remona rena renae renaldo renata renate renato renay renda rene renea renee renetta renita renna ressie reta retha retta reuben reva rey reyes reyna reynalda reynaldo rhea rheba rhett rhiannon rhoda rhona rhonda ria ricarda ricardo rich richard richelle richie rick rickey ricki rickie ricky rico rigoberto rikki riley rima rina risa rita riva rivka rob robbi robbie robbin robby robbyn robena robert roberta roberto robin robt robyn rocco rochel rochell rochelle rocio rocky rod roderick rodger rodney rodolfo rodrick rodrigo rogelio roger roland rolanda rolande rolando rolf rolland roma romaine romana romelia romeo romona ron rona ronald ronda roni ronna ronni ronnie ronny roosevelt rory rosa rosalba rosalee rosalia rosalie rosalina rosalind rosalinda rosaline rosalva rosalyn rosamaria rosamond rosana rosann rosanna rosanne rosaria rosario rosaura roscoe rose roseann roseanna roseanne roselee roselia roseline rosella roselle roselyn rosemarie rosemary rosena rosenda rosendo rosetta rosette rosia rosie rosina rosio rosita roslyn ross rossana rossie rosy rowena roxana roxane roxann roxanna roxanne roxie roxy roy royal royce rozanne rozella ruben rubi rubie rubin ruby rubye rudolf rudolph rudy rueben rufina rufus rupert russ russel russell rusty ruth rutha ruthann ruthanne ruthe ruthie ryan ryann sabina sabine sabra sabrina sacha sachiko sade sadie sadye sage sal salena salina salley sallie sally salome salvador salvatore samantha samara samatha samella samira sammie sammy samual samuel sana sanda sandee sandi sandie sandra sandy sanford sang sanjuana sanjuanita sanora santa santana santiago santina santo santos sara sarah sarai saran sari sarina sarita sasha saturnina sau saul saundra savanna savannah scarlet scarlett scot scott scottie scotty sean season sebastian sebrina seema selena selene selina selma sena senaida september serafina serena sergio serina serita seth setsuko seymour sha shad shae shaina shakia shakira shakita shala shalanda shalon shalonda shameka shamika shan shana shanae shanda shandi shandra shane shaneka shanel shanell shanelle shani shanice shanika shaniqua shanita shanna shannan shannon shanon shanta shantae shantay shante shantel shantell shantelle shanti shaquana shaquita shara sharan sharda sharee sharell sharen shari sharice sharie sharika sharilyn sharita sharla sharleen sharlene sharmaine sharolyn sharon sharonda sharri sharron sharyl sharyn shasta shaun shauna shaunda shaunna shaunta shaunte shavon shavonda shavonne shawana shawanda shawanna shawn shawna shawnda shawnee shawnna shawnta shay shayla shayna shayne shea sheba sheena sheila sheilah shela shelba shelby sheldon shelia shella shelley shelli shellie shelly shelton shemeka shemika shena shenika shenita shenna shera sheree sherell sheri sherice sheridan sherie sherika sherill sherilyn sherise sherita sherlene sherley sherly sherlyn sherman sheron sherrell sherri sherrie sherril sherrill sherron sherry sherryl sherwood shery sheryl sheryll shiela shila shiloh shin shira shirely shirl shirlee shirleen shirlene shirley shirly shizue shizuko shon shona shonda shondra shonna shonta shoshana shu shyla sibyl sidney sierra signe sigrid silas silva silvana silvia sima simon simona simone simonne sina sindy siobhan sirena siu sixta skye slyvia socorro sofia soila solange soledad solomon somer sommer sona sondra song sonia sonja sonny sonya sook soon sophia sophie soraya sparkle spencer stacee stacey staci stacia stacie stacy stan stanford stanley stanton starla starr stasia stefan stefani stefania stefanie stefany steffanie stella stepanie stephaine stephan stephane stephani stephania stephanie stephany stephen stephenie stephine stephnie sterling steve steven stevie stewart stormy stuart suanne sudie sueann suellen suk sulema sumiko summer sun sunday sung sunni sunny sunshine susan susana susann susanna susannah susanne susie susy suzan suzann suzanna suzanne suzette suzi suzie suzy svetlana sybil syble sydney sylvester sylvia sylvie synthia syreeta tabatha tabetha tabitha tad tai taina taisha tajuana takako takisha talia talisha talitha tam tama tamala tamar tamara tamatha tambra tameika tameka tamekia tamela tamera tamesha tami tamica tamie tamika tamiko tamisha tammara tammera tammi tammie tammy tamra tana tandra tandy taneka tanesha tangela tania tanika tanisha tanja tanna tanner tanya tara tarah taren tari tarra tarsha taryn tasha tashia tashina tasia tatiana tatum tatyana taunya tawana tawanda tawanna tawna tawny tawnya taylor tayna teddy teena tegan teisha telma temeka temika tempie temple tena tenesha tenisha tennie tennille teodora teodoro teofila tequila tera tereasa terence teresa terese teresia teresita teressa teri terica terina terisa terra terrance terrell terrence terresa terri terrie terrilyn terry tesha tess tessa tessie thad thaddeus thalia thanh thao thea theda thelma theo theodora theodore theola theresa therese theresia theressa theron thersa thi thomas thomasena thomasina thomasine thora thresa thu thurman thuy tia tiana tianna tiara tien tiera tierra tiesha tifany tiffaney tiffani tiffanie tiffany tiffiny tijuana tilda tillie tim timika timmy timothy tina tinisha tiny tisa tish tisha titus tobi tobias tobie toby toccara tod todd toi tom tomas tomasa tomeka tomi tomika tomiko tommie tommy tommye tomoko tona tonda tonette toney toni tonia tonie tonisha tonita tonja tony tonya tora tori torie torri torrie tory tosha toshia toshiko tova towanda toya tracee tracey traci tracie tracy tran trang travis treasa treena trena trent trenton tresa tressa tressie treva trevor trey tricia trina trinh trinidad trinity trish trisha trista tristan troy trudi trudie trudy trula truman tuan tula tuyet twana twanda twanna twila twyla ty tyesha tyisha tyler tynisha tyra tyree tyrell tyron tyrone tyson ula ulrike ulysses ursula usha ute vada valarie valda valencia valene valentin valentina valentine valeri valeria valerie valery vallie valorie valrie van vance vanda vanesa vanessa vanetta vania vanita vanna vannesa vannessa vashti vasiliki vaughn veda velda velia vella velma velva velvet vena venessa venetta venice venita vennie venus veola vera verda verdell verdie verena vergie verla verlene verlie verline vern verna vernell vernetta vernia vernice vernie vernita vernon verona veronica veronika veronique versie vertie vesta veta vicenta vicente vickey vicki vickie vicky victor victoria victorina vida viki vikki vilma vina vince vincent vincenza vincenzo vinita vinnie viola violet violeta violette virgen virgie virgil virgilio virgina virginia vita vito viva vivan vivian viviana vivien vivienne von voncile vonda vonnie wade wai waldo walker wallace wally walter walton waltraud wanda waneta wanetta wanita warner warren wava waylon wayne wei weldon wen wendell wendi wendie wendolyn wendy wenona werner wes wesley weston whitley whitney wilber wilbert wilbur wilburn wilda wiley wilford wilfred wilfredo wilhelmina wilhemina willa willard willena willene willetta willette willia william williams willian willie williemae willis willodean willow willy wilma wilmer wilson wilton windy winford winfred winifred winnie winnifred winona winston winter wonda woodrow wyatt wynell wynona xavier xenia xiao xiomara xochitl xuan yadira yaeko yael yahaira yajaira yan yang yanira yasmin yasmine yasuko yee yelena yer yesenia yessenia yetta yevette yi ying yoko yolanda yolande yolando yolonda yon yong yoshie yoshiko youlanda yu yuette yuk yuki yukiko yuko yulanda yun yung yuonne yuri yuriko yvette yvone yvonne zachariah zachary zachery zack zackary zada zaida zana zandra zane zelda zella zelma zena zenaida zenia zenobia zetta zina zita zoe zofia zoila zola zona zonia zora zoraida zula zulema zulma'''
text='''<158>Apr 15 2015 10:52:41 NFJD-SW1 %%01SHELL/6/DISPLAY_CMDRECORD(l): Record command information. (Task=vt0, Ip=172.172.0.209, User=chenyiming, Command="display interface GigabitEthernet 3/0/34")
'''
text1='''2016-01-26 16:19:59,885 INFO  [org.jboss.resteasy.spi.ResteasyDeployment] (ajp-/127.0.0.1:8702-6) Adding singleton resource org.ovirt.engine.api.restapi.resource.BackendUsersResource from Application javax.ws.rs.core.Application'''


s='''
2016-01-26 16:19:59,885 INFO  [org.jboss.resteasy.spi.ResteasyDeployment] (ajp-/127.0.0.1:8702-6) Adding singleton resource org.ovirt.engine.api.restapi.resource.BackendUsersResource from Application javax.ws.rs.core.Application
2016-01-26 16:19:59,885 INFO  [org.jboss.resteasy.spi.ResteasyDeployment] (ajp-/127.0.0.1:8702-6) Adding singleton resource org.ovirt.engine.api.restapi.resource.BackendStorageServerConnectionsResource from Application javax.ws.rs.core.Application
2016-01-26 16:19:59,886 INFO  [org.jboss.resteasy.spi.ResteasyDeployment] (ajp-/127.0.0.1:8702-6) Adding singleton resource org.ovirt.engine.api.restapi.resource.BackendVmPoolsResource from Application javax.ws.rs.core.Application
2016-01-26 16:19:59,886 INFO  [org.jboss.resteasy.spi.ResteasyDeployment] (ajp-/127.0.0.1:8702-6) Adding singleton resource org.ovirt.engine.api.restapi.resource.BackendApiResource from Application javax.ws.rs.core.Application
2016-01-26 16:19:59,887 INFO  [org.jboss.resteasy.spi.ResteasyDeployment] (ajp-/127.0.0.1:8702-6) Adding singleton resource org.ovirt.engine.api.restapi.resource.BackendDomainsResource from Application javax.ws.rs.core.Application
'''

gloabl_V=set()
global _remove_number,_debug
_remove_number=0
_debug=0
def read_sourcetype_conf():
    global gloabl_V
    file_path=r'etc/system/default/sourcetypes.conf'
    f=open(file_path)
    content=f.read()
    f.close()
    ret=[]
    result=content.split("[")
    result= result[1:]
    V=[]
    for content in result:
        temp= content.split('\n')
        t=temp[1:]#

        dd={}
        for d in t:
            dict=split_eq(d)
            dd.update(dict)

        del dd["_source"]
        ss=dd.keys()
        V.extend(ss)
        dd["word_number"]=len(ss)-1
        ret.append(dd)
        # print dd["word_number"]
    gloabl_V=set(V)
    gloabl_V.remove("_sourcetype")
    # for x in gloabl_V:
    #     if x=="_source":
    #         print 'yes'
    #     if x=="_sourcetype":
    #         print 'no'



    return ret
def split_eq(str):
    if '=' not in str:
        return ""
    t=str.replace("=",'').split()
    return {t[0]:t[1]}
def preprocess(file_path):
    # f=open(file_path)
    # text_list=f.readlines()
    # text_list=text_list[:1000]
    # f.close()
    text_list=file_path
    ret={}
    for line in text_list:
        punc=get_punc_string1(line)
        if ret.has_key(punc):
            ret[punc]+=1
        else:
            ret[punc]=1
    # print text,len(text)
    s_list=remove_stop_word(text_list)
    if _remove_number==1:
        s_list=remove_number(s_list)
    content_dict= count_words(s_list)
    if _debug:
        print ret
    content_dict.update(ret)
    return content_dict
def remove_number(s_list):
    str=[]
    for word in s_list:
        if word.isdigit():
            pass
        else:
            str.append(word)
    return str
def remove_stop_word(text):
    ret=[]
    for line in text:
        l=get_punc_string(line)
        ret.extend([word.lower() for word in l.split() if word not in ignored_model_keywords])
    return ret
def get_punc_string1(line):
    eventtype=""
    for x in line:
        if x in string.punctuation and x!=r'_':
            eventtype+=x
        else:
            if x=='\t':
                eventtype+='t'
            else:
                if x.isspace():
                    eventtype+=r'_'
    eventtype=eventtype[:10]
    eventtype=eventtype.replace('=',"EQ")
    eventtype=eventtype.replace('[',"L7(")
    eventtype=eventtype.replace(']',r"L7)")
    return 'L-'+eventtype
def get_punc_string(line):
    reStr=""
    # eventtype=""
    # for x in line:
    #     if x in string.punctuation and x!=r'_':
    #         eventtype+=x
    #     else:
    #         if x=='\t':
    #             eventtype+='t'
    #         else:
    #             if x.isspace():
    #                 eventtype+=r'_'
    for x in line:
        if x not in string.punctuation:
            reStr+=x
        else:
            reStr+=' '
    # eventtype=eventtype[:10]
    # eventtype=eventtype.replace('=',"EQ")
    # eventtype=eventtype.replace('[',"L7(")
    # eventtype=eventtype.replace(']',r"L7)")
    # return (reStr,'L-'+eventtype)
    return reStr

def count_words(list_content):#统计给定的text中的单词频数
    text_count={}
    word_list=list_content
    for x in word_list:
        if text_count.has_key(x):
            text_count[x]+=1
        else:
            text_count[x]=1
    return text_count
def compute_prior(different_source_type_dis):
    "由于不知道先验概率,默认所有的类别的先验一致,所以在计算的时候,不计算先验概率"
    source_type_vector=[source_type["_sourcetype"] for source_type in different_source_type_dis]
    total_count= count_words(source_type_vector)
    ttt= sum(total_count.values())
    for x in total_count:
        print x,float(total_count[x])/ttt

def get_score(source_type_dict,content_dict):
    ret=[]
    for key in content_dict:
        if source_type_dict.has_key(key):
            # if key=="L-t_........":
            #     print "get!",key,source_type_dict[key],content_dict[key]
            ret.append((source_type_dict[key],content_dict[key]))
        else:

            # print "aaaaaP",source_type_dict['word_number'],key,content_dict[key]
            # print (1.0/(len(gloabl_V)+source_type_dict['word_number']),content_dict[key])
            ret.append((1.0/(len(gloabl_V)+source_type_dict['word_number']),content_dict[key]))
    return ret
def predict_source_type(content_dict,different_source_type_dis):
    pre=[]
    tttt=[]
    # the length of gloabl vacabulery,return a int
    for source_type in different_source_type_dis:
        pred={}
        pred["source_type"]=source_type['_sourcetype']
        pred["score_vector"]=get_score(source_type,content_dict)
        pre.append(pred)

    for x in pre:
        # print X["score_vector"]
        if len(x["score_vector"])==0:
            pass
        else:
            # print x["source_type"],x["score_vector"]
            temp=[math.log(float(item[0]))*item[1] for item in x["score_vector"]]

            tttt.append([x["source_type"],sum(temp)])
    maxscore=max([x[1] for x in tttt])
    if _debug==1:
        # print [x[1] for x in tttt]
        # print maxscore
        pass
    for x in tttt:
        if maxscore in x:
            print "the probability of sourcetype:'%s' is high"%(x[0])
            return x[0]
    # print "the probability of sourcetype %s is high"%(chr(result.index(maxscore)+1))

def read_conf(filename):
    ret={}
    f=open(filename)
    contentlist=f.readlines()


    key_reg="\[.*\]"
    key=""

    for line in contentlist:
        if line[0]=='#' or line.isspace():
            pass
        else:
            if re.match(key_reg,line):
                line=line.strip()
                ret[line.strip()]={}
                key=line
            else:
                # print line
                line=line.strip()
                sub=line.split("=",1)
                sub_key,sub_value=sub[0].rstrip(),sub[1].lstrip()
                # print sub_key,sub_value
                ret[key][sub_key]=sub_value
    f.close()
    # print contentlist
    return ret
def this_reg_match(line,reg):
    if _debug:
        # print line
        # print reg
        pass
    ttt=re.match(reg,line)
    if ttt is None:
        if _debug:
            # print "))))))))))))"
            pass
        return False
    return True

def get_regMatch_uploadMatch():

    filename=r"etc/system/default/source.conf"
    reg_conf_dict=read_conf(filename)

    #rule base
    reg_for_match={}
    #upload path base
    upload_for_match={}
    for key in reg_conf_dict:
        if "rule" in key and "delayedrule" not in key:
            if _debug:
                print "正则可以匹配哪些sourcetype:"
                print key
            for sub_key in reg_conf_dict[key]:

                if "MORE_THAN_" in sub_key:
                    reg_for_match[key.split("::")[1][:-1]]=reg_conf_dict[key][sub_key]
                    # print key,sub_key,reg_conf_dict[key][sub_key]
        else:
            if  "source::" in key:

                upload_for_match[reg_conf_dict[key]['sourcetype']]=key.split("source::...")[1][:-1]
                # print key,reg_conf_dict[key]['sourcetype']
    return (reg_for_match,upload_for_match)
def use_reg_match_source_type(content_text_list,reg_for_match):

    # for s in reg_for_match:
    #     print s
    #     print reg_for_match[s]
    # access_combined
    # ^\S+ \S+ \S+ \S* ?\[[^\]]+\] "[^"]*" \S+ \S+ \S+ "[^"]*"$
    # access_combined_wcookie
    # ^\S+ \S+ \S+ \S* ?\[[^\]]+\] "[^"]*" \S+ \S+(?: \S+)? "[^"]*" "[^"]*"
    # snort
    # (?:[0-9A-F]{2} ){16}
    # access_common
    # ^\S+ \S+ \S+ \[[^\]]+\] "[^"]+" \S+ \S+$
    # sendmail_syslog
    # ^\w{3} +\d+ \d\d:\d\d:\d\d .* (sendmail|imapd|ipop3d)\[\d+\]:
    # postfix_syslog
    # ^\w{3} +\d+ \d\d:\d\d:\d\d .* postfix(/\w+)?\[\d+\]:
    statistics={}

    if _debug:
        print reg_for_match
        print len(content_text_list)
    for line in content_text_list:
        for source_type in reg_for_match:
            if this_reg_match(line,reg_for_match[source_type]):
                if statistics.has_key(source_type):
                    statistics[source_type]+=1
                else:
                    statistics[source_type]=1
    if _debug:
        print statistics

    total=len(content_text_list)
    hit_sourcetype=""
    percent=0.75
    max_percent=0.0
    for type_ in statistics:
        if float(statistics[type_])/total>max_percent:
            max_percent=float(statistics[type_])/total
        if max_percent>=percent:
            if _debug:
                print max_percent,"aaa"
            hit_sourcetype=type_
            return hit_sourcetype
    if _debug:
        # print hit_sourcetype
        # print total,statistics[hit_sourcetype]
        pass
    return False

def use_upload_match_sourcetype(upload_path,upload_for_match):
    for key in upload_for_match:
        if re.match(upload_for_match[key],upload_path)!=None:
            return upload_for_match[key]
    return False

def try_to_detect_file_sourcetype(filename,upload_path=None):
    # 1:regular match
    # 2:upload path
    # 3:bayes
    sourcetype=False

    (reg_for_match,upload_for_match)=get_regMatch_uploadMatch()

    if upload_path is not None:


        sourcetype=use_upload_match_sourcetype(upload_path,upload_for_match)
    if sourcetype:
        if _debug:
            print "upload match!"
        return sourcetype
    else:
        # filename="/Users/xiaoge/Downloads/extract/log/apache.log"
        if _debug:
            print "upload no match,try regular match"
        # f=open(filename)
        # content_text_list=f.readlines()
        # f.close()
        content_text_list=filename
        sourcetype=use_reg_match_source_type(content_text_list,reg_for_match)
        if sourcetype:
            if _debug:
                print "regular match"
            return sourcetype
        else:
            if _debug:
                print "both upload and regular no match,try bayes match"
            content_dict= preprocess(filename)
            different_source_type_dis=read_sourcetype_conf()
            sourcetype=predict_source_type(content_dict,different_source_type_dis)
            if sourcetype:
                if _debug:
                    print "bayes match"
                return sourcetype
            else:
                return None
def main1():
    _remove_number=1
    _debug=1
    _how_many_sourcetype_splunk_have=1

    # content_dict= preprocess(r'/Users/xiaoge/Downloads/LogSample/syslog/receiver/172.172.0.21/syslog.log')
    # content_dict= preprocess(r'/Users/xiaoge/Downloads/LogSample/OpenVPN/openvpn_syslog (3).log')
    # content_dict= preprocess(r'/Users/xiaoge/Downloads/LogSample/secure/secure.log')
    # content_dict= preprocess(r'/Users/xiaoge/Downloads/LogSample/tomcat/catalina1_part_ac')
    # content_dict= preprocess(r'/Users/xiaoge/splunk/var/log/splunk/web_access.log')
    # content_dict= preprocess(r'/Users/xiaoge/Downloads/LogSample/Cisco Switch/n5k交换机_syslog.log')

    content_dict= preprocess(r'/Users/xiaoge/Downloads/LogSample/syslog/receiver/192.168.180.61/syslog.log')
    content_dict= preprocess(r'/Users/xiaoge/splunk/var/log/splunk/web_service.log')


    different_source_type_dis=read_sourcetype_conf()

    if _how_many_sourcetype_splunk_have:
        types=set()
        for x in different_source_type_dis:
            types.add(x['_sourcetype'])
        print "total %d differents types splunk can automatic detect:"%len(types)
        for t in types:
            print t
        print '------'

    predict_source_type(content_dict,different_source_type_dis)
def main():
    filename="/Users/xiaoge/Downloads/extract/log/apache.log"
    # filename="/Volumes/Transcend/Data/LogSample/syslog/receiver/192.168.180.61/syslog.log"
    filename="/Volumes/Transcend/Data/LogSample/apache/access_log"
    upload_path=filename
    result=try_to_detect_file_sourcetype(filename,filename)

    if result==None:
        print "用户手动指定 sourcetype吧"
    else:
        print "发现了sourcetype ,可能是 %s"%(result)

if __name__=="__main__":
    # filename="/Users/xiaoge/Downloads/extract/log/apache.log"
    # f=open(filename)
    # con=f.readlines()
    # f.close()
    # get=use_reg_match_source_type(con)
    # print get
    global _remove_number,_debug
    _remove_number=1
    _debug=1
    main()