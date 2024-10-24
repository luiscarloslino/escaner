from datetime import datetime
import pandas as pd

# Definir el diccionario con los datos
diccionario = {
    "29593447"	:	[	            1	,	"29593447"	,	"993481701"	,	"BALLON CANO, GHINA"	                            ,	"GHINA BALLÓN"         	,	"PROMOTORA"                     ]	,
    "40562059"	:	[	            2	,	"40562059"	,	"983110909"	,	"AGUIRRE CUTIPA, HENRY YOEL"	                    ,	"MAXIMO"            	,	"PRESTACION"                	]	,
    "29366764"	:	[	            3	,	"29366764"	,	"958273066"	,	"AGUIRRE GUZMAN DE CHIRINOS, IVIS LOURDES"	        ,	"MAXIMO"            	,	"FISCALIZACIÓN"             	]	,
    "45655378"	:	[	            4	,	"45655378"	,	"958216619"	,	"ALFARO ORIHUELA, JORGE ELVIS"	                    ,	"MAXIMO"            	,	"ECONOMÍA"                  	]	,
    "44690762"	:	[	            5	,	"44690762"	,	"970777414"	,	"ALLER ALLER, CRISTIAN"	                            ,	"WENDY"             	,	"TRABAJO SOCIAL"            	]	,
    "72322452"	:	[	            6	,	"72322452"	,	"922901029"	,	"ALVAREZ GONZALES, FRANK REY"	                    ,	"ROCIO"	                ,	"TRABAJO SOCIAL"            	]	,
    "80498608"	:	[	            7	,	"80498608"	,	"913242011"	,	"ALVAREZ HANAMPA, LORENZO"	                        ,	"MARILU"            	,	"ECONOMÍA"                  	]	,
    "47996952"	:	[	            8	,	"47996952"	,	"929966788"	,	"ALVAREZ HUAYHUA, WILNOR IVAN"	                    ,	"MARILU"            	,	"ADMINISTRACIÓN"            	]	,
    "29344434"	:	[	            9	,	"29344434"	,	"982381763"	,	"ALVAREZ IBARCENA, AURELIA ANANI"	                ,	"W. MOLINA"         	,	"PRESTACION"                	]	,
    "70129774"	:	[	            10	,	"70129774"	,	"955703353"	,	"ALVAREZ MENACHO, JOHAN ANDREE"	                    ,	"MARILU"            	,	"PRESTACION"                	]	,
    "47620916"	:	[	            11	,	"47620916"	,	"992543528"	,	"ALVAREZ PAYAHUANCA, ALEX LEONCIO"      	        ,	"MARILU"            	,	"PRESTACION"                	]	,
    "76960039"  :   [               11  ,   "76960039"  ,   "         " ,   "BALDEON SOTO, GONZALO MAIR"                        ,   "YENY"                  ,   "NULO"                          ]   , # NUEVO
    "29664230"	:	[	            12	,	"29664230"	,	"925134147"	,	"ANCO CHARCA, MATILDE CECILIA"	                    ,	"MAXIMO"            	,	"ABASTECIMIENTOS"             	]	,
    "29679521"	:	[	            13	,	"29679521"	,	"989261845"	,	"APAZA CCANA, WILBER"	                            ,	"ROCIO"	                ,	"PRESTACION"                	]	,
    "02172176"	:	[	            14	,	"02172176"	,	"941121941"	,	"APAZA MAMANI, WILSON ROLANDO"	                    ,	"ROCIO"	                ,	"FISCALIZACIÓN"             	]	,
    "04732159"	:	[	            15	,	"04732159"	,	"977131650"	,	"APAZA PANIAGUA, ELBIO ALBERTO"	                    ,	"ROCIO"	                ,	"PRESTACION"                	]	,
    "29538917"	:	[	            16	,	"29538917"	,	"989941160"	,	"APAZA TIZNADO, VICTORIA LUISA"	                    ,	"MARILU"            	,	"ABASTECIMIENTOS"             	]	,
    "76169044"	:	[	            17	,	"76169044"	,	"922122204"	,	"AREVALO BUSTAMANTE, ANDRES GONZALO"	            ,	"WENDY"             	,	"PRESTACION"                	]	,
    "29671014"	:	[	            18	,	"29671014"	,	"960486157"	,	"ARHUIRI MOGOLLON, MARIA LUISA"	                    ,	"ROCIO"	                ,	"TRABAJO SOCIAL"            	]	,
    "71457548"	:	[	            19	,	"71457548"	,	"984759876"	,	"ARIAS CORONEL, ADELAYDE ROCIO"	                    ,	"MARILU"            	,	"PRESTACION"                	]	,
    "29558210"	:	[	            20	,	"29558210"	,	"987721597"	,	"ARIAS LLAZA, VICTOR LUIS"	                        ,	"MARILU"            	,	"PRESTACION"                	]	,
    "74542039"	:	[	            21	,	"74542039"	,	"946939372"	,	"ARREDONDO PUGA, BRISEIDA"	                        ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "74499799"	:	[	            22	,	"74499799"	,	"951706270"	,	"ARREDONDO PUGA, LUZ CAYLA"	                        ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "29337748"	:	[	            23	,	"29337748"	,	"959948368"	,	"AVILA ANAHUE, JULIO CESAR"	                        ,	"W. MOLINA"         	,	"PRESTACION"                	]	,
    "29560983"	:	[	            24	,	"29560983"	,	"990015881"	,	"AVILES SEQUEIROS, ROSAURA"	                        ,	"MARIA"	                ,	"ECONOMÍA"                  	]	,
    "46635324"	:	[	            25	,	"46635324"	,	"910121303"	,	"BARRIENTOS VERA, IGNACIO"	                        ,	"EVANGELINA"        	,	"ECONOMÍA"                  	]	,
    "73878989"	:	[	            26	,	"73878989"	,	"962043087"	,	"BARRIOS GALLEGOS, CARLA ALEJANDRA"	                ,	"MARILU"            	,	"PRESTACION"                	]	,
    "76138379"	:	[	            27	,	"76138379"	,	"961335949"	,	"BAZAN GARCIA, DANIEL JOAQUIN"	                    ,	"MARILU"            	,	"TRABAJO SOCIAL"            	]	,
    "44063382"	:	[	            28	,	"44063382"	,	"927991878"	,	"BEDREGAL CORNEJO, WALTER HUMBERTO"	                ,	"J. BEDREGAL"       	,	"ABASTECIMIENTOS"             	]	,
    "41939373"	:	[	            29	,	"41939373"	,	"953454429"	,	"BEDREGAL CORNEJO, WILFREDO PAUL"	                ,	"J. BEDREGAL"       	,	"ECONOMÍA"                  	]	,
    "29340834"	:	[	            30	,	"29340834"	,	"959219076"	,	"BEDREGAL VARGAS, JOSE INOCENCIO"	                ,	"J. BEDREGAL"       	,	"PRESIDENTE"                	]	,
    "29540849"	:	[	            31	,	"29540849"	,	"975870647"	,	"BELILLE CHALCO, MARILU VIVIANA"	                ,	"W. MOLINA"         	,	"PRESTACION"                	]	,
    "10059583"	:	[	            32	,	"10059583"	,	"944712557"	,	"CENTENO LAZARO DE SEJJE, ROSA ANGELICA"	        ,	"GHINA BALLÓN"      	,	"TRABAJO SOCIAL"            	]	,
    "29553087"	:	[	            33	,	"29553087"	,	"959837776"	,	"BETANCUR ATAJO, FIDEL"	                            ,	"FIDEL B."          	,	"ECONOMÍA"                  	]	,
    "45008193"	:	[	            34	,	"45008193"	,	"958369770"	,	"BUSTAMANTE QUISPE, LOURDES"	                    ,	"BUSTAMANTE"        	,	"ECONOMÍA"                  	]	,
    "41339169"	:	[	            35	,	"41339169"	,	"997076896"	,	"BUSTAMANTE QUISPE, WILBER PORFIRIO"	            ,	"BUSTAMANTE"        	,	"PROMOTORÍA-ADMINISTRACION"	    ]	,
    "73973090"	:	[	            36	,	"73973090"	,	"954787104"	,	"CACERES ABARCA, ROBERTO MARTIN"	                ,	"ROCIO"	                ,	"PRESTACION"                	]	,
    "10315370"	:	[	            37	,	"10315370"	,	"900721800"	,	"CAHUANA INCA, JUAN UBALDINO"	                    ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "70398834"	:	[	            38	,	"70398834"	,	"958920334"	,	"CAJIA COLQUE, IVAN"	                            ,	"IVAN"              	,	"FISCALIZACIÓN"             	]	,
    "46260574"	:	[	            39	,	"46260574"	,	"955142912"	,	"CALDERON CASTRILLON, EDBERSON TOMAS"	            ,	"EVANGELINA"        	,	"FISCALIZACIÓN"             	]	,
    "72413088"	:	[	            40	,	"72413088"	,	"929705555"	,	"CANALES MOTTA, MARGARET VERONIKA"	                ,	"MAXIMO"            	,	"ADMINISTRACIÓN"            	]	,
    "43657189"	:	[	            41	,	"43657189"	,	"973134037"	,	"CANAZA RAMOS, JUAN FRANCISCO"	                    ,	"WENDY"             	,	"PRESTACION"                	]	,
    "29321148"	:	[	            42	,	"29321148"	,	"959901360"	,	"CARDENAS, MANUEL BERNARDO"	                        ,	"MARIA"	                ,	"ECONOMÍA"                  	]	,
    "41424450"	:	[	            43	,	"41424450"	,	"913587232"	,	"CARDENAS ALARCON, LUIS ANGEL"	                    ,	"ROCIO"	                ,	"ABASTECIMIENTOS"             	]	,
    "29468722"	:	[	            44	,	"29468722"	,	"965710719"	,	"CARPIO ARAGON DE NINA, ELIETT VERONICA"	        ,	"MARILU"            	,	"ABASTECIMIENTOS"             	]	,
    "41838084"  :   [               44  ,   "41838084"  ,   "         " ,   "COILA MIRANDA, ALBERTH"                            ,   "YENY"                  ,   "NULO"                          ]   , # NUEVO
    "72240689"	:	[	            45	,	"72240689"	,	"981170892"	,	"CARRASCO JALLO, WASHINGTON PIERO"	                ,	"MARILU"            	,	"ECONOMÍA"                  	]	,
    "04721781"	:	[	            46	,	"04721781"	,	"951729951"	,	"CASTRO CASTRO, SEGUNDO"	                        ,	"ROCIO"	                ,	"ADMINISTRACIÓN"            	]	,
    "41341853"	:	[	            47	,	"41341853"	,	"999561055"	,	"CASTRO LLAMOCA, YENY ROCIO"	                    ,	"IVAN"              	,	"TRABAJO SOCIAL"            	]	,
    "71768368"	:	[	            48	,	"71768368"	,	"989215967"	,	"CCAMA VILLAFUERTE, EMMA ISABEL"	                ,	"MARILU"            	,	"PRESTACION"                	]	,
    "74119784"	:	[	            49	,	"74119784"	,	"997095815"	,	"MACEDO ORE, JAMES FERNANDO"	                    ,	"GHINA BALLÓN"      	,	"ABASTECIMIENTOS"             	]	,
    "40572234"	:	[	            50	,	"40572234"	,	"902265592"	,	"CCAZA MENDOZA, ROSA"	                            ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "42642750"	:	[	            51	,	"42642750"	,	"921388815"	,	"CCAZA MENDOZA, ROSMERI"	                        ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "42955254"	:	[	            52	,	"42955254"	,	"959151200"	,	"CHALCO FIGUEROA, LORENA LIZET"	                    ,	"ROCIO"	                ,	"ECONOMÍA"                  	]	,
    "46022787"	:	[	            53	,	"46022787"	,	"934574739"	,	"CHAMBI AROSQUIPA, ROCIO MILAGROS"	                ,	"ROCIO"	                ,	"TRABAJO SOCIAL"            	]	,
    "02439587"	:	[	            54	,	"02439587"	,	"977384707"	,	"CHAMBI HUARANCA, ANGELICA"	                        ,	"ROCIO"	                ,	"ECONOMÍA"                  	]	,
    "02412064"	:	[	            55	,	"02412064"	,	"936595712"	,	"CHAMBI HUARANCA, MARTINA FLORA"	                ,	"ROCIO"	                ,	"FISCALIZACIÓN"             	]	,
    "10736153"	:	[	            56	,	"10736153"	,	"973888893"	,	"CHAMPI FLORES, EUDOCIA ALEJANDRINA"	            ,	"ROCIO"	                ,	"ABASTECIMIENTOS"             	]	,
    "47380932"	:	[	            57	,	"47380932"	,	"923477118"	,	"CHILLIHUANI ANDRADE, DORIS"	                    ,	"MARILU"            	,	"PRESTACION"                	]	,
    "60273818"	:	[	            58	,	"60273818"	,	"926313237"	,	"CHILLIHUANI CUCHUYRUMI, JAISON"	                ,	"MARILU"            	,	"PRESTACION"                	]	,
    "44835411"	:	[	            59	,	"44835411"	,	"968729113"	,	"CHIRINOS AGUIRRE, MELISSA PAMELA"	                ,	"MAXIMO"            	,	"PRESIDENCIA"	                ]	,
    "71461516"	:	[	            60	,	"71461516"	,	"962219057"	,	"CHIRINOS AGUIRRE, YOISY ALEXANDRA"	                ,	"MAXIMO"            	,	"ADMINISTRACIÓN"            	]	,
    "29366763"	:	[	            61	,	"29366763"	,	"959204811"	,	"CHIRINOS OTAZU, MAXIMO"	                        ,	"MAXIMO"            	,	"FISCALIZACIÓN"             	]	,
    "73509089"	:	[	            62	,	"73509089"	,	"991510064"	,	"CHISE BIZARRO, BEATRIZ"	                        ,	"ROCIO"	                ,	"ADMINISTRACIÓN"            	]	,
    "73509088"	:	[	            63	,	"73509088"	,	"919066393"	,	"CHISE BIZARRO, MARGARITA"	                        ,	"ROCIO"	                ,	"ECONOMÍA"                  	]	,
    "04732076"	:	[	            64	,	"04732076"	,	"941777832"	,	"CHOQUE CASANI, SIXTO"	                            ,	"ROCIO"	                ,	"ABASTECIMIENTOS"             	]	,
    "70553113"	:	[	            65	,	"70553113"	,	"966515192"	,	"CHOQUE COAQUIRA, CYNTHIA IVONNE"	                ,	"MARILU"            	,	"ABASTECIMIENTOS"             	]	,
    "72961601"	:	[	            66	,	"72961601"	,	"950698513"	,	"CHOQUE ROSAS, FLOR DEL PILAR"          	        ,	"IVAN"              	,	"PRESTACION"                	]	,
    "45542086"	:	[	            67	,	"45542086"	,	"986167670"	,	"CHOQUEANCCO GONZALES, GABRIELA RITA"	            ,	"W. MOLINA"         	,	"ECONOMÍA"                  	]	,
    "43944950"	:	[	            68	,	"43944950"	,	"910121303"	,	"CHOQUECONSA CCALLISAYA, HILDA"	                    ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "42059423"	:	[	            69	,	"42059423"	,	"959946667"	,	"CHOQUEHUANCA MAMANI, JUAN FERNANDO"	            ,	"WENDY"             	,	"PRESTACION"                	]	,
    "29735336"	:	[	            70	,	"29735336"	,	"929094682"	,	"COAGUILA COAQUIRA, ELVIRA ELSA"	                ,	"ROCIO"	                ,	"FISCALIZACIÓN"             	]	,
    "40757674"	:	[	            71	,	"40757674"	,	"935778580"	,	"COAGUILA COAQUIRA, YULEYME ISAVED"	                ,	"ROCIO"	                ,	"ECONOMÍA"                  	]	,
    "29327840"	:	[	            72	,	"29327840"	,	"984608826"	,	"COAQUIRA CHOQUE, TEOFILA"	                        ,	"MARILU"            	,	"PRESTACION"                	]	,
    "40950756"	:	[	            73	,	"40950756"	,	"956772506"	,	"COILA MIRANDA, MARIBEL"	                        ,	"MARILU"            	,	"FISCALIZACIÓN"             	]	,
    "02416572"	:	[	            74	,	"02416572"	,	"959910269"	,	"COILA MIRANDA, YENY"	                            ,	"MARILU"            	,	"FISCALIZACIÓN"             	]	,
    "60169050"	:	[	            75	,	"60169050"	,	"901445978"	,	"COJOMA CHAMBI, ARACELI EVELYN"	                    ,	"ROCIO"	                ,	"ABASTECIMIENTOS"             	]	,
    "61880814"	:	[	            76	,	"61880814"	,	"         "	,	"COILA FLORES, RAFAEL ANDRE"	                    ,	"GHINA BALLÓN"      	,	"ABASTECIMIENTOS"             	]	,
    "02384496"	:	[	            77	,	"02384496"	,	"         "	,	"ZANABRIA DE LINO, EMILIANA"	                    ,	"GHINA BALLÓN"      	,	"ABASTECIMIENTOS"             	]	,
    "04732923"	:	[	            78	,	"04732923"	,	"973132234"	,	"COJOMA PEREZ, TADEA SIMONA"	                    ,	"ROCIO"	                ,	"PROMOTORÍA"                	]	,
    "48034842"	:	[	            79	,	"48034842"	,	"957708102"	,	"COJOMA ZABALAGA, DAYNER DENNIS"                    ,	"ROCIO"	                ,	"PRESTACION"                	]	,
    "45389655"	:	[	            80	,	"45389655"	,	"964119209"	,	"COJOMA ZABALAGA, RONAL YULMER"	                    ,	"ROCIO"	                ,	"ECONOMÍA"                  	]	,
    "46022791"	:	[	            81	,	"46022791"	,	"950398966"	,	"COJOMA ZABALAGA, ROYHER JHANZ"	                    ,	"ROCIO"	                ,	"TRABAJO SOCIAL"            	]	,
    "60060061"	:	[	            82	,	"60060061"	,	"967571759"	,	"COLLADO HUAMANI, ARNALDO LUIS"	                    ,	"WENDY"             	,	"PRESTACION"                	]	,
    "43883389"	:	[	            83	,	"43883389"	,	"992274275"	,	"COLQUE VILLANUEVA, XIOMARA VIRGINIA"	            ,	"ANGELA"            	,	"PRESTACION"                	]	,
    "02425725"	:	[	            84	,	"02425725"	,	"958661854"	,	"COLQUEHUANCA RODRIGUEZ, JACINTA"	                ,	"MARILU"            	,	"FISCALIZACIÓN"             	]	,
    "72963655"	:	[	            85	,	"72963655"	,	"958989082"	,	"CONDORI CCOYA, MELANIE ALEJANDRA"	                ,	"MARILU"            	,	"PRESTACION"                	]	,
    "72690599"	:	[	            86	,	"72690599"	,	"907107850"	,	"CORNEJO CHICAÑA, KATHERINE CLAUDIA"    	        ,	"MARILU"            	,	"ECONOMÍA"                  	]	,
    "29341309"	:	[	            87	,	"29341309"	,	"964757284"	,	"CORNEJO DURAN, ROSARIO DAMIANA"	                ,	"J. BEDREGAL"       	,	"ECONOMÍA"                  	]	,
    "29472035"	:	[	            88	,	"29472035"	,	"961347211"	,	"CORONEL QUISPE, ANA MARIA"	                        ,	"MARILU"            	,	"FISCALIZACIÓN"             	]	,
    "04728408"	:	[	            89	,	"04728408"	,	"959579433"	,	"COSSI CONDORI, URBANO FELIX"	                    ,	"MARILU"            	,	"PRESTACION"                	]	,
    "40820488"	:	[	            89	,	"40820488"	,	"         "	,	"CASANA MINAYA, PENNY CYNTHIA"	                    ,	"YENY"	                ,	"NULO"                	        ]	, # NUEVO
    "40610714"	:	[	            90	,	"40610714"	,	"942748693"	,	"CCOSI MAMANI, MARIA CARMEN"	                    ,	"ROCIO"	                ,	"ABASTECIMIENTOS"             	]	,
    "75445170"	:	[	            91	,	"75445170"	,	"945061651"	,	"COSSI SINCHE, ALAN JOB"	                        ,	"MARILU"            	,	"PRESTACION"                	]	,
    "00243926"  :   [               91  ,   "00243926"  ,   "         " ,   "HERNANDEZ RAMIREZ, LUIS ENRIQUE"                   ,   "YENY"                  ,   "NULO"                          ]   , # NUEVO
    "75445345"	:	[	            92	,	"75445345"	,	"997129931"	,	"COSSI SINCHE, DALINA KAREM"	                    ,	"MARILU"            	,	"ADMINISTRACIÓN"            	]	,
    "41917750"  :   [               92  ,   "41917750"  ,   "         " ,   "INCAHUANACO MAMANI, ISMAEL RAUL"                   ,   "YENY"                  ,   "NULO"                          ]   , # NUEVO
    "43438567"	:	[	            93	,	"43438567"	,	"         "	,	"CRUZ ALVAREZ, JULIA MARIA JOANY"	                ,	"W. MOLINA"         	,	"ECONOMÍA"                  	]	,
    "47485216"	:	[	            94	,	"47485216"	,	"958237028"	,	"CRUZ ANCO, DENIS WILY"	                            ,	"ROCIO"	                ,	"PRESTACION"                	]	,
    "29305830"	:	[	            95	,	"29305830"	,	"         "	,	"CRUZ ARENAS, JHONY BRAULIO"	                    ,	"W. MOLINA"         	,	"PRESTACION"                	]	,
    "40726286"	:	[	            96	,	"40726286"	,	"959742163"	,	"CUADROS DIAZ, JUAN CARLOS"	                        ,	"MARILU"            	,	"FISCALIZACIÓN-ADMINISTRACION"	]	,
    "04732954"	:	[	            97	,	"04732954"	,	"940200839"	,	"CUAGUILA RODRIGUEZ, WALDO JUAN"	                ,	"ROCIO"	                ,	"ADMINISTRACIÓN"            	]	,
    "44366282"	:	[	            98	,	"44366282"	,	"958175234"	,	"CUAQUIRA FLORES, ANA MARIA"	                    ,	"ROCIO"	                ,	"ABASTECIMIENTOS"             	]	,
    "41351672"	:	[	            99	,	"41351672"	,	"998919744"	,	"CUCHUYRUMI CONDORI, GENOVEVA"	                    ,	"MARILU"            	,	"PRESTACION"                	]	,
    "29317072"	:	[	            100	,	"29317072"	,	"958912996"	,	"CUEVA MAMANI, INES"	                            ,	"MARIA"	                ,	"TRABAJO SOCIAL"            	]	,
    "40720526"	:	[	            101	,	"40720526"	,	"900376947"	,	"CUSI MALLQUI, ABEL"	                            ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "77816401"	:	[	            102	,	"77816401"	,	"983093416"	,	"DEL AGUILA VILCA, JOB JOEL"	                    ,	"ROCIO"	                ,	"PRESTACION"                	]	,
    "29553479"	:	[	            103	,	"29553479"	,	"948484847"	,	"DIAZ CUEVA, WILBERT DAVID"	                        ,	"MARIA"	                ,	"FISCALIZACIÓN"             	]	,
    "29579680"	:	[	            104	,	"29579680"	,	"957549053"	,	"DIAZ MANCHEGO, VICTOR GAMALIEL"	                ,	"ROCIO"	                ,	"PRESTACION"                	]	,
    "29628481"	:	[	            105	,	"29628481"	,	"973792594"	,	"DIAZ SALAZAR, CARLOS WASHINGTON"	                ,	"MAXIMO"            	,	"PRESTACION"                	]	,
    "41640414"	:	[	            106	,	"41640414"	,	"957880745"	,	"ENCINAS ACO, JOSE ORLANDO"             	        ,	"MARILU"            	,	"ABASTECIMIENTOS"             	]	,
    "41809560"	:	[	            107	,	"41809560"	,	"958258963"	,	"ESPEJO AYALA, DAVID ELVIS"             	        ,	"ANGELA"            	,	"ADMINISTRACIÓN"            	]	,
    "10189542"	:	[	            108	,	"10189542"	,	"945408653"	,	"ESPINAL TEJADA, BRAULIO PEDRO"	                    ,	"MARIA"	                ,	"TRABAJO SOCIAL"            	]	,
    "45474201"	:	[	            109	,	"45474201"	,	"958576886"	,	"FEBRES CHAVEZ, MAYRA"	                            ,	"MAXIMO"            	,	"ABASTECIMIENTOS"             	]	,
    "40736587"	:	[	            110	,	"40736587"	,	"949059979"	,	"FERNANDEZ BERNAL DE GALLEGOS, MARTHA ELIZABETH"	,	"MARILU"            	,	"ADMINISTRACIÓN"            	]	,
    "45930742"	:	[	            111	,	"45930742"	,	"925834427"	,	"FLORES ALVAREZ, ELIDA VELINDA"	                    ,	"ROCIO"	                ,	"PRESTACION"                	]	,
    "70606802"	:	[	            112	,	"70606802"	,	"900834584"	,	"FLORES APAZA, LIZBETH NADIA"	                    ,	"MARILU"            	,	"PRESTACION"                	]	,
    "76157474"	:	[	            113	,	"76157474"	,	"974149132"	,	"FLORES BUSTAMANTE, STEFANY NATALY"             	,	"WENDY"             	,	"PRESTACION"                	]	,
    "75615578"	:	[	            114	,	"75615578"	,	"902446061"	,	"FLORES CONDORI, KELLY LORENA"	                    ,	"MARILU"            	,	"ADMINISTRACIÓN"            	]	,
    "70512723"	:	[	            115	,	"70512723"	,	"966892922"	,	"FLORES GALLEGOS, EDWARD ALEJANDRO"	                ,	"MARILU"            	,	"ADMINISTRACIÓN"            	]	,
    "70512722"	:	[	            116	,	"70512722"	,	"976045923"	,	"FLORES GALLEGOS, SERGIO HYMANOL"	                ,	"MARILU"            	,	"ECONOMÍA"                  	]	,
    "29711637"	:	[	            117	,	"29711637"	,	"918206630"	,	"FLORES MARIÑO, LIZ BEATRIZ"	                    ,	"ROCIO"	                ,	"ECONOMÍA"                  	]	,
    "42396134"	:	[	            118	,	"42396134"	,	"920098954"	,	"FLORES PAYAHUANCA, TEOFILA"	                    ,	"MARILU"            	,	"ABASTECIMIENTOS"             	]	,
    "80455729"  :   [               118,    "80455729"  ,   "         " ,   "MAMANI CAYALTA, EDWIN WILLIAM"                     ,   "YENY"                  ,   "NULO"                          ]   , # NUEVO
    "29642144"	:	[	            119	,	"29642144"	,	"957051406"	,	"FLORES PUMA, EDWARD OSWALDO"	                    ,	"MARILU"            	,	"PRESTACION"                	]	,
    "40238332"	:	[	            120	,	"40238332"	,	"973104819"	,	"FLORES PUMA, ERIKA JULIA"	                        ,	"MARILU"            	,	"ECONOMÍA"                  	]	,
    "29306655"	:	[	            121	,	"29306655"	,	"958330723"	,	"FLORES SANTILLANA, JANET AURORA"	                ,	"MARILU"            	,	"ADMINISTRACIÓN"            	]	,
    "74557450"	:	[	            122	,	"74557450"	,	"982378413"	,	"FLORES VERA, WENDY PENELOPE"	                    ,	"MARILU"            	,	"ADMINISTRACIÓN"            	]	,
    "72745779"	:	[	            123	,	"72745779"	,	"944789909"	,	"FLORES VILCA, BRIAN JOB"	                        ,	"ROCIO"	                ,	"FISCALIZACIÓN"             	]	,
    "45425166"	:	[	            124	,	"45425166"	,	"918554007"	,	"FLORES VILCA, YORDY ANGUIELO"	                    ,	"ROCIO"	                ,	"ADMINISTRACIÓN"            	]	,
    "73455183"	:	[	            125	,	"73455183"	,	"914765578"	,	"GALLEGOS FERNANDEZ, FRANCISCO ALBERTO"	            ,	"MARILU"            	,	"PRESTACION"                	]	,
    "73650299"	:	[	            126	,	"73650299"	,	"912159643"	,	"GALLEGOS PAREDES, HUGO DITHER"	                    ,	"MARILU"            	,	"PRESTACION"                	]	,
    "73650301"	:	[	            127	,	"73650301"	,	"923253570"	,	"GALLEGOS PAREDES, MARILYN ROSARIO"	                ,	"MARILU"            	,	"PRESTACION"                	]	,
    "01332258"	:	[	            128	,	"01332258"	,	"932391092"	,	"GALLEGOS VALENCIA DE JALLO, MARILU ANA"	        ,	"MARILU"            	,	"TRABAJO SOCIAL"            	]	,
    "29557215"	:	[	            129	,	"29557215"	,	"957016555"	,	"GALLEGOS VALENCIA, HENRY ANTONIO"	                ,	"MARILU"            	,	"ABASTECIMIENTOS"             	]	,
    "29346367"	:	[	            130	,	"29346367"	,	"915318350"	,	"GALLEGOS VALENCIA, HUGO TEODORO"	                ,	"MARILU"            	,	"TRABAJO SOCIAL"            	]	,
    "29698838"	:	[	            131	,	"29698838"	,	"978447984"	,	"GALLEGOS VALENCIA, ISABEL YOVANA"	                ,	"MARILU"            	,	"TRABAJO SOCIAL"            	]	,
    "80618125"	:	[	            132	,	"80618125"	,	"954072377"	,	"GALLEGOS VALENCIA, LUIS ALBERTO"	                ,	"MARILU"            	,	"PRESTACION"                	]	,
    "29559108"	:	[	            133	,	"29559108"	,	"927251430"	,	"GALLEGOS VALENCIA, MARIA ASUNTA"	                ,	"MARILU"            	,	"FISCALIZACIÓN"             	]	,
    "29251118"	:	[	            134	,	"29251118"	,	"958073568"	,	"GAMIO MARTINEZ, OSCAR ALFREDO"	                    ,	"MAXIMO"            	,	"PRESTACION"                	]	,
    "47745294"	:	[	            135	,	"47745294"	,	"906301122"	,	"GARCIA ROSAS, LUISA ISABEL"	                    ,	"W. MOLINA"         	,	"PRESTACION"                	]	,
    "71421363"	:	[	            136	,	"71421363"	,	"982169478"	,	"GAVILAN ALLER, ROCIO YESIKA"	                    ,	"WENDY"             	,	"FISCALIZACIÓN"             	]	,
    "43503382"	:	[	            137	,	"43503382"	,	"946251552"	,	"GONZALES CHITE, YUDI ESTHER"	                    ,	"ROCIO"	                ,	"ADMINISTRACIÓN"            	]	,
    "73597451"	:	[	            138	,	"73597451"	,	"921442107"	,	"GUEVARA TORRES, CRISTIAN"	                        ,	"CRISTIAN G."       	,	"FISCALIZACIÓN"             	]	,
    "71863736"	:	[	            139	,	"71863736"	,	"950104246"	,	"GUEVARA TORRES, ROMARIO"	                        ,	"CRISTIAN G."       	,	"TRABAJO SOCIAL"            	]	,
    "73597450"	:	[	            140	,	"73597450"	,	"964180811"	,	"GUEVARA TORRES, ZULEMA"	                        ,	"CRISTIAN G."       	,	"ECONOMÍA"                  	]	,
    "40029162"	:	[	            141	,	"40029162"	,	"901627859"	,	"GUTIERREZ COSTA, ALEX MARTIN"	                    ,	"ANGELA"            	,	"PRESIDENTE"                	]	,
    "71642260"	:	[	            142	,	"71642260"	,	"914635522"	,	"GUTIERREZ JALLO, ERIKA PAMELA"	                    ,	"MARILU"            	,	"PRESTACION"                	]	,
    "29552182"	:	[	            143	,	"29552182"	,	"989990180"	,	"GUTIERREZ PALO, ANGELA GRACIELA"	                ,	"ANGELA"            	,	"PROMOTORÍA"                	]	,
    "73821305"	:	[	            144	,	"73821305"	,	"974337658"	,	"GUTIERREZ PUMA, MELANY LEONORA"	                ,	"EVANGELINA"        	,	"ABASTECIMIENTOS"             	]	,
    "29632063"	:	[	            145	,	"29632063"	,	"936664448"	,	"HANCCO ATAMARI, MARILU JULIA"	                    ,	"MARILU"            	,	"TRABAJO SOCIAL"            	]	,
    "43213330"	:	[	            146	,	"43213330"	,	"986942655"	,	"HANCCO PANCCA, ROSA BETY"	                        ,	"ROCIO"	                ,	"ECONOMÍA"                  	]	,
    "46445333"	:	[	            147	,	"46445333"	,	"948333242"	,	"HAÑARI MAMANI, IMELDA"	                            ,	"ROCIO"	                ,	"FISCALIZACIÓN"             	]	,
    "40972903"	:	[	            148	,	"40972903"	,	"953706381"	,	"HERRERA CABALLERO, JACQUELINE LISSETTE"	        ,	"MARILU"            	,	"FISCALIZACIÓN"             	]	,
    "29670101"	:	[	            149	,	"29670101"	,	"912752646"	,	"HERRERA VILCA, MEYBOL XIOMARA"	                    ,	"MARILU"            	,	"PRESTACION"                	]	,
    "29649039"	:	[	            150	,	"29649039"	,	"989832922"	,	"HUACO FLORES, BEATRIZ ROCIO"	                    ,	"MARILU"            	,	"ECONOMÍA"                  	]	,
    "43636297"	:	[	            151	,	"43636297"	,	"957822324"	,	"HUAHUASONCCO GUZMAN, SONIA"	                    ,	"ROBERTO"	            ,	"ADMINISTRACIÓN"            	]	,
    "71957384"	:	[	            152	,	"71957384"	,	"951250572"	,	"HUAHUASONCCO HANCCO, MEGALYT ROSSIO"	            ,	"IVAN"              	,	"ADMINISTRACIÓN"            	]	,
    "45739321"	:	[	            153	,	"45739321"	,	"927185045"	,	"HUAMAN MAMANI, FRANK WILFREDO"	                    ,	"ROCIO"	                ,	"PRESTACION"                	]	,
    "02168327"	:	[	            154	,	"02168327"	,	"953460234"	,	"HUAMAN MAMANI, MARY LUZ"	                        ,	"ROCIO"	                ,	"PRESTACION"                	]	,
    "42062256"	:	[	            155	,	"42062256"	,	"944077196"	,	"HUAMANI PALOMINO, VERONICA JANETH"	                ,	"WENDY"             	,	"PRESTACION"                	]	,
    "42707017"	:	[	            156	,	"42707017"	,	"971018824"	,	"HUANCA MAMANI, ALICIA"	                            ,	"Alicia"	            ,	"ECONOMÍA"                  	]	,
    "44137660"	:	[	            157	,	"44137660"	,	"921596900"	,	"HUERTA BELLIDO, LEIDY MILAGROS"	                ,	"ROCIO"	                ,	"PRESTACION"                	]	,
    "42449078"	:	[	            158	,	"42449078"	,	"953275454"	,	"INFANTAS GUTIERREZ, DENNY"	                        ,	"MARILU"            	,	"PRESTACION"                	]	,
    "29632167"	:	[	            159	,	"29632167"	,	"923731734"	,	"INFANTES MOLINA, MIGUEL ANGEL"	                    ,	"W. MOLINA"         	,	"PRESTACION"                	]	,
    "29541056"	:	[	            160	,	"29541056"	,	"930503189"	,	"JALLO CORONEL, DOLBERTA ILDA"	                    ,	"MARILU"            	,	"ECONOMÍA"                  	]	,
    "29348568"	:	[	            161	,	"29348568"	,	"994777670"	,	"JALLO CORONEL, VENANCIO ESTEBAN"	                ,	"ROCIO"	                ,	"FISCALIZACIÓN"             	]	,
    "44936053"	:	[	            162	,	"44936053"	,	"958220796"	,	"JALLO GALLEGOS, JULIO DANIEL"                      ,	"MARILU"            	,	"PROMOTORÍA"                	]	,
    "46243075"	:	[	            163	,	"46243075"	,	"972422594"	,	"JALLO GALLEGOS, SHEILA GENESIS"	                ,	"MARILU"            	,	"FISCALIZACIÓN"             	]	,
    "29273553"	:	[	            164	,	"29273553"	,	"947304211"	,	"JALLO ROQUE, GREGORIA NANCY"	                    ,	"MARILU"            	,	"PRESTACION"                	]	,
    "45967801"	:	[	            165	,	"45967801"	,	"963140803"	,	"LASTARRIA ESTAÑA, RUTH LUSMILA"	                ,	"MARIA"	                ,	"ADMINISTRACIÓN"            	]	,
    "41346095"	:	[	            166	,	"41346095"	,	"968420015"	,	"LEON NIEVES, PABLO HERNAN"	                        ,	"MARILU"            	,	"PRESTACION"                	]	,
    "42881035"	:	[	            167	,	"42881035"	,	"980200805"	,	"LINARES LINARES, HANS HARRY"	                    ,	"ANGELA"            	,	"FISCALIZACIÓN"             	]	,
    "40281637"	:	[	            168	,	"40281637"	,	"984916281"	,	"LINO ZANABRIA, MARIELA"	                        ,	"MARILU"            	,	"PROMOTORÍA"                	]	,
    "47315697"	:	[	            169	,	"47315697"	,	"921362223"	,	"REYNOSO GONZALES, DIEGO SEBASTIAN"	                ,	"GHINA BALLÓN"      	,	"FISCALIZACIÓN"             	]	,
    "40005060"	:	[	            170	,	"40005060"	,	"959915100"	,	"MAMANI QUISPE, SILVANA"	                        ,	"GHINA BALLÓN"      	,	"ECONOMÍA"                  	]	,
    "44103470"	:	[	            171	,	"44103470"	,	"951368765"	,	"LLERENA FLORES, ZAMIRA SULAY"	                    ,	"MARILU"            	,	"ABASTECIMIENTOS"             	]	,
    "43898777"	:	[	            172	,	"43898777"	,	"980888527"	,	"LLERENA MONTOYA, ELVIS MIGUEL"	                    ,	"MARILU"            	,	"TRABAJO SOCIAL"            	]	,
    "29310949"	:	[	            173	,	"29310949"	,	"959793595"	,	"LUQUE CALLATA, GRACIELA"	                        ,	"MAXIMO"            	,	"PRESTACION"                	]	,
    "41471430"	:	[	            174	,	"41471430"	,	"958652878"	,	"MACEDO TOLEDO, JANETH CAROLINA"	                ,	"MARILU"            	,	"PRESTACION"                	]	,
    "75876054"	:	[	            175	,	"75876054"	,	"997078908"	,	"MACHACA APAZA, DENIS EDIÑO"	                    ,	"MARILU"            	,	"FISCALIZACIÓN"             	]	,
    "22084327"	:	[	            176	,	"22084327"	,	"950243328"	,	"MALAGA OCHOA, WALTER BENIGNO"	                    ,	"MARILU"            	,	"PRESTACION"                	]	,
    "42100288"	:	[	            177	,	"42100288"	,	"982139545"	,	"MAMANI HUAHUACHAMPI, ROBERTO"	                    ,	"ROBERTO"	            ,	"FISCALIZACIÓN"             	]	,
    "40387458"	:	[	            178	,	"40387458"	,	"950222138"	,	"MAMANI MALDONADO, JOSEFINA"	                    ,	"ROCIO"	                ,	"TRABAJO SOCIAL"            	]	,
    "29365764"	:	[	            179	,	"29365764"	,	"968054939"	,	"MAMANI YANQUI, LUIS MAURO"	                        ,	"M. PALACIOS"       	,	"PRESTACION"                	]	,
    "29335810"	:	[	            180	,	"29335810"	,	"958007490"	,	"MANRIQUE RODRIGUEZ, JOSE RAUL"	                    ,	"W. MOLINA"         	,	"PRESTACION"                	]	,
    "80663981"	:	[	            181	,	"80663981"	,	"964473797"	,	"MAQUE CONDORI, ALVARO MARTIN"	                    ,	"J. RAMOS"          	,	"PRESTACION"                	]	,
    "02384495"	:	[	            182	,	"02384495"	,	"971472356"	,	"LINO DELGADO, PRISCO EDILBERTO"	                ,	"GHINA BALLÓN"      	,	"ABASTECIMIENTOS"             	]	,
    "29327902"	:	[	            183	,	"29327902"	,	"939970029"	,	"MEJIA MENDIGURI, EUSTAQUIO VALENTIN"	            ,	"MARIA"	                ,	"ECONOMÍA"                  	]	,
    "29634804"	:	[	            184	,	"29634804"	,	"935238709"	,	"MEJIA MENDIGURI, VICTORIA SOLEDAD"                 ,	"MARIA"	                ,	"ADMINISTRACIÓN"            	]	,
    "70313876"	:	[	            185	,	"70313876"	,	"954707317"	,	"MEJIA MIRANDA, DIEGO VALENTIN"     	            ,	"MARIA"	                ,	"ECONOMÍA"                  	]	,
    "29514308"	:	[	            186	,	"29514308"	,	"959855815"	,	"MENACHO OBLITAS, FANNY"	                        ,	"MARILU"            	,	"PRESTACION"                	]	,
    "73366489"	:	[	            187	,	"73366489"	,	"938307720"	,	"MENDOZA HANCCO, LUIGGI ARMANDO"	                ,	"MARILU"            	,	"ECONOMÍA"                  	]	,
    "30834834"	:	[	            188	,	"30834834"	,	"958803030"	,	"MENDOZA PERALTA, LUIS ALFREDO"	                    ,	"MARILU"            	,	"ECONOMÍA"                  	]	,
    "29663377"	:	[	            189	,	"29663377"	,	"950368551"	,	"MERMA CCAÑIHUA, BERTHA ALICIA"	                    ,	"MARILU"            	,	"PRESTACION"                	]	,
    "44560904"	:	[	            190	,	"44560904"	,	"971908586"	,	"MERMA MERMA, ANAYIN"	                            ,	"MARILU"            	,	"FISCALIZACIÓN"             	]	,
    "47107807"	:	[	            191	,	"47107807"	,	"953778572"	,	"MEZA ALEJO, MIGUEL ANGEL"	                        ,	"W. MOLINA"         	,	"ABASTECIMIENTOS"             	]	,
    "29636462"	:	[	            192	,	"29636462"	,	"913109449"	,	"MEZA VALDIVIA, LILIAN LETY"	                    ,	"MAXIMO"            	,	"TRABAJO SOCIAL"            	]	,
    "29620415"	:	[	            193	,	"29620415"	,	"945166819"	,	"MIRANDA CUEVA, MARIA ALEJANDRA"	                ,	"MARIA"	                ,	"PROMOTORÍA"                	]	,
    "29412112"	:	[	            194	,	"29412112"	,	"960278253"	,	"MIRANDA HUACHANI, LUIS SABINO"	                    ,	"MARIA"	                ,	"ECONOMÍA"                  	]	,
    "61777807"	:	[	            195	,	"61777807"	,	"989601587"	,	"MIRANDA OSCCO, JUAN ANGEL"	                        ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "46196362"	:	[	            196	,	"46196362"	,	"944066469"	,	"MIRAVAL CHATA, VERONICA YOLANDA"	                ,	"MARILU"            	,	"PRESTACION"                	]	,
    "73775582"	:	[	            197	,	"73775582"	,	"960274065"	,	"MOLINA AGOSTINELLI, FIORELA LORENA"	            ,	"W. MOLINA"         	,	"ECONOMÍA"                  	]	,
    "73775594"	:	[	            198	,	"73775594"	,	"972664400"	,	"MOLINA AGOSTINELLI, SOFIA MANUELA" 	            ,	"W. MOLINA"         	,	"PRESTACION"                	]	,
    "74131096"	:	[	            199	,	"74131096"	,	"972249273"	,	"MOLINA LUQUE, ALEJANDRA GABRIELA"	                ,	"W. MOLINA"         	,	"ECONOMÍA"                  	]	,
    "76129495"	:	[	            200	,	"76129495"	,	"902250255"	,	"MOLINA LUQUE, JIMENA CONSUELO"	                    ,	"W. MOLINA"         	,	"PRESTACION"                	]	,
    "74658119"	:	[	            201	,	"74658119"	,	"970786500"	,	"MOLINA LUQUE, LUIS FELIPE"	                        ,	"W. MOLINA"         	,	"ABASTECIMIENTOS"             	]	,
    "29540887"	:	[	            202	,	"29540887"	,	"936263325"	,	"MOLINA VARGAS, WILBER JUAN"	                    ,	"W. MOLINA"         	,	"ABASTECIMIENTOS"             	]	,
    "29686572"	:	[	            203	,	"29686572"	,	"959850246"	,	"MOTTA QUISPE, VERONICA SIMONA"	                    ,	"MAXIMO"            	,	"ECONOMÍA"                  	]	,
    "45427715"	:	[	            204	,	"45427715"	,	"956753366"	,	"MUÑOZ MUÑOZ, VICTOR HUGO"	                        ,	"ANGELA"            	,	"PRESTACION"                	]	,
    "46406060"	:	[	            205	,	"46406060"	,	"984304829"	,	"NAVARRO JALLO, MARIA FRANCISCA"	                ,	"MARILU"            	,	"PRESTACION"                	]	,
    "30858970"	:	[	            206	,	"30858970"	,	"941272497"	,	"NIEVES ARANA GLADYS EDITH"	                        ,	"MARILU"            	,	"PRESTACION"                	]	,
    "80610157"	:	[	            207	,	"80610157"	,	"974077661"	,	"NINA CALCINA, MARISOL"	                            ,	"MARILU"            	,	"ABASTECIMIENTOS"             	]	,
    "46060572"	:	[	            208	,	"46060572"	,	"915903876"	,	"NINA COLQUE, MAGDALENA"	                        ,	"MARILU"            	,	"FISCALIZACIÓN"             	]	,
    "29328005"	:	[	            209	,	"29328005"	,	"955736982"	,	"NINA FLORES, ROCIO ELVIRA"	                        ,	"IVAN"              	,	"ABASTECIMIENTOS"             	]	,
    "29424416"	:	[	            210	,	"29424416"	,	"974533610"	,	"NINA QUISPE, JUAN TOMAS"	                        ,	"MARILU"            	,	"PRESTACION"                	]	,
    "44614648"	:	[	            211	,	"44614648"	,	"983329069"	,	"NUÑEZ MOLINA, FERNANDO GOMER"	                    ,	"W. MOLINA"         	,	"TRABAJO SOCIAL"            	]	,
    "29291168"	:	[	            212	,	"29291168"	,	"959740318"	,	"NUÑEZ RODRIGUEZ, GASPAR WILFREDO"	                ,	"MAXIMO"            	,	"ECONOMÍA"                  	]	,
    "70390230"	:	[	            213	,	"70390230"	,	"971865102"	,	"ORDOÑEZ LINO, LUIS CARLOS"	                        ,	"MARILU"            	,	"FISCALIZACIÓN"             	]	,
    "41578024"	:	[	            214	,	"41578024"	,	"971886819"	,	"ORE LAYME, ALICIA"	                                ,	"MARILU"            	,	"ECONOMÍA"                  	]	,
    "46591643"	:	[	            215	,	"46591643"	,	"952662757"	,	"OSCCO URBANO, CIRILA"	                            ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "48239363"	:	[	            216	,	"48239363"	,	"972164934"	,	"PACCO CONDORI, ERICK FELICIANO"	                ,	"BUSTAMANTE"        	,	"ECONOMÍA"                  	]	,
    "70217690"	:	[	            217	,	"70217690"	,	"974468911"	,	"PACHECO DELGADO, CHRISTIAN DANIEL"	                ,	"MAXIMO"            	,	"PRESTACION"                	]	,
    "29717523"	:	[	            218	,	"29717523"	,	"959527776"	,	"PACHECO GOZALVEZ, MIGUEL PERCY"	                ,	"MAXIMO"            	,	"FISCALIZACIÓN"             	]	,
    "29362980"	:	[	            219	,	"29362980"	,	"906152072"	,	"PALACIOS LAJO, MANUEL"                             ,	"M. PALACIOS"       	,	"TRABAJO SOCIAL"            	]	,
    "40380177"	:	[	            220	,	"40380177"	,	"937039109"	,	"PALOMINO CIÑA, SANDY ADELA"	                    ,	"M. PALACIOS"       	,	"FISCALIZACIÓN"             	]	,
    "73250760"	:	[	            221	,	"73250760"	,	"927006301"	,	"PANDIA REYES, NUHAD LIZBETH"	                    ,	"WENDY"             	,	"PRESTACION"                	]	,
    "09630365"	:	[	            222	,	"09630365"	,	"912159643"	,	"PAREDES CORREA, ELA MARIA"	                        ,	"MARILU"            	,	"PRESTACION"                	]	,
    "60470878"	:	[	            223	,	"60470878"	,	"966951690"	,	"PAUCARIMA SALDIVAR, RAFAELA"	                    ,	"EVANGELINA"        	,	"ECONOMÍA"                  	]	,
    "30962477"	:	[	            224	,	"30962477"	,	"993496100"	,	"PERALTA CHOCATA GUILLERMO"	                        ,	"CRISTIAN G."       	,	"FISCALIZACIÓN"             	]	,
    "76161787"	:	[	            225	,	"76161787"	,	"956758108"	,	"PERALTA ROJAS, ESTEFANIA VANESA"	                ,	"CRISTIAN G."       	,	"TRABAJO SOCIAL"            	]	,
    "77074029"	:	[	            226	,	"77074029"	,	"966090732"	,	"PEREZ MAMANI, ROSA ANGELICA"	                    ,	"MAXIMO"            	,	"PRESTACION"                	]	,
    "41569302"	:	[	            227	,	"41569302"	,	"948995050"	,	"QUISPE QUISPE, JOSE LUIS"	                        ,	"GHINA BALLÓN"      	,	"ADMINISTRACIÓN"            	]	,
    "76235796"	:	[	            228	,	"76235796"	,	"930978780"	,	"PINTO SALDIVAR, ROYER" 	                        ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "23855533"	:	[	            229	,	"23855533"	,	"930954267"	,	"POCCO CUARESMA, DANIEL"	                        ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "42794362"	:	[	            230	,	"42794362"	,	"958092607"	,	"POCOHUANCA MAZA, ELVIA MIRIAN"	                    ,	"MARILU"            	,	"TRABAJO SOCIAL"            	]	,
    "74542040"	:	[	            231	,	"74542040"	,	"935899091"	,	"POLICARPO PUGA, FLOR SOLEDAD"	                    ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "40001519"	:	[	            232	,	"40001519"	,	"931883065"	,	"POLINO GUTIERREZ, JUAN CARLOS"	                    ,	"ANGELA"            	,	"PRESTACION"                	]	,
    "48700446"	:	[	            233	,	"48700446"	,	"917269150"	,	"PORTUGAL FLORES, YEIME NATHALY"	                ,	"WENDY"             	,	"PRESTACION"                	]	,
    "73896621"	:	[	            234	,	"73896621"	,	"950765863"	,	"ESCALANTE GALLEGOS, FABRICIO ANDRES"	            ,	"GHINA BALLÓN"      	,	"ABASTECIMIENTOS"             	]	,
    "46586545"	:	[	            235	,	"46586545"	,	"926403028"	,	"PUMA CASTELLANOS, ALICIA"	                        ,	"WENDY"             	,	"PRESTACION"                	]	,
    "10426861"	:	[	            236	,	"10426861"	,	"930205534"	,	"QUICAÑA VALERO, JORGE CONCORDIO"	                ,	"J. BEDREGAL"       	,	"ABASTECIMIENTOS"             	]	,
    "42972577"	:	[	            237	,	"42972577"	,	"993426042"	,	"QUINTANA SILVA, JHIMY"	                            ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "29541218"	:	[	            238	,	"29541218"	,	"959980081"	,	"QUISPE APAZA, DAMIANA ANA"	                        ,	"MARILU"            	,	"PRESTACION"                	]	,
    "43318032"	:	[	            239	,	"43318032"	,	"927006301"	,	"QUISPE CACERES, EDY MERCEDO"	                    ,	"MARILU"            	,	"ECONOMÍA"                  	]	,
    "74441428"	:	[	            240	,	"74441428"	,	"929703913"	,	"QUISPE FLORES, ALLISON MISHELLE"	                ,	"ROCIO"	                ,	"TRABAJO SOCIAL"            	]	,
    "43149997"	:	[	            241	,	"43149997"	,	"997519468"	,	"QUISPE HUAHUACONDORI, WILLIAN ROLANDO"	            ,	"MARILU"            	,	"PRESTACION"                	]	,
    "41630929"	:	[	            242	,	"41630929"	,	"914610763"	,	"QUISPE LOPEZ, MARIBEL DINADEYSE"	                ,	"EVANGELINA"        	,	"ABASTECIMIENTOS"             	]	,
    "29303775"	:	[	            243	,	"29303775"	,	"972059904"	,	"QUISPE QUISPE, ELIA"	                            ,	"MARILU"            	,	"ECONOMÍA"                  	]	,
    "73460917"	:	[	            244	,	"73460917"	,	"925230584"	,	"QUISPE QUISPE, NATALIA MARITZA"	                ,	"BUSTAMANTE"        	,	"ECONOMÍA"                  	]	,
    "73368921"	:	[	            245	,	"73368921"	,	"980931751"	,	"QUISPE TORRES, JOEL ARNOLD"	                    ,	"EVANGELINA"        	,	"ECONOMÍA"                  	]	,
    "45866243"	:	[	            246	,	"45866243"	,	"973865243"	,	"QUISPE TORRES, RONALD YRVIN"	                    ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "77177620"	:	[	            247	,	"77177620"	,	"918261574"	,	"QUISPITUPA CHARA, GLORIA"	                        ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "60782567"	:	[	            248	,	"60782567"	,	"944448942"	,	"ORDOÑEZ LINO, CARLOS ARTURO"	                    ,	"GHINA BALLÓN"      	,	"ADMINISTRACIÓN"            	]	,
    "71409506"	:	[	            249	,	"71409506"	,	"956361878"	,	"QUISPITUPA CHARA, SEGUNDINA"	                    ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "02275895"	:	[	            250	,	"02275895"	,	"970673173"	,	"QUIZA SANO, JENNY MARY"	                        ,	"MARILU"            	,	"PRESTACION"                	]	,
    "29665924"	:	[	            251	,	"29665924"	,	"984809507"	,	"RAMOS ADCO, JUAN FRANCISCO"	                    ,	"J. RAMOS"          	,	"FISCALIZACIÓN"             	]	,
    "04732893"	:	[	            252	,	"04732893"	,	"982373500"	,	"RAMOS ALE, TOMAS TEODULO"	                        ,	"ROCIO"	                ,	"TRABAJO SOCIAL"            	]	,
    "45676138"	:	[	            253	,	"45676138"	,	"973552523"	,	"RAMOS COJOMA, GLENY ROCIO"	                        ,	"ROCIO"	                ,	"ECONOMÍA"                  	]	,
    "47221485"	:	[	            254	,	"47221485"	,	"991510064"	,	"RAMOS COJOMA, TEODULO SAUL"	                    ,	"ROCIO"	                ,	"TRABAJO SOCIAL"            	]	,
    "47334323"	:	[	            255	,	"47334323"	,	"939824575"	,	"RAMOS GARAY, MAGGIE CANDY"	                        ,	"ANGELA"            	,	"ECONOMÍA"                  	]	,
    "72743526"	:	[	            256	,	"72743526"	,	"939869821"	,	"RAMOS VALENZUELA, ERICK JOVAN"	                    ,	"J. RAMOS"          	,	"PRESTACION"                	]	,
    "73378741"	:	[	            257	,	"73378741"	,	"973511865"	,	"RIVERA LUQUE, MELIZA JERALDINE"	                ,	"MARILU"            	,	"PRESTACION"                	]	,
    "70516443"	:	[	            258	,	"70516443"	,	"974422313"	,	"RIVERA SOLIS, ADELA JUDIT"	                        ,	"WENDY"             	,	"PRESTACION"                	]	,
    "77381539"	:	[	            259	,	"77381539"	,	"974737485"	,	"RIVERA SOLIS, SHIRLEY FLOR DE MARIA"	            ,	"WENDY"             	,	"TRABAJO SOCIAL"            	]	,
    "42688104"	:	[	            260	,	"42688104"	,	"921160380"	,	"RIVERO MALLQUI, ASUNTA"	                        ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "73500670"	:	[	            261	,	"73500670"	,	"         "	,	"ROBERTS INFANTES, JOAMARCO MANUEL"	                ,	"W. MOLINA"         	,	"PRESTACION"                	]	,
    "45615648"	:	[	            262	,	"45615648"	,	"951104168"	,	"ROQUE LOPEZ, LIZBETH BERTHA"	                    ,	"ROCIO"	                ,	"TRABAJO SOCIAL"            	]	,
    "29634240"	:	[	            263	,	"29634240"	,	"957766528"	,	"ROQUE MAMANI, JULIETH JESUSA"	                    ,	"MARILU"            	,	"FISCALIZACIÓN"             	]	,
    "44086582"	:	[	            264	,	"44086582"	,	"913165285"	,	"ROSAS VELASQUEZ, RUTH"	                            ,	"W. MOLINA"         	,	"ECONOMÍA"                  	]	,
    "80447107"	:	[	            265	,	"80447107"	,	"927854471"	,	"SALDIVAR JAUREGUI, EVANGELINA"	                    ,	"EVANGELINA"        	,	"PROMOTORÍA"                	]	,
    "47548288"	:	[	            266	,	"47548288"	,	"942361026"	,	"SALINAS NIEVES, CHRISTIAN"	                        ,	"MARILU"            	,	"ECONOMÍA"                  	]	,
    "30667317"	:	[	            267	,	"30667317"	,	"923357563"	,	"SANCHEZ RIVERA, LIDA SORAYA"	                    ,	"ROCIO"	                ,	"PRESTACION"                	]	,
    "80550080"	:	[	            268	,	"80550080"	,	"982967923"	,	"SANCHEZ SALCE, ADRIAN"	                            ,	"MARILU"            	,	"PRESTACION"                	]	,
    "45738172"	:	[	            269	,	"45738172"	,	"910756285"	,	"SANTAYANA LUQUE, ANA JOISSI"	                    ,	"MARILU"            	,	"ADMINISTRACIÓN"            	]	,
    "43561859"	:	[	            270	,	"43561859"	,	"982073077"	,	"SARCCO HUAMAN, DAVID"	                            ,	"MARILU"            	,	"PRESTACION"                	]	,
    "40659907"	:	[	            271	,	"40659907"	,	"         "	,	"SOLIS TAPIA, ROGER"	                            ,	"W. MOLINA"         	,	"PRESTACION"                	]	,
    "31028966"	:	[	            272	,	"31028966"	,	"927628227"	,	"SULLCA SULLCAHUAMAN, EBERT"	                    ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "22093383"	:	[	            273	,	"22093383"	,	"956293852"	,	"BURGOS TASSARA, YULL"	                            ,	"EVANGELINA"        	,	"ECONOMÍA"                  	]	,
    "29450264"	:	[	            274	,	"29450264"	,	"954912134"	,	"TALAVERA CUSIRRAMOS, JUAN PASTOR"	                ,	"ANGELA"            	,	"ABASTECIMIENTOS"             	]	,
    "29590909"	:	[	            275	,	"29590909"	,	"959004104"	,	"TALAVERA CUSIRRAMOS, ROBERT DANIEL"	            ,	"ANGELA"            	,	"TRABAJO SOCIAL"            	]	,
    "47154760"	:	[	            276	,	"47154760"	,	"989123742"	,	"TALAVERA GUTIERREZ, JOSSELIN NICOLLE"	            ,	"ANGELA"            	,	"ECONOMÍA"                  	]	,
    "75993394"	:	[	            277	,	"75993394"	,	"952518008"	,	"TAPIA CASTRO, JOSE EMANUEL"	                    ,	"MARILU"            	,	"PRESTACION"                	]	,
    "29346118"	:	[	            278	,	"29346118"	,	"982525634"	,	"TEJADA REYES INCA, LISSETI ROXANA"	                ,	"W. MOLINA"         	,	"TRABAJO SOCIAL"            	]	,
    "30834089"	:	[	            279	,	"30834089"	,	"945724111"	,	"ARUHUANCA CCAMA, ISIDRO JAIME"	                    ,	"GHINA BALLÓN"      	,	"PRESTACION"                	]	,
    "72727970"	:	[	            280	,	"72727970"	,	"924875835"	,	"TEJADA VERA, RUTH ADRIANA"	                        ,	"WENDY"             	,	"PRESTACION"                	]	,
    "72413084"	:	[	            281	,	"72413084"	,	"920106310"	,	"TINTA MOTTA, VALERIA TERESA"	                    ,	"MAXIMO"            	,	"PRESTACION"                	]	,
    "45545560"	:	[	            282	,	"45545560"	,	"918339525"	,	"VALDERRAMA OCHUPE, SOFIA"	                        ,	"EVANGELINA"        	,	"PRESTACION"                	]	,
    "04733030"	:	[	            283	,	"04733030"	,	"930688262"	,	"VALDEZ ESQUIA, BERNABE FELIX"	                    ,	"ROCIO"	                ,	"PRESTACION"                	]	,
    "41931254"	:	[	            284	,	"41931254"	,	"999666027"	,	"VALDIVIA GUTIERREZ, DARLYN JUNIOR"	                ,	"WENDY"             	,	"PRESTACION"                	]	,
    "73378737"	:	[	            285	,	"73378737"	,	"950813197"	,	"VALDIVIA LUQUE, ADRIANA ISABEL"	                ,	"MARILU"            	,	"PRESTACION"                	]	,
    "73378743"	:	[	            286	,	"73378743"	,	"979338492"	,	"VALDIVIA LUQUE, DARIANA ANGELA"	                ,	"MARILU"            	,	"ADMINISTRACIÓN"            	]	,
    "41409592"	:	[	            287	,	"41409592"	,	"902247397"	,	"VALENZUELA CONDORI, SONIA"	                        ,	"J. RAMOS"          	,	"FISCALIZACIÓN"             	]	,
    "76452291"	:	[	            288	,	"76452291"	,	"935055185"	,	"VARGAS HUAMANI, CARLA JANETH"	                    ,	"MARILU"            	,	"ADMINISTRACIÓN"            	]	,
    "60489108"	:	[	            289	,	"60489108"	,	"931178769"	,	"VARGAS HUAMANI, CAROL JANETH"	                    ,	"WENDY"             	,	"PRESTACION"                	]	,
    "60063481"	:	[	            290	,	"60063481"	,	"931689728"	,	"VASQUEZ COAGUILA, KARLA ROMINA"	                ,	"ROCIO"	                ,	"PRESTACION"                	]	,
    "29610869"	:	[	            291	,	"29610869"	,	"925227713"	,	"PAREDES PACHECO, ALEXANDER"	                    ,	"GHINA BALLÓN"      	,	"FISCALIZACIÓN"             	]	,
    "29624525"	:	[	            292	,	"29624525"	,	"925206882"	,	"VERA ALIAGA, ZULEMA JESUS"	                        ,	"MARILU"            	,	"PRESTACION"                	]	,
    "72963057"	:	[	            293	,	"72963057"	,	"         "	,	"VILCA JINCHO, KAREN JESEBEL"	                    ,	"W. MOLINA"         	,	"PRESTACION"                	]	,
    "75385721"	:	[	            294	,	"75385721"	,	"932871229"	,	"VILLALOBOS GARAY, PAUL WASHINGTON"	                ,	"ANGELA"            	,	"PRESTACION"                	]	,
    "75385720"	:	[	            295	,	"75385720"	,	"932870927"	,	"VILLALOBOS GARAY, JACOB ALEJANDRO"	                ,	"ANGELA"            	,	"PRESTACION"                	]	,
    "73095499"	:	[	            296	,	"73095499"	,	"946698824"	,	"VILLEGAS GALLEGOS, JEFFER ALEXANDER"	            ,	"EVANGELINA"        	,	"ECONOMÍA"                  	]	,
    "04732755"	:	[	            297	,	"04732755"	,	"966728613"	,	"ZABALAGA ALEJO, TEODOCIA SUSANA"	                ,	"ROCIO"	                ,	"ECONOMÍA"                  	]	,
    "29734769"	:	[	            298	,	"29734769"	,	"927941378"	,	"ZABALAGA FLORES, JUAN HUALVERTO"	                ,	"ROCIO"	                ,	"ADMINISTRACIÓN"            	]	,
    "41625164"	:	[	            299	,	"41625164"	,	"907327848"	,	"ZABALAGA FLORES, PEDRO ROBERTO"	                ,	"ROCIO"	                ,	"TRABAJO SOCIAL"            	]	,
    "75181447"	:	[	            300	,	"75181447"	,	"953221688"	,	"ZAMBRANO ARTEAGA, ANGIE CAMILA"	                ,	"ROCIO"	                ,	"ADMINISTRACIÓN"            	]	,
    "25460363"	:	[	            301	,	"25460363"	,	"945725943"	,	"ZAMBRANO FLORES, JAVIER"	                        ,	"ROCIO"	                ,	"ADMINISTRACIÓN"            	]	,
    "72782089"	:	[	            302	,	"72782089"	,	"922412040"	,	"ZAMBRANO SANCHEZ, DIEGO JAVIER"	                ,	"ROCIO"	                ,	"ECONOMÍA"                  	]	,
    "18210587"	:	[	            303	,	"18210587"	,	"970874034"	,	"CASANA MINAYA, OMAR DENYS"	                        ,	"GHINA BALLÓN"      	,	"ECONOMÍA"                  	]	,
    "10088545"	:	[	            304	,	"10088545"	,	"949910752"	,	"CHIRI ZEGARRA, SILVIA"                             ,	"GHINA BALLÓN"      	,	"ECONOMÍA"                  	]	,
    "02438195"  :   [               304 ,   "02438195"  ,   "         " ,   "RODRIGUEZ HUANCA, INES"                            ,   "YENY"                  ,   "NULO"                          ]   , # NUEVO
    "70063484"	:	[	            305	,	"70063484"	,	"994332608"	,	"CHOQUE APAZA, DAVID"	                            ,	"GHINA BALLÓN"      	,	"FISCALIZACIÓN"             	]	,
    "02440396"	:	[	            306	,	"02440396"	,	"950040410"	,	"CHOQUE APAZA, RICHARD WALTER"	                    ,	"GHINA BALLÓN"      	,	"FISCALIZACIÓN"             	]	,
    "29610134"  :   [               306 ,   "29610134"  ,   "         " ,   "SALAZAR MOGOLLON, RITA MONICA"                     ,   "YENY"                  ,   "NULO"                          ]   , # NUEVO
    "02437768"	:	[	            307	,	"02437768"	,	"951625161"	,	"COILA MIRANDA, ELSA"	                            ,	"GHINA BALLÓN"      	,	"PROMOTORÍA"                	]	,
    "40689301"	:	[	            308	,	"40689301"	,	"951074707"	,	"COILA MIRANDA, PABLO CESAR"	                    ,	"GHINA BALLÓN"      	,	"ADMINISTRACIÓN"            	]	,
    "02435175"	:	[	            309	,	"02435175"	,	"959222875"	,	"LINO ZANABRIA, EDILBERTO"	                        ,	"GHINA BALLÓN"      	,	"FISCALIZACIÓN"             	]	,
    "29662719"	:	[	            310	,	"29662719"	,	"927747025"	,	"MACEDO QUISPE, TONY DIONICIO"	                    ,	"GHINA BALLÓN"      	,	"FISCALIZACIÓN"             	]	,
    "29429346"	:	[	            311	,	"29429346"	,	"         "	,	"CHIRI ZEGARRA, MARIBEL"	                        ,	"GHINA BALLÓN"      	,	"TRABAJO SOCIAL"            	]	,
    "02441378"  :   [               311 ,   "02441378"  ,   "         " ,   "SANCHEZ VDA. DE MAMANI, PASCUALA"                  ,   "YENY"                  ,   "NULO"                          ]   , # NUEVO
    "46276257"	:	[	"2  PROMOTORIA"	,	"46276257"	,	"         "	,	"CENTENO CHALLA, MARCO ANTONIO"	                    ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
#   "29633007"	:	[	"3  PROMOTORIA"	,	"29633007"	,	"         "	,	"CHACON GONZALES ROXANA EMPERATRIZ"	                ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
    "29624686"	:	[	"4  PROMOTORIA"	,	"29624686"	,	"         "	,	"CONDORI PINTO, SANTOS"	                            ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
    "48507520"	:	[	"5  PROMOTORIA"	,	"48507520"	,	"         "	,	"CONDORI SUNI, EDWARD FERNANDO"	                    ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
    "74048973"  :   [   "6  PROMOTORIA" ,   "74048973"  ,   "         " ,   "SARAVIA CORBEÑA, SEBASTIAN"                        ,   "GHINA BALLÓN"          ,   "PROMOTORIA"                    ]   ,
    "76658804"	:	[	"7  PROMOTORIA"	,	"02447538"	,	"         "	,	"SUMI RAMOS, VALERIO"	                            ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
#   "41380535"	:	[	"8  PROMOTORIA"	,	"41380535"	,	"         "	,	"LLANOS PUMA JOSE LUIS"	                            ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
    "80455729"	:	[	"9  PROMOTORIA"	,	"80455729"	,	"         "	,	"MAMANI CAYALTA EDWIN WILLIAN"	                    ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
    "02441774"	:	[	"10 PROMOTORIA"	,	"02441774"	,	"         "	,	"MAMANI CRUZ RENE DAVID"	                        ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
    "44044493"	:	[	"11 PROMOTORIA"	,	"44044493"	,	"         "	,	"MAMANI SANCHEZ LISBETH CLARA"	                    ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
    "48062527"	:	[	"12 PROMOTORIA"	,	"48062527"	,	"         "	,	"MAMANI SANCHEZ, MARIO CIPRIANI"	                ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
    "74656149"	:	[	"13 PROMOTORIA"	,	"74656149"	,	"         "	,	"MIÑANO ACOSTA, PABLO RODOLFO"	                    ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
    "29649988"	:	[	"17 PROMOTORIA"	,	"29649988"	,	"         "	,	"TORRES SARAVIA LUZ MARINA"	                        ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
    "46149236"	:	[	"18 PROMOTORIA"	,	"46149236"	,	"         "	,	"VELARDE COILA, KATYA PAOLA"	                    ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
#   "43487968"	:	[	"19 PROMOTORIA"	,	"43487968"	,	"         "	,	"VIDAL LARICO MARCO ALONSO"	                        ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
    "47737671"	:	[	"19 PROMOTORIA"	,	"47737671"	,	"         "	,	"CONDORI SUNI LUIS ALBERTO"	                        ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
    "23958382"  :   [   "22 PROMOTORIA" ,   "23958382"  ,   "         " ,   "CAYALTA LOPEZ, SONIA"                              ,   "GHINA BALLÓN"          ,   "PROMOTORIA"                    ]   ,
    "40820488"	:	[	"23 PROMOTORIA"	,	"40820488"	,	"         "	,	"CASANA MINAYA, CYNTHIA"	                        ,	"GHINA BALLÓN"      	,	"PROMOTORIA"                	]	,
    "29738928"	:	[	"01 PROMOTORIA"	,	"29738928"	,	"         "	,	"ACOSTA VIZCARRA, HOMERO ENRIQUE"	                ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "76411584"	:	[	"02 PROMOTORIA"	,	"76411584"	,	"         "	,	"BALDEON SOTO, BRIAN ALFREDO"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "75651416"	:	[	"03 PROMOTORIA"	,	"75651416"	,	"         "	,	"BALDEON SOTO, WILFREDO DANIEL"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "47555420"	:	[	"04 PROMOTORIA"	,	"47555420"	,	"         "	,	"CABANILLAS SERRANO, AMANDA ELIZABETH"	            ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "01486431"	:	[	"05 PROMOTORIA"	,	"01486431"	,	"         "	,	"CALCINA VILCAPAZA, MARCIAL DIEGO"	                ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "43989842"	:	[	"06 PROMOTORIA"	,	"43989842"	,	"         "	,	"CALLA MAMANI, KARREN PATRICIA"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "71801673"	:	[	"07 PROMOTORIA"	,	"71801673"	,	"         "	,	"CHIRI VILCA, YEFFERSON DAVID"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "43179140"	:	[	"08 PROMOTORIA"	,	"43179140"	,	"         "	,	"CHIRI ZEGARRA, ALEJANDRO"	                        ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "40588814"	:	[	"09 PROMOTORIA"	,	"40588814"	,	"         "	,	"CHIRI ZEGARRA, ANITA"	                            ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "29429346"	:	[	"10 PROMOTORIA"	,	"29429346"	,	"         "	,	"CHIRI ZEGARRA, MARIBEL"	                        ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "10088545"	:	[	"11 PROMOTORIA"	,	"10088545"	,	"         "	,	"CHIRI ZEGARRA, SILVIA"	                            ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "02440396"	:	[	"12 PROMOTORIA"	,	"02440396"	,	"         "	,	"CHOQUE APAZA, RICHARD WALTER"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "80374986"	:	[	"13 PROMOTORIA"	,	"80374986"	,	"         "	,	"CHURATA MIRANDA, JOSE LUIS"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "46776095"	:	[	"14 PROMOTORIA"	,	"46776095"	,	"         "	,	"CONDORI VILCA, EDSON ENRIQUE"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "29623309"	:	[	"15 PROMOTORIA"	,	"29623309"	,	"         "	,	"CUTIPA CABANA, GASPAR BALTAZAR"	                ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "71927405"	:	[	"16 PROMOTORIA"	,	"71927405"	,	"         "	,	"GARATE RIVERA, LUZ MILAGROS"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "75786460"	:	[	"17 PROMOTORIA"	,	"75786460"	,	"         "	,	"HUANCCO HUANCCO, CRISTIAN YONI"	                ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "75797827"	:	[	"18 PROMOTORIA"	,	"75797827"	,	"         "	,	"HUANCCO QUISPE, AYDEE MARIBEL"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "44796372"	:	[	"19 PROMOTORIA"	,	"44796372"	,	"         "	,	"HUANCCO QUISPE, JULIO"	                            ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "43517733"	:	[	"20 PROMOTORIA"	,	"43517733"	,	"         "	,	"HUAYTA PAUCAR, ALAN FAUSTINO"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "73694244"	:	[	"22 PROMOTORIA"	,	"73694244"	,	"         "	,	"HUMPIRI VILCA, HENRY"	                            ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "47212100"	:	[	"23 PROMOTORIA"	,	"47212100"	,	"         "	,	"HUMPIRI VILCA, MILTON"	                            ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "02447538"	:	[	"24 PROMOTORIA"	,	"02447538"	,	"         "	,	"LLANOS PUMA, GLADYS ANTONIA"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "70946061"	:	[	"25 PROMOTORIA"	,	"70946061"	,	"         "	,	"LUNA ROQUE, DAYANA ALEJANDRA"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "29581082"	:	[	"26 PROMOTORIA"	,	"29581082"	,	"         "	,	"LUQUE ROJAS, GUISELA"	                            ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "42257320"	:	[	"27 PROMOTORIA"	,	"42257320"	,	"         "	,	"MAMANI CAYALTA, HELBERT MARCIAL"	                ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "47204836"	:	[	"28 PROMOTORIA"	,	"47204836"	,	"         "	,	"MAMANI CUTIPA, CARLOS ALBERTO"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "72280651"	:	[	"29 PROMOTORIA"	,	"72280651"	,	"         "	,	"MAMANI MAYTA, YAJAIRA ROSARIO"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "02435066"	:	[	"32 PROMOTORIA"	,	"02435066"	,	"         "	,	"MENDOZA CRUZ, PEDRO ROBERTO"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "44002807"	:	[	"33 PROMOTORIA"	,	"44002807"	,	"         "	,	"PACHA SUCAPUCA, DIETER JAVIER"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "41898165"	:	[	"34 PROMOTORIA"	,	"41898165"	,	"         "	,	"PACHA SUCAPUCA, EVA"	                            ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "44683616"	:	[	"35 PROMOTORIA"	,	"44683616"	,	"         "	,	"PACORI ZAPANA, CLEVER"	                            ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "75727626"	:	[	"36 PROMOTORIA"	,	"75727626"	,	"         "	,	"QUICO YUCRA, FABRIZIO YOEL"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "41323651"	:	[	"37 PROMOTORIA"	,	"41323651"	,	"         "	,	"QUICO YUCRA, LIZETH MARIBEL"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "29727979"	:	[	"38 PROMOTORIA"	,	"29727979"	,	"         "	,	"QUISPE SANGA, DAVID JOSE"	                        ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "71798794"	:	[	"39 PROMOTORIA"	,	"71798794"	,	"         "	,	"RIOS CHIRI, ANTONY ANIBAL"	                        ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "70175120"	:	[	"40 PROMOTORIA"	,	"70175120"	,	"         "	,	"RODRIGUEZ QUICO, ANELY MADELEYNE"	                ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "42217397"	:	[	"41 PROMOTORIA"	,	"42217397"	,	"         "	,	"ROMAN MATTOS, EDYNNSHON NORELL"	                ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "19260280"	:	[	"42 PROMOTORIA"	,	"19260280"	,	"         "	,	"SERRANO CUBAS, JAIRO NIXON"	                    ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "26730993"	:	[	"43 PROMOTORIA"	,	"26730993"	,	"         "	,	"SERRANO CUBAS, MARIBEL"	                        ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,
    "76651937"	:	[	"44 PROMOTORIA"	,	"76651937"	,	"         "	,	"SUMI RAMOS, JORGE"	                                ,	"GHINA BALLÓN"	        ,	"PROMOTORIA"                	]	,

}

# Listas personalizables de exoneración
exoneracion_entrada = ["70390230", "40281637","30834834", "29632063", "41339169", "45008193"]
exoneracion_multa = ["12345678", "87654321"]
exoneracion_estudiante = ["75385721", "75385720", "72413084", "47154760", "72743526", "60782567", "74441428", "70390230", "45427715", "76129495",
                          "61777807", "73366489", "40005060", "47315697", "73821305", "73455183", "72745779", "70512722", "75445170", "74119784", "61880814", "72963655"]

# Diccionario para almacenar las horas de entrada y salida
registro_asistencia = {}

# Diccionario para contar las veces que se ingresa un DNI
contador_dnis = {}

# Lista para almacenar los registros
registros = []

# Contador de registros autoincrementable
contador_registros = 0

# Función para buscar y mostrar la información
def buscar_persona_por_dni(dni):
    global contador_registros
    current_time = datetime.now().strftime("%I:%M:%S %p")  # Obtener la hora actual

    if dni in diccionario:
        informacion = diccionario[dni]
        nombre_completo = informacion[3]
        lider = informacion[4]
        cargo = informacion[5]
        contador_dnis[dni] = contador_dnis.get(dni, 0) + 1

        # Imprimir en consola la cantidad de veces que un DNI ya ha sido registrado
        if contador_dnis[dni] > 1:
            print(f"El DNI {dni} ya ha sido registrado {contador_dnis[dni]} veces")

        if dni not in registro_asistencia:
            registro_asistencia[dni] = {
                "Nombre": nombre_completo,
                "Entrada": current_time,
                "Salida": "",
                "N°": informacion[0],
                "Celular": informacion[2],
                "Lider": lider,
                "Cargo": cargo,
                "Puesto": contador_registros + 1,
                "Exonerado": "",
                "Pago Entrada": 2  # Pago de 2 soles por defecto
            }
            contador_registros += 1
            print(f"{contador_registros}: {current_time} → {nombre_completo} → {dni} → {lider} → {cargo}")

        # Determinar tipo de exoneración
        if dni in exoneracion_entrada:
            registro_asistencia[dni]["Exonerado"] = "NO PAGA ENTRADA"
            registro_asistencia[dni]["Pago Entrada"] = 0
        elif dni in exoneracion_multa:
            registro_asistencia[dni]["Exonerado"] = "libre de pago de multa"
        elif dni in exoneracion_estudiante:
            registro_asistencia[dni]["Exonerado"] = "ESTUDIANTE, NO PAGA MULTAS NI TARDANZA"

# Función para guardar los registros en un archivo Excel
def guardar_registros_en_excel():
    registros = []
    for dni, informacion in diccionario.items():
        entrada = registro_asistencia[dni]["Entrada"] if dni in registro_asistencia else ""
        puesto = registro_asistencia[dni]["Puesto"] if dni in registro_asistencia else ""
        exonerado = registro_asistencia[dni]["Exonerado"] if dni in registro_asistencia else ""
        pago_entrada = registro_asistencia[dni]["Pago Entrada"] if dni in registro_asistencia else ""

        puntualidad = "INASISTENCIA"
        if entrada:
            entrada_time = datetime.strptime(entrada, "%I:%M:%S %p")
            hora_limite = datetime.strptime("16:50", "%H:%M")
            puntualidad = "ASISTIO" if entrada_time <= hora_limite else "TARDANZA"

        registros.append({
            "Puesto": puesto,
            "N°": informacion[0],
            "DNI": dni,
            "Apellidos y nombres": informacion[3],
            "Lider": informacion[4],
            "Cargo": informacion[5],
            "Hora de entrada": entrada,
            "Pago Entrada": pago_entrada,
            "Exonerado": exonerado,
            "Puntualidad": puntualidad
        })
    df = pd.DataFrame(registros)
    fecha_actual = datetime.now().strftime("%d-%m-%Y")
    nombre_archivo = f"REG_ENTRADA_{fecha_actual}.xlsx"
    df.to_excel(nombre_archivo, index=False, columns=[
                "Puesto", "N°", "DNI", "Apellidos y nombres", "Lider", "Cargo", "Hora de entrada", "Pago Entrada", "Exonerado", "Puntualidad"])

# Función para manejar el ingreso del DNI desde la terminal
def ingresar_dni_terminal():
    while True:
        dni = input("Ingrese el DNI (o 'salir' para terminar): ")
        if dni.lower() == 'salir':
            break
        buscar_persona_por_dni(dni)

# Ejecutar el ingreso de DNI en el hilo principal
ingresar_dni_terminal()

# Guardar los registros en un archivo Excel
guardar_registros_en_excel()
