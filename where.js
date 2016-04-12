myData = [
[30.2929634,120.1689207, '中国浙江省杭州市下城区浙江工业大学 邮政编码: 310000'],
[42.340082,-71.0894884, 'Northeastern, Boston, MA 02115美国'],
[38.2113643,-85.7470011, 'Bradley Ave, Louisville, KY, 美国'],
[32.778949,35.019648, 'Technion/ Sports Building, Haifa'],
[18.4574518,73.8837999, 'Vishwakarma Institutes Play Ground, Yashodhan Society, Kapil Nagar, Kondhwa Budrukh, Vishwakarma, Maharashtra 411048印度'],
[33.1561058,131.826132, '日本〒875-0002 Ōita-ken, Usuki-shi, Shitanoe, 1232−2 ＵＭＤ'],
[42.4036847,-71.120482, 'South Hall Tufts University, 30 Lower Campus Rd, Somerville, MA 02144美国'],
[-38.1518106,145.1345412, 'Monash University, 澳大利亚'],
[53.2948229,69.4047872, '哈萨克斯坦科克舍套邮政编码: 020000'],
[40.7127837,-74.0059413, '美国纽约州纽约'],
[52.2869741,104.3050183, '俄罗斯伊尔库茨克州伊尔库茨克'],
[31.1790053,121.4237432, '中国上海市徐汇区上海交通大学附属第六人民医院 邮政编码: 200231'],
[8.481302,4.611479, 'University Rd, Ilorin, 尼日利亚'],
[-38.3105571,146.4292232, 'Monash University Gippsland Student Lounge, 7N Mary Grant Bruce Dr, Churchill VIC 3842澳大利亚'],
[-34.9221963,138.5922272, 'Yungondi Building, North Terrace, Adelaide SA 5000澳大利亚'],
[47.80949,13.05501, '奥地利萨尔茨堡'],
[61.4977524,23.7609535, '芬兰坦佩雷'],
[59.9342802,30.3350986, '俄罗斯图瓦共和国圣彼得堡'],
[-23.5505199,-46.6333094, '巴西圣保罗州圣保罗圣保罗'],
[54.7903112,32.0503663, '俄罗斯斯摩棱斯克州斯摩棱斯克'],
[24.8614622,67.0099388, '巴基斯坦卡拉奇'],
[40.4469796,-3.7278167, 'Av. Complutense, Madrid, Madrid, 西班牙'],
[24.4325423,54.6174842, 'Masdar Institute Bus Station - Abu Dhabi - 阿拉伯联合酋长国'],
[51.5266171,-0.1260773, 'University Of London, 1-11 Cartwright Gardens, Kings Cross, London WC1H 9EB英国'],
[39.5069974,-84.745231, '美国俄亥俄州牛津邮政编码: 45056'],
[59.393847,24.6650872, 'TTÜ staadion, 12616 Tallinn, 爱沙尼亚'],
[58.3733281,26.7265098, 'Tartu Ülikooli Füüsikahoone, 50103 Tartu, 爱沙尼亚'],
[45.410225,11.893188, 'Universita degli studi di Padova - Ingegneria, 35131 Padova PD, 意大利'],
[18.5544976,73.8257325, 'Pune University, Ganeshkhind, Pune, Maharashtra, 印度'],
[37.8764984,-122.2804342, 'California St, Berkeley, CA, 美国'],
[43.0412831,-89.4301473, 'University of Wisconsin-Madison Arboretum, 1207 Seminole Hwy, Madison, WI 53711美国'],
[51.745806,19.4489068, 'Instytut Informatyki Stosowanej, Politechnika Łódzka, 90-924 Łódź, 波兰'],
[38.3946981,27.0322689, 'İnciraltı, Dokuz Eylül Ünv. Hst., 35330 Balçova/İzmir, 土耳其'],
[39.9314428,116.3049709, '中国北京市海淀区北京师范大学 邮政编码: 100000'],
[37.983917,23.7293599, '希腊雅典'],
[10.7295115,79.0196067, 'Sastra University Road, Tirumalaisamudram, Tamil Nadu 613401印度'],
[21.1470404,79.0397862, 'Nagpur University Campus, Nagpur, Maharashtra 440033印度'],
[38.6633104,-90.3403858, 'Duke Dr, University City, MO 63130美国'],
[37.7634766,-122.4390923, 'States St, San Francisco, CA 94114美国'],
[-23.5505199,-46.6333094, '巴西圣保罗州圣保罗圣保罗'],
[30.2850284,-97.7335226, 'University of Texas at Austin, Austin, TX, 美国'],
[61.6887271,27.2721457, '芬兰圣米歇尔'],
[32.4204729,-85.0323718, 'H. Curtis Pitts Hall, 3413 S Seale Rd, Phenix City, AL 36869美国'],
[41.557583,-8.397568, 'Universidade do Minho, 4710 Braga, 葡萄牙'],
[28.1655981,112.9526566, '中国湖南省长沙市岳麓区岳麓山国家大学科技园创业大厦 邮政编码: 410006'],
[-33.0444219,-71.6066334, 'Pontificia Universidad Catolica De Valparaiso - Gimpert, Valparaíso, Valparaíso, Región de Valparaíso, 智利'],
[40.6331249,-89.3985283, '美国伊利诺伊州'],
[30.0199119,31.5001527, 'AUC Library, Cairo Governorate 11835埃及'],
[55.1170375,36.5970818, '俄罗斯卡卢加州奥勃宁斯克'],
[14.6032462,121.043633, 'Washington, San Juan, Metro Manila, 菲律宾'],
[49.9935,36.230383, '乌克兰哈尔科夫州哈尔科夫'],
[43.8562586,18.4130763, '波斯尼亚 黑塞哥维那萨拉热窝'],
[3.4321247,-76.5461709, 'Parqueadero Universidad Del Valle, Cali, Cali, Valle del Cauca, 哥伦比亚'],
[40.0082221,-105.2591119, 'Colorado Ave & University Heights, Boulder, CO 80302美国'],
[53.4129429,59.0016233, '俄罗斯车里雅宾斯克州马格尼托哥尔斯克'],
[46.4062583,8.9040484, 'Usc, 6749瑞士'],
[34.0247033,-81.0131844, 'New York Ave, Columbia, SC 29204美国'],
[38.1999105,-85.7659121, 'Southern Pkwy, Louisville, KY, 美国'],
[14.6063194,121.0977669, 'Warsaw, Pasig, Metro Manila, 菲律宾'],
[52.2296756,21.0122287, '波兰华沙'],
[-40.900557,174.885971, '新西兰'],
[-40.3850866,175.6140639, 'Massey University, Palmerston North, 新西兰'],
[35.8715218,-97.5672431, 'Noble Ave, Guthrie, OK 73044美国'],
[45.1847248,9.1582069, '意大利帕维亚帕维亚'],
[38.9033716,-92.2785174, 'University of Missouri R1 Dam, Columbia, MO 65201美国'],
[50.0755381,14.4378005, '捷克共和国布拉格'],
[41.8313852,-87.6272216, 'Iit Tower, 10 W 35th St, Chicago, IL 60616美国'],
[40.8072337,-77.8608888, 'Penn State University, College Township, PA 16802美国'],
[33.4249307,-111.8884532, 'Utah, Tempe, AZ 85281美国'],
[39.4813156,-0.3505, 'Universitat Politècnica, 46022 Valencia, Valencia, 西班牙'],
[14.6747569,121.0966402, 'Vienna, Quezon City, Metro Manila, 菲律宾'],
[44.4267674,26.1025384, '罗马尼亚布加勒斯特'],
[33.7063317,-117.7733121, 'New Haven, Irvine, CA 92620美国'],
[47.761605,-122.19303, 'UW Bothell & Cascadia College, Bothell, WA 98011美国'],
[38.6679152,-90.3322259, 'Drexel Dr, University City, MO 63130美国'],
[60.1698557,24.938379, '芬兰赫尔辛基'],
[42.2783714,-83.7371794, 'University of Michigan, Ann Arbor, MI, 美国'],
[40.4432289,-79.9441368, 'Carnegie Mellon University, Pausch Bridge, Pittsburgh, PA 15213美国'],
[55.8304307,49.0660806, '俄罗斯鞑靼斯坦共和国喀山'],
[12.0263438,79.8492812, 'Pondicherry University, Kalapet, Puducherry 605014印度'],
[30.7897514,120.7760636, '中国浙江省嘉兴市秀洲区嘉兴南洋职业技术学院 邮政编码: 314000'],
[35.712815,135.9711705, 'Nyu, Mihama, Mikata District, Fukui Prefecture 919-1201日本'],
[-23.5431786,-46.6291845, '巴西圣保罗州'],
[47.5316049,21.6273123, '匈牙利德布勒森'],
[34.1515641,-117.3354402, 'N State St, California, 美国'],
[50.4501,30.5234, '乌克兰基辅基辅邮政编码: 02000'],
[46.4618977,-80.9664534, 'University Laurentian, Copper Cliff, ON P0M 1N0加拿大'],
[55.755826,37.6173, '俄罗斯莫斯科莫斯科'],
[52.2016671,0.1177882, 'University Of Cambridge, Cambridge, Cambridge, Cambridgeshire CB2英国'],
[35.7209093,50.826614, 'Tehran, Mahdasht, Ordibehesht Rd, University Payam Noor, 伊朗'],
[35.246756,33.0307541, 'ODTÜ Misafirhane, Kalkanlı'],
[46.5189865,6.5676007, 'EPFL, 1015 Lausanne, 瑞士'],
[45.2671352,19.8335496, '塞尔维亚诺维萨德'],
[57.70887,11.97456, '瑞典哥德堡'],
[45.7488716,21.2086793, '罗马尼亚泰梅什堡'],
[53.8931837,27.547338, 'Monument to Fallen Professors and Students of the Belarusian State University, Minsk, 白俄罗斯'],
[22.4828735,88.394867, 'Jadavpur University Lake, Sahid Smirity Colony, Pancha Sayar, Kolkata, West Bengal 700094'],
[26.1529683,91.6639235, 'Gauhati University, Jalukbari, Guwahati, Assam, 印度'],
[-34.4414891,-58.7595663, 'Universidad de Buenos Aires, Manuel Alberti, Buenos Aires, 阿根廷'],
[44.4061457,8.9682634, 'Università degli studi di Genova - Dipartimento di Medicina Sperimentale (DIMES), 16143 Genova, 意大利'],
[13.7164911,100.4874338, '泰国曼谷曼谷吞武里'],
[4.8602595,-74.0333032, 'Universidad De La Sabana, Chía, Chía, Cundinamarca, 哥伦比亚'],
[48.5441917,12.1468532, '德国兰茨胡特'],
[17.4930263,78.3906218, 'Jawaharlal Nehru Technological University, Kukatpally, Hyderabad, Telangana, 印度'],
[50.503887,4.469936, '比利时'],
[42.3400868,-71.1669778, 'Boston College, Boston, MA 02467美国'],
[64.9078809,-147.7117155, 'Manchester Loop, Fairbanks, AK 99712美国'],
[51.1877226,6.7938734, 'Fachhochschule Düsseldorf, 40225 Düsseldorf, 德国'],
[27.6169691,-99.4631289, 'Simon Bolivar Blvd, Laredo, TX 78045美国'],
[39.174335,-86.505469, 'Hilltop Garden and Nature Center at Indiana University, 2367 E 10th St, Bloomington, IN 47408美国'],
[18.9331831,72.8341894, 'KP Shethi Building, Janmabhoomi Marg, Kala Ghoda, Fort, Mumbai, Maharashtra 400001印度'],
[42.3077541,-83.0182189, 'Ottawa St, Windsor, ON, 加拿大'],
[28.3580163,75.5887989, 'BITS, Pilani, Rajasthan 333031印度'],
[38.0269358,-84.5059723, 'University Dr, Lexington, KY, 美国'],
[25.25968,82.989115, 'IIT Gymkhana, RR 11, Banaras Hindu University Campus, Varanasi, Uttar Pradesh 221001印度'],
[50.862282,-2.4998561, 'E M Mitchell & Sons, Hermitage, Dorchester, Dorset DT2 7BB英国'],
[18.4074917,-66.062465, 'Ave Central, San Juan, San Juan, 波多黎各'],
[50.4471975,30.4522355, 'Obshchezhitiye NTUU KPI №10, Vyborzka St, 2/24, Kyiv, 乌克兰'],
[-18.916396,-48.2580759, 'Universidade Federal de Uberlândia - Av. Segismundo Pereira, 2121 - Santa Mônica, Uberlândia - MG, 38400-902巴西'],
[47.497912,19.040235, '匈牙利布达佩斯'],
[55.755826,37.6173, '俄罗斯莫斯科莫斯科'],
[59.9342802,30.3350986, '俄罗斯图瓦共和国圣彼得堡'],
[41.7508391,-88.1535352, '美国伊利诺伊州内珀维尔'],
[37.424106,-122.1660756, '美国加利福尼亚州斯坦福'],
[45.7484997,21.2399277, 'Cantina Politehnică, Strada Alexandru Vaida - Voievod, Timișoara, 罗马尼亚'],
[17.9831867,79.5297432, 'Department of Mechanical Engineering, National Institute of Technology Campus, Hanamkonda, Telangana 506004印度'],
[-35.4158638,149.0897893, 'Monash ACT 2904澳大利亚'],
[-7.2159454,-35.9065247, 'Campo da UFCG - R. Silva Barbosa - Universitário, Campina Grande - PB, 58400-850巴西'],
[19.3188895,-99.1843676, 'National Autonomous University of Mexico, Mexico City, Federal District, 墨西哥'],
[35.7024056,51.3931954, 'Tehran, Tehran, 16 Azar St, Polyclinic of University of Tehran, 伊朗'],
[36.8838958,-76.3040214, 'Old Dominion University, 5115 Hampton Blvd, Norfolk, VA 23508美国'],
[50.4501,30.5234, '乌克兰基辅基辅邮政编码: 02000'],
[32.2366945,-110.9456894, 'Babcock Building, 1717 E Speedway Blvd, Tucson, AZ 85719美国']
];