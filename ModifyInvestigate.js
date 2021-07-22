var SeqColumnName = 1;
var last_elTop = 0;
var last_scrollTop = 0;
var zipcode = [{ "year": 109, "RelationGroupId": 1, "code": "0201", "city": "宜蘭縣", "town": "宜蘭市" }, { "year": 109, "RelationGroupId": 2, "code": "0202", "city": "宜蘭縣", "town": "羅東鎮" }, { "year": 109, "RelationGroupId": 3, "code": "0203", "city": "宜蘭縣", "town": "蘇澳鎮" }, { "year": 109, "RelationGroupId": 4, "code": "0204", "city": "宜蘭縣", "town": "頭城鎮" }, { "year": 109, "RelationGroupId": 5, "code": "0205", "city": "宜蘭縣", "town": "礁溪鄉" }, { "year": 109, "RelationGroupId": 6, "code": "0206", "city": "宜蘭縣", "town": "壯圍鄉" }, { "year": 109, "RelationGroupId": 7, "code": "0207", "city": "宜蘭縣", "town": "員山鄉" }, { "year": 109, "RelationGroupId": 8, "code": "0208", "city": "宜蘭縣", "town": "冬山鄉" }, { "year": 109, "RelationGroupId": 9, "code": "0209", "city": "宜蘭縣", "town": "五結鄉" }, { "year": 109, "RelationGroupId": 10, "code": "0210", "city": "宜蘭縣", "town": "三星鄉" }, { "year": 109, "RelationGroupId": 11, "code": "0211", "city": "宜蘭縣", "town": "大同鄉" }, { "year": 109, "RelationGroupId": 12, "code": "0212", "city": "宜蘭縣", "town": "南澳鄉" }, { "year": 109, "RelationGroupId": 13, "code": "0401", "city": "新竹縣", "town": "竹北市" }, { "year": 109, "RelationGroupId": 14, "code": "0402", "city": "新竹縣", "town": "竹東鎮" }, { "year": 109, "RelationGroupId": 15, "code": "0403", "city": "新竹縣", "town": "新埔鎮" }, { "year": 109, "RelationGroupId": 16, "code": "0404", "city": "新竹縣", "town": "關西鎮" }, { "year": 109, "RelationGroupId": 17, "code": "0405", "city": "新竹縣", "town": "湖口鄉" }, { "year": 109, "RelationGroupId": 18, "code": "0406", "city": "新竹縣", "town": "新豐鄉" }, { "year": 109, "RelationGroupId": 19, "code": "0407", "city": "新竹縣", "town": "芎林鄉" }, { "year": 109, "RelationGroupId": 20, "code": "0408", "city": "新竹縣", "town": "橫山鄉" }, { "year": 109, "RelationGroupId": 21, "code": "0409", "city": "新竹縣", "town": "北埔鄉" }, { "year": 109, "RelationGroupId": 22, "code": "0410", "city": "新竹縣", "town": "寶山鄉" }, { "year": 109, "RelationGroupId": 23, "code": "0411", "city": "新竹縣", "town": "峨眉鄉" }, { "year": 109, "RelationGroupId": 24, "code": "0412", "city": "新竹縣", "town": "尖石鄉" }, { "year": 109, "RelationGroupId": 25, "code": "0413", "city": "新竹縣", "town": "五峰鄉" }, { "year": 109, "RelationGroupId": 26, "code": "0501", "city": "苗栗縣", "town": "苗栗市" }, { "year": 109, "RelationGroupId": 27, "code": "0502", "city": "苗栗縣", "town": "苑裡鎮" }, { "year": 109, "RelationGroupId": 28, "code": "0503", "city": "苗栗縣", "town": "通霄鎮" }, { "year": 109, "RelationGroupId": 29, "code": "0504", "city": "苗栗縣", "town": "竹南鎮" }, { "year": 109, "RelationGroupId": 30, "code": "0505", "city": "苗栗縣", "town": "頭份市" }, { "year": 109, "RelationGroupId": 31, "code": "0506", "city": "苗栗縣", "town": "後龍鎮" }, { "year": 109, "RelationGroupId": 32, "code": "0507", "city": "苗栗縣", "town": "卓蘭鎮" }, { "year": 109, "RelationGroupId": 33, "code": "0508", "city": "苗栗縣", "town": "大湖鄉" }, { "year": 109, "RelationGroupId": 34, "code": "0509", "city": "苗栗縣", "town": "公館鄉" }, { "year": 109, "RelationGroupId": 35, "code": "0510", "city": "苗栗縣", "town": "銅鑼鄉" }, { "year": 109, "RelationGroupId": 36, "code": "0511", "city": "苗栗縣", "town": "南庄鄉" }, { "year": 109, "RelationGroupId": 37, "code": "0512", "city": "苗栗縣", "town": "頭屋鄉" }, { "year": 109, "RelationGroupId": 38, "code": "0513", "city": "苗栗縣", "town": "三義鄉" }, { "year": 109, "RelationGroupId": 39, "code": "0514", "city": "苗栗縣", "town": "西湖鄉" }, { "year": 109, "RelationGroupId": 40, "code": "0515", "city": "苗栗縣", "town": "造橋鄉" }, { "year": 109, "RelationGroupId": 41, "code": "0516", "city": "苗栗縣", "town": "三灣鄉" }, { "year": 109, "RelationGroupId": 42, "code": "0517", "city": "苗栗縣", "town": "獅潭鄉" }, { "year": 109, "RelationGroupId": 43, "code": "0518", "city": "苗栗縣", "town": "泰安鄉" }, { "year": 109, "RelationGroupId": 44, "code": "0701", "city": "彰化縣", "town": "彰化市" }, { "year": 109, "RelationGroupId": 45, "code": "0702", "city": "彰化縣", "town": "鹿港鎮" }, { "year": 109, "RelationGroupId": 46, "code": "0703", "city": "彰化縣", "town": "和美鎮" }, { "year": 109, "RelationGroupId": 47, "code": "0704", "city": "彰化縣", "town": "線西鄉" }, { "year": 109, "RelationGroupId": 48, "code": "0705", "city": "彰化縣", "town": "伸港鄉" }, { "year": 109, "RelationGroupId": 49, "code": "0706", "city": "彰化縣", "town": "福興鄉" }, { "year": 109, "RelationGroupId": 50, "code": "0707", "city": "彰化縣", "town": "秀水鄉" }, { "year": 109, "RelationGroupId": 51, "code": "0708", "city": "彰化縣", "town": "花壇鄉" }, { "year": 109, "RelationGroupId": 52, "code": "0709", "city": "彰化縣", "town": "芬園鄉" }, { "year": 109, "RelationGroupId": 53, "code": "0710", "city": "彰化縣", "town": "員林市" }, { "year": 109, "RelationGroupId": 54, "code": "0711", "city": "彰化縣", "town": "溪湖鎮" }, { "year": 109, "RelationGroupId": 55, "code": "0712", "city": "彰化縣", "town": "田中鎮" }, { "year": 109, "RelationGroupId": 56, "code": "0713", "city": "彰化縣", "town": "大村鄉" }, { "year": 109, "RelationGroupId": 57, "code": "0714", "city": "彰化縣", "town": "埔鹽鄉" }, { "year": 109, "RelationGroupId": 58, "code": "0715", "city": "彰化縣", "town": "埔心鄉" }, { "year": 109, "RelationGroupId": 59, "code": "0716", "city": "彰化縣", "town": "永靖鄉" }, { "year": 109, "RelationGroupId": 60, "code": "0717", "city": "彰化縣", "town": "社頭鄉" }, { "year": 109, "RelationGroupId": 61, "code": "0718", "city": "彰化縣", "town": "二水鄉" }, { "year": 109, "RelationGroupId": 62, "code": "0719", "city": "彰化縣", "town": "北斗鎮" }, { "year": 109, "RelationGroupId": 63, "code": "0720", "city": "彰化縣", "town": "二林鎮" }, { "year": 109, "RelationGroupId": 64, "code": "0721", "city": "彰化縣", "town": "田尾鄉" }, { "year": 109, "RelationGroupId": 65, "code": "0722", "city": "彰化縣", "town": "埤頭鄉" }, { "year": 109, "RelationGroupId": 66, "code": "0723", "city": "彰化縣", "town": "芳苑鄉" }, { "year": 109, "RelationGroupId": 67, "code": "0724", "city": "彰化縣", "town": "大城鄉" }, { "year": 109, "RelationGroupId": 68, "code": "0725", "city": "彰化縣", "town": "竹塘鄉" }, { "year": 109, "RelationGroupId": 69, "code": "0726", "city": "彰化縣", "town": "溪州鄉" }, { "year": 109, "RelationGroupId": 70, "code": "0801", "city": "南投縣", "town": "南投市" }, { "year": 109, "RelationGroupId": 71, "code": "0802", "city": "南投縣", "town": "埔里鎮" }, { "year": 109, "RelationGroupId": 72, "code": "0803", "city": "南投縣", "town": "草屯鎮" }, { "year": 109, "RelationGroupId": 73, "code": "0804", "city": "南投縣", "town": "竹山鎮" }, { "year": 109, "RelationGroupId": 74, "code": "0805", "city": "南投縣", "town": "集集鎮" }, { "year": 109, "RelationGroupId": 75, "code": "0806", "city": "南投縣", "town": "名間鄉" }, { "year": 109, "RelationGroupId": 76, "code": "0807", "city": "南投縣", "town": "鹿谷鄉" }, { "year": 109, "RelationGroupId": 77, "code": "0808", "city": "南投縣", "town": "中寮鄉" }, { "year": 109, "RelationGroupId": 78, "code": "0809", "city": "南投縣", "town": "魚池鄉" }, { "year": 109, "RelationGroupId": 79, "code": "0810", "city": "南投縣", "town": "國姓鄉" }, { "year": 109, "RelationGroupId": 80, "code": "0811", "city": "南投縣", "town": "水里鄉" }, { "year": 109, "RelationGroupId": 81, "code": "0812", "city": "南投縣", "town": "信義鄉" }, { "year": 109, "RelationGroupId": 82, "code": "0813", "city": "南投縣", "town": "仁愛鄉" }, { "year": 109, "RelationGroupId": 83, "code": "0901", "city": "雲林縣", "town": "斗六市" }, { "year": 109, "RelationGroupId": 84, "code": "0902", "city": "雲林縣", "town": "斗南鎮" }, { "year": 109, "RelationGroupId": 85, "code": "0903", "city": "雲林縣", "town": "虎尾鎮" }, { "year": 109, "RelationGroupId": 86, "code": "0904", "city": "雲林縣", "town": "西螺鎮" }, { "year": 109, "RelationGroupId": 87, "code": "0905", "city": "雲林縣", "town": "土庫鎮" }, { "year": 109, "RelationGroupId": 88, "code": "0906", "city": "雲林縣", "town": "北港鎮" }, { "year": 109, "RelationGroupId": 89, "code": "0907", "city": "雲林縣", "town": "古坑鄉" }, { "year": 109, "RelationGroupId": 90, "code": "0908", "city": "雲林縣", "town": "大埤鄉" }, { "year": 109, "RelationGroupId": 91, "code": "0909", "city": "雲林縣", "town": "莿桐鄉" }, { "year": 109, "RelationGroupId": 92, "code": "0910", "city": "雲林縣", "town": "林內鄉" }, { "year": 109, "RelationGroupId": 93, "code": "0911", "city": "雲林縣", "town": "二崙鄉" }, { "year": 109, "RelationGroupId": 94, "code": "0912", "city": "雲林縣", "town": "崙背鄉" }, { "year": 109, "RelationGroupId": 95, "code": "0913", "city": "雲林縣", "town": "麥寮鄉" }, { "year": 109, "RelationGroupId": 96, "code": "0914", "city": "雲林縣", "town": "東勢鄉" }, { "year": 109, "RelationGroupId": 97, "code": "0915", "city": "雲林縣", "town": "褒忠鄉" }, { "year": 109, "RelationGroupId": 98, "code": "0916", "city": "雲林縣", "town": "臺西鄉" }, { "year": 109, "RelationGroupId": 99, "code": "0917", "city": "雲林縣", "town": "元長鄉" }, { "year": 109, "RelationGroupId": 100, "code": "0918", "city": "雲林縣", "town": "四湖鄉" }, { "year": 109, "RelationGroupId": 101, "code": "0919", "city": "雲林縣", "town": "口湖鄉" }, { "year": 109, "RelationGroupId": 102, "code": "0920", "city": "雲林縣", "town": "水林鄉" }, { "year": 109, "RelationGroupId": 103, "code": "1001", "city": "嘉義縣", "town": "太保市" }, { "year": 109, "RelationGroupId": 104, "code": "1002", "city": "嘉義縣", "town": "朴子市" }, { "year": 109, "RelationGroupId": 105, "code": "1003", "city": "嘉義縣", "town": "布袋鎮" }, { "year": 109, "RelationGroupId": 106, "code": "1004", "city": "嘉義縣", "town": "大林鎮" }, { "year": 109, "RelationGroupId": 107, "code": "1005", "city": "嘉義縣", "town": "民雄鄉" }, { "year": 109, "RelationGroupId": 108, "code": "1006", "city": "嘉義縣", "town": "溪口鄉" }, { "year": 109, "RelationGroupId": 109, "code": "1007", "city": "嘉義縣", "town": "新港鄉" }, { "year": 109, "RelationGroupId": 110, "code": "1008", "city": "嘉義縣", "town": "六腳鄉" }, { "year": 109, "RelationGroupId": 111, "code": "1009", "city": "嘉義縣", "town": "東石鄉" }, { "year": 109, "RelationGroupId": 112, "code": "1010", "city": "嘉義縣", "town": "義竹鄉" }, { "year": 109, "RelationGroupId": 113, "code": "1011", "city": "嘉義縣", "town": "鹿草鄉" }, { "year": 109, "RelationGroupId": 114, "code": "1012", "city": "嘉義縣", "town": "水上鄉" }, { "year": 109, "RelationGroupId": 115, "code": "1013", "city": "嘉義縣", "town": "中埔鄉" }, { "year": 109, "RelationGroupId": 116, "code": "1014", "city": "嘉義縣", "town": "竹崎鄉" }, { "year": 109, "RelationGroupId": 117, "code": "1015", "city": "嘉義縣", "town": "梅山鄉" }, { "year": 109, "RelationGroupId": 118, "code": "1016", "city": "嘉義縣", "town": "番路鄉" }, { "year": 109, "RelationGroupId": 119, "code": "1017", "city": "嘉義縣", "town": "大埔鄉" }, { "year": 109, "RelationGroupId": 120, "code": "1018", "city": "嘉義縣", "town": "阿里山鄉" }, { "year": 109, "RelationGroupId": 121, "code": "1301", "city": "屏東縣", "town": "屏東市" }, { "year": 109, "RelationGroupId": 122, "code": "1302", "city": "屏東縣", "town": "潮州鎮" }, { "year": 109, "RelationGroupId": 123, "code": "1303", "city": "屏東縣", "town": "東港鎮" }, { "year": 109, "RelationGroupId": 124, "code": "1304", "city": "屏東縣", "town": "恆春鎮" }, { "year": 109, "RelationGroupId": 125, "code": "1305", "city": "屏東縣", "town": "萬丹鄉" }, { "year": 109, "RelationGroupId": 126, "code": "1306", "city": "屏東縣", "town": "長治鄉" }, { "year": 109, "RelationGroupId": 127, "code": "1307", "city": "屏東縣", "town": "麟洛鄉" }, { "year": 109, "RelationGroupId": 128, "code": "1308", "city": "屏東縣", "town": "九如鄉" }, { "year": 109, "RelationGroupId": 129, "code": "1309", "city": "屏東縣", "town": "里港鄉" }, { "year": 109, "RelationGroupId": 130, "code": "1310", "city": "屏東縣", "town": "鹽埔鄉" }, { "year": 109, "RelationGroupId": 131, "code": "1311", "city": "屏東縣", "town": "高樹鄉" }, { "year": 109, "RelationGroupId": 132, "code": "1312", "city": "屏東縣", "town": "萬巒鄉" }, { "year": 109, "RelationGroupId": 133, "code": "1313", "city": "屏東縣", "town": "內埔鄉" }, { "year": 109, "RelationGroupId": 134, "code": "1314", "city": "屏東縣", "town": "竹田鄉" }, { "year": 109, "RelationGroupId": 135, "code": "1315", "city": "屏東縣", "town": "新埤鄉" }, { "year": 109, "RelationGroupId": 136, "code": "1316", "city": "屏東縣", "town": "枋寮鄉" }, { "year": 109, "RelationGroupId": 137, "code": "1317", "city": "屏東縣", "town": "新園鄉" }, { "year": 109, "RelationGroupId": 138, "code": "1318", "city": "屏東縣", "town": "崁頂鄉" }, { "year": 109, "RelationGroupId": 139, "code": "1319", "city": "屏東縣", "town": "林邊鄉" }, { "year": 109, "RelationGroupId": 140, "code": "1320", "city": "屏東縣", "town": "南州鄉" }, { "year": 109, "RelationGroupId": 141, "code": "1321", "city": "屏東縣", "town": "佳冬鄉" }, { "year": 109, "RelationGroupId": 142, "code": "1322", "city": "屏東縣", "town": "琉球鄉" }, { "year": 109, "RelationGroupId": 143, "code": "1323", "city": "屏東縣", "town": "車城鄉" }, { "year": 109, "RelationGroupId": 144, "code": "1324", "city": "屏東縣", "town": "滿州鄉" }, { "year": 109, "RelationGroupId": 145, "code": "1325", "city": "屏東縣", "town": "枋山鄉" }, { "year": 109, "RelationGroupId": 146, "code": "1326", "city": "屏東縣", "town": "三地門鄉" }, { "year": 109, "RelationGroupId": 147, "code": "1327", "city": "屏東縣", "town": "霧臺鄉" }, { "year": 109, "RelationGroupId": 148, "code": "1328", "city": "屏東縣", "town": "瑪家鄉" }, { "year": 109, "RelationGroupId": 149, "code": "1329", "city": "屏東縣", "town": "泰武鄉" }, { "year": 109, "RelationGroupId": 150, "code": "1330", "city": "屏東縣", "town": "來義鄉" }, { "year": 109, "RelationGroupId": 151, "code": "1331", "city": "屏東縣", "town": "春日鄉" }, { "year": 109, "RelationGroupId": 152, "code": "1332", "city": "屏東縣", "town": "獅子鄉" }, { "year": 109, "RelationGroupId": 153, "code": "1333", "city": "屏東縣", "town": "牡丹鄉" }, { "year": 109, "RelationGroupId": 154, "code": "1401", "city": "臺東縣", "town": "臺東市" }, { "year": 109, "RelationGroupId": 155, "code": "1402", "city": "臺東縣", "town": "成功鎮" }, { "year": 109, "RelationGroupId": 156, "code": "1403", "city": "臺東縣", "town": "關山鎮" }, { "year": 109, "RelationGroupId": 157, "code": "1404", "city": "臺東縣", "town": "卑南鄉" }, { "year": 109, "RelationGroupId": 158, "code": "1405", "city": "臺東縣", "town": "鹿野鄉" }, { "year": 109, "RelationGroupId": 159, "code": "1406", "city": "臺東縣", "town": "池上鄉" }, { "year": 109, "RelationGroupId": 160, "code": "1407", "city": "臺東縣", "town": "東河鄉" }, { "year": 109, "RelationGroupId": 161, "code": "1408", "city": "臺東縣", "town": "長濱鄉" }, { "year": 109, "RelationGroupId": 162, "code": "1409", "city": "臺東縣", "town": "太麻里鄉" }, { "year": 109, "RelationGroupId": 163, "code": "1410", "city": "臺東縣", "town": "大武鄉" }, { "year": 109, "RelationGroupId": 164, "code": "1411", "city": "臺東縣", "town": "綠島鄉" }, { "year": 109, "RelationGroupId": 165, "code": "1412", "city": "臺東縣", "town": "海端鄉" }, { "year": 109, "RelationGroupId": 166, "code": "1413", "city": "臺東縣", "town": "延平鄉" }, { "year": 109, "RelationGroupId": 167, "code": "1414", "city": "臺東縣", "town": "金峰鄉" }, { "year": 109, "RelationGroupId": 168, "code": "1415", "city": "臺東縣", "town": "達仁鄉" }, { "year": 109, "RelationGroupId": 169, "code": "1416", "city": "臺東縣", "town": "蘭嶼鄉" }, { "year": 109, "RelationGroupId": 170, "code": "1501", "city": "花蓮縣", "town": "花蓮市" }, { "year": 109, "RelationGroupId": 171, "code": "1502", "city": "花蓮縣", "town": "鳳林鎮" }, { "year": 109, "RelationGroupId": 172, "code": "1503", "city": "花蓮縣", "town": "玉里鎮" }, { "year": 109, "RelationGroupId": 173, "code": "1504", "city": "花蓮縣", "town": "新城鄉" }, { "year": 109, "RelationGroupId": 174, "code": "1505", "city": "花蓮縣", "town": "吉安鄉" }, { "year": 109, "RelationGroupId": 175, "code": "1506", "city": "花蓮縣", "town": "壽豐鄉" }, { "year": 109, "RelationGroupId": 176, "code": "1507", "city": "花蓮縣", "town": "光復鄉" }, { "year": 109, "RelationGroupId": 177, "code": "1508", "city": "花蓮縣", "town": "豐濱鄉" }, { "year": 109, "RelationGroupId": 178, "code": "1509", "city": "花蓮縣", "town": "瑞穗鄉" }, { "year": 109, "RelationGroupId": 179, "code": "1510", "city": "花蓮縣", "town": "富里鄉" }, { "year": 109, "RelationGroupId": 180, "code": "1511", "city": "花蓮縣", "town": "秀林鄉" }, { "year": 109, "RelationGroupId": 181, "code": "1512", "city": "花蓮縣", "town": "萬榮鄉" }, { "year": 109, "RelationGroupId": 182, "code": "1513", "city": "花蓮縣", "town": "卓溪鄉" }, { "year": 109, "RelationGroupId": 183, "code": "1601", "city": "澎湖縣", "town": "馬公市" }, { "year": 109, "RelationGroupId": 184, "code": "1602", "city": "澎湖縣", "town": "湖西鄉" }, { "year": 109, "RelationGroupId": 185, "code": "1603", "city": "澎湖縣", "town": "白沙鄉" }, { "year": 109, "RelationGroupId": 186, "code": "1604", "city": "澎湖縣", "town": "西嶼鄉" }, { "year": 109, "RelationGroupId": 187, "code": "1605", "city": "澎湖縣", "town": "望安鄉" }, { "year": 109, "RelationGroupId": 188, "code": "1606", "city": "澎湖縣", "town": "七美鄉" }, { "year": 109, "RelationGroupId": 189, "code": "1701", "city": "基隆市", "town": "中正區" }, { "year": 109, "RelationGroupId": 190, "code": "1702", "city": "基隆市", "town": "七堵區" }, { "year": 109, "RelationGroupId": 191, "code": "1703", "city": "基隆市", "town": "暖暖區" }, { "year": 109, "RelationGroupId": 192, "code": "1704", "city": "基隆市", "town": "仁愛區" }, { "year": 109, "RelationGroupId": 193, "code": "1705", "city": "基隆市", "town": "中山區" }, { "year": 109, "RelationGroupId": 194, "code": "1706", "city": "基隆市", "town": "安樂區" }, { "year": 109, "RelationGroupId": 195, "code": "1707", "city": "基隆市", "town": "信義區" }, { "year": 109, "RelationGroupId": 196, "code": "1801", "city": "新竹市", "town": "東區" }, { "year": 109, "RelationGroupId": 197, "code": "1802", "city": "新竹市", "town": "北區" }, { "year": 109, "RelationGroupId": 198, "code": "1803", "city": "新竹市", "town": "香山區" }, { "year": 109, "RelationGroupId": 199, "code": "2001", "city": "嘉義市", "town": "東區" }, { "year": 109, "RelationGroupId": 200, "code": "2002", "city": "嘉義市", "town": "西區" }, { "year": 109, "RelationGroupId": 201, "code": "6301", "city": "臺北市", "town": "松山區" }, { "year": 109, "RelationGroupId": 202, "code": "6302", "city": "臺北市", "town": "信義區" }, { "year": 109, "RelationGroupId": 203, "code": "6303", "city": "臺北市", "town": "大安區" }, { "year": 109, "RelationGroupId": 204, "code": "6304", "city": "臺北市", "town": "中山區" }, { "year": 109, "RelationGroupId": 205, "code": "6305", "city": "臺北市", "town": "中正區" }, { "year": 109, "RelationGroupId": 206, "code": "6306", "city": "臺北市", "town": "大同區" }, { "year": 109, "RelationGroupId": 207, "code": "6307", "city": "臺北市", "town": "萬華區" }, { "year": 109, "RelationGroupId": 208, "code": "6308", "city": "臺北市", "town": "文山區" }, { "year": 109, "RelationGroupId": 209, "code": "6309", "city": "臺北市", "town": "南港區" }, { "year": 109, "RelationGroupId": 210, "code": "6310", "city": "臺北市", "town": "內湖區" }, { "year": 109, "RelationGroupId": 211, "code": "6311", "city": "臺北市", "town": "士林區" }, { "year": 109, "RelationGroupId": 212, "code": "6312", "city": "臺北市", "town": "北投區" }, { "year": 109, "RelationGroupId": 213, "code": "6401", "city": "高雄市", "town": "鹽埕區" }, { "year": 109, "RelationGroupId": 214, "code": "6402", "city": "高雄市", "town": "鼓山區" }, { "year": 109, "RelationGroupId": 215, "code": "6403", "city": "高雄市", "town": "左營區" }, { "year": 109, "RelationGroupId": 216, "code": "6404", "city": "高雄市", "town": "楠梓區" }, { "year": 109, "RelationGroupId": 217, "code": "6405", "city": "高雄市", "town": "三民區" }, { "year": 109, "RelationGroupId": 218, "code": "6406", "city": "高雄市", "town": "新興區" }, { "year": 109, "RelationGroupId": 219, "code": "6407", "city": "高雄市", "town": "前金區" }, { "year": 109, "RelationGroupId": 220, "code": "6408", "city": "高雄市", "town": "苓雅區" }, { "year": 109, "RelationGroupId": 221, "code": "6409", "city": "高雄市", "town": "前鎮區" }, { "year": 109, "RelationGroupId": 222, "code": "6410", "city": "高雄市", "town": "旗津區" }, { "year": 109, "RelationGroupId": 223, "code": "6411", "city": "高雄市", "town": "小港區" }, { "year": 109, "RelationGroupId": 224, "code": "6412", "city": "高雄市", "town": "鳳山區" }, { "year": 109, "RelationGroupId": 225, "code": "6413", "city": "高雄市", "town": "林園區" }, { "year": 109, "RelationGroupId": 226, "code": "6414", "city": "高雄市", "town": "大寮區" }, { "year": 109, "RelationGroupId": 227, "code": "6415", "city": "高雄市", "town": "大樹區" }, { "year": 109, "RelationGroupId": 228, "code": "6416", "city": "高雄市", "town": "大社區" }, { "year": 109, "RelationGroupId": 229, "code": "6417", "city": "高雄市", "town": "仁武區" }, { "year": 109, "RelationGroupId": 230, "code": "6418", "city": "高雄市", "town": "鳥松區" }, { "year": 109, "RelationGroupId": 231, "code": "6419", "city": "高雄市", "town": "岡山區" }, { "year": 109, "RelationGroupId": 232, "code": "6420", "city": "高雄市", "town": "橋頭區" }, { "year": 109, "RelationGroupId": 233, "code": "6421", "city": "高雄市", "town": "燕巢區" }, { "year": 109, "RelationGroupId": 234, "code": "6422", "city": "高雄市", "town": "田寮區" }, { "year": 109, "RelationGroupId": 235, "code": "6423", "city": "高雄市", "town": "阿蓮區" }, { "year": 109, "RelationGroupId": 236, "code": "6424", "city": "高雄市", "town": "路竹區" }, { "year": 109, "RelationGroupId": 237, "code": "6425", "city": "高雄市", "town": "湖內區" }, { "year": 109, "RelationGroupId": 238, "code": "6426", "city": "高雄市", "town": "茄萣區" }, { "year": 109, "RelationGroupId": 239, "code": "6427", "city": "高雄市", "town": "永安區" }, { "year": 109, "RelationGroupId": 240, "code": "6428", "city": "高雄市", "town": "彌陀區" }, { "year": 109, "RelationGroupId": 241, "code": "6429", "city": "高雄市", "town": "梓官區" }, { "year": 109, "RelationGroupId": 242, "code": "6430", "city": "高雄市", "town": "旗山區" }, { "year": 109, "RelationGroupId": 243, "code": "6431", "city": "高雄市", "town": "美濃區" }, { "year": 109, "RelationGroupId": 244, "code": "6432", "city": "高雄市", "town": "六龜區" }, { "year": 109, "RelationGroupId": 245, "code": "6433", "city": "高雄市", "town": "甲仙區" }, { "year": 109, "RelationGroupId": 246, "code": "6434", "city": "高雄市", "town": "杉林區" }, { "year": 109, "RelationGroupId": 247, "code": "6435", "city": "高雄市", "town": "內門區" }, { "year": 109, "RelationGroupId": 248, "code": "6436", "city": "高雄市", "town": "茂林區" }, { "year": 109, "RelationGroupId": 249, "code": "6437", "city": "高雄市", "town": "桃源區" }, { "year": 109, "RelationGroupId": 250, "code": "6438", "city": "高雄市", "town": "那瑪夏區" }, { "year": 109, "RelationGroupId": 251, "code": "6501", "city": "新北市", "town": "板橋區" }, { "year": 109, "RelationGroupId": 252, "code": "6502", "city": "新北市", "town": "三重區" }, { "year": 109, "RelationGroupId": 253, "code": "6503", "city": "新北市", "town": "中和區" }, { "year": 109, "RelationGroupId": 254, "code": "6504", "city": "新北市", "town": "永和區" }, { "year": 109, "RelationGroupId": 255, "code": "6505", "city": "新北市", "town": "新莊區" }, { "year": 109, "RelationGroupId": 256, "code": "6506", "city": "新北市", "town": "新店區" }, { "year": 109, "RelationGroupId": 257, "code": "6507", "city": "新北市", "town": "樹林區" }, { "year": 109, "RelationGroupId": 258, "code": "6508", "city": "新北市", "town": "鶯歌區" }, { "year": 109, "RelationGroupId": 259, "code": "6509", "city": "新北市", "town": "三峽區" }, { "year": 109, "RelationGroupId": 260, "code": "6510", "city": "新北市", "town": "淡水區" }, { "year": 109, "RelationGroupId": 261, "code": "6511", "city": "新北市", "town": "汐止區" }, { "year": 109, "RelationGroupId": 262, "code": "6512", "city": "新北市", "town": "瑞芳區" }, { "year": 109, "RelationGroupId": 263, "code": "6513", "city": "新北市", "town": "土城區" }, { "year": 109, "RelationGroupId": 264, "code": "6514", "city": "新北市", "town": "蘆洲區" }, { "year": 109, "RelationGroupId": 265, "code": "6515", "city": "新北市", "town": "五股區" }, { "year": 109, "RelationGroupId": 266, "code": "6516", "city": "新北市", "town": "泰山區" }, { "year": 109, "RelationGroupId": 267, "code": "6517", "city": "新北市", "town": "林口區" }, { "year": 109, "RelationGroupId": 268, "code": "6518", "city": "新北市", "town": "深坑區" }, { "year": 109, "RelationGroupId": 269, "code": "6519", "city": "新北市", "town": "石碇區" }, { "year": 109, "RelationGroupId": 270, "code": "6520", "city": "新北市", "town": "坪林區" }, { "year": 109, "RelationGroupId": 271, "code": "6521", "city": "新北市", "town": "三芝區" }, { "year": 109, "RelationGroupId": 272, "code": "6522", "city": "新北市", "town": "石門區" }, { "year": 109, "RelationGroupId": 273, "code": "6523", "city": "新北市", "town": "八里區" }, { "year": 109, "RelationGroupId": 274, "code": "6524", "city": "新北市", "town": "平溪區" }, { "year": 109, "RelationGroupId": 275, "code": "6525", "city": "新北市", "town": "雙溪區" }, { "year": 109, "RelationGroupId": 276, "code": "6526", "city": "新北市", "town": "貢寮區" }, { "year": 109, "RelationGroupId": 277, "code": "6527", "city": "新北市", "town": "金山區" }, { "year": 109, "RelationGroupId": 278, "code": "6528", "city": "新北市", "town": "萬里區" }, { "year": 109, "RelationGroupId": 279, "code": "6529", "city": "新北市", "town": "烏來區" }, { "year": 109, "RelationGroupId": 280, "code": "6601", "city": "臺中市", "town": "中區" }, { "year": 109, "RelationGroupId": 281, "code": "6602", "city": "臺中市", "town": "東區" }, { "year": 109, "RelationGroupId": 282, "code": "6603", "city": "臺中市", "town": "南區" }, { "year": 109, "RelationGroupId": 283, "code": "6604", "city": "臺中市", "town": "西區" }, { "year": 109, "RelationGroupId": 284, "code": "6605", "city": "臺中市", "town": "北區" }, { "year": 109, "RelationGroupId": 285, "code": "6606", "city": "臺中市", "town": "西屯區" }, { "year": 109, "RelationGroupId": 286, "code": "6607", "city": "臺中市", "town": "南屯區" }, { "year": 109, "RelationGroupId": 287, "code": "6608", "city": "臺中市", "town": "北屯區" }, { "year": 109, "RelationGroupId": 288, "code": "6609", "city": "臺中市", "town": "豐原區" }, { "year": 109, "RelationGroupId": 289, "code": "6610", "city": "臺中市", "town": "東勢區" }, { "year": 109, "RelationGroupId": 290, "code": "6611", "city": "臺中市", "town": "大甲區" }, { "year": 109, "RelationGroupId": 291, "code": "6612", "city": "臺中市", "town": "清水區" }, { "year": 109, "RelationGroupId": 292, "code": "6613", "city": "臺中市", "town": "沙鹿區" }, { "year": 109, "RelationGroupId": 293, "code": "6614", "city": "臺中市", "town": "梧棲區" }, { "year": 109, "RelationGroupId": 294, "code": "6615", "city": "臺中市", "town": "后里區" }, { "year": 109, "RelationGroupId": 295, "code": "6616", "city": "臺中市", "town": "神岡區" }, { "year": 109, "RelationGroupId": 296, "code": "6617", "city": "臺中市", "town": "潭子區" }, { "year": 109, "RelationGroupId": 297, "code": "6618", "city": "臺中市", "town": "大雅區" }, { "year": 109, "RelationGroupId": 298, "code": "6619", "city": "臺中市", "town": "新社區" }, { "year": 109, "RelationGroupId": 299, "code": "6620", "city": "臺中市", "town": "石岡區" }, { "year": 109, "RelationGroupId": 300, "code": "6621", "city": "臺中市", "town": "外埔區" }, { "year": 109, "RelationGroupId": 301, "code": "6622", "city": "臺中市", "town": "大安區" }, { "year": 109, "RelationGroupId": 302, "code": "6623", "city": "臺中市", "town": "烏日區" }, { "year": 109, "RelationGroupId": 303, "code": "6624", "city": "臺中市", "town": "大肚區" }, { "year": 109, "RelationGroupId": 304, "code": "6625", "city": "臺中市", "town": "龍井區" }, { "year": 109, "RelationGroupId": 305, "code": "6626", "city": "臺中市", "town": "霧峰區" }, { "year": 109, "RelationGroupId": 306, "code": "6627", "city": "臺中市", "town": "太平區" }, { "year": 109, "RelationGroupId": 307, "code": "6628", "city": "臺中市", "town": "大里區" }, { "year": 109, "RelationGroupId": 308, "code": "6629", "city": "臺中市", "town": "和平區" }, { "year": 109, "RelationGroupId": 309, "code": "6701", "city": "臺南市", "town": "新營區" }, { "year": 109, "RelationGroupId": 310, "code": "6702", "city": "臺南市", "town": "鹽水區" }, { "year": 109, "RelationGroupId": 311, "code": "6703", "city": "臺南市", "town": "白河區" }, { "year": 109, "RelationGroupId": 312, "code": "6704", "city": "臺南市", "town": "柳營區" }, { "year": 109, "RelationGroupId": 313, "code": "6705", "city": "臺南市", "town": "後壁區" }, { "year": 109, "RelationGroupId": 314, "code": "6706", "city": "臺南市", "town": "東山區" }, { "year": 109, "RelationGroupId": 315, "code": "6707", "city": "臺南市", "town": "麻豆區" }, { "year": 109, "RelationGroupId": 316, "code": "6708", "city": "臺南市", "town": "下營區" }, { "year": 109, "RelationGroupId": 317, "code": "6709", "city": "臺南市", "town": "六甲區" }, { "year": 109, "RelationGroupId": 318, "code": "6710", "city": "臺南市", "town": "官田區" }, { "year": 109, "RelationGroupId": 319, "code": "6711", "city": "臺南市", "town": "大內區" }, { "year": 109, "RelationGroupId": 320, "code": "6712", "city": "臺南市", "town": "佳里區" }, { "year": 109, "RelationGroupId": 321, "code": "6713", "city": "臺南市", "town": "學甲區" }, { "year": 109, "RelationGroupId": 322, "code": "6714", "city": "臺南市", "town": "西港區" }, { "year": 109, "RelationGroupId": 323, "code": "6715", "city": "臺南市", "town": "七股區" }, { "year": 109, "RelationGroupId": 324, "code": "6716", "city": "臺南市", "town": "將軍區" }, { "year": 109, "RelationGroupId": 325, "code": "6717", "city": "臺南市", "town": "北門區" }, { "year": 109, "RelationGroupId": 326, "code": "6718", "city": "臺南市", "town": "新化區" }, { "year": 109, "RelationGroupId": 327, "code": "6719", "city": "臺南市", "town": "善化區" }, { "year": 109, "RelationGroupId": 328, "code": "6720", "city": "臺南市", "town": "新市區" }, { "year": 109, "RelationGroupId": 329, "code": "6721", "city": "臺南市", "town": "安定區" }, { "year": 109, "RelationGroupId": 330, "code": "6722", "city": "臺南市", "town": "山上區" }, { "year": 109, "RelationGroupId": 331, "code": "6723", "city": "臺南市", "town": "玉井區" }, { "year": 109, "RelationGroupId": 332, "code": "6724", "city": "臺南市", "town": "楠西區" }, { "year": 109, "RelationGroupId": 333, "code": "6725", "city": "臺南市", "town": "南化區" }, { "year": 109, "RelationGroupId": 334, "code": "6726", "city": "臺南市", "town": "左鎮區" }, { "year": 109, "RelationGroupId": 335, "code": "6727", "city": "臺南市", "town": "仁德區" }, { "year": 109, "RelationGroupId": 336, "code": "6728", "city": "臺南市", "town": "歸仁區" }, { "year": 109, "RelationGroupId": 337, "code": "6729", "city": "臺南市", "town": "關廟區" }, { "year": 109, "RelationGroupId": 338, "code": "6730", "city": "臺南市", "town": "龍崎區" }, { "year": 109, "RelationGroupId": 339, "code": "6731", "city": "臺南市", "town": "永康區" }, { "year": 109, "RelationGroupId": 340, "code": "6732", "city": "臺南市", "town": "東區" }, { "year": 109, "RelationGroupId": 341, "code": "6733", "city": "臺南市", "town": "南區" }, { "year": 109, "RelationGroupId": 342, "code": "6734", "city": "臺南市", "town": "北區" }, { "year": 109, "RelationGroupId": 343, "code": "6735", "city": "臺南市", "town": "安南區" }, { "year": 109, "RelationGroupId": 344, "code": "6736", "city": "臺南市", "town": "安平區" }, { "year": 109, "RelationGroupId": 345, "code": "6737", "city": "臺南市", "town": "中西區" }, { "year": 109, "RelationGroupId": 346, "code": "6801", "city": "桃園市", "town": "桃園區" }, { "year": 109, "RelationGroupId": 347, "code": "6802", "city": "桃園市", "town": "中壢區" }, { "year": 109, "RelationGroupId": 348, "code": "6803", "city": "桃園市", "town": "大溪區" }, { "year": 109, "RelationGroupId": 349, "code": "6804", "city": "桃園市", "town": "楊梅區" }, { "year": 109, "RelationGroupId": 350, "code": "6805", "city": "桃園市", "town": "蘆竹區" }, { "year": 109, "RelationGroupId": 351, "code": "6806", "city": "桃園市", "town": "大園區" }, { "year": 109, "RelationGroupId": 352, "code": "6807", "city": "桃園市", "town": "龜山區" }, { "year": 109, "RelationGroupId": 353, "code": "6808", "city": "桃園市", "town": "八德區" }, { "year": 109, "RelationGroupId": 354, "code": "6809", "city": "桃園市", "town": "龍潭區" }, { "year": 109, "RelationGroupId": 355, "code": "6810", "city": "桃園市", "town": "平鎮區" }, { "year": 109, "RelationGroupId": 356, "code": "6811", "city": "桃園市", "town": "新屋區" }, { "year": 109, "RelationGroupId": 357, "code": "6812", "city": "桃園市", "town": "觀音區" }, { "year": 109, "RelationGroupId": 358, "code": "6813", "city": "桃園市", "town": "復興區" }, { "year": 109, "RelationGroupId": 359, "code": "7101", "city": "連江縣", "town": "南竿鄉" }, { "year": 109, "RelationGroupId": 360, "code": "7102", "city": "連江縣", "town": "北竿鄉" }, { "year": 109, "RelationGroupId": 361, "code": "7103", "city": "連江縣", "town": "莒光鄉" }, { "year": 109, "RelationGroupId": 362, "code": "7104", "city": "連江縣", "town": "東引鄉" }, { "year": 109, "RelationGroupId": 363, "code": "7201", "city": "金門縣", "town": "金城鎮" }, { "year": 109, "RelationGroupId": 364, "code": "7202", "city": "金門縣", "town": "金沙鎮" }, { "year": 109, "RelationGroupId": 365, "code": "7203", "city": "金門縣", "town": "金湖鎮" }, { "year": 109, "RelationGroupId": 366, "code": "7204", "city": "金門縣", "town": "金寧鄉" }, { "year": 109, "RelationGroupId": 367, "code": "7205", "city": "金門縣", "town": "烈嶼鄉" }, { "year": 109, "RelationGroupId": 368, "code": "7206", "city": "金門縣", "town": "烏坵鄉" }];
var zipcity = [];
var countycode = [{ "Code": "02", "Name": "宜蘭縣" }, { "Code": "04", "Name": "新竹縣" }, { "Code": "05", "Name": "苗栗縣" }, { "Code": "07", "Name": "彰化縣" }, { "Code": "08", "Name": "南投縣" }, { "Code": "09", "Name": "雲林縣" }, { "Code": "10", "Name": "嘉義縣" }, { "Code": "13", "Name": "屏東縣" }, { "Code": "14", "Name": "臺東縣" }, { "Code": "15", "Name": "花蓮縣" }, { "Code": "16", "Name": "澎湖縣" }, { "Code": "17", "Name": "基隆市" }, { "Code": "18", "Name": "新竹市" }, { "Code": "20", "Name": "嘉義市" }, { "Code": "63", "Name": "臺北市" }, { "Code": "64", "Name": "高雄市" }, { "Code": "65", "Name": "新北市" }, { "Code": "66", "Name": "臺中市" }, { "Code": "67", "Name": "臺南市" }, { "Code": "68", "Name": "桃園市" }, { "Code": "71", "Name": "連江縣" }, { "Code": "72", "Name": "金門縣" }];
var cropcode = [{ "Code": 101, "Name": "S稻作" }, { "Code": 201, "Name": "S硬質玉米（飼料玉米）" }, { "Code": 202, "Name": "S食用玉米" }, { "Code": 203, "Name": "S麥類（大麥、小麥）" }, { "Code": 204, "Name": "S粟（小米）" }, { "Code": 205, "Name": "S蜀黍(高粱)" }, { "Code": 206, "Name": "S大豆（黃豆、珠仔豆、白豆、米豆）" }, { "Code": 207, "Name": "S花豆（大紅豆）" }, { "Code": 208, "Name": "S紅豆" }, { "Code": 209, "Name": "S綠豆" }, { "Code": 210, "Name": "S甘藷（地瓜）" }, { "Code": 211, "Name": "S落花生（土豆）" }, { "Code": 212, "Name": "S薏苡（薏仁）" }, { "Code": 213, "Name": "其他雜糧（黍、蕎麥、蠶豆、紅藜、藜麥、黑豆、樹豆）" }, { "Code": 301, "Name": "L山藥（淮山、紅薯）" }, { "Code": 302, "Name": "L樹薯（木薯）" }, { "Code": 303, "Name": "L茶" }, { "Code": 304, "Name": "S菸草" }, { "Code": 305, "Name": "S芝麻（胡麻）" }, { "Code": 306, "Name": "L瓊麻" }, { "Code": 307, "Name": "牧草（青割玉米、盤固拉、狼尾草）" }, { "Code": 308, "Name": "L桑樹" }, { "Code": 309, "Name": "L荖花（荖藤、荖葉）" }, { "Code": 310, "Name": "L山葵" }, { "Code": 311, "Name": "S綠肥作物（大菜、田菁、大豆、豌豆、富貴豆、鐵虎豆、青皮豆、黃花羽扇豆、虎爪豆、山珠豆、魯冰、紫雲英、太陽麻、油菜、爬地蘭、埃及三葉草、苕子、波斯菊）" }, { "Code": 312, "Name": "L油茶（苦茶樹）" }, { "Code": 313, "Name": "L破布子" }, { "Code": 314, "Name": "L咖啡" }, { "Code": 315, "Name": "L甘蔗" }, { "Code": 316, "Name": "其他特用作物（棉花、藺草、柴胡、當歸、薄荷、黃耆、枸杞、黃芩、麥門冬、七葉膽、刺五加、明日葉、狗尾草、通天草、牛樟芝、牛樟菇、澤瀉、桔梗、除蟲菊、地黃、藤心、洛神花、茉莉、秀英、杭菊、甜菊、桂花、肉桂、可可、黃梔、葛藤、通草、南薑、黃麻、亞麻、苧麻、蒔茶、澳洲茶樹、香茅(香水茅)、蘆薈、無患子、樹蘭、貴黍（掃帚草）、黃梔、仙草、愛玉子、食用仙人掌、天山雪蓮、金線連、諾麗果、山葡萄、薑黃、蛹蟲草、白馬蜈蚣草、腰子草、魚腥草、靈芝草、山胡椒、馬告、石蓮花、月桃葉、貓薄荷、蓖麻、紫蘇、香椿、大風草、南非葉、食用玫瑰" }, { "Code": 401, "Name": "S蘿蔔（菜頭、白蘿蔔）" }, { "Code": 402, "Name": "S胡蘿蔔（紅蘿蔔）" }, { "Code": 403, "Name": "S薑（生薑、老薑、粉薑）" }, { "Code": 404, "Name": "S芋頭（芋頭）" }, { "Code": 405, "Name": "S馬鈴薯" }, { "Code": 406, "Name": "S牛蒡" }, { "Code": 407, "Name": "S蔥（蔥、四季蔥、粉蔥、珠蔥）" }, { "Code": 408, "Name": "S蔥頭（紅蔥頭、大頭蔥、大官蔥、火蔥、毛蔥、朱蔥、冬蔥、油蔥、科蔥、香蔥、慈蔥、綿蔥）" }, { "Code": 409, "Name": "S洋蔥" }, { "Code": 410, "Name": "S青蒜（蒜苗）" }, { "Code": 411, "Name": "S蒜頭（大蒜）" }, { "Code": 412, "Name": "S荸薺" }, { "Code": 413, "Name": "L韭菜" }, { "Code": 414, "Name": "L竹筍（綠竹筍、桂竹筍、轎篙筍、麻竹筍、毛竹筍）" }, { "Code": 415, "Name": "L蘆筍（白蘆筍、綠蘆筍）" }, { "Code": 416, "Name": "S茭白筍" }, { "Code": 417, "Name": "S大芥菜" }, { "Code": 418, "Name": "S大心芥菜（菜心、四川榨菜）" }, { "Code": 419, "Name": "S芹菜（水芹、旱芹、土芹菜、西洋芹）" }, { "Code": 420, "Name": "S蕹菜（空心菜）" }, { "Code": 421, "Name": "S甘藍（高麗菜）" }, { "Code": 422, "Name": "S芥藍（格藍菜）" }, { "Code": 423, "Name": "S球莖甘藍（結頭菜）" }, { "Code": 424, "Name": "S結球白菜（包心白菜、娃娃菜）" }, { "Code": 425, "Name": "S不結球白菜（黃金小白菜、鳳山小白菜、皺葉白菜、廣東白菜、黑葉白菜、青梗白菜、青江白菜、青江菜、蚵白菜、小白菜、青江菜）" }, { "Code": 426, "Name": "S花椰菜(白花菜、青花菜、青花苔)" }, { "Code": 427, "Name": "S菠菜（菠蔆菜）" }, { "Code": 428, "Name": "S莧菜" }, { "Code": 429, "Name": "S萵苣（Ａ菜、吉康菜、本島萵苣、油麥菜、福山萵苣、大陸妹）" }, { "Code": 430, "Name": "S茼蒿" }, { "Code": 431, "Name": "S絲瓜（菜瓜、角瓜）" }, { "Code": 432, "Name": "S越瓜（菴瓜、醃瓜）" }, { "Code": 433, "Name": "S胡瓜（大黃瓜、莿瓜、小黃瓜、櫛瓜、毛瓜、花胡瓜）" }, { "Code": 434, "Name": "S冬瓜" }, { "Code": 435, "Name": "S苦瓜" }, { "Code": 436, "Name": "S扁蒲（蒲子）" }, { "Code": 437, "Name": "S茄子" }, { "Code": 438, "Name": "S番茄（食用番茄、加工番茄、小番茄）" }, { "Code": 439, "Name": "S番椒（青椒、甜椒、辣椒、糯米椒）" }, { "Code": 440, "Name": "S毛豆" }, { "Code": 441, "Name": "S豌豆（荷蘭豆、甜豆）" }, { "Code": 442, "Name": "S長豇豆（菜豆、敏豆、四季豆、醜豆、粉豆）" }, { "Code": 443, "Name": "S西瓜（嘉寶瓜）" }, { "Code": 444, "Name": "S香瓜（美濃瓜）" }, { "Code": 445, "Name": "S洋香瓜（哈蜜瓜）" }, { "Code": 446, "Name": "S瓜子瓜" }, { "Code": 447, "Name": "S草莓" }, { "Code": 448, "Name": "S地瓜葉" }, { "Code": 449, "Name": "S紅菜" }, { "Code": 450, "Name": "S南瓜" }, { "Code": 451, "Name": "L龍鬚菜（佛手瓜）" }, { "Code": 452, "Name": "S蓮藕" }, { "Code": 453, "Name": "L蕨類（過貓、山蘇、山蕨）" }, { "Code": 454, "Name": "S豆苗（豌豆苗、大豆苗）" }, { "Code": 455, "Name": "S菱角" }, { "Code": 456, "Name": "L金針" }, { "Code": 457, "Name": "S香菜（芫荽）" }, { "Code": 458, "Name": "S蓮子" }, { "Code": 459, "Name": "其他蔬菜（高麗菜苗、抱子甘藍、青花筍、玉米筍、川七、紅鳳菜、小芥菜、麻薏、珊瑚草、麒麟菜、水蓮、慈菇、刺蔥、蕗蕎、甜菜根、檳榔心、半天筍、牧草筍、秋葵、香椿、皇宮菜、豆薯、香瓜茄、節豆、皇帝豆、虎豆、白鳳豆、刀豆、鵲豆、肉豆、關刀豆、豆芽、小麥草、苜蓿芽、波羅門蔘、羅勒、九層塔、茴香、香芹、巴西里）" }, { "Code": 501, "Name": "L香蕉" }, { "Code": 502, "Name": "L鳳梨" }, { "Code": 503, "Name": "L柑桔類（金桔、金柑、海梨柑、茂谷柑、四季桔、金棗、椪柑、桶柑、雪柑、溫州蜜柑、晚侖西亞橙、柳橙、檸檬、萊姆、葡萄柚及雜柑類）" }, { "Code": 504, "Name": "L柚類（文旦柚、斗柚、白柚、帝王柚、西施柚）" }, { "Code": 505, "Name": "L龍眼" }, { "Code": 506, "Name": "L芒果" }, { "Code": 507, "Name": "L番石榴" }, { "Code": 508, "Name": "L蓮霧" }, { "Code": 509, "Name": "L葡萄（巨峰葡萄、義大利葡萄、金香葡萄、黑后葡萄）" }, { "Code": 510, "Name": "L枇杷" }, { "Code": 511, "Name": "L李" }, { "Code": 512, "Name": "L桃（鶯歌桃、甜桃、水蜜桃）" }, { "Code": 513, "Name": "L柿（水柿、紅柿、甜柿、筆柿、牛心柿、毛柿、軟柿）" }, { "Code": 514, "Name": "L梅" }, { "Code": 515, "Name": "L荔枝" }, { "Code": 516, "Name": "L橄欖" }, { "Code": 517, "Name": "L楊桃" }, { "Code": 518, "Name": "L梨（橫山梨、新世紀梨、豐水梨、新興梨）" }, { "Code": 519, "Name": "L蘋果" }, { "Code": 520, "Name": "L木瓜" }, { "Code": 521, "Name": "L棗（紅棗）" }, { "Code": 522, "Name": "L番荔枝（釋迦）" }, { "Code": 523, "Name": "L百香果" }, { "Code": 524, "Name": "L可可椰子" }, { "Code": 525, "Name": "L檳榔" }, { "Code": 526, "Name": "L紅龍果" }, { "Code": 527, "Name": "L菠蘿蜜" }, { "Code": 528, "Name": "L酪梨" }, { "Code": 529, "Name": "其他果樹（栗子樹、人蔘果、香瓜茄、蛋黃果、奇異果、獼猴桃、蘋婆、神秘果、楊梅、麵包樹、嘉寶果、樹葡萄、人心果、吳鳳柿、仙桃、油柑、無花果、黃金果、餘甘子、馬拉巴栗）" }, { "Code": 601, "Name": "S洋菇" }, { "Code": 602, "Name": "S香菇" }, { "Code": 603, "Name": "S金針菇" }, { "Code": 604, "Name": "S杏鮑菇" }, { "Code": 605, "Name": "S木耳" }, { "Code": 606, "Name": "S其他食用菇蕈（草菇、鮑魚菇、靈芝、蠔菇、鴻禧菇、雪白菇、柳松菇、袖珍菇、珊瑚菇、雨來菇、時雨菇、情人的眼淚）" }, { "Code": 701, "Name": "切花類（菊花、唐菖蒲、劍蘭、夜來香、大理花、洋桔梗、香石竹、百合、玫瑰、火鶴花、非洲菊、天堂鳥、海芋、滿天星、卡斯比亞、情人草、康乃馨、玉蘭花、野薑花、雞冠花、麥稈菊、銀柳）" }, { "Code": 702, "Name": "S球根類（水仙、鬱金香、風信子）" }, { "Code": 703, "Name": "盆花類（杜鵑、福祿桐、仙客來、鳳梨花、聖誕紅、水草、萬年青）" }, { "Code": 704, "Name": "L蘭花（蝴蝶蘭、文心蘭、蕙蘭、春蘭、寒蘭、建蘭、墨蘭、石斛蘭、虎頭蘭、拖鞋蘭、兜蘭、萬代蘭、嘉德麗雅蘭、嘉得利亞蘭）" }, { "Code": 705, "Name": "其他花卉（觀賞苗圃）" }, { "Code": 801, "Name": "S草皮（韓國草）" }, { "Code": 802, "Name": "S秧苗" }, { "Code": 803, "Name": "S食用菇菌種" }, { "Code": 804, "Name": "S蘭花種苗" }, { "Code": 805, "Name": "其他種苗（蕹菜籽、果樹苗木、花卉種苗、蔬菜種苗、林業苗木、福木苗、馬拉巴栗苗）" }, { "Code": 806, "Name": "其他作物（松、柏、鐵樹、落羽松、五葉松、櫻花、桃花、杏花等觀賞用植物）" }];
var poultrycode = [{ "Code": 10, "Name": "仔豬" }, { "Code": 11, "Name": "肉豬" }, { "Code": 12, "Name": "種豬" }, { "Code": 13, "Name": "山豬" }, { "Code": 14, "Name": "肉（役）牛（黃牛、水牛、雜種牛、荷蘭牛、乳公牛）" }, { "Code": 15, "Name": "產乳牛（泌乳牛）" }, { "Code": 16, "Name": "未產乳牛（小女牛、大女牛）" }, { "Code": 17, "Name": "肉羊（山羊、黑面羊、乳公羊）" }, { "Code": 18, "Name": "綿羊" }, { "Code": 19, "Name": "乳羊" }, { "Code": 20, "Name": "鹿（水鹿、梅花鹿）" }, { "Code": 21, "Name": "兔" }, { "Code": 22, "Name": "未列之家畜（馬）" }, { "Code": 31, "Name": "白肉雞（珍珠雞）" }, { "Code": 32, "Name": "有色肉雞（烏骨雞、仿仔雞、本地雞、仿土雞、放山雞、土雞、閹雞、鬥雞）" }, { "Code": 33, "Name": "肉種雞" }, { "Code": 34, "Name": "蛋雞" }, { "Code": 35, "Name": "蛋種雞" }, { "Code": 36, "Name": "肉鴨（土番鴨、北京鴨）" }, { "Code": 37, "Name": "肉種鴨" }, { "Code": 38, "Name": "蛋鴨" }, { "Code": 39, "Name": "蛋種鴨" }, { "Code": 40, "Name": "鵝" }, { "Code": 41, "Name": "火雞" }, { "Code": 42, "Name": "鵪鶉" }, { "Code": 43, "Name": "鴕鳥" }, { "Code": 44, "Name": "未列之家禽（珠雞、肉鴿）" }, { "Code": 51, "Name": "蜜蜂（箱）" }, { "Code": 52, "Name": "蠶（盒）" }];
var poultryservicecode = [{ "Code": "01", "Name": "稻作" }, { "Code": "02", "Name": "雜糧" }, { "Code": "03", "Name": "特用作物" }, { "Code": "04", "Name": "蔬菜" }, { "Code": "05", "Name": "果樹" }, { "Code": "06", "Name": "食用菇蕈" }, { "Code": "07", "Name": "花卉" }, { "Code": "08", "Name": "其他農作物" }, { "Code": "09", "Name": "牛" }, { "Code": "10", "Name": "豬" }, { "Code": "11", "Name": "其他家畜" }, { "Code": "12", "Name": "雞" }, { "Code": "13", "Name": "鴨" }, { "Code": "14", "Name": "其他家禽" }];
var fish_3_2 = [{ "Code": "0R", "Name": "漁筏-動力漁筏" }, { "Code": "0Y", "Name": "漁筏-無動力漁筏" }, { "Code": "0S", "Name": "舢舨-動力舢舨" }, { "Code": "0X", "Name": "舢舨-無動力舢舨" }, { "Code": "F0", "Name": "專營娛樂漁船-未滿5噸" }, { "Code": "F1", "Name": "專營娛樂漁船-5噸~未滿10噸" }, { "Code": "F2", "Name": "專營娛樂漁船-10噸~未滿20噸" }, { "Code": "F3", "Name": "專營娛樂漁船-20噸~未滿50噸" }, { "Code": "00", "Name": "動力漁船-未滿5噸" }, { "Code": "01", "Name": "動力漁船-5噸~未滿10噸" }, { "Code": "02", "Name": "動力漁船-10噸~未滿20噸" }, { "Code": "03", "Name": "動力漁船-20噸~未滿50噸" }, { "Code": "04", "Name": "動力漁船-50噸~未滿100噸" }, { "Code": "05", "Name": "動力漁船-100噸~未滿200噸" }, { "Code": "06", "Name": "動力漁船-200噸~未滿500噸" }, { "Code": "07", "Name": "動力漁船-500噸~未滿1000噸" }, { "Code": "08", "Name": "動力漁船-1000噸以上" }];
var fish_3_4 = [{ "Code": 1, "Name": "單船拖網" }, { "Code": 2, "Name": "雙船拖網" }, { "Code": 3, "Name": "鰹鮪圍網" }, { "Code": 4, "Name": "鮪延繩釣" }, { "Code": 5, "Name": "魷釣" }, { "Code": 6, "Name": "秋刀魚棒受網" }, { "Code": 7, "Name": "採撈珊瑚" }, { "Code": 8, "Name": "巾著網" }, { "Code": 9, "Name": "鯖鰺圍網" }, { "Code": 10, "Name": "扒網" }, { "Code": 11, "Name": "棒受網(含焚寄網)" }, { "Code": 12, "Name": "刺網" }, { "Code": 13, "Name": "追逐網" }, { "Code": 14, "Name": "雜魚延繩釣" }, { "Code": 15, "Name": "一支釣" }, { "Code": 16, "Name": "曳繩釣" }, { "Code": 17, "Name": "鏢旗魚" }, { "Code": 18, "Name": "地曳網" }, { "Code": 19, "Name": "定置網" }, { "Code": 20, "Name": "其他網" }, { "Code": 21, "Name": "其他釣" }, { "Code": 22, "Name": "觀光休閒" }, { "Code": 23, "Name": "籠具" }, { "Code": 24, "Name": "採捕魚貝苗" }, { "Code": 25, "Name": "採藻類" }, { "Code": 26, "Name": "其他" }];
var fish_5_3 = [{ "Code": "1", "Name": "自有自用" }, { "Code": "2", "Name": "租(借、占)用國、公有地" }, { "Code": "3", "Name": "租(借、占)用私有地" }, { "Code": "4", "Name": "接受委託經營" }];
var fish_5_4 = [{ "Code": 1, "Name": "鯉魚類" }, { "Code": 2, "Name": "鱒魚" }, { "Code": 3, "Name": "鰻魚類" }, { "Code": 4, "Name": "鱸魚" }, { "Code": 5, "Name": "石斑魚類" }, { "Code": 6, "Name": "虱目魚" }, { "Code": 7, "Name": "烏魚" }, { "Code": 8, "Name": "吳郭魚類" }, { "Code": 9, "Name": "鯛魚類" }, { "Code": 10, "Name": "黃臘鰺" }, { "Code": 11, "Name": "海螺" }, { "Code": 12, "Name": "觀賞魚類" }, { "Code": 13, "Name": "午仔魚" }, { "Code": 14, "Name": "其他魚類" }, { "Code": 15, "Name": "草蝦" }, { "Code": 16, "Name": "斑節蝦" }, { "Code": 17, "Name": "長腳大蝦" }, { "Code": 18, "Name": "白蝦" }, { "Code": 19, "Name": "其他蝦類" }, { "Code": 20, "Name": "蟳蟹類" }, { "Code": 21, "Name": "牡蠣" }, { "Code": 22, "Name": "文蛤" }, { "Code": 23, "Name": "九孔" }, { "Code": 24, "Name": "蜆" }, { "Code": 25, "Name": "其他貝介類" }, { "Code": 26, "Name": "龍鬚菜" }, { "Code": 27, "Name": "其他澡網" }, { "Code": 28, "Name": "鱉" }, { "Code": 29, "Name": "其他水產生物" }, { "Code": 30, "Name": "全年休養" }];
var fish_5_5 = [{ "Code": "1", "Name": "止水式魚塭養繁殖" }, { "Code": "2", "Name": "流水式魚塭養繁殖" }, { "Code": "3", "Name": "循環式魚塭養繁殖" }, { "Code": "4", "Name": "淺海養繁殖" }, { "Code": "5", "Name": "箱網養繁殖" }, { "Code": "6", "Name": "其他養繁殖" }, { "Code": "7", "Name": "全年休養" }];
var fish_5_6 = [{ "Code": "1", "Name": "單養" }, { "Code": "2", "Name": "混養" }, { "Code": "3", "Name": "繁殖" }, { "Code": "4", "Name": "買成魚供人垂釣" }, { "Code": "5", "Name": "全年未使用" }];
var fish_5_8 = [{ "Code": "1", "Name": "地下水" }, { "Code": "2", "Name": "海水" }, { "Code": "3", "Name": "河川、水庫水" }, { "Code": "4", "Name": "淡水混用" }, { "Code": "5", "Name": "淡海水混用(以淡水為主)" }, { "Code": "6", "Name": "淡海水混用(以海水為主)" }, { "Code": "7", "Name": "其他水源" }, { "Code": "8", "Name": "全年未使用" }];
var fish_14_4 = [{ "Code": "1", "Name": "不識字" }, { "Code": "2", "Name": "小學及自修" }, { "Code": "3", "Name": "國(初)中" }, { "Code": "4", "Name": "高中(職)" }, { "Code": "5", "Name": "大專及以上" }];
var fish_14_5 = [{ "Code": "1", "Name": "指揮者" }, { "Code": "2", "Name": "決策關係人" }, { "Code": "3", "Name": "決策關係人兼承接者" }, { "Code": "4", "Name": "承接者" }, { "Code": "5", "Name": "非上述者" }];
var fish_14_6 = [{ "Code": "1", "Name": "無" }, { "Code": "2", "Name": "1~29日" }, { "Code": "3", "Name": "30~59日" }, { "Code": "4", "Name": "60~89日" }, { "Code": "5", "Name": "90~149日" }, { "Code": "6", "Name": "150~179日" }, { "Code": "7", "Name": "180~249日" }, { "Code": "8", "Name": "250日以上" }];
var fish_14_7 = [{ "Code": "1", "Name": "無" }, { "Code": "2", "Name": "1~29日" }, { "Code": "3", "Name": "30~59日" }, { "Code": "4", "Name": "60~89日" }, { "Code": "5", "Name": "90~149日" }, { "Code": "6", "Name": "150~179日" }, { "Code": "7", "Name": "180~249日" }, { "Code": "8", "Name": "250日以上" }];
var farm_3_2 = [{ "Code": 1, "Name": "可耕作地" }, { "Code": 2, "Name": "人工鋪面" }];
var farm_3_5 = [{ "Code": 1, "Name": "自有租用" }, { "Code": 2, "Name": "租(借、占)用國、公有地" }, { "Code": 3, "Name": "租(借、占)用國、私有地" }, { "Code": 4, "Name": "接受委託經營" }];
var farm_3_6 = [{ "Code": 1, "Name": "水利會供水" }, { "Code": 2, "Name": "地下水" }, { "Code": 3, "Name": "河川、埤池水" }, { "Code": 4, "Name": "其他水源" }, { "Code": 5, "Name": "無灌溉(含雨水)" }];
var farm_3_7 = [{ "Code": 1, "Name": "開放參觀、採摘(含市民農園)" }, { "Code": 2, "Name": "生產短期作物" }, { "Code": 3, "Name": "生產長期作物" }, { "Code": 4, "Name": "種植綠肥作物" }, { "Code": 5, "Name": "造林(6年以下)" }, { "Code": 6, "Name": "暫作栽培農作物以外用途" }, { "Code": 7, "Name": "全年未使用" }];
var farm_4_3 = [{ "Code": 1, "Name": "公畝" }, { "Code": 2, "Name": "公斤" }, { "Code": 3, "Name": "箱" }, { "Code": 4, "Name": "盆" }, { "Code": 5, "Name": "包" }, { "Code": 6, "Name": "瓶" }];
var farm_4_5 = [{ "Code": 1, "Name": "簡易隧道棚" }, { "Code": 2, "Name": "水平棚架" }, { "Code": 3, "Name": "網室(含遮陰網)" }, { "Code": 4, "Name": "塑膠布網室" }, { "Code": 5, "Name": "溫室" }, { "Code": 6, "Name": "其他" }, { "Code": 7, "Name": "不使用" }];
var farm_4_6 = [{ "Code": 1, "Name": "僅使用化學肥料" }, { "Code": 2, "Name": "僅使用合成農藥" }, { "Code": 3, "Name": "兩者皆有使用" }, { "Code": 4, "Name": "兩者皆不使用" }];
var farm_12_5 = [{ "Code": 1, "Name": "指揮者" }, { "Code": 2, "Name": "決策關係人" }, { "Code": 3, "Name": "決策關係人兼承接者" }, { "Code": 4, "Name": "承接者" }, { "Code": 5, "Name": "非上述者" }];
var farm_12_6 = [{ "Code": 1, "Name": "無" }, { "Code": 2, "Name": "未滿一年" }, { "Code": 3, "Name": "1~未滿5年" }, { "Code": 4, "Name": "5~未滿10年" }, { "Code": 5, "Name": "10~未滿20年" }, { "Code": 6, "Name": "20年以上" }];
var farm_12_7 = [{ "Code": 1, "Name": "無" }, { "Code": 2, "Name": "1~29日" }, { "Code": 3, "Name": "30~59日" }, { "Code": 4, "Name": "60~89日" }, { "Code": 5, "Name": "90~149日" }, { "Code": 6, "Name": "150~179日" }, { "Code": 7, "Name": "180~249日" }, { "Code": 8, "Name": "250日以上" }];
var farm_12_8 = [{ "Code": 1, "Name": "自營農牧工業工作" }, { "Code": 2, "Name": "受雇農牧業工作" }, { "Code": 3, "Name": "自營農牧業外工作" }, { "Code": 4, "Name": "受雇農牧業外工作" }, { "Code": 5, "Name": "料理家務" }, { "Code": 6, "Name": "求學及準備升學" }, { "Code": 7, "Name": "疾病、養老" }, { "Code": 8, "Name": "其他" }];
var farm_1 = [{ "Code": 1, "Name": "可耕作地" }, { "Code": 2, "Name": "人工鋪面" }];
var farm_2 = [{ "Code": 1, "Name": "自有自用" }, { "Code": 2, "Name": "租(借、占)用國、公有地" }, { "Code": 3, "Name": "租(借、占)用或接受委託他人私有地(書面約定)" }, { "Code": 4, "Name": "租(借、占)用或接受委託他人私有地(非書面約定" }];
var farm_3 = [{ "Code": 1, "Name": "水利會供水" }, { "Code": 2, "Name": "地下水" }, { "Code": 3, "Name": "河川、埤池水" }, { "Code": 4, "Name": "其他水源" }, { "Code": 5, "Name": "無灌溉(含雨水、全年未種植)" }];
var farm_4 = [{ "Code": 1, "Name": "開放參觀、採摘(含市民農園)" }, { "Code": 2, "Name": "生產短期作物" }, { "Code": 3, "Name": "生產長期作物" }, { "Code": 4, "Name": "種植綠肥作物" }, { "Code": 5, "Name": "造林(6年以下)" }, { "Code": 6, "Name": "暫作栽培農作物以外用途" }, { "Code": 7, "Name": "全年未使用" }];
var farm_5 = [{ "Code": 1, "Name": "簡易隧道棚" }, { "Code": 2, "Name": "水平棚架" }, { "Code": 3, "Name": "水平棚架網室" }, { "Code": 4, "Name": "簡易塑膠布溫網室" }, { "Code": 5, "Name": "結構型鋼骨溫網室" }, { "Code": 6, "Name": "傳統菇舍" }, { "Code": 7, "Name": "環控菇舍" }, { "Code": 8, "Name": "其他" }, { "Code": 9, "Name": "不使用" }];
var farm_6 = [{ "Code": 1, "Name": "僅使用化學肥料" }, { "Code": 2, "Name": "僅使用合成農藥" }, { "Code": 3, "Name": "兩者皆有使用" }, { "Code": 4, "Name": "兩者皆不使用" }];
var farm_7 = [{ "Code": 1, "Name": "公畝" }, { "Code": 2, "Name": "公斤(段木)" }, { "Code": 3, "Name": "箱(育苗箱)" }, { "Code": 4, "Name": "盆(盆栽)" }, { "Code": 5, "Name": "包(太空包)" }, { "Code": 6, "Name": "瓶(栽培瓶)" }];
var farm_8 = [{ "Code": 10, "Name": "仔豬" }, { "Code": 11, "Name": "肉豬" }, { "Code": 12, "Name": "種豬" }, { "Code": 13, "Name": "山豬" }, { "Code": 14, "Name": "肉(役)牛" }, { "Code": 15, "Name": "產乳牛" }
    , { "Code": 16, "Name": "未產乳牛" }, { "Code": 17, "Name": "肉羊" }, { "Code": 18, "Name": "綿羊" }, { "Code": 19, "Name": "乳羊" }, { "Code": 20, "Name": "鹿" }, { "Code": 21, "Name": "兔" }
    , { "Code": 22, "Name": "未列之家畜" }, { "Code": 31, "Name": "白肉雞" }, { "Code": 32, "Name": "有色肉雞" }, { "Code": 33, "Name": "肉種雞" }, { "Code": 34, "Name": "蛋雞" }, { "Code": 35, "Name": "蛋種雞" }
    , { "Code": 36, "Name": "肉鴨" }, { "Code": 37, "Name": "肉種鴨" }, { "Code": 38, "Name": "蛋鴨" }, { "Code": 39, "Name": "蛋種鴨" }, { "Code": 40, "Name": "鵝" }, { "Code": 41, "Name": "火雞" }
    , { "Code": 42, "Name": "鵪鶉" }, { "Code": 43, "Name": "鴕鳥" }, { "Code": 44, "Name": "未列之家禽" }, { "Code": 51, "Name": "蜜蜂" }, { "Code": 52, "Name": "蠶" }
];

var farm_9 = [{ "Code": 1, "Name": "不識字" }, { "Code": 2, "Name": "國小及自修" }, { "Code": 3, "Name": "國(初)中" }, { "Code": 4, "Name": "高級中等(高中、高職)" }, { "Code": 5, "Name": "大專及以上" }];
var farm_10 = [{ "Code": 1, "Name": "指揮者" }, { "Code": 2, "Name": "決策關係人" }, { "Code": 3, "Name": "決策關係人兼承接者" }, { "Code": 4, "Name": "承接者" }, { "Code": 5, "Name": "非上述者" }];
var farm_11 = [{ "Code": 1, "Name": "無" }, { "Code": 2, "Name": "1~29日" }, { "Code": 3, "Name": "30~59日" }, { "Code": 4, "Name": "60~89日" }, { "Code": 5, "Name": "90~149日" }, { "Code": 6, "Name": "150~179日" }, { "Code": 7, "Name": "180~249日" }, { "Code": 8, "Name": "250日以上" }];
var farm_12 = [{ "Code": 1, "Name": "自營農牧工業工作" }, { "Code": 2, "Name": "受僱農牧業工作" }, { "Code": 3, "Name": "自營農牧業外工作" }, { "Code": 4, "Name": "受僱農牧業外工作" }, { "Code": 5, "Name": "料理家務" }, { "Code": 6, "Name": "求學及準備升學" }, { "Code": 7, "Name": "疾病、養老" }, { "Code": 8, "Name": "其他" }];
var farm_13 = [{ "Code": 1, "Name": "男" }, { "Code": 2, "Name": "女" }];
var farm_14 = [{ "Code": 1, "Name": "是" }, { "Code": 2, "Name": "否" }];
var farm_15 = [{ "Code": 1, "Name": "有" }, { "Code": 2, "Name": "無" }];

var fish_1 = [{ "Code": 1, "Name": "鯉魚類" }, { "Code": 2, "Name": "鱒魚" }, { "Code": 3, "Name": "鰻魚類" }, { "Code": 4, "Name": "鱸魚" }, { "Code": 5, "Name": "石斑魚類" }, { "Code": 6, "Name": "虱目魚" }, { "Code": 7, "Name": "烏魚" }, { "Code": 8, "Name": "吳郭魚類" }, { "Code": 9, "Name": "鯛魚類" }, { "Code": 10, "Name": "黃臘(鱲)鰺" }, { "Code": 11, "Name": "海鱺" }, { "Code": 12, "Name": "觀賞魚類" }, { "Code": 13, "Name": "午仔魚" }, { "Code": 14, "Name": "泥鰍" }, { "Code": 15, "Name": "其他魚類" }, { "Code": 16, "Name": "草蝦" }, { "Code": 17, "Name": "斑節蝦" }, { "Code": 18, "Name": "長腳大蝦" }, { "Code": 19, "Name": "白蝦" }, { "Code": 20, "Name": "其他蝦類" }, { "Code": 21, "Name": "蟳蟹類" }, { "Code": 22, "Name": "牡蠣" }, { "Code": 23, "Name": "文蛤" }, { "Code": 24, "Name": "九孔" }, { "Code": 25, "Name": "蜆" }, { "Code": 26, "Name": "其他貝介類" }, { "Code": 27, "Name": "龍鬚菜" }, { "Code": 28, "Name": "其他藻類" }, { "Code": 29, "Name": "鱉" }, { "Code": 30, "Name": "其他水產生物" }, { "Code": 31, "Name": "全年休養" }];
var fish_2 = [{ "Code": 1, "Name": "室外硬池式" }, { "Code": 2, "Name": "室外土池式" }, { "Code": 3, "Name": "室內池" }];
var fish_3 = [{ "Code": 1, "Name": "單養" }, { "Code": 2, "Name": "混養" }, { "Code": 3, "Name": "中間育成" }, { "Code": 4, "Name": "繁殖" }, { "Code": 5, "Name": "買成魚供人垂釣" }, { "Code": 6, "Name": "全年未使用" }];
var fish_4 = [{ "Code": 1, "Name": "海水" }, { "Code": 2, "Name": "地下水" }, { "Code": 3, "Name": "河川、水庫水" }, { "Code": 4, "Name": "淡水混用" }, { "Code": 5, "Name": "淡海水混用" }, { "Code": 6, "Name": "其他水源" }, { "Code": 7, "Name": "全年未使用" }];
var fish_5 = [{ "Code": 1, "Name": "僅使用智慧生產" }, { "Code": 2, "Name": "僅架設太陽能板" }, { "Code": 3, "Name": "兩者皆有" }, { "Code": 4, "Name": "兩者皆無" }];

var canUnMask_js = false; // 可視遮罩資料
var MaskColumnList_js = false; // 整理設定遮罩的 ColumnName

for (var item, i = 0; item = zipcode[i++];) {
    let city = item.city;

    if (zipcity.indexOf(city) == -1) {
        zipcity.push(city);
    }
}

zipcity = zipcity.sort((a, b) => a > b ? 1 : -1);

var DataResult = {};
$(function () {

    $.busyLoadFull("show");

    let __RequestVerificationToken = $('[name="__RequestVerificationToken"]').val();
    let modeFlagDic = { "#error-list": 0, "#modify-list": 1, "#modify-process": 2 };
    let modeFlag = modeFlagDic[window.location.hash];

    let first_data = {
        projectId: projectId,
        conditionMissionId: missionId,
        dataErrorListId: dataErrorListId,
        modeFlag: modeFlag,
        searchStr: searchStr,
        auditor: auditor,
        dataIdCopy: dataIdCopy, // 2020/09 調查表更正若為人口群組，提供「調查表新增」功能，並預帶該筆Id部分欄位
    }

    $.ajax({
        type: 'get',
        url: '/api/project/modifyKeyup',
        data: first_data,
        contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
        dataType: 'json',
        success: function (result) {
            DataResult = result;

            console.log("接到資料瞜");

            /*執行Vue.js程式碼---開始*/


            var app = new Vue({

                el: '#app',
                data: {

                    hasAuthorization: false,
                    //漁業參考檔
                    fish_3_2Code: window.fish_3_2,
                    fish_3_4Code: window.fish_3_4,
                    fish_5_3Code: window.fish_5_3,
                    fish_5_4Code: window.fish_5_4,
                    fish_5_5Code: window.fish_5_5,
                    fish_5_6Code: window.fish_5_6,
                    fish_5_8Code: window.fish_5_8,
                    fish_14_4Code: window.fish_14_4,
                    fish_14_5Code: window.fish_14_5,
                    fish_14_6Code: window.fish_14_6,
                    fish_14_7Code: window.fish_14_7,
                    farm_3_2Code: window.farm_3_2,
                    farm_3_5Code: window.farm_3_5,
                    farm_3_6Code: window.farm_3_6,
                    farm_3_7Code: window.farm_3_7,
                    farm_4_3Code: window.farm_4_3,
                    farm_4_5Code: window.farm_4_5,
                    farm_4_6Code: window.farm_4_6,
                    farm_12_5Code: window.farm_12_5,
                    farm_12_6Code: window.farm_12_6,
                    farm_12_7Code: window.farm_12_7,
                    farm_12_8Code: window.farm_12_8,



                    tableAll: [{
                        "farm_1": window.farm_1, "farm_2": window.farm_2, "farm_3": window.farm_3, "farm_4": window.farm_4, "farm_5": window.farm_5
                        , "farm_6": window.farm_6, "farm_7": window.farm_7, "farm_8": window.farm_8, "farm_9": window.farm_9, "farm_10": window.farm_10
                        , "farm_11": window.farm_11, "farm_12": window.farm_12, "farm_13": window.farm_13, "farm_14": window.farm_14, "farm_15": window.farm_15
                        , "fish_1": window.fish_1, "fish_2": window.fish_2, "fish_3": window.fish_3, "fish_4": window.fish_4, "fish_5": window.fish_5
                    }],
                    classcode: ["zipcode", "countycode", "cropcode", "poultrycode", "poultryservicecode", "fish_3_2", "fish_3_4",
                        "fish_5_3", "fish_5_4", "fish_5_5", "fish_5_6", "fish_5_8", "fish_14_4", "fish_14_5", "fish_14_6", "fish_14_7",
                        "farm_3_2", "farm_3_5", "farm_3_6", "farm_3_7", "farm_4_3", "farm_4_5", "farm_4_6", "farm_12_5", "farm_12_6", "farm_12_7", "farm_12_8", "farm_1", "farm_2", "farm_3", "farm_4"
                        , "farm_5", "farm_6", "farm_7", "farm_8", "farm_9", "farm_10", "farm_11", "farm_12", "farm_13", "farm_14", "farm_15"
                        , "fish_1", "fish_2", "fish_3", "fish_4", "fish_5"],

                    //
                    classcode2: '',
                    updateId: '',
                    ////
                    currentPoultryCodeDataList: { Code: null, Poultry: null },
                    currentPoultry: '',
                    currentCropCodeDataList: { Code: null, Crop: null },
                    currentCropCode: '',
                    currentCrop: '',
                    currentcurrentCodeDataList: { Code: null, Name: null },
                    currentcurrentCode: '',
                    currentcurrentName: '',
                    currentZipCodeDataList: { Code: null, Town: null, City: null },
                    currentTown: '',
                    currentCity: '',
                    currentCode: '',
                    poultryserviceCode: window.poultryservicecode,
                    poultryCode: window.poultrycode,
                    countyCode: window.countycode,
                    cropCode: window.cropcode,
                    zipCode: window.zipcode,
                    zipCity: window.zipcity,
                    filterCodeName: '',
                    filterCropName: '',
                    filterPoultryName: '',
                    filterCityName: window.zipcity[0],
                    SeqColumnName: window.SeqColumnName,
                    bathA: "0",
                    bathB: "0",
                    currentDataErrorListId: -1, //目前的dataErrorListId
                    dataErrors: [{
                        seq: -1,
                        dataErrorListId: '',
                        censusNo: '',           //普查編號
                        dataId: null,
                        relationGroupId: null,
                        conditionList: [],      //condition history list
                        dataErrorColumnList: [],    //全欄位列表
                        specialSkipRemark: '',   //特意註記
                        isPageValue: 1,            //相關資料tab文字
                        conHisId: -1,               //condition history id
                        sourceId: '',            //流水號
                        isDelete: false,

                        // 公式化計算 舊作法 dataErrorColumnListForCheckFormula: [], // 供存檔時，檢查公式化欄位用
                    }],
                    isNoConditionFilter: false,
                    allConditionList: [],
                    allMissionConditionList: [],
                    currentConditionHistoryId: -1,
                    cardData: [],
                    cardDataHIndex: 0,
                    submitType: 'get',  //傳送的方式
                    path: '/api/project/modifyKeyup',    //傳送的路徑

                    fileSchemaId: -1,
                    tableName: '',
                    auditor: window.auditor,  // 錯誤清單:0  更正清單:1
                    userId: '',            // 當前更正者
                    userName: '',
                    ExecuteUserId: '',     // 被分配的更正者
                    ExecuteUserName: '',
                    CreatorId: '',         // 分派者 = 審查員
                    CreatorName: '',
                    unlockAllColumn: false,     //全部解鎖
                    isSubmit: false,

                    firstRander: true,  //第一次render 結束
                    needRander: true, //每當下一筆回來render後

                    noWaitResults: false, //儲存後是否等待API回傳並顯示結果或直接跳到清單列表頁
                    dataErrorListId: window.dataErrorListId, // 新增mode:-1  更正mode:資料id

                    ParentId: window.ParentId, // 最上層群組GroupId ( 11 農林漁牧業,82 工業及服務業,84 人口及住宅)
                    dataIdCopy: window.dataIdCopy, // 2020/09 調查表更正若為人口群組，提供「調查表新增」功能，並預帶該筆Id部分欄位
                    CMHConditionInfoListOrigin: [], // 保留viewModel資料，因做公式化欄位計算需重新更新頁面，可依其
                    LoginUserId: window.LoginUserId, //目前登入者

                    relateDataList: [],
                    IsRelateDataViewEnabled: window.IsRelateDataViewEnabled,

                    canUnMask: false, // 可視遮罩資料
                    MaskColumnList: [], // 整理設定遮罩的 ColumnName

                },
                methods: {
                    Biglock: function () {
                        var bigel = document.getElementById("Investigate");
                        var el = $(bigel).children().find("*");
                        debugger;
                        $(el).prop('disabled', true);
                    },
                    Advenceunlock: function (values, id) {
                        if (values == 7) {
                            document.getElementById(id).disabled = false;
                        }
                    },
                    GetTabHash: function () { return window.location.hash; },
                    cursorFocus: function (elem) {
                        //var x = window.scrollX, y = window.scrollY;
                        elem.focus();
                        //window.scrollTo(x, y);
                    },
                    //解鎖與該問題有同時性編輯的所有跟隨欄位
                    unLockFollowColumn: function (event) {
                        var name = event.target.name;
                        //var order = $(event.target).data("order");
                        var tagName = event.target.tagName;
                        var type = event.target.type;
                        var value = event.target.value;
                        //var els = $(`.table-scroll ${tagName}[name=${name}]`);
                        var fels = $(".table-scroll").find(`[data-follow=${name}]`);
                        $(fels).prop('disabled', true);
                        var hasRange = false;
                        $(fels).each(function (fi, fe) {
                            if ($(fe).data("range")) {
                                var fr = $(fe).data("range").toString();
                                if (fr.indexOf(value) > -1) {
                                    $(fe).prop('disabled', false);
                                    hasRange = true;
                                }
                            } else {
                                $(fe).prop('disabled', false);
                                hasRange = true;
                            }
                        });

                        //switch (tagName.toLowerCase()) {
                        //    case 'input':
                        //        if (type == 'radio') {
                        //            var hasRange = false;
                        //            $(fels).each(function (fi, fe) {
                        //                if ($(fe).data("range")) {
                        //                    var fr = $(fe).data("range").toString();
                        //                    if (fr.indexOf(value) > -1) {
                        //                        $(fe).prop('disabled', false);
                        //                        hasRange = true;
                        //                    }
                        //                } else {
                        //                    $(fe).prop('disabled', false);
                        //                    hasRange = true;
                        //                }
                        //            });
                        //        }
                        //        break;
                        //    case 'select':
                        //        var hasRange = false;
                        //        $(fels).each(function (fi, fe) {
                        //            if ($(fe).data("range")) {
                        //                alert($(fe).data("range")[0].name);
                        //                var fr = $(fe).data("range").toString();
                        //                if (fr.indexOf(value) > -1) {
                        //                    $(fe).prop('disabled', false);
                        //                    hasRange = true;
                        //                }
                        //            } else {
                        //                $(fe).prop('disabled', false);
                        //                hasRange = true;
                        //            }
                        //        });
                        //        break;
                        //}
                    },
                    //ajax接到資料後Reset
                    resetData: function (result) {
                        var that = this;
                        let type = this.submitType;
                        let _seqColumnName = this.SeqColumnName;
                        this.hasAuthorization = result.HashasAuthorization;
                        this.isSubmit = result.IsSubmit;
                        this.unlockAllColumn = result.IsCreateModifyType;
                        this.fileSchemaId = result.FileSchemaId;
                        this.tableName = result.TableName;
                        this.userId = result.UserId;
                        this.userName = result.UserName;

                        this.ExecuteUserId = result.ExecuteUserId;
                        this.ExecuteUserName = result.ExecuteUserName;
                        this.CreatorId = result.CreatorId;
                        this.CreatorName = result.CreatorName;
                        this.canUnMask = result.canUnMask;
                        window.canUnMask_js = this.canUnMask; // 設定全域 供函式unlock用
                        this.MaskColumnList = result.MaskColumnList;
                        window.MaskColumnList_js = this.MaskColumnList; // 設定全域 供函式unlock用

                        this.currentDataErrorListId = -1;
                        this.allConditionList = [];

                        if (result.CMHConditionInfoList != null) {
                            this.CMHConditionInfoListOrigin.push(...result.CMHConditionInfoList);
                        }

                        // 原程式 this.allMissionConditionList = result.CMHConditionInfoList.sort(function (a, b) {
                        // 原程式     return a.ConditionName > b.ConditionName ? 1 : -1;
                        // 原程式 });
                        // 新程式
                        this.allMissionConditionList = this.CMHConditionInfoListOrigin.sort(function (a, b) {
                            return a.ConditionName > b.ConditionName ? 1 : -1;
                        });

                        this.currentConditionHistoryId = -1;
                        if (result.ModifyKeyupDataErrorList.length) {
                            //依指定欄位的值排序
                            //result.ModifyKeyupDataErrorList.forEach(function (d, i) {
                            //    var _seqColumn = d.DataErrorColumnList.find(x => x.ColumnEName == _seqColumnName);

                            //    if (_seqColumn.ModifyValue == "" || _seqColumn.ModifyValue == null) {
                            //        d.seq = _seqColumn.PreviousData;
                            //    } else {
                            //        d.seq = _seqColumn.ModifyValue;
                            //    }
                            //});
                            //result.ModifyKeyupDataErrorList = result.ModifyKeyupDataErrorList.sort(function (a, b) {
                            //    return a.seq > b.seq ? 1 : -1;
                            //});
                            this.dataErrors = result.ModifyKeyupDataErrorList.map(x => {
                                return {
                                    dataErrorListId: x.DataErrorListId,
                                    censusNo: x.CensusNo,           //普查編號
                                    dataId: x.DataId,
                                    relationGroupId: x.RelationGroupId,
                                    conditionList: x.ConditionInfoList,      //condition history list
                                    dataErrorColumnList: x.DataErrorColumnList,    //全欄位列表
                                    specialSkipRemark: x.SpecialSkipRemark,   //特意註記
                                    isPageValue: x.IsPageValue,
                                    conHisId: -1,               //condition history id
                                    sourceId: x.SourceId,      //流水號
                                    isDelete: x.isDelete,      //目前是否為刪除更正狀態
                                }
                            });

                            let tmp_allConditionList = [];
                            //資料重整
                            this.dataErrors.forEach(function (d, i) {
                                tmp_allConditionList.push(...d.conditionList);
                                that.cardData[i] = {};
                                that.cardData[i].dataErrorListId = d.dataErrorListId;
                                that.cardData[i].censusNo = d.censusNo;
                                that.cardData[i].dataId = d.dataId;
                                that.cardData[i].relationGroupId = d.relationGroupId;
                                that.cardData[i].specialSkipRemark = d.specialSkipRemark;
                                that.cardData[i].sourceId = d.sourceId;

                                d.dataErrorColumnList.forEach(function (c, ci) {

                                    if (!c.IsManual) {
                                        Vue.set(c, 'FormValue', c.PreviousData);

                                        // 計算公式化欄位後 重新更新欄位 保留頁面user改之值
                                        if (c.PreviousData != '' && c.ModifyValue != '') {
                                            Vue.set(c, 'FormValue', c.ModifyValue);
                                        }

                                    } else {
                                        Vue.set(c, 'FormValue', c.ModifyValue);
                                    }

                                    // 2020/09 判斷若為公式化異動者 更新其值
                                    if (c.IsFormulaChange) {
                                        Vue.set(c, 'FormValue', c.ModifyValue);
                                    }

                                    Vue.set(c, 'hasFormModified', false);

                                    // 2020/10 針對衛浴 小數點處理
                                    if (i == 0 && c.ColumnEName == 'D01103') {
                                        var tmp = c.FormValue;
                                        tmp = tmp == null ? "" : tmp.toString();
                                        if (tmp.length > 1) {
                                            that.bathA = tmp.substring(0, tmp.length - 1);
                                            that.bathB = tmp.substring(tmp.length - 1, tmp.length);

                                            //Vue.set(c, 'bathA', parseInt(tmp.substring(0, tmp.length - 1)));
                                            //Vue.set(c, 'bathB', parseInt(tmp.substring(tmp.length - 1, tmp.length)));
                                        } else if (tmp.length == 1) {
                                            //Vue.set(c, 'bathA', 0);
                                            //Vue.set(c, 'bathB', parseInt(tmp.substring(tmp.length - 1, tmp.length)));

                                            that.bathA = 0;
                                            that.bathB = tmp.substring(tmp.length - 1, tmp.length);
                                        } else {
                                            //Vue.set(c, 'bathA', 0);
                                            //Vue.set(c, 'bathB', 0);
                                            that.bathA = "0";
                                            that.bathB = "0";
                                        }
                                    }
                                    that.cardData[i][c.ColumnEName] = c;
                                });
                            });

                            //var xxx = tmp_allConditionList.map(function (acl) { return { ConditionHistoryId: acl.ConditionHistoryId, ConditionName: acl.ConditionName }; });

                            that.allConditionList = Array.from(new Set(tmp_allConditionList.map(acl => acl.ConditionHistoryId))).map(function (c) {
                                var _condition = tmp_allConditionList.find(s => s.ConditionHistoryId == c);
                                return { ConditionHistoryId: c, ConditionName: _condition.ConditionName, ConditionString: _condition.ConditionString, ConditionDescription: _condition.ConditionDescription };
                            });
                            that.allConditionList = that.allConditionList.sort(function (a, b) {
                                return a.ConditionName > b.ConditionName ? 1 : -1;
                            });
                            that.allConditionList.forEach(function (d, i) {
                                d.hasError = true;
                            });
                            that.allMissionConditionList.forEach(function (d, i) {
                                d.hasError = false;
                            });
                            that.allConditionList.forEach(function (d, i) {
                                that.allMissionConditionList.find(x => x.ConditionHistoryId == d.ConditionHistoryId).hasError = true;
                            });

                            that.currentDataErrorListId = that.dataErrors[0].dataErrorListId;

                            // 調查表更正mode(currentDataErrorListId <> -1)，且為人口群組時，才有「調查表新增」按鈕
                            // 預設第一筆DataId，後續頁面點選多卡時，由vue click更新所選dataId 
                            if (that.currentDataErrorListId !== -1 && that.ParentId === 84) {
                                that.dataIdCopy = that.dataErrors[0].dataId;
                            }
                        }
                        //if (this.isSubmit) {
                        //    $('#app :input:not(select)').prop('disabled', true);
                        //}
                    },
                    //驗證資料
                    validation: function () {
                        let type = this.submitType;
                        switch (type) {
                            case 'get':
                                return true;
                            case 'post':
                                return true;
                            default:
                                return true;
                        }
                    },
                    openlayout: function (dataErrorListId, upOrDown,result) {
                        swal(`已換成${upOrDown}一筆普查編號：  ${result.ModifyKeyupDataErrorList.length ? result.ModifyKeyupDataErrorList.map(x => x.CensusNo).join(',') : '無普查編號'}`).then((isOK) => {
                            saveOrNotSave = 1;
                            window.location.href = '/Project/Modify/Layout/?id=' + window.projectId + "&conditionMissionId=" + window.missionId + "&dataErrorListId=" + dataErrorListId;
                        }
                        );
                    },
                    //組合要傳到後端的資料
                    getPayload: function () {
                        let type = this.submitType;
                        let __RequestVerificationToken = $('[name="__RequestVerificationToken"]').val();
                        let that = this;
                        let modeFlagDic = { "#error-list": 0, "#modify-list": 1, "#modify-process": 2 };
                        let modeFlag = modeFlagDic[window.location.hash];
                        switch (type) {
                            case 'get':
                                return {
                                    projectId: projectId,
                                    conditionMissionId: missionId,
                                    dataErrorListId: dataErrorListId,
                                    modeFlag: modeFlag,
                                    searchStr: searchStr,
                                    auditor: auditor,
                                    dataIdCopy: dataIdCopy,
                                }
                            case 'post':

                                var viewModel = {
                                    Auditor: that.auditor,
                                    UserId: that.userId,
                                    UserName: that.userName,
                                    ExecuteUserId: that.ExecuteUserId,  // 更正員
                                    ExecuteUserName: that.ExecuteUserName,
                                    CreatorId: that.CreatorId,  // 分派者 = 審查員
                                    CreatorName: that.CreatorName,
                                    ProjectId: projectId,
                                    ConditionMissionId: missionId,
                                    SearchStr: searchStr,
                                    ModifyKeyupDataErrorList: that.dataErrors.map((x, xi) => {

                                        return {
                                            DataErrorListId: x.dataErrorListId,
                                            CensusNo: x.censusNo,           //普查編號
                                            DataId: x.dataId,
                                            RelationGroupId: x.relationGroupId,
                                            ConditionInfoList: x.conditionList,      //condition history list
                                            DataErrorColumnList: that.LayoutLoad(xi, x.dataErrorColumnList),    //全欄位列表
                                            SpecialSkipRemark: x.specialSkipRemark,   //特意註記
                                            IsPageValue: x.isPageValue,
                                            auditor: auditor,
                                            isDelete: x.isDelete,   // 是否刪除

                                            // 公式化計算 舊作法 全欄位列表 供存檔時，檢查公式化欄位用
                                            // DataErrorColumnListForCheckFormula: that.LayoutLoadForCheckFormula(xi, x.dataErrorColumnList)
                                        }
                                    })
                                }
                                //把依指定欄位的值排序這陣列還原成DataId排序
                                //viewModel.ModifyKeyupDataErrorList = viewModel.ModifyKeyupDataErrorList.sort(function (a, b) {
                                //    return a.DataId > b.DataId ? 1 : -1;
                                //});
                                return { 'ModifyKeyupViewModel': viewModel, '__RequestVerificationToken': __RequestVerificationToken };
                            case 'delete':
                                var viewModel = {
                                    ProjectId: projectId,
                                    MissionId: missionId,
                                    Page: 1,
                                    SearchStr: '',
                                    SelectAll: false,
                                    ErrorDataListCount: 0,
                                    ColumnNames: [],
                                    SelectDataErrorListIdList: [dataErrorListId],
                                    Auditor: auditor,
                                }
                                return { 'info': viewModel, 'modifyTypeId': 55, '__RequestVerificationToken': __RequestVerificationToken };//修改之前56
                            default:
                                return;
                        }
                    },
                    //傳送
                    handleSubmit: function (options = { silenceQuickCheck: false, index: -1 }) {
                        //開啟遮罩
                        $.busyLoadFull("show");

                        var that = this;

                        //測試用-------s
                        //if (this.submitType.toLowerCase() == "post") {
                        //    that.getPayload();
                        //    $.busyLoadFull("hide");
                        //    return;
                        //}
                        //測試用-------e

                        $.ajax({
                            type: this.submitType,
                            url: this.path,
                            data: that.getPayload(),
                            contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
                            dataType: 'json',
                            success: function (result) {

                                switch (that.submitType) {
                                    case 'get':
                                        console.log("接到資料瞜");
                                        that.resetData(result);
                                        //關閉遮罩
                                        $.busyLoadFull("hide");
                                        break;
                                    case 'post':
                                        //關閉遮罩
                                        $.busyLoadFull("hide");

                                        swal({ title: '儲存成功', icon: 'success' }).then(function () {
                                            // 若非新增mode而是更正mode，才更新「更正」頁面
                                            if (that.dataErrorListId != -1) {
                                                window.opener.app.getSingleData(that.dataErrors[0].dataErrorListId);
                                            }
                                            //window.opener.app.getSingleData(that.currentDataErrorListId);
                                            window.onbeforeunload = null;
                                            window.close();
                                        });
                                        //swal({ title: '儲存成功', icon: 'success' }).then(function () {
                                        //    window.location.href = '/Project/Modify/?id=' + projectId + '&missionId=' + missionId + '&searchStr=' + searchStr + '&page=' + page + that.GetTabHash();
                                        //});
                                        break;
                                    case 'delete':
                                        swal({ title: '刪除成功', icon: 'success' }).then(function () {
                                            window.opener.app.getSingleData(that.currentDataErrorListId);
                                            window.onbeforeunload = null;
                                            window.close();
                                        });
                                        //swal({ title: '刪除成功', icon: 'success' }).then(function () {
                                        //    window.location.href = '/Project/Modify/?id=' + projectId + '&missionId=' + missionId + '&searchStr=' + searchStr + '&page=' + page + that.GetTabHash();
                                        //});
                                        break;
                                    default:
                                        return;
                                }

                            },
                            error: function (jqXHR, textStatus, errorThrown) {
                                if (that.submitType == 'get' || !that.noWaitResults) {
                                    //關閉遮罩
                                    $.busyLoadFull("hide");
                                    if (jqXHR.status !== 401) {
                                        swal(jqXHR.responseText);
                                    }
                                }
                            }
                        });

                    },
                    showRelateData: function (del_index) {
                        let that = this;
                        let options = { silenceQuickCheck: false, index: del_index }
                        var send_data = that.getCheckPayload(options);

                        //開啟遮罩
                        $.busyLoadFull("show");
                        $.ajax({
                            type: 'post',
                            url: '/api/project/getRelateDataTable',
                            data: send_data,
                            contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
                            dataType: 'json',
                            success: function (result) {

                                that.relateDataList = result.relateDataList;

                                $('#relateData-modal').modal('show');
                                //關閉遮罩
                                $.busyLoadFull("hide");
                            },
                            error: function (jqXHR, textStatus, errorThrown) {
                                //關閉遮罩
                                $.busyLoadFull("hide");
                                if (jqXHR.status !== 401) {
                                    swal(jqXHR.responseText);
                                }
                            }
                        });
                    },
                    deleteCard: function (del_index) {
                        let that = this;
                        let sourceId = that.dataErrors[del_index].sourceId;
                        swal({
                            title: `刪除流水號資料`,
                            text: `此操作會將流水號[${sourceId}]這筆資料更正為刪除，是否要刪除?`,
                            animation: "slide-from-top",
                            icon: "warning",
                            buttons: true,
                            dangerMode: true
                        }).then((isDeleted) => {
                            if (isDeleted) {
                                //To Do...
                                that.dataErrors[del_index].isDelete = true;
                                swal(`流水號[${sourceId}]已更正為刪除`);
                            } else {
                                return;
                            }
                        });
                    },
                    recycleCard: function (del_index) {
                        let that = this;
                        let sourceId = that.dataErrors[del_index].sourceId;
                        swal({
                            title: `回收刪除的流水號`,
                            text: `此操作將從垃圾桶回收流水號[${sourceId}]這筆資料，是否要回收?`,
                            animation: "slide-from-top",
                            icon: "warning",
                            buttons: true,
                            dangerMode: true
                        }).then((isDeleted) => {
                            if (isDeleted) {
                                //To Do...
                                that.dataErrors[del_index].isDelete = false;
                                swal(`流水號[${sourceId}]已成功回收`);
                            } else {
                                return;
                            }
                        });
                    },
                    // 處理 全部解鎖 
                    clickLocker: function (event) {
                        this.unlockAllColumn = event.target.checked;
                    },
                    //取得此dataErrorList的資料
                    handleGet: function () {
                        this.submitType = 'get';
                        this.path = '/api/project/modifyKeyup';
                        this.handleSubmit();

                    },
                    //儲存
                    handlePost: function (options = { silenceQuickCheck: false, index: -1 }) {
                        // 檢核資料
                        if (this.checkData()) {
                            // alert('通過');

                            // 先執行公式化欄位更新
                            let that = this;

                            // 作法2 利用快檢的Payload資料post後送，執行公式欄位計算，將回來之data同用get方式bind至頁面上
                            var send_data = that.getCheckPayload(options);
                            // console.log("ready送公式化演算viewModel");
                            // console.log(send_data);

                            //開啟遮罩
                            $.busyLoadFull("show");
                            $.ajax({
                                type: 'post',
                                url: '/api/project/exeFormulaUpdate',
                                data: send_data,
                                contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
                                dataType: 'json',
                                success: function (result) {
                                    // console.log("接到資料瞜 Yenhe");
                                    // console.log(result);

                                    that.resetData(result); // 將公式化演算後回來之data Bind到頁面欄位
                                    //關閉遮罩
                                    $.busyLoadFull("hide");

                                    /******** 原程式要做的事 開始  *******/

                                    that.handleQuickCheck(options);
                                    that.submitType = 'post';
                                    that.path = '/api/project/modifyLayout';
                                    that.handleSubmit(options);

                                    /******** 原程式要做的事 結束  *******/
                                },
                                error: function (jqXHR, textStatus, errorThrown) {
                                    //關閉遮罩
                                    $.busyLoadFull("hide");
                                    if (jqXHR.status !== 401) {
                                        swal(jqXHR.responseText);
                                    }
                                }
                            });
                        } else {
                            // alert('不通過');

                        }
                    },
                    OnlySave: function () {
                        var that = this;
                        that.submitType = 'post';
                        $.ajax({
                            type: 'post',
                            url: '/api/project/modifyLayout',
                            data: that.getPayload(),
                            contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
                            dataType: 'json',
                            success: function (result) {

                            },
                            error: function (jqXHR, textStatus, errorThrown) {
                                //關閉遮罩
                                if (!options.silenceQuickCheck) {
                                    $.busyLoadFull("hide");
                                    if (jqXHR.status !== 401) {
                                        swal(jqXHR.responseText);
                                    }
                                }
                            }
                        });
                    },
                    OnlyFindNext: function (IsOrderByDesc, gotoLast) {
                        let that = this;
                        let data = that.getPayload();
                        data.ModifyKeyupViewModel.IsOrderByDesc = IsOrderByDesc;
                        data.ModifyKeyupViewModel.gotoLast = gotoLast;
                        let upOrDown = gotoLast ? '上' : '下';
                        //開啟遮罩
                        $.busyLoadFull("show");
                        that.submitType = 'post';
                        $.ajax({
                            type: 'post',
                            url: '/api/project/FindNextData',
                            data: data,
                            contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
                            dataType: 'json',
                            success: function (result) {
                                //關閉遮罩
                                $.busyLoadFull("hide");

                                console.log("接到資料瞜")
                                window.opener.app.getSingleData(that.currentDataErrorListId);
                                if (!result.ModifyKeyupDataErrorList) {
                                    swal(`無${upOrDown}一筆資料，準備跳轉至錯誤清單頁`)
                                        .then(function () {
                                            window.onbeforeunload = null;
                                            window.close();
                                            //projectId = result.projectId;
                                            //conditionMissionId: missionId;
                                            //window.location.href = '/Project/Modify/?id=' + projectId + '&missionId=' + missionId + '&searchStr=' + searchStr + "&page=" + page + that.GetTabHash();
                                        });
                                } else {

                                    
                                    //that.Biglock();
                                    projectId = result.ProjectId;
                                    missionId = result.ConditionMissionId;
                                    searchStr = result.SearchStr;
                                    that.unlockAllColumn = false;
                                    that.currentDataErrorListId = -1
                                    that.allConditionList = [];
                                    that.allMissionConditionList = result.CMHConditionInfoList;
                                    that.currentConditionHistoryId = -1;
                                    that.cardData = {};
                                    that.isNoConditionFilter = false;
                                    if (result.ModifyKeyupDataErrorList.length) {
                                        //依指定欄位的值排序
                                        //result.ModifyKeyupDataErrorList.forEach(function (d, i) {
                                        //    var _seqColumn = d.DataErrorColumnList.find(x => x.ColumnEName == _seqColumnName);

                                        //    if (_seqColumn.ModifyValue == "" || _seqColumn.ModifyValue == null) {
                                        //        d.seq = _seqColumn.PreviousData;
                                        //    } else {
                                        //        d.seq = _seqColumn.ModifyValue;
                                        //    }
                                        //});
                                        //result.ModifyKeyupDataErrorList = result.ModifyKeyupDataErrorList.sort(function (a, b) {
                                        //    return a.seq > b.seq ? 1 : -1;
                                        //});
                                        that.dataErrors = result.ModifyKeyupDataErrorList.map(x => {

                                            return {
                                                dataErrorListId: x.DataErrorListId,
                                                censusNo: x.CensusNo,           //普查編號
                                                dataId: x.DataId,
                                                relationGroupId: x.RelationGroupId,
                                                conditionList: x.ConditionInfoList,      //condition history list
                                                dataErrorColumnList: x.DataErrorColumnList,    //全欄位列表
                                                specialSkipRemark: x.SpecialSkipRemark,   //特意註記
                                                isPageValue: x.IsPageValue,
                                                conHisId: -1,               //condition history id
                                                sourceId: x.SourceId,      //流水號
                                            }
                                        });

                                        let tmp_allConditionList = [];
                                        //資料重整
                                        that.dataErrors.forEach(function (d, i) {
                                            tmp_allConditionList.push(...d.conditionList);
                                            that.cardData[i] = {};
                                            that.cardData[i].dataErrorListId = d.dataErrorListId;
                                            that.cardData[i].censusNo = d.censusNo;
                                            that.cardData[i].dataId = d.dataId;
                                            that.cardData[i].relationGroupId = d.relationGroupId;
                                            that.cardData[i].specialSkipRemark = d.specialSkipRemark;
                                            that.cardData[i].sourceId = d.sourceId;

                                            d.dataErrorColumnList.forEach(function (c, ci) {

                                                if (!c.IsManual) {
                                                    Vue.set(c, 'FormValue', c.PreviousData);
                                                } else {
                                                    Vue.set(c, 'FormValue', c.ModifyValue);
                                                }
                                                Vue.set(c, 'hasFormModified', false);

                                                if (i == 0 && c.ColumnEName == 'D01103') {
                                                    var tmp = c.FormValue.toString();
                                                    if (tmp.length > 1) {
                                                        that.bathA = tmp.substring(0, tmp.length - 1);
                                                        that.bathB = tmp.substring(tmp.length - 1, tmp.length);

                                                        //Vue.set(c, 'bathA', parseInt(tmp.substring(0, tmp.length - 1)));
                                                        //Vue.set(c, 'bathB', parseInt(tmp.substring(tmp.length - 1, tmp.length)));
                                                    } else if (tmp.length == 1) {
                                                        //Vue.set(c, 'bathA', 0);
                                                        //Vue.set(c, 'bathB', parseInt(tmp.substring(tmp.length - 1, tmp.length)));

                                                        that.bathA = 0;
                                                        that.bathB = tmp.substring(tmp.length - 1, tmp.length);
                                                    } else {
                                                        //Vue.set(c, 'bathA', 0);
                                                        //Vue.set(c, 'bathB', 0);
                                                        that.bathA = "0";
                                                        that.bathB = "0";
                                                    }
                                                }
                                                that.cardData[i][c.ColumnEName] = c;
                                            });

                                        });

                                        //var xxx = tmp_allConditionList.map(function (acl) { return { ConditionHistoryId: acl.ConditionHistoryId, ConditionName: acl.ConditionName }; });

                                        that.allConditionList = Array.from(new Set(tmp_allConditionList.map(acl => acl.ConditionHistoryId))).map(function (c) {
                                            var _condition = tmp_allConditionList.find(s => s.ConditionHistoryId == c);
                                            return { ConditionHistoryId: c, ConditionName: _condition.ConditionName, ConditionString: _condition.ConditionString, ConditionDescription: _condition.ConditionDescription };
                                        });

                                        that.allConditionList.forEach(function (d, i) {
                                            d.hasError = true;
                                        });
                                        that.allMissionConditionList.forEach(function (d, i) {
                                            d.hasError = false;
                                        });
                                        that.allConditionList.forEach(function (d, i) {
                                            that.allMissionConditionList.find(x => x.ConditionHistoryId == d.ConditionHistoryId).hasError = true;
                                        });

                                        that.currentDataErrorListId = that.dataErrors[0].dataErrorListId;

                                 
                                         }
                                    that.needRander = true;
                                    that.openlayout(that.currentDataErrorListId,upOrDown,result);
                                }
                             
                            },complete: function (XMLHttpRequest, textStatus) { 

                             
                               

                        },
                            error: function (jqXHR, textStatus, errorThrown) {
                                if (jqXHR.status !== 401) {
                                    swal(jqXHR.responseText);
                                }
                            }
                        });

                    },
                    //儲存且呈現上一筆資料
                    handlePostAndPrev: function (options = { silenceQuickCheck: false, index: -1 }) {
                        // 檢核資料
                        if (this.checkData()) {
                            // alert('通過');

                            // 先執行公式化欄位更新
                            let that = this;

                            // 作法2 利用快檢的Payload資料post後送，執行公式欄位計算，將回來之data同用get方式bind至頁面上
                            var send_data = that.getCheckPayload(options);
                            // console.log("ready送公式化演算viewModel");
                            // console.log(send_data);

                            //開啟遮罩
                            $.busyLoadFull("show");
                            $.ajax({
                                type: 'post',
                                url: '/api/project/exeFormulaUpdate',
                                data: send_data,
                                contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
                                dataType: 'json',
                                success: function (result) {
                                    // console.log("接到資料瞜 Yenhe");
                                    that.resetData(result); // 將公式化演算後回來之data Bind到頁面欄位
                                    //關閉遮罩
                                    $.busyLoadFull("hide");

                                    /******** 原程式要做的事 開始  *******/

                                    // 取母頁設定的排序flag
                                    let sortClass = window.opener.app.SortClass;
                                    // 2020/12 判斷遞增減排序
                                    let IsOrderByDesc = false;
                                    if (sortClass === "DESC") {
                                        IsOrderByDesc = true;
                                    }
                                    let gotoLast = true; // 回上一筆

                                    that.handleQuickCheck(options);
                                    that.OnlySave();
                                    that.OnlyFindNext(IsOrderByDesc, gotoLast);

                                    /******** 原程式要做的事 結束  *******/
                                },
                                error: function (jqXHR, textStatus, errorThrown) {
                                    //關閉遮罩
                                    $.busyLoadFull("hide");
                                    if (jqXHR.status !== 401) {
                                        swal(jqXHR.responseText);
                                    }
                                }
                            });

                        } else {
                            // alert('不通過');
                        }
                    },
                    //儲存且呈現下一筆資料
                    handlePostAndNext: function (options = { silenceQuickCheck: false, index: -1 }) {

                        // 檢核資料
                        if (this.checkData()) {
                            // alert('通過');

                            // 先執行公式化欄位更新
                            let that = this;

                            // 作法2 利用快檢的Payload資料post後送，執行公式欄位計算，將回來之data同用get方式bind至頁面上
                            var send_data = that.getCheckPayload(options);
                            // console.log("ready送公式化演算viewModel");
                            // console.log(send_data);

                            //開啟遮罩
                            $.busyLoadFull("show");
                            $.ajax({
                                type: 'post',
                                url: '/api/project/exeFormulaUpdate',
                                data: send_data,
                                contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
                                dataType: 'json',
                                success: function (result) {
                                    // console.log("接到資料瞜 Yenhe");
                                    // console.log(result);

                                    that.resetData(result); // 將公式化演算後回來之data Bind到頁面欄位
                                    //關閉遮罩
                                    $.busyLoadFull("hide");
                                    /******** 原程式要做的事 開始  *******/

                                    // 取母頁設定的排序flag
                                    let sortClass = window.opener.app.SortClass; 
                                    // 2020/12 判斷遞增減排序
                                    let IsOrderByDesc = false;
                                    if (sortClass === "DESC") {
                                        IsOrderByDesc = true;
                                    }
                                    let gotoLast = false; // 回上一筆

                                    that.handleQuickCheck(options);
                                    that.OnlySave();
                                    that.OnlyFindNext(IsOrderByDesc, gotoLast);

                                    /******** 原程式要做的事 結束  *******/
                                },
                                error: function (jqXHR, textStatus, errorThrown) {
                                    //關閉遮罩
                                    $.busyLoadFull("hide");
                                    if (jqXHR.status !== 401) {
                                        swal(jqXHR.responseText);
                                    }
                                }
                            });

                        } else {
                            // alert('不通過');
                        }
                    },
                    //刪除
                    handleDelete: function () {
                        this.submitType = 'delete';
                        this.path = '/api/project/modifyErrorList'
                        var that = this;
                        swal({
                            title: "增修型別為新增類型，會真實異動到資料\n其他類型則不會\n是否要刪除?",
                            icon: "warning",
                            buttons: true,
                            dangerMode: true
                        }).then((isDeleted) => {
                            if (isDeleted) {
                                that.handleSubmit();
                                //window.opener.app.getSingleData(that.currentDataErrorListId);
                            } else {
                                return;
                            }
                        });

                    },
                    //取消
                    handleCancel: function () {
                        window.opener.$.busyLoadFull("hide");
                        window.close();
                        //var that = this;
                        //swal({
                        //    title: '你尚未儲存，確定要取消嗎?',
                        //    buttons: true,
                        //    icon: 'warning',
                        //}).then((isCancel) => {
                        //    if (isCancel) {
                        //        window.location.href = '/Project/Modify/?id=' + projectId + '&missionId=' + missionId + '&searchStr=' + searchStr + '&page=' + page + that.GetTabHash();
                        //    }
                        //})
                    },
                    //sanitaryware: function () {
                    //    var tmp = parseInt(`${this.cardData[0].D01103.ModifyValue1}${this.cardData[0].D01103.ModifyValue0}`);
                    //    return tmp;
                    //},
                    //點擊錯誤欄位，列表滑動到那位置
                    focusRow_old: function (dataErrorListId, columnName) {
                        var currentItem = $(`.table-scroll input[name="${columnName}"] `);
                        var divTop = $(`.table-scroll`).offset().top;
                        var elTop = 0;
                        var distance = (elTop - divTop) - 2;
                        // console.log('distance', distance)
                        $(`.table-scroll`).animate({
                            scrollTop: distance
                        }, 1000, function () {
                            currentItem.focus();
                        });
                    },
                    focusRow: function (index, columnName) {
                        let that = this;
                        var currentItem = $(`.table-scroll input[name^="${index}_${columnName}"]`);
                        if (currentItem.length < 1) {
                            currentItem = $(`.table-scroll select[name^="${index}_${columnName}"] `);
                        } else if (currentItem.length > 1) {
                            currentItem = $(`.table-scroll input[name^="${index}_${columnName}"]:checked`);
                            if (currentItem.length == 0) {
                                currentItem = $(`.table-scroll input[name^="${index}_${columnName}"]:eq(0)`);
                            }
                        }

                        //都找不到時找表頭
                        if (currentItem.length < 1) {
                            currentItem = $(`.headerForm input[name^="0_${columnName}"]`);
                            if (currentItem.length < 1) {
                                currentItem = $(`.headerForm select[name^="0_${columnName}"] `);
                            } else if (currentItem.length > 1) {
                                currentItem = $(`.headerForm input[name^="0_${columnName}"]:checked`);
                                if (currentItem.length == 0) {
                                    currentItem = $(`.headerForm input[name^="0_${columnName}"]:eq(0)`);
                                }
                            }
                        }

                        var elTop = 0;
                        if (currentItem.length < 1) {
                            swal("欄位搜尋失敗，請確定上層欄位驗證是否正確");
                            return;
                        } else if (currentItem.length == 1) {
                            elTop = currentItem.offset().top;
                        }

                        const divTop = $(`.table-scroll`).offset().top;
                        var form_div_scrollTop = $(`.table-scroll`).scrollTop();
                        var middleTop = 100;
                        var distance = elTop - divTop;

                        var scrollTop = form_div_scrollTop + distance - middleTop;

                        if (distance != 0) {
                            $(`.table-scroll`).animate({
                                scrollTop: scrollTop
                            }, 300, function () {
                                that.cursorFocus(currentItem);
                            });
                        } else {
                            that.cursorFocus(currentItem);
                        }
                    },
                    //調查表更正
                    LayoutLoadForQuickCheck: function (dataErrorColumnList) {
                        var decl = [];
                        for (var a = 0; a < dataErrorColumnList.length; a++) {
                            decl[a] = { ...dataErrorColumnList[a] };
                        }

                        for (var j = 0; j < decl.length; j++) {
                            decl[j].ModifyValue = decl[j].FormValue;
                        }

                        return decl;
                    },
                    LayoutLoad: function (index, dataErrorColumnList) {
                        dataErrorColumnList.forEach((column, i) => {
                            if (column.IsManual) {
                                column.ModifyValue = column.FormValue;
                                column.hasFormModified = true;

                            } else {
                                if (column.PreviousData != column.FormValue) {
                                    column.ModifyValue = column.FormValue;
                                    column.hasFormModified = true;
                                }

                                // 判斷為新增mode:全部欄位皆更新
                                if (this.dataErrorListId == -1) {
                                    column.ModifyValue = column.FormValue;
                                }
                            }

                            // 2020/09 判斷是否因系統做公式化計算而變更 需另用flag判斷
                            if (column.IsFormulaChange === true) {
                                column.hasFormModified = true;
                            }

                            // 2020/12 彈增:判斷遮罩機敏資料，無權限
                            // 更正模式
                            if (this.dataErrorListId !== -1) {
                                // 更正員無權限 一律為false 不可改該隱碼遮罩欄位
                                if (this.canUnMask === false && column.IsMask === true) {
                                    column.hasFormModified = false;
                                }
                            }

                        });

                        // 判斷為新增mode:全部欄位皆後傳，更正mode:維持舊邏輯僅後傳異動的欄位
                        if (this.dataErrorListId == -1) {
                            return dataErrorColumnList;
                        } else {

                            return dataErrorColumnList.filter(x => x.hasFormModified);
                        }
                    },

                    // // 公式化計算 舊作法  儲存時，針對處理公式化欄位所需資料，全欄位後傳
                    // LayoutLoadForCheckFormula: function (index, dataErrorColumnList) {
                    //     dataErrorColumnList.forEach((column, i) => {
                    //         // 頁面 「更正後資料」欄位為 FormValue
                    //         column.ModifyValue = column.FormValue;
                    //         column.hasFormModified = true;
                    //     });
                    // 
                    //     // 僅 針對有修改後的欄位
                    //     return dataErrorColumnList.filter(x => x.hasFormModified);
                    // },

                    //前往資料查找頁
                    handleRedirectDetail() {
                        var dataError = this.dataErrors.find(x => x.dataErrorListId === this.currentDataErrorListId);
                        if (dataError) {
                            if (!dataError.dataId) {
                                swal('此資料為新增，審核通過才會真正新增至表格，故無法進行查找資料');
                                return;
                            }
                            window.open('/DManagement/Search/?ConditionMissionId=' + missionId + "&TableName="
                                + this.tableName + "&DataId=" + dataError.dataId + "&ProjectId=" + projectId
                                + "&FileSchemaId=" + this.fileSchemaId + "&Type=1", '資料查找', 'width=' + (window.screen.availWidth - 10) + ',height=' + (window.screen.availHeight - 30) + ',top=0,left=0,resizable=yes,status=yes,menubar=no,scrollbars=yes');
                            //window.open('/DManagement/Search/?ConditionMissionId=' + missionId + "&TableName="
                            //    + this.tableName + "&DataId=" + dataError.dataId + "&ProjectId=" + projectId
                            //    + "&FileSchemaId=" + this.fileSchemaId,
                            //    '_blank');
                        }

                    },
                    handleOCR: function () {

                        var dataError = this.dataErrors.find(x => x.dataErrorListId === this.currentDataErrorListId);
                        var url = "";
                        var cApplyNo = dataError.censusNo;
                        var print = "1";
                        var mask = "0";
                        //var Account = this.userId;
                        var Account = 'test';
                        $.ajax({
                            type: this.submitType,
                            url: '/api/project/GetORCUrl/' + missionId,
                            contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
                            dataType: 'json',
                            async: false,
                            success: function (result) {
                                if (result.status == "success") {
                                    url = result.url;
                                    //url = url + "?cApplyNo=" + cApplyNo + "&print=" + print + "&mask=" + mask + "&Account=" + Account;
                                    url = url + "?cApplyNo=" + cApplyNo + "&print=" + print + "&mask=" + mask + "&cAccount=" + result.user;
                                } else {
                                    swal(result.message);
                                }
                            },
                            error: function (jqXHR, textStatus, errorThrown) {
                                if (jqXHR.status !== 401) {
                                    swal(jqXHR.responseText);
                                }
                            }
                        })
                        window.open(url, '_blank');

                    },

                    //組合要傳到後端快檢的資料
                    getCheckPayload: function (options = { silenceQuickCheck: false, index: -1 }) {

                        let that = this;
                        let __RequestVerificationToken = $('[name="__RequestVerificationToken"]').val();

                        let viewModel = {
                            ProjectId: projectId,
                            ConditionMissionId: missionId,
                            FileSchemaId: this.fileSchemaId,
                            TableName: this.tableName,
                            UserId: this.userId,
                            UserName: this.UserName,
                            ExecuteUserId: this.ExecuteUserId,  // 更正員
                            ExecuteUserName: this.ExecuteUserName,
                            CreatorId: this.CreatorId,  // 分派者 = 審查員
                            CreatorName: this.CreatorName,
                            canUnMask : this.canUnMask,
                            MaskColumnList : this.MaskColumnList,


                            silenceQuickCheck: options.silenceQuickCheck,
                        };

                        viewModel.ModifyKeyupDataErrorList = [];

                        //取某個卡，或取全部卡
                        let len = this.dataErrors.length;
                        let i = 0;
                        
                        console.log("sdfsdf" + len + options.index);
                        if (options.index > -1) {
                            i = options.index;
                            len = i + 1;
                            
                        }

                        for (i; i < len; i++) {
                            if (options.index > -1) {//第幾筆關聯參考黨與資料檔的關聯表

                                viewModel.ModifyKeyupDataErrorList[0] = {
                                    DataErrorListId: this.dataErrors[i].dataErrorListId,
                                    CensusNo: this.dataErrors[i].censusNo,
                                    DataId: this.dataErrors[i].dataId,
                                    SourceId: this.dataErrors[i].sourceId,
                                    isDelete: this.dataErrors[i].isDelete,
                                    RelationGroupId: this.dataErrors[i].relationGroupId,
                                    ConditionInfoList: this.dataErrors[i].conditionList,
                                    DataErrorColumnList: that.LayoutLoadForQuickCheck(this.dataErrors[i].dataErrorColumnList),
                                    SpecialSkipRemark: this.dataErrors[i].specialSkipRemark,
                                    IsPageValue: this.dataErrors[i].isPageValue
                                }
                                break;
                            }
                            else {
                                viewModel.ModifyKeyupDataErrorList[i] = {
                                    DataErrorListId: this.dataErrors[i].dataErrorListId,
                                    CensusNo: this.dataErrors[i].censusNo,
                                    DataId: this.dataErrors[i].dataId,
                                    SourceId: this.dataErrors[i].sourceId,
                                    isDelete: this.dataErrors[i].isDelete,
                                    RelationGroupId: this.dataErrors[i].relationGroupId,
                                    ConditionInfoList: this.dataErrors[i].conditionList,
                                    DataErrorColumnList: that.LayoutLoadForQuickCheck(this.dataErrors[i].dataErrorColumnList),
                                    SpecialSkipRemark: this.dataErrors[i].specialSkipRemark,
                                    IsPageValue: this.dataErrors[i].isPageValue
                                }

                            }
                        }

                        return { 'ModifyKeyupViewModel': viewModel, '__RequestVerificationToken': __RequestVerificationToken };
                    },
                    ConditionCheckResult: function (ErrorDataList) {
                        let all_tmp = '';
                        let obj = ErrorDataList.Result;

                        if (obj.length > 0) {
                            obj.forEach((x, i) => {
                                let tmp = '';
                                x.cons.forEach(c => {
                                    //tmp += `[序號(${c.cid});名稱(${c.cn})]\r\n`;
                                    tmp += `[檢誤條件名稱(${c.cn})]\r\n`;
                                });
                                all_tmp += `流水號(...${x.id}) 未通過檢誤條件如下：\r\n${tmp}\r\n`
                            });
                        } else {
                            all_tmp = `資料檢誤通過\r\n\r\n`;;
                        }

                        swal('快速檢誤結果一覽', all_tmp);
                    },
                    ConditionCheckResult_Old: function (ErrorDataList) {
                        let a = 0;
                        let count = ErrorDataList.Result.length;
                        let all_tmp = '';

                        for (let index in ErrorDataList.Result) {
                            a++;
                            let tmp = '';
                            let DataId = {};
                            for (let ScriptStates in ErrorDataList.Result[index]) { //data being the object
                                for (let i in ErrorDataList.Result[index][ScriptStates].SelectResults) {
                                    if (!DataId[ErrorDataList.Result[index][ScriptStates].SelectResults[i].Id]) {
                                        DataId[ErrorDataList.Result[index][ScriptStates].SelectResults[i].Id] = { DataId: ErrorDataList.Result[index][ScriptStates].SelectResults[i].Id, tmp: '' };
                                    }
                                    DataId[ErrorDataList.Result[index][ScriptStates].SelectResults[i].Id].tmp += `[序號(${ErrorDataList.Result[index][ScriptStates].SelectResults[i].conId});名稱(${ErrorDataList.Result[index][ScriptStates].SelectResults[i].conName})]\r\n`;
                                }
                            }
                            for (let dataid in DataId) {
                                if (DataId[dataid].tmp !== '') {
                                    var dataError = this.dataErrors.find(x => x.dataId == dataid);

                                    //依指定欄位的值排序
                                    //if (this.SeqColumnName) {
                                    //    DataId[dataid].cardSno = dataError.dataErrorColumnList.find(x => x.ColumnEName == this.SeqColumnName).FormValue;
                                    //} else {
                                    //    DataId[dataid].cardSno = this.dataErrors.indexOf(dataError) + 1;
                                    //}

                                    DataId[dataid].cardSno = this.dataErrors.indexOf(dataError) + 1;
                                }
                            }

                            let ErrorList = [];
                            for (let dataid in DataId) {
                                ErrorList.push(DataId[dataid]);
                            }
                            ErrorList = ErrorList.sort(function (a, b) {
                                return a.cardSno > b.cardSno ? 1 : -1;
                            });
                            ErrorList.forEach((del, i) => {
                                tmp += `第[${del.cardSno}]筆 未通過檢誤條件如下：\r\n${del.tmp}\r\n`
                            });

                            if (!tmp) {
                                tmp = `資料檢誤通過\r\n\r\n`;
                            }
                            all_tmp += tmp;

                            //for (let key in result[a].Result) { //data being the object
                            //    if (result.Result[a][key].length > 0) {
                            //        let k_index = key.lastIndexOf('_');
                            //        let cn = key.substr(0, k_index);
                            //        let id = key.substr(k_index + 1);
                            //        //tmp += `\n[(${id})-${cn}]`;
                            //        tmp += `\n[${cn}]`;
                            //    }
                            //}
                        }

                        swal('快速檢誤結果一覽', all_tmp);

                        //swal(JSON.stringify(result));
                        //swal(result.Result === 'True' ?);
                    },
                    handleBeforeQuickCheck: function (options = { silenceQuickCheck: false, index: -1 }) {
                        // 執行快檢前 先執行公式化欄位更新
                        let that = this;

                        // 利用快檢的Payload資料post後送，執行公式欄位計算，將回來之data同用get方式bind至頁面上
                        var send_data = that.getCheckPayload(options);
                        // console.log("ready送公式化演算viewModel");
                        // console.log(send_data);

                        //開啟遮罩
                        $.busyLoadFull("show");
                        $.ajax({
                            type: 'post',
                            url: '/api/project/exeFormulaUpdate',
                            data: send_data,
                            contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
                            dataType: 'json',
                            success: function (result) {
                                // console.log("接到資料瞜 Yenhe");
                                // console.log(result);
                                // 用get方式 更新頁面資料
                                that.submitType = 'get';
                                that.resetData(result);
                                //關閉遮罩
                                $.busyLoadFull("hide");

                                /******** 原程式要做的事 開始  *******/
                                that.handleQuickCheck(options);
                                /******** 原程式要做的事 結束  *******/
                            },
                            error: function (jqXHR, textStatus, errorThrown) {
                                //關閉遮罩
                                $.busyLoadFull("hide");
                                if (jqXHR.status !== 401) {
                                    swal(jqXHR.responseText);
                                }
                            }
                        });
                    },
                    handleQuickCheck: function (options = { silenceQuickCheck: false, index: -1 }) {

                        if (this.dataErrors.some(x => x.dataId == -1)) {
                            return; //swal("該普查編號因有「新增資料」，須請「送審」通過及執行檢誤，再進行後續更正。");
                        } else {
                            let that = this;

                            //if (that.conditionList.length < 1) {
                            //開啟遮罩
                            let apiUrl = '/api/project/modifyQuickCheck';
                            if (!options.silenceQuickCheck) {
                                $.busyLoadFull("show");
                                //apiUrl = '/api/project/modifyQuickCheck';
                            } else {
                                //apiUrl = '/api/project/modifyNextQuickCheck';
                            }

                            that.submitType = 'post';
                            //let quick_xhr = $.ajax({
                            $.ajax({
                                type: that.submitType,
                                url: apiUrl,
                                data: that.getCheckPayload(options),
                                contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
                                dataType: 'json',
                                success: function (result) {
                                    if (!options.silenceQuickCheck) {
                                        that.ConditionCheckResult(result);

                                        //關閉遮罩
                                        $.busyLoadFull("hide");
                                    }
                                },
                                error: function (jqXHR, textStatus, errorThrown) {
                                    //關閉遮罩
                                    if (!options.silenceQuickCheck) {
                                        $.busyLoadFull("hide");
                                        if (jqXHR.status !== 401) {
                                            swal(jqXHR.responseText);
                                        }
                                    }
                                }
                            });

                            //if (options.silenceQuickCheck) {
                            //    setTimeout(() => quick_xhr.abort(), 100);
                            //}
                        }
                    },
                    getVD: function (vd) {
                        console.log(vd)
                        var vdJson = vd ? JSON.parse(vd) : {};
                        var tmp = "";
                        var val_arr = []; //val_arr.concat(pieces);

                        for (var key in vdJson) {
                            var IsDesKey = key.endsWith("_des");
                            var pieces = key.split(/[_]+/).filter(x => x && x != "des");

                            var ValueStr = "";
                            if (key !== 'Id') {
                                switch (typeof (vdJson[key])) {
                                    case "number":
                                        ValueStr = `${vdJson[key]}`;
                                        break;
                                    case "string":
                                        ValueStr = `"${vdJson[key]}"`;
                                        break;
                                    case "boolean":
                                        ValueStr = `${vdJson[key]}`;
                                        break;
                                    default:
                                        ValueStr = `${vdJson[key]}`;
                                        break;
                                }

                                pieces.forEach(k => {
                                    var vdObj = { col: k, val: ValueStr, type: IsDesKey ? 'des' : 'vd' };
                                    val_arr.push(vdObj);
                                });
                            }
                        }

                        var valTmp = "";
                        var desTmp = "";
                        val_arr.forEach(o => {
                            if (o.type == 'vd') {
                                valTmp += `${o.col} = ${o.val};\n`;
                            } else {
                                desTmp += `${o.col}：${o.val};\n`;
                            }
                        });
                        tmp = valTmp + '\n說明：\n' + desTmp;
                        return tmp;
                    },
                    switchData: function () {

                        $(".errorCols div").removeClass("currentDataList");
                        var currentItem = $(`.errorCols div[data-id=${this.currentDataErrorListId}]`);

                        let itemH = 27;
                        //itemH = currentItem[0].offsetHeight;
                        //if (itemH > 30) {
                        //    itemH = 30;
                        //}
                        //$(`.errorColsBlank`).css("height", `${itemH}px`);

                        var divTop = $(`.errorCols`).offset().top;
                        var divTop = $(`.errorCols`).offset().top;
                        var form_div_scrollTop = $(`.errorCols`).scrollTop();
                        var elTop = currentItem.offset().top;
                        var distance = (elTop - divTop);
                        var scrollTop = form_div_scrollTop + distance;
                        if (distance != 0) {
                            console.log('distance', distance)
                            $(`.errorCols`).animate({
                                scrollTop: scrollTop - itemH
                            }, 500, function () {
                                $(currentItem).addClass("currentDataList");
                            });
                        } else {
                            $(currentItem).addClass("currentDataList");
                        }
                    },
                    GetCurrentDataErrors: function () {
                        return this.dataErrors.find(x => x.dataErrorListId === this.currentDataErrorListId);
                    },
                    ClearFormValue: function (fi, fe) {
                        let that = this;
                        let fullname = $(fe).prop("name");
                        let sub_arr = fullname.split('_');
                        let sub_index = sub_arr[0];
                        let sub_name = sub_arr[1];
                        that.cardData[sub_index][sub_name].FormValue = null;

                        //人口住宅衛浴套數有轉換小數點，欄位需要做特別處理
                        if (sub_name == 'D01103') {
                            that.bathA = null;
                            that.bathB = null;
                        }

                        let fels = $(".table-scroll").find(`[data-follow=${fullname}]`);
                        $(fels).each(that.ClearFormValue);
                    },
                    clickTown: function (code, town, city) {
                        this.currentCode = code;
                        this.currentTown = town;
                        this.currentCity = city;

                        if (this.currentZipCodeDataList.Code !== null)
                            this.currentZipCodeDataList.Code.FormValue = this.currentCode;

                        if (this.currentZipCodeDataList.Town !== null)
                            this.currentZipCodeDataList.Town.FormValue = this.currentTown;

                        if (this.currentZipCodeDataList.City !== null)
                            this.currentZipCodeDataList.City.FormValue = this.currentCity;

                        $("#zip-modal").modal('hide');

                        return false;
                    },
                    //clickCrop: function (code, crop) {
                    //    this.currentCropCode = code;
                    //    this.currentCrop = crop;

                    //    if (this.currentCropCodeDataList.Code !== null)
                    //        this.currentCropCodeDataList.Code.FormValue = this.currentCropCode;

                    //    if (this.currentCropCodeDataList.Crop !== null)
                    //        this.currentCropCodeDataList.Crop.FormValue = this.currentCrop;

                    //    $("#crop-modal").modal('hide');

                    //    return false;
                    //},
                    clickCode: function (code, name) {
                        //debugger;
                        this.currentcurrentCode = code;
                        this.currentcurrentName = name;

                        if (this.currentcurrentCodeDataList.Code !== null)
                            this.currentcurrentCodeDataList.Code.FormValue = this.currentcurrentCode;

                        if (this.currentcurrentCodeDataList.Name !== null)
                            this.currentcurrentCodeDataList.Name.FormValue = this.currentcurrentName;

                        $("#zip2-modal").modal('hide');

                        return false;
                    },
                    //clickPoultry: function (code, Poultry) {
                    //    this.currentPoultryCode = code;
                    //    this.currentPoultry = Poultry;

                    //    if (this.currentPoultryCodeDataList.Code !== null)
                    //        this.currentPoultryCodeDataList.Code.FormValue = this.currentPoultryCode;

                    //    if (this.currentPoultryCodeDataList.Poultry !== null)
                    //        this.currentPoultryCodeDataList.Poultry.FormValue = this.currentPoultry;

                    //    $("#poultry-modal").modal('hide');

                    //    return false;
                    //},
                    toggleTab: function () {   //讓這頁的頁籤是對的
                        $('.nav-tabs li:not(.sub-tab)').removeClass('active');
                        //其他頁面跳轉進來，開啟Tab
                        var hash = window.location.hash;
                        if (hash && hash !== '') {
                            $('a[href*="' + hash + '"]').closest('li').addClass('active');
                        }
                    },
                    // click儲存後的檢核
                    checkData: function () {
                        // alert('檢查中');

                        let err_msg = '';

                        // 每一卡資料loop
                        this.dataErrors.forEach(function (dataErr, di) {
                            // 計算第幾卡
                            var card_idx = di + 1;
                            // 此卡 所有欄位loop
                            dataErr.dataErrorColumnList.forEach(function (c, ci) {
                                // 判斷是否 普編or多卡 關鍵欄位
                                if (c.isCensusNoCol || c.IsRelationKey) {
                                    // 判斷是否填足位數
                                    if (c.FormValue.length != c.DataLength) {
                                        err_msg += '第' + card_idx + `卡 [${c.ColumnEName}]不足位數(${c.DataLength})\r\n`;
                                    }
                                }

                                // 檢查 int欄位 是否key數字
                                if (c.DataTypeId === 2) {
                                    var theVal = c.FormValue;
                                    if (isNaN(parseInt(theVal))) {
                                        err_msg += '第' + card_idx + `卡 [${c.ColumnEName}]請輸入半形數字\r\n`;
                                    }
                                }
                            });
                        });

                        // 有錯誤訊息
                        if (err_msg != '') {
                            swal('如下欄位檢核有誤:\r\n' + err_msg);
                            return false;
                        }

                        return true;
                    },
                    // 2020/09 需求訪談: 人口，可調查表新增，並預帶部分欄位
                    AddDataLayout: function (dataId) {
                        var that = this;
                        // 新增資料 開新窗 
                        // 新版新增 以dataErrorListId=-1代表新增模式
                        winson = window.open('/Project/Modify/Layout/?id=' + window.projectId + "&conditionMissionId=" + window.missionId + "&dataErrorListId=-1&searchStr=&page=1&auditor=0&dataIdCopy=" + dataId
                            + this.GetTabHash()
                            , '調查表新增', 'width=' + (window.screen.availWidth - 10) + ',height=' + (window.screen.availHeight - 30) + ',top=0,left=0,resizable=yes,status=yes,menubar=no,scrollbars=yes');
                        // 更正資料 關本窗 
                        window.onbeforeunload = null;
                        window.close();
                    },
                },
                computed: {
                    IsEnableEdit: {
                        get: function () {
                            //return this.userId == this.LoginUserId;
                            return true;
                        }
                    },
                    currentZipCity: {
                        get: function () {
                            if (this.filterCityName) {
                                return this.zipCode.filter((t => t.city == this.filterCityName));
                            }
                        }
                    },
                    AllCode: {
                        get: function () {
                            var _this = this;
                            var tableElement;
                            if (_this.tableAll.find(item => item[_this.classcode2]) != undefined) {
                                if (_this.filterCodeName) {
                                    _this.tableAll.forEach(function (item) {

                                        tableElement = item[_this.classcode2].filter((t => t.Name.includes(_this.filterCodeName)));

                                    });

                                } else {
                                    _this.tableAll.forEach(function (item) {

                                        tableElement = item[_this.classcode2];
                                    });
                                }
                            }



                            if (this.classcode2 == "countycode") {
                                if (this.filterCodeName) {
                                    return this.countyCode.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.countyCode;
                                }
                            }
                            else if (this.classcode2 == "cropcode") {
                                if (this.filterCodeName) {
                                    return this.cropCode.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.cropCode;
                                }
                            }
                            else if (this.classcode2 == "poultrycode") {
                                if (this.filterCodeName) {
                                    return this.poultryCode.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.poultryCode;
                                }
                            }
                            else if (this.classcode2 == "poultryservicecode") {
                                if (this.filterCodeName) {
                                    return this.poultryserviceCode.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.poultryserviceCode;
                                }
                            }
                            else if (this.classcode2 == "fish_3_2") {
                                if (this.filterCodeName) {
                                    return this.fish_3_2Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.fish_3_2Code;
                                }
                            }
                            else if (this.classcode2 == "fish_3_4") {
                                if (this.filterCodeName) {
                                    return this.fish_3_4Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.fish_3_4Code;
                                }
                            }
                            else if (this.classcode2 == "fish_5_3") {
                                if (this.filterCodeName) {
                                    return this.fish_5_3Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.fish_5_3Code;
                                }
                            }
                            else if (this.classcode2 == "fish_5_4") {
                                if (this.filterCodeName) {
                                    return this.fish_5_4Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.fish_5_4Code;
                                }
                            }
                            else if (this.classcode2 == "fish_5_5") {
                                if (this.filterCodeName) {
                                    return this.fish_5_5Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.fish_5_5Code;
                                }
                            }
                            else if (this.classcode2 == "fish_5_6") {
                                if (this.filterCodeName) {
                                    return this.fish_5_6Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.fish_5_6Code;
                                }
                            }
                            else if (this.classcode2 == "fish_5_8") {
                                if (this.filterCodeName) {
                                    return this.fish_5_8Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.fish_5_8Code;
                                }
                            }
                            else if (this.classcode2 == "fish_14_4") {
                                if (this.filterCodeName) {
                                    return this.fish_14_4Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.fish_14_4Code;
                                }
                            }
                            else if (this.classcode2 == "fish_14_5") {
                                if (this.filterCodeName) {
                                    return this.fish_14_5Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.fish_14_5Code;
                                }
                            }
                            else if (this.classcode2 == "fish_14_6") {
                                if (this.filterCodeName) {
                                    return this.fish_14_6Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.fish_14_6Code;
                                }
                            }
                            else if (this.classcode2 == "fish_14_7") {
                                if (this.filterCodeName) {
                                    return this.fish_14_7Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.fish_14_7Code;
                                }
                            }
                            //
                            else if (this.classcode2 == "farm_3_2") {
                                if (this.filterCodeName) {
                                    return this.farm_3_2Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.farm_3_2Code;
                                }
                            }
                            else if (this.classcode2 == "farm_3_5") {
                                if (this.filterCodeName) {
                                    return this.farm_3_5Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.farm_3_5Code;
                                }
                            }
                            else if (this.classcode2 == "farm_3_6") {
                                if (this.filterCodeName) {
                                    return this.farm_3_6Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.farm_3_6Code;
                                }
                            }
                            else if (this.classcode2 == "farm_3_7") {
                                if (this.filterCodeName) {
                                    return this.farm_3_7Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.farm_3_7Code;
                                }
                            }
                            else if (this.classcode2 == "farm_4_3") {
                                if (this.filterCodeName) {
                                    return this.farm_4_3Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.farm_4_3Code;
                                }
                            }
                            else if (this.classcode2 == "farm_4_5") {
                                if (this.filterCodeName) {
                                    return this.farm_4_5Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.farm_4_5Code;
                                }
                            }
                            else if (this.classcode2 == "farm_4_6") {
                                if (this.filterCodeName) {
                                    return this.farm_4_6Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.farm_4_6Code;
                                }
                            }
                            else if (this.classcode2 == "farm_12_5") {
                                if (this.filterCodeName) {
                                    return this.farm_12_5Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.farm_12_5Code;
                                }
                            }
                            else if (this.classcode2 == "farm_12_6") {
                                if (this.filterCodeName) {
                                    return this.farm_12_6Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.farm_12_6Code;
                                }
                            }
                            else if (this.classcode2 == "farm_12_7") {
                                if (this.filterCodeName) {
                                    return this.farm_12_7Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.farm_12_7Code;
                                }
                            }
                            else if (this.classcode2 == "farm_12_8") {
                                if (this.filterCodeName) {
                                    return this.farm_12_8Code.filter((t => t.Name.includes(this.filterCodeName)));
                                } else {
                                    return this.farm_12_8Code;
                                }

                            }
                            return tableElement;
                        }
                    },
                    currentConditionHasError: {
                        get: function () {
                            if (this.currentConditionHistoryId != -1) {
                                return this.allMissionConditionList.find(x => x.ConditionHistoryId == this.currentConditionHistoryId).hasError;
                            } else {
                                return false;
                            }
                        }
                    },
                    myConditionList: {
                        get: function () {
                            if (this.isNoConditionFilter) {
                                return this.allMissionConditionList;
                            } else {
                                return this.allConditionList;
                            }
                        }
                    },
                    DataSourceId: {
                        get: function () {
                            var del = this.GetCurrentDataErrors();
                            if (del) {
                                return del.sourceId;
                            }
                            else {
                                return -1;
                            }
                        },
                        set: function (value) {
                            var del = this.GetCurrentDataErrors();
                            if (del) {
                                del.sourceId = value;
                            }
                            else {
                                del.sourceId = -1;
                            }
                        }
                    },
                    //若按所有條件，條件欄位顯示資訊不一樣
                    conditionNameTextArea: {
                        get: function () {
                            var that = this;
                            var result = {
                                allCondition: false,
                                firstFieldLabel: '檢誤條件語法',
                                firstField: '',
                                secondField: '',
                                thirdField: ''
                            }

                            var dataError = that.dataErrors.find(x => x.dataErrorListId === that.currentDataErrorListId);
                            if (dataError) {
                                if (that.currentConditionHistoryId === -1) {
                                    if (dataError.conditionList.length > 0) {
                                        result.firstField = dataError.conditionList.map(x => x.ConditionName).join(', ');
                                    }
                                    return { ...result, allCondition: true, firstFieldLabel: '檢誤條件名稱' };
                                } else {
                                    var condition = that.myConditionList.find(s => s.ConditionHistoryId == that.currentConditionHistoryId);
                                    var conditionHis = dataError.conditionList.find(x => x.ConditionHistoryId === that.currentConditionHistoryId)
                                    var VirtualValue = "";
                                    if (conditionHis) {
                                        VirtualValue = that.getVD(conditionHis.VirtualValue);
                                    }
                                    return {
                                        ...result,
                                        firstField: condition.ConditionString,
                                        secondField: VirtualValue,
                                        thirdField: condition.ConditionDescription,
                                    };
                                }
                            }
                            return { ...result };

                        }
                    },
                    //是否要略過次條件的呈現
                    passCondition: {
                        get: function () {
                            var that = this;
                            var dataError = that.dataErrors.find(x => x.dataErrorListId === that.currentDataErrorListId);
                            if (dataError)
                                if (that.currentConditionHistoryId !== -1) {
                                    var conditionHis2 = dataError.conditionList.find(x => x.ConditionHistoryId === that.currentConditionHistoryId);
                                    if (typeof (conditionHis2) != "undefined") {
                                        return dataError.conditionList.find(x => x.ConditionHistoryId === that.currentConditionHistoryId).PassCondition
                                    } else {
                                        return false
                                    }
                                }
                            return false;
                        },
                        set: function (value) {
                            var that = this;
                            //var dataError = that.dataErrors.find(x => x.dataErrorListId === that.currentDataErrorListId);
                            //if (dataError)
                            //    if (that.currentConditionHistoryId !== -1) {
                            //        dataError.conditionList.find(x => x.ConditionHistoryId === that.currentConditionHistoryId).PassCondition = value;
                            //    }
                            if (that.currentConditionHistoryId !== -1) {
                                that.dataErrors.forEach((dataError, i) => {
                                    dataError.conditionList.find(x => x.ConditionHistoryId === that.currentConditionHistoryId).PassCondition = value;
                                });
                            }
                        }
                    },
                    //若cannotPass == true ，就不能按掠過此條件的紐
                    passConditionLock: {
                        get: function () {
                            var that = this;
                            var dataError = that.dataErrors.find(x => x.dataErrorListId === that.currentDataErrorListId);
                            if (dataError)
                                if (that.currentConditionHistoryId !== -1) {
                                    var conditionHis = dataError.conditionList.find(x => x.ConditionHistoryId === that.currentConditionHistoryId)
                                    if (typeof (conditionHis) != "undefined") {
                                        return conditionHis.CannotPass;
                                    } else {
                                        return true;
                                    }
                                }
                            return true;
                        }
                    },
                    //錯誤欄位列表(非table)
                    dataErrorListColumnNames: {
                        get: function () {
                            var arr = [];
                            var ccl = this.allConditionList;

                            var cchid = this.currentConditionHistoryId;

                            var conditionName = '';
                            if (cchid != -1) {
                                var ccc = ccl.filter(function (c) { return c.ConditionHistoryId == cchid });
                                var c_arr = ccc.map(cn => cn.ConditionName);
                                if (c_arr.length > 0) conditionName = c_arr[0];
                            }

                            this.dataErrors.forEach((dataError, i) => {

                                if (dataError) {
                                    arr[i] = dataError.dataErrorColumnList.filter(function (x) {
                                        var ret = true;

                                        if (x.ConditionNameList.length == 0) {
                                            ret = false;   //如果沒有錯誤條件，代表是對的column，要lock
                                        } else {
                                            //目前的錯誤檢誤條件下拉選單是全部還是有被指定到
                                            if (conditionName) {
                                                if (x.ConditionNameList.indexOf(conditionName) == -1) {
                                                    ret = false;
                                                }
                                            }
                                        }

                                        return ret;
                                    }).map(function (x) {
                                        return {
                                            ColumnEName: x.ColumnEName,
                                            DataErrorListColumnId: x.DataErrorListColumnId
                                        }
                                    });
                                }
                            });
                       
                            return arr;
                        }
                    },
                },
                watch: {
                    bathA(newVal, oldVal) {
                        if (newVal != oldVal)
                            this.cardData[0].D01103.FormValue = parseInt(newVal + this.bathB);
                    },
                    bathB(newVal, oldVal) {
                        if (newVal != oldVal)
                            this.cardData[0].D01103.FormValue = parseInt(this.bathA + newVal);
                    },

                },
                created: function () {
                    //vue instance 被 constructor 建立後，在這裡完成 data binding

                    if (layoutExist) {
                        var that = this;
                        that.resetData(DataResult);
                    } else {
                        swal("尚未設定調查表，請至普查設定 / 調查表新增").then(val => {
                            window.history.go(-1);
                            return false;
                        });
                    }
                },
                mounted: function () {

                    //if (layoutExist) {
                    //    var that = this;
                    //    that.resetData(DataResult);
                    //} else {
                    //    swal("尚未設定調查表，請至普查設定 / 調查表新增").then(val => {
                    //        window.history.go(-1);
                    //        return false;
                    //    });
                    //}

                    let that = this;
                    console.log("aaa");


                    this.toggleTab();

                    //等到全部render完，再填入全部的調查表
                    this.$nextTick(function () {

                        if (this.firstRander) {

                            //this.LayoutInit();
                            // 新增mode (不用鎖頭效果，並解開全部唯讀)
                            if (that.dataErrorListId == -1) {
                                $(".table-scroll input[disabled=disabled]").removeAttr("disabled");
                                $(".table-scroll select[disabled=disabled]").removeAttr("disabled");
                            } else {
                                // 更正mode 要加鎖頭效果
                                $(".lockGroupTR").append("<td  border=\"0\" style=\" margin:0px; border:none; background: transparent;position:fixed; bottom:1%; right:10px;\" class=\"fa fa-lock unlockBtn2\" aria-hidden=\"true\" title=\"解鎖\" onclick=\"unlock(this)\"></td>");
                                $(".lockGroup").append("<i class=\"fa fa-lock unlockBtn\" aria-hidden=\"true\" title=\"解鎖\" onclick=\"unlock(this)\"></i>");
                            }

                            $('#BackTop').click(function () {
                                $('html,body').animate({ scrollTop: 0 }, 333);
                            });

                            $(window).scroll(function () {
                                if ($(this).scrollTop() > 300) {
                                    $('#BackTop').fadeIn(222);
                                } else {
                                    $('#BackTop').stop().fadeOut(222);
                                }
                            }).scroll();

                            this.firstRander = false;//第一次更新完
                        };

                        if (this.needRander) {
                            $(".table-scroll input[type=radio]").each(function () {
                                $(this).prop("title", `${$(this).prop("name")} (${$(this).data("value")})`);
                            });
                            $(".table-scroll input[type=checkbox]").each(function () {
                            
                                $(this).prop("title", `${$(this).prop("name")} (${$(this).data("value")})`);
                            });
                            $(".table-scroll input[type=text]").each(function () {
                                $(this).prop("title", `${$(this).prop("name")}`);
                            });
                            $(".table-scroll textarea").each(function () {
                                $(this).prop("title", `${$(this).prop("name")}`);
                            });
                            $(".table-scroll select").each(function () {
                                $(this).prop("title", `${$(this).prop("name")} (${$(this).data("value")})`);
                            });
                            //右鍵清除欄位值
                            $(".table-scroll input").contextmenu(function () {
                                var name = $(this).prop("name");
                                var name_arr = $(this).prop("name").split('_');
                                var dataIndex = name_arr[0];
                                var col_name = name_arr[1];
                                var type = $(this).prop("type");
                                swal({
                                    text: `$清除 ${col_name} 的資料?`,
                                    buttons: ['取消', '確認'],
                                }).then(value => {
                                    if (value) {
                                        that.ClearFormValue(0, this);
                                        //that.cardData[dataIndex][col_name].FormValue = null;
                                        //if (col_name == 'D01103') {
                                        //    that.bathA = null;
                                        //    that.bathB = null;
                                        //}

                                        //var fels = $(".table-scroll").find(`[data-follow=${name}]`);
                                        ////$(fels).hide();

                                        //$(fels).each(that.ClearFormValue);
                                    } else {
                                        return;
                                    }
                                })
                                return false;
                            });
                            $(".table-scroll select").contextmenu(function () {
                                var name = $(this).prop("name");
                                var name_arr = $(this).prop("name").split('_');
                                var dataIndex = name_arr[0];
                                var col_name = name_arr[1];
                                var type = $(this).prop("type").split('-')[0];
                                swal({
                                    text: `$清除 ${col_name} 的資料?`,
                                    buttons: ['取消', '確認'],
                                }).then(value => {
                                    if (value) {
                                        that.ClearFormValue(0, this);
                                        //that.cardData[dataIndex][col_name].FormValue = null;

                                        //let fels = $(".table-scroll").find(`[data-follow=${name}]`);
                                        ////$(fels).hide();

                                        //$(fels).each(that.ClearFormValue);
                                    } else {
                                        return;
                                    }
                                })
                                return false;
                            });

                            //縣市鄉鎮代號
                            $(".table-scroll input[type=text].zipcode").click(function (x) {

                                //取得所在位置的所有input欄位
                                var el = $(this).parent().find("input[type=text]").toArray();

                                //縣市鄉鎮代號在所在位置的所有input欄位中的索引
                                let codeField_index = el.indexOf(this);
                                //鄉鎮市區名稱欄位在所在位置的所有input欄位中的索引
                                let townField_index = codeField_index - 1;
                                //縣市名稱欄位在所在位置的所有input欄位中的索引
                                let cityField_index = codeField_index - 2;

                                let zip = that.zipCode.filter((t => t.code == el[codeField_index].value));
                                if (zip.length > 0) {
                                    that.currentCode = zip[0].code;
                                    that.currentTown = zip[0].town;
                                    that.currentCity = zip[0].city;

                                    that.filterCityName = that.currentCity;
                                } else {
                                    that.currentCode = that.currentTown = that.currentCity = that.filterCityName = '';
                                }

                                if (codeField_index >= 2) {
                                    let fullname = el[cityField_index].name;
                                    let sub_arr = fullname.split('_');
                                    let sub_index = sub_arr[0];
                                    let sub_name = sub_arr[1];
                                    that.currentZipCodeDataList.City = that.cardData[sub_index][sub_name];
                                } else {
                                    that.currentZipCodeDataList.Code = null;
                                }

                                if (codeField_index >= 1) {
                                    let fullname = el[townField_index].name;
                                    let sub_arr = fullname.split('_');
                                    let sub_index = sub_arr[0];
                                    let sub_name = sub_arr[1];
                                    that.currentZipCodeDataList.Town = that.cardData[sub_index][sub_name];
                                } else {
                                    that.currentZipCodeDataList.Town = null;
                                }

                                if (codeField_index >= 0) {
                                    let fullname = el[codeField_index].name;
                                    let sub_arr = fullname.split('_');
                                    let sub_index = sub_arr[0];
                                    let sub_name = sub_arr[1];
                                    that.currentZipCodeDataList.Code = that.cardData[sub_index][sub_name];
                                } else {
                                    that.currentZipCodeDataList.Code = null;
                                }

                                $("#zip-modal").modal('show');

                                return false;
                            });
                            //縣市鄉鎮代號
                            $(".table-scroll input[type=text].zipcode2").click(function (x) {

                                //取得所在位置的所有input欄位
                                var el = $(this).parent().find("input[type=text]").toArray();
                                // console.log(el);
                                //縣市鄉鎮代號在所在位置的所有input欄位中的索引
                                let codeField_index = el.indexOf(this);
                                //鄉鎮市區名稱欄位在所在位置的所有input欄位中的索引
                                let townField_index = codeField_index + 1;
                                //縣市名稱欄位在所在位置的所有input欄位中的索引
                                let cityField_index = codeField_index + 2;

                                let zip = that.zipCode.filter((t => t.code == el[codeField_index].value));
                                if (zip.length > 0) {
                                    that.currentCode = zip[0].code;
                                    that.currentTown = zip[0].town;
                                    that.currentCity = zip[0].city;

                                    that.filterCityName = that.currentCity;
                                } else {
                                    that.currentCode = that.currentTown = that.currentCity = that.filterCityName = '';
                                }

                                //if (codeField_index >= 2) {
                                //    let fullname = el[cityField_index].name;
                                //    let sub_arr = fullname.split('_');
                                //    let sub_index = sub_arr[0];
                                //    let sub_name = sub_arr[1];
                                //    that.currentZipCodeDataList.City = that.cardData[sub_index][sub_name];
                                //} else {
                                //    that.currentZipCodeDataList.Code = null;
                                //}

                                //if (codeField_index >= 1) {
                                //    let fullname = el[townField_index].name;
                                //    let sub_arr = fullname.split('_');
                                //    let sub_index = sub_arr[0];
                                //    let sub_name = sub_arr[1];
                                //    that.currentZipCodeDataList.Town = that.cardData[sub_index][sub_name];
                                //} else {
                                //    that.currentZipCodeDataList.Town = null;
                                //}

                                if (codeField_index == 0) {
                                    let fullname = el[codeField_index].name;
                                    let sub_arr = fullname.split('_');
                                    let sub_index = sub_arr[0];
                                    let sub_name = sub_arr[1];
                                    that.currentZipCodeDataList.City = that.cardData[sub_index][sub_name];
                                } else {
                                    that.currentZipCodeDataList.City = null;
                                }
                                if (codeField_index == 0) {

                                    let fullname = el[townField_index].name;
                                    //console.log(fullname);
                                    let sub_arr = fullname.split('_');
                                    let sub_index = sub_arr[0];
                                    let sub_name = sub_arr[1];
                                    that.currentZipCodeDataList.Town = that.cardData[sub_index][sub_name];
                                } else {
                                    that.currentZipCodeDataList.Town = null;
                                }
                                $("#zip-modal").modal('show');

                                return false;
                            });

                            //$(".table-scroll input[type=text].CropCode").click(function () {
                            //    //取得所在位置的所有input欄位
                            //    var el = $(this).parent().find("input[type=text]").toArray();

                            //    //作物代號在所在位置的所有input欄位中的索引
                            //    let codeField_index = el.indexOf(this);
                            //    //作物名稱欄位在所在位置的所有input欄位中的索引
                            //    let cropField_index = codeField_index - 1;


                            //    let CROP = that.cropCode.filter((t => t.Code == el[codeField_index].value));
                            //    if (CROP.length > 0) {
                            //        that.currentCropCode = CROP[0].code;
                            //        that.currentCrop = CROP[0].town;
                            //    } else {
                            //        that.currentCropCode = that.currentCrop = '';
                            //    }


                            //    if (codeField_index >= 1) {
                            //        let fullname = el[cropField_index].name;
                            //        let sub_arr = fullname.split('_');
                            //        let sub_index = sub_arr[0];
                            //        let sub_name = sub_arr[1];
                            //        that.currentCropCodeDataList.Crop = that.cardData[sub_index][sub_name];
                            //    } else {
                            //        that.currentCropCodeDataList.Crop = null;
                            //    }

                            //    if (codeField_index >= 0) {
                            //        let fullname = el[codeField_index].name;
                            //        let sub_arr = fullname.split('_');
                            //        let sub_index = sub_arr[0];
                            //        let sub_name = sub_arr[1];
                            //        that.currentCropCodeDataList.Code = that.cardData[sub_index][sub_name];
                            //    } else {
                            //        that.currentCropCodeDataList.Code = null;
                            //    }

                            //    $("#crop-modal").modal('show');

                            //    return false;
                            //});

                            //$(".table-scroll input[type=text].PoultryCode").click(function () {
                            //    //取得所在位置的所有input欄位
                            //    var el = $(this).parent().find("input[type=text]").toArray();

                            //    //禽畜代號在所在位置的所有input欄位中的索引
                            //    let codeField_index = el.indexOf(this);
                            //    //禽畜市區名稱欄位在所在位置的所有input欄位中的索引
                            //    let cropField_index = codeField_index - 1;


                            //    let POULTRY = that.poultryCode.filter((t => t.Code == el[codeField_index].value));
                            //    if (POULTRY.length > 0) {
                            //        that.currentPoultryCode = POULTRY[0].code;
                            //        that.currentCrop = POULTRY[0].town;
                            //    } else {
                            //        that.currentPoultryCode = that.currentPoultry = '';
                            //    }


                            //    if (codeField_index >= 1) {
                            //        let fullname = el[cropField_index].name;
                            //        let sub_arr = fullname.split('_');
                            //        let sub_index = sub_arr[0];
                            //        let sub_name = sub_arr[1];
                            //        that.currentPoultryCodeDataList.Poultry = that.cardData[sub_index][sub_name];
                            //    } else {
                            //        that.currentPoultryCodeDataList.Poultry = null;
                            //    }

                            //    if (codeField_index >= 0) {
                            //        let fullname = el[codeField_index].name;
                            //        let sub_arr = fullname.split('_');
                            //        let sub_index = sub_arr[0];
                            //        let sub_name = sub_arr[1];
                            //        that.currentPoultryCodeDataList.Code = that.cardData[sub_index][sub_name];
                            //    } else {
                            //        that.currentPoultryCodeDataList.Code = null;
                            //    }

                            //    $("#poultry-modal").modal('show');

                            //    return false;
                            //});
                            $(".table-scroll input[type=text].currentCode").click(function () {

                                //取得所在位置的所有input欄位
                                var el = $(this).parent().find("input[type=text]").toArray();
                                that.filterCodeName = '';
                                //代號在所在位置的所有input欄位中的索引
                                let codeField_index = el.indexOf(this);
                                var x = that.classcode;
                                var classat = '';
                                let code = '';
                                for (var i = 0; i < x.length; i++) {
                                    if ($(this).hasClass(x[i])) { classat = x[i]; that.classcode2 = x[i]; }
                                }
                                if (that.tableAll.find(item => item[classat]) != undefined) {
                                    that.tableAll.forEach(function (item) {

                                        code = item[classat];

                                    });


                                }


                                switch (classat) {
                                    case "countycode":
                                        code = that.countyCode;
                                        break;
                                    case "cropcode":
                                        code = that.cropCode;
                                        break;
                                    case "poultrycode":
                                        code = that.poultryCode;
                                        break;
                                    case "poultryservicecode":
                                        code = that.poultryserviceCode;
                                        break;
                                    case "fish_3_2":
                                        code = that.fish_3_2Code;
                                        break;
                                    case "fish_3_4":
                                        code = that.fish_3_4Code;
                                        break;
                                    case "fish_5_3":
                                        code = that.fish_5_3Code;
                                        break;
                                    case "fish_5_4":
                                        code = that.fish_5_4Code;
                                        break;
                                    case "fish_5_5":
                                        code = that.fish_5_5Code;
                                        break;
                                    case "fish_5_6":
                                        code = that.fish_5_6Code;
                                        break;
                                    case "fish_5_8":
                                        code = that.fish_5_8Code;
                                        break;
                                    case "fish_14_4":
                                        code = that.fish_14_4Code;
                                        break;
                                    case "fish_14_5":
                                        code = that.fish_14_5Code;
                                        break;
                                    case "fish_14_6":
                                        code = that.fish_14_6Code;
                                        break;
                                    case "fish_14_7":
                                        code = that.fish_14_7Code;
                                        break;
                                    case "farm_3_2":
                                        code = that.farm_3_2Code;
                                        break;
                                    case "farm_3_5":
                                        code = that.farm_3_5Code;
                                        break;
                                    case "farm_3_6":
                                        code = that.farm_3_5Code;
                                        break;
                                    case "farm_3_7":
                                        code = that.farm_3_7Code;
                                        break;
                                    case "farm_4_3":
                                        code = that.farm_4_3Code;
                                        break;
                                    case "farm_4_5":
                                        code = that.farm_4_5Code;
                                        break;
                                    case "farm_4_6":
                                        code = that.farm_4_5Code;
                                        break;
                                    case "farm_12_5":
                                        code = that.farm_12_5Code;
                                        break;
                                    case "farm_12_6":
                                        code = that.farm_12_6Code;
                                        break;
                                    case "farm_12_7":
                                        code = that.farm_12_7Code;
                                        break;
                                    case "farm_12_8":
                                        code = that.farm_12_8Code;
                                        break;
                                    default:
                                        break;

                                }



                                if (code.length > 0) {

                                    that.currentcurrentCode = code[0].Code;
                                    that.currentcurrentName = code[0].Name;

                                } else {
                                    that.currentcurrentCodeDataList = that.currentcurrentName = '';
                                }


                                if (codeField_index >= 1) {
                                    let fullname = el[cropField_index].name;
                                    let sub_arr = fullname.split('_');
                                    let sub_index = sub_arr[0];
                                    let sub_name = sub_arr[1];
                                    that.currentcurrentCodeDataList.Name = that.cardData[sub_index][sub_name];

                                } else {
                                    that.currentcurrentCodeDataList.Name = null;
                                }

                                if (codeField_index >= 0) {
                                    let fullname = el[codeField_index].name;
                                    let sub_arr = fullname.split('_');
                                    let sub_index = sub_arr[0];
                                    let sub_name = sub_arr[1];
                                    that.currentcurrentCodeDataList.Code = that.cardData[sub_index][sub_name];

                                } else {
                                    that.currentcurrentCodeDataList.Code = null;
                                }
                                $("#zip2-modal").modal('show');

                                return false;
                            });
                            //$("#zip-modal").on('hidden.bs.modal', function () {
                            //    return false;
                            //});

                            this.needRander = false;
                        };
                    });

                    // 初始化完頁面Dom 遮罩欄位全disable
                    maskAllCoumn();

                },
                updated: function () {
                    let that = this;
                    //this.toggleTab();

                    // 完成頁面更新 遮罩欄位全disable
                    maskAllCoumn();
             
                    // 2020/08/20 修改架構，此部分已移至mounted處理
                    ////等到全部render完，再填入全部的調查表
                    //this.$nextTick(function () {

                    //    if (this.firstRander) {

                    //        //this.LayoutInit();
                    //        // 新增mode (不用鎖頭效果，並解開全部唯讀)
                    //        if (that.dataErrorListId == -1) {
                    //            $(".table-scroll input[disabled=disabled]").removeAttr("disabled");
                    //            $(".table-scroll select[disabled=disabled]").removeAttr("disabled");
                    //        } else {
                    //            // 更正mode 要加鎖頭效果
                    //            $(".lockGroupTR").append("<td  border=\"0\" style=\" margin:0px; border:none; background: transparent;position:fixed; bottom:1%; right:10px;\" class=\"fa fa-lock unlockBtn2\" aria-hidden=\"true\" title=\"解鎖\" onclick=\"unlock(this)\"></td>");
                    //            $(".lockGroup").append("<i class=\"fa fa-lock unlockBtn\" aria-hidden=\"true\" title=\"解鎖\" onclick=\"unlock(this)\"></i>");
                    //        }

                    //        $('#BackTop').click(function () {
                    //            $('html,body').animate({ scrollTop: 0 }, 333);
                    //        });

                    //        $(window).scroll(function () {
                    //            if ($(this).scrollTop() > 300) {
                    //                $('#BackTop').fadeIn(222);
                    //            } else {
                    //                $('#BackTop').stop().fadeOut(222);
                    //            }
                    //        }).scroll();

                    //        this.firstRander = false;//第一次更新完
                    //    };

                    //    if (this.needRander) {
                    //        $(".table-scroll input[type=radio]").each(function () {
                    //            $(this).prop("title", `${$(this).prop("name")} (${$(this).data("value")})`);
                    //        });
                    //        $(".table-scroll input[type=checkbox]").each(function () {
                    //            $(this).prop("title", `${$(this).prop("name")} (${$(this).data("value")})`);
                    //        });
                    //        $(".table-scroll input[type=text]").each(function () {
                    //            $(this).prop("title", `${$(this).prop("name")}`);
                    //        });
                    //        $(".table-scroll textarea").each(function () {
                    //            $(this).prop("title", `${$(this).prop("name")}`);
                    //        });
                    //        $(".table-scroll select").each(function () {
                    //            $(this).prop("title", `${$(this).prop("name")} (${$(this).data("value")})`);
                    //        });

                    //        //右鍵清除欄位值
                    //        $(".table-scroll input").contextmenu(function () {
                    //            var name = $(this).prop("name");
                    //            var name_arr = $(this).prop("name").split('_');
                    //            var dataIndex = name_arr[0];
                    //            var col_name = name_arr[1];
                    //            var type = $(this).prop("type");
                    //            swal({
                    //                text: `$清除 ${col_name} 的資料?`,
                    //                buttons: ['取消', '確認'],
                    //            }).then(value => {
                    //                if (value) {
                    //                    that.ClearFormValue(0, this);
                    //                    //that.cardData[dataIndex][col_name].FormValue = null;
                    //                    //if (col_name == 'D01103') {
                    //                    //    that.bathA = null;
                    //                    //    that.bathB = null;
                    //                    //}

                    //                    //var fels = $(".table-scroll").find(`[data-follow=${name}]`);
                    //                    ////$(fels).hide();

                    //                    //$(fels).each(that.ClearFormValue);
                    //                } else {
                    //                    return;
                    //                }
                    //            })
                    //            return false;
                    //        });
                    //        $(".table-scroll select").contextmenu(function () {
                    //            var name = $(this).prop("name");
                    //            var name_arr = $(this).prop("name").split('_');
                    //            var dataIndex = name_arr[0];
                    //            var col_name = name_arr[1];
                    //            var type = $(this).prop("type").split('-')[0];
                    //            swal({
                    //                text: `$清除 ${col_name} 的資料?`,
                    //                buttons: ['取消', '確認'],
                    //            }).then(value => {
                    //                if (value) {
                    //                    that.ClearFormValue(0, this);
                    //                    //that.cardData[dataIndex][col_name].FormValue = null;

                    //                    //let fels = $(".table-scroll").find(`[data-follow=${name}]`);
                    //                    ////$(fels).hide();

                    //                    //$(fels).each(that.ClearFormValue);
                    //                } else {
                    //                    return;
                    //                }
                    //            })
                    //            return false;
                    //        });

                    //        //縣市鄉鎮代號
                    //        $(".table-scroll input[type=text].zipcode").click(function (x) {

                    //            //取得所在位置的所有input欄位
                    //            var el = $(this).parent().find("input[type=text]").toArray();

                    //            //縣市鄉鎮代號在所在位置的所有input欄位中的索引
                    //            let codeField_index = el.indexOf(this);
                    //            //鄉鎮市區名稱欄位在所在位置的所有input欄位中的索引
                    //            let townField_index = codeField_index - 1;
                    //            //縣市名稱欄位在所在位置的所有input欄位中的索引
                    //            let cityField_index = codeField_index - 2;

                    //            let zip = that.zipCode.filter((t => t.code == el[codeField_index].value));
                    //            if (zip.length > 0) {
                    //                that.currentCode = zip[0].code;
                    //                that.currentTown = zip[0].town;
                    //                that.currentCity = zip[0].city;

                    //                that.filterCityName = that.currentCity;
                    //            } else {
                    //                that.currentCode = that.currentTown = that.currentCity = that.filterCityName = '';
                    //            }

                    //            if (codeField_index >= 2) {
                    //                let fullname = el[cityField_index].name;
                    //                let sub_arr = fullname.split('_');
                    //                let sub_index = sub_arr[0];
                    //                let sub_name = sub_arr[1];
                    //                that.currentZipCodeDataList.City = that.cardData[sub_index][sub_name];
                    //            } else {
                    //                that.currentZipCodeDataList.Code = null;
                    //            }

                    //            if (codeField_index >= 1) {
                    //                let fullname = el[townField_index].name;
                    //                let sub_arr = fullname.split('_');
                    //                let sub_index = sub_arr[0];
                    //                let sub_name = sub_arr[1];
                    //                that.currentZipCodeDataList.Town = that.cardData[sub_index][sub_name];
                    //            } else {
                    //                that.currentZipCodeDataList.Town = null;
                    //            }

                    //            if (codeField_index >= 0) {
                    //                let fullname = el[codeField_index].name;
                    //                let sub_arr = fullname.split('_');
                    //                let sub_index = sub_arr[0];
                    //                let sub_name = sub_arr[1];
                    //                that.currentZipCodeDataList.Code = that.cardData[sub_index][sub_name];
                    //            } else {
                    //                that.currentZipCodeDataList.Code = null;
                    //            }

                    //            $("#zip-modal").modal('show');

                    //            return false;
                    //        });
                    //        //縣市鄉鎮代號
                    //        $(".table-scroll input[type=text].zipcode2").click(function (x) {

                    //            //取得所在位置的所有input欄位
                    //            var el = $(this).parent().find("input[type=text]").toArray();
                    //            console.log(el);
                    //            //縣市鄉鎮代號在所在位置的所有input欄位中的索引
                    //            let codeField_index = el.indexOf(this);
                    //            //鄉鎮市區名稱欄位在所在位置的所有input欄位中的索引
                    //            let townField_index = codeField_index + 1;
                    //            //縣市名稱欄位在所在位置的所有input欄位中的索引
                    //            let cityField_index = codeField_index + 2;

                    //            let zip = that.zipCode.filter((t => t.code == el[codeField_index].value));
                    //            if (zip.length > 0) {
                    //                that.currentCode = zip[0].code;
                    //                that.currentTown = zip[0].town;
                    //                that.currentCity = zip[0].city;

                    //                that.filterCityName = that.currentCity;
                    //            } else {
                    //                that.currentCode = that.currentTown = that.currentCity = that.filterCityName = '';
                    //            }

                    //            //if (codeField_index >= 2) {
                    //            //    let fullname = el[cityField_index].name;
                    //            //    let sub_arr = fullname.split('_');
                    //            //    let sub_index = sub_arr[0];
                    //            //    let sub_name = sub_arr[1];
                    //            //    that.currentZipCodeDataList.City = that.cardData[sub_index][sub_name];
                    //            //} else {
                    //            //    that.currentZipCodeDataList.Code = null;
                    //            //}

                    //            //if (codeField_index >= 1) {
                    //            //    let fullname = el[townField_index].name;
                    //            //    let sub_arr = fullname.split('_');
                    //            //    let sub_index = sub_arr[0];
                    //            //    let sub_name = sub_arr[1];
                    //            //    that.currentZipCodeDataList.Town = that.cardData[sub_index][sub_name];
                    //            //} else {
                    //            //    that.currentZipCodeDataList.Town = null;
                    //            //}

                    //            if (codeField_index == 0) {
                    //                let fullname = el[codeField_index].name;
                    //                let sub_arr = fullname.split('_');
                    //                let sub_index = sub_arr[0];
                    //                let sub_name = sub_arr[1];
                    //                that.currentZipCodeDataList.City = that.cardData[sub_index][sub_name];
                    //            } else {
                    //                that.currentZipCodeDataList.City = null;
                    //            }
                    //            if (codeField_index == 0) {

                    //                let fullname = el[townField_index].name;
                    //                console.log(fullname);
                    //                let sub_arr = fullname.split('_');
                    //                let sub_index = sub_arr[0];
                    //                let sub_name = sub_arr[1];
                    //                that.currentZipCodeDataList.Town = that.cardData[sub_index][sub_name];
                    //            } else {
                    //                that.currentZipCodeDataList.Town = null;
                    //            }
                    //            $("#zip-modal").modal('show');

                    //            return false;
                    //        });

                    //        //$(".table-scroll input[type=text].CropCode").click(function () {
                    //        //    //取得所在位置的所有input欄位
                    //        //    var el = $(this).parent().find("input[type=text]").toArray();

                    //        //    //作物代號在所在位置的所有input欄位中的索引
                    //        //    let codeField_index = el.indexOf(this);
                    //        //    //作物名稱欄位在所在位置的所有input欄位中的索引
                    //        //    let cropField_index = codeField_index - 1;


                    //        //    let CROP = that.cropCode.filter((t => t.Code == el[codeField_index].value));
                    //        //    if (CROP.length > 0) {
                    //        //        that.currentCropCode = CROP[0].code;
                    //        //        that.currentCrop = CROP[0].town;
                    //        //    } else {
                    //        //        that.currentCropCode = that.currentCrop = '';
                    //        //    }


                    //        //    if (codeField_index >= 1) {
                    //        //        let fullname = el[cropField_index].name;
                    //        //        let sub_arr = fullname.split('_');
                    //        //        let sub_index = sub_arr[0];
                    //        //        let sub_name = sub_arr[1];
                    //        //        that.currentCropCodeDataList.Crop = that.cardData[sub_index][sub_name];
                    //        //    } else {
                    //        //        that.currentCropCodeDataList.Crop = null;
                    //        //    }

                    //        //    if (codeField_index >= 0) {
                    //        //        let fullname = el[codeField_index].name;
                    //        //        let sub_arr = fullname.split('_');
                    //        //        let sub_index = sub_arr[0];
                    //        //        let sub_name = sub_arr[1];
                    //        //        that.currentCropCodeDataList.Code = that.cardData[sub_index][sub_name];
                    //        //    } else {
                    //        //        that.currentCropCodeDataList.Code = null;
                    //        //    }

                    //        //    $("#crop-modal").modal('show');

                    //        //    return false;
                    //        //});

                    //        //$(".table-scroll input[type=text].PoultryCode").click(function () {
                    //        //    //取得所在位置的所有input欄位
                    //        //    var el = $(this).parent().find("input[type=text]").toArray();

                    //        //    //禽畜代號在所在位置的所有input欄位中的索引
                    //        //    let codeField_index = el.indexOf(this);
                    //        //    //禽畜市區名稱欄位在所在位置的所有input欄位中的索引
                    //        //    let cropField_index = codeField_index - 1;


                    //        //    let POULTRY = that.poultryCode.filter((t => t.Code == el[codeField_index].value));
                    //        //    if (POULTRY.length > 0) {
                    //        //        that.currentPoultryCode = POULTRY[0].code;
                    //        //        that.currentCrop = POULTRY[0].town;
                    //        //    } else {
                    //        //        that.currentPoultryCode = that.currentPoultry = '';
                    //        //    }


                    //        //    if (codeField_index >= 1) {
                    //        //        let fullname = el[cropField_index].name;
                    //        //        let sub_arr = fullname.split('_');
                    //        //        let sub_index = sub_arr[0];
                    //        //        let sub_name = sub_arr[1];
                    //        //        that.currentPoultryCodeDataList.Poultry = that.cardData[sub_index][sub_name];
                    //        //    } else {
                    //        //        that.currentPoultryCodeDataList.Poultry = null;
                    //        //    }

                    //        //    if (codeField_index >= 0) {
                    //        //        let fullname = el[codeField_index].name;
                    //        //        let sub_arr = fullname.split('_');
                    //        //        let sub_index = sub_arr[0];
                    //        //        let sub_name = sub_arr[1];
                    //        //        that.currentPoultryCodeDataList.Code = that.cardData[sub_index][sub_name];
                    //        //    } else {
                    //        //        that.currentPoultryCodeDataList.Code = null;
                    //        //    }

                    //        //    $("#poultry-modal").modal('show');

                    //        //    return false;
                    //        //});
                    //        $(".table-scroll input[type=text].currentCode").click(function () {

                    //            //取得所在位置的所有input欄位
                    //            var el = $(this).parent().find("input[type=text]").toArray();
                    //            that.filterCodeName = '';
                    //            //代號在所在位置的所有input欄位中的索引
                    //            let codeField_index = el.indexOf(this);
                    //            var x = that.classcode;
                    //            var classat = '';
                    //            let code = '';
                    //            for (var i = 0; i < x.length; i++) {
                    //                if ($(this).hasClass(x[i])) { classat = x[i]; that.classcode2 = x[i]; }
                    //            }
                    //            if (that.tableAll.find(item => item[classat]) != undefined) {
                    //                that.tableAll.forEach(function (item) {

                    //                    code = item[classat];

                    //                });


                    //            }


                    //            switch (classat) {
                    //                case "countycode":
                    //                    code = that.countyCode;
                    //                    break;
                    //                case "cropcode":
                    //                    code = that.cropCode;
                    //                    break;
                    //                case "poultrycode":
                    //                    code = that.poultryCode;
                    //                    break;
                    //                case "poultryservicecode":
                    //                    code = that.poultryserviceCode;
                    //                    break;
                    //                case "fish_3_2":
                    //                    code = that.fish_3_2Code;
                    //                    break;
                    //                case "fish_3_4":
                    //                    code = that.fish_3_4Code;
                    //                    break;
                    //                case "fish_5_3":
                    //                    code = that.fish_5_3Code;
                    //                    break;
                    //                case "fish_5_4":
                    //                    code = that.fish_5_4Code;
                    //                    break;
                    //                case "fish_5_5":
                    //                    code = that.fish_5_5Code;
                    //                    break;
                    //                case "fish_5_6":
                    //                    code = that.fish_5_6Code;
                    //                    break;
                    //                case "fish_5_8":
                    //                    code = that.fish_5_8Code;
                    //                    break;
                    //                case "fish_14_4":
                    //                    code = that.fish_14_4Code;
                    //                    break;
                    //                case "fish_14_5":
                    //                    code = that.fish_14_5Code;
                    //                    break;
                    //                case "fish_14_6":
                    //                    code = that.fish_14_6Code;
                    //                    break;
                    //                case "fish_14_7":
                    //                    code = that.fish_14_7Code;
                    //                    break;
                    //                case "farm_3_2":
                    //                    code = that.farm_3_2Code;
                    //                    break;
                    //                case "farm_3_5":
                    //                    code = that.farm_3_5Code;
                    //                    break;
                    //                case "farm_3_6":
                    //                    code = that.farm_3_5Code;
                    //                    break;
                    //                case "farm_3_7":
                    //                    code = that.farm_3_7Code;
                    //                    break;
                    //                case "farm_4_3":
                    //                    code = that.farm_4_3Code;
                    //                    break;
                    //                case "farm_4_5":
                    //                    code = that.farm_4_5Code;
                    //                    break;
                    //                case "farm_4_6":
                    //                    code = that.farm_4_5Code;
                    //                    break;
                    //                case "farm_12_5":
                    //                    code = that.farm_12_5Code;
                    //                    break;
                    //                case "farm_12_6":
                    //                    code = that.farm_12_6Code;
                    //                    break;
                    //                case "farm_12_7":
                    //                    code = that.farm_12_7Code;
                    //                    break;
                    //                case "farm_12_8":
                    //                    code = that.farm_12_8Code;
                    //                    break;
                    //                default:
                    //                    break;

                    //            }



                    //            if (code.length > 0) {

                    //                that.currentcurrentCode = code[0].Code;
                    //                that.currentcurrentName = code[0].Name;

                    //            } else {
                    //                that.currentcurrentCodeDataList = that.currentcurrentName = '';
                    //            }


                    //            if (codeField_index >= 1) {
                    //                let fullname = el[cropField_index].name;
                    //                let sub_arr = fullname.split('_');
                    //                let sub_index = sub_arr[0];
                    //                let sub_name = sub_arr[1];
                    //                that.currentcurrentCodeDataList.Name = that.cardData[sub_index][sub_name];

                    //            } else {
                    //                that.currentcurrentCodeDataList.Name = null;
                    //            }

                    //            if (codeField_index >= 0) {
                    //                let fullname = el[codeField_index].name;
                    //                let sub_arr = fullname.split('_');
                    //                let sub_index = sub_arr[0];
                    //                let sub_name = sub_arr[1];
                    //                that.currentcurrentCodeDataList.Code = that.cardData[sub_index][sub_name];

                    //            } else {
                    //                that.currentcurrentCodeDataList.Code = null;
                    //            }
                    //            $("#zip2-modal").modal('show');

                    //            return false;
                    //        });
                    //        //$("#zip-modal").on('hidden.bs.modal', function () {
                    //        //    return false;
                    //        //});

                    //        this.needRander = false;
                    //    };
                    //})
                },
            });


            $.busyLoadFull("hide");
            /*執行Vue.js程式碼---結束*/
        },
        error: function (jqXHR, textStatus, errorThrown) {
            $.busyLoadFull("hide");
            if (jqXHR.status !== 401) {
                swal(jqXHR.responseText);
            }
        }
    });



});
var vm = new Vue({
    el: '#app2',
    data: {
        ProjectName: "",
        MissionName: ""
    },
    mounted() {
        this.ProjectName = window.ProjectName;
        this.MissionName = window.MissionName;
        var dataErrorListId = window.dataErrorListId; // 新增mode:-1  更正mode:資料id
        var x = document.getElementsByTagName("li");
        for (var i = 0; i < x.length; i++) {
            var res = x[i].innerHTML.replace("XXX專案名稱XXX", this.ProjectName)
                .replace("XXX任務名稱XXX", this.MissionName);
            if (dataErrorListId == -1) {
                res = res.replace("調查表更正", "調查表新增");
            }
            x[i].innerHTML = res;
        }
    },
})

// 區塊 解鎖/上鎖 功能
function unlock(e) {
    var isLock = $(e).hasClass("fa-lock");
    if (isLock) {
        var el = $(e).parent().find("*");
        $(el).prop('disabled', false);

        $(e).removeClass("fa-lock").addClass("fa-unlock");
        //此區欄位編輯中，點擊關閉編輯
        $(e).prop("title", "關閉編輯");
    } else {
        var el = $(e).parent().find("*[haserror=-1]");
        $(el).prop('disabled', true);

        $(e).removeClass("fa-unlock").addClass("fa-lock");
        //目前欄位不可編輯，請點擊解鎖
        $(e).prop("title", "解鎖");
    }

    //$(e).remove();

    // 若當前User 無檢視隱碼遮罩欄位 權限，一律將之上鎖
    if (canUnMask_js === false) { 
        // 判斷解鎖欄位，有無包含 隱碼欄位
        $(e).parent().find("input").each(function (n) {
            var split = this.name.split("_");	// 將欄名切割 0_E01000
            if (MaskColumnList_js.includes(split[1].toUpperCase())) {
                $(this).prop('disabled', true);
            }
        });
    }

}
// 遮罩欄位全disable
function maskAllCoumn() {
    // 若當前User 無檢視隱碼遮罩欄位 權限，一律將之上鎖
    if (canUnMask_js === false && MaskColumnList_js.length > 0) {
        // 將隱碼欄位 全部上鎖
        MaskColumnList_js.forEach(function (value) {
            $("input[name*='" + value + "']").prop('disabled', true);

        });
    }
}




window.onbeforeunload = function (event) {
    if (saveOrNotSave == 0) {
        //event.preventDefault(); //chrome無效, ff有效, ie11有效
        event.returnValue = '系統可能不會儲存您所做的變更。'; //chrome無效, ff無效, ie11有效
    } else {
        saveOrNotSave = 0;
    }
    //return ''; //chrome有效, ff有效, ie11有效
};
window.onunload = function () {
    window.opener.winson = null;
    window.opener.$.busyLoadFull("hide");
}
