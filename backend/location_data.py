# backend/location_data.py

STATE_CITY_MAP = {

    "Andhra Pradesh": [
        "Andamukonda", "Addanki", "Amalapuram", "Amaravati", "Anantapur", "Atmakur", "Badvel",
        "Bapatla", "Bhimavaram", "Chilakaluripet", "Chittoor", "Dharmavaram", "Eluru",
        "Gooty", "Guntur", "Guntakal", "Hindupur", "Ichchapuram", "Jammalamadugu",
        "Kakinada", "Kadapa", "Kadiri", "Kanigiri", "Kandukur", "Kavali", "Kurnool",
        "Madanapalle", "Mangalagiri", "Mandapeta", "Markapur", "Mydukur", "Nadendla",
        "Naidupeta", "Narsaraopet", "Narsipatnam", "Nellore", "Nandyal", "Ongole",
        "Palakollu", "Palasa", "Penukonda", "Pileru", "Ponnur", "Proddatur", "Pulivendula",
        "Puttaparthi", "Rajahmundry", "Ramachandrapuram", "Rayachoti", "Repalle",
        "Sattenapalle", "Salur", "Samalkot", "Srikakulam", "Sullurpeta", "Tanuku",
        "Tadepalligudem", "Tadipatri", "Tenali", "Tirupati", "Venkatagiri", "Vijayawada",
        "Vizianagaram", "Visakhapatnam", "Yemmiganur", "Yerraguntla"

    ],
  
    "Arunachal Pradesh": [
        "Along", "Aalo", "Bomdila", "Changlang", "Daporijo", "Itanagar", "Jairampur",
        "Khonsa", "Koloriang", "Longding", "Naharlagun", "Namsai", "Pasighat",
        "Roing", "Seppa", "Tezu", "Tawang", "Ziro"

    ],

    "Assam": [
        "Abhayapuri", "Barpeta", "Bongaigaon", "Cachar", "Dhubri", "Dibrugarh", "Diphu",
        "Golaghat", "Goalpara", "Guwahati", "Hojai", "Jorhat", "Kamrup", "Karimganj",
        "Kokrajhar", "Lakhimpur", "Morigaon", "Nagaon", "Silchar", "Sivasagar", "Tezpur",
        "Tinsukia", "Titabar", "Udalguri"


    ],

    "Bihar": [
        "Arrah", "Araria", "Aurangabad", "Baheri", "Bakhtiyarpur", "Barauli", "Barh",
        "Bagaha", "Bhabua", "Begusarai", "Bettiah", "Belaganj", "Benipur", "Bhagalpur",
        "Bihar Sharif", "Buxar", "Chapra", "Chhapra", "Dalsinghsarai", "Danapur",
        "Darbhanga", "Dumraon", "Fatuha", "Forbesganj", "Gopalganj", "Gaya", "Hajipur",
        "Hayaghat", "Hilsa", "Islampur", "Jale", "Jamalpur", "Jehanabad", "Katihar",
        "Khagaria", "Kishanganj", "Lakhisarai", "Madhepura", "Madhubani", "Maharajganj",
        "Maner", "Masaurhi", "Mirganj", "Mohania", "Motihari", "Muzaffarpur", "Nawada",
        "Nalanda", "Narkatiaganj", "Patna", "Phulwari Sharif", "Purnia", "Rajgir",
        "Ramgarh", "Raxaul", "Revelganj", "Rosera", "Saharsa", "Samastipur", "Sheikhpura",
        "Silao", "Singhwara", "Sitamarhi", "Siwan", "Sugauli", "Supaul", "Tekari",
        "Teghra", "Warisliganj", "Wazirganj"

    ],

    "Chhattisgarh": [
        "Ambikapur", "Bhilai", "Bilaspur", "Dhamtari", "Durg", "Jagdalpur", "Korba",
        "Mahasamund", "Raigarh", "Raipur", "Rajnandgaon", "Surajpur", "Tilda", "Bemetara",
        "Balod", "Baloda Bazar", "Balrampur", "Bastar", "Kanker", "Kabirdham", "Gariaband",
        "Jashpur", "Mungeli", "Narayanpur", "Sukma", "Sarguja", "Dantewada"

    ],

    "Goa": [
        "Bicholim", "Curchorem", "Mapusa", "Margao", 
        "Panaji", "Ponda", "Sanquelim", "Vasco da Gama"
    ],

    "Gujarat": [
        "Ahmedabad", "Amreli", "Anand", "Anjar", "Anklav", "Balasinor", "Bardoli", "Bharuch",
        "Bhavnagar", "Bhuj", "Bilimora", "Borsad", "Botad", "Chikhli", "Dahod", "Deesa",
        "Dholka", "Dwarka", "Gandhidham", "Gandhinagar", "Gandevi", "Godhra", "Gondal",
        "Halol", "Himatnagar", "Idar", "Jamnagar", "Jasdan", "Jetpur", "Junagadh", "Kadi",
        "Kalol", "Kalol (PMS)", "Kapadvanj", "Khambhalia", "Khambhat", "Limkheda", "Lunawada",
        "Mahuva", "Mandvi", "Mehsana", "Modasa", "Morbi", "Mundra", "Nakhatrana", "Navsari",
        "Palanpur", "Patan", "Pardi", "Petlad", "Porbandar", "Rajkot", "Rajula", "Sanand","Santrampur", 
        "Savarkundla", "Songadh", "Surat", "Surendranagar", "Talaja", "Umbergaon","Upleta", "Unjha", 
        "Vadodara", "Vapi", "Valsad", "Veraval", "Viramgam", "Visnagar", "Vyara"

    ],

    "Haryana": [
        "Ambala", "Bahadurgarh", "Bhiwani", "Ellenabad", "Faridabad", "Fatehabad", "Gohana",
        "Gurugram", "Hansi", "Hisar", "Jind", "Kalanaur", "Kaithal", "Karnal", "Ladwa",
        "Narnaul", "Narwana", "Palwal", "Panipat", "Panchkula", "Pehowa", "Ratia", "Rewari",
        "Rohtak", "Samalkha", "Sirsa", "Sonipat", "Thanesar", "Tohana", "Yamunanagar"

    ],

    "Himachal Pradesh": [
        "Bilaspur", "Chamba", "Dharamshala", "Hamirpur", "Jogindernagar", "Kangra",
        "Kullu", "Manali", "Mandi", "Nahan", "Nalagarh", "Palampur", "Paonta Sahib",
        "Rampur", "Rohru", "Shimla", "Solan", "Sundarnagar", "Theog", "Una"

    ],

    "Jharkhand": [
        "Bokaro", "Chaibasa", "Chirkunda", "Deoghar", "Dhanbad", "Dumka", "Giridih",
        "Godda", "Hazaribagh", "Jamshedpur", "Jhumri Telaiya", "Latehar", "Lohardaga",
        "Medininagar", "Pakur", "Phusro", "Ramgarh", "Ranchi", "Sahebganj"

    ],
    
    "Karnataka": [
        "Afzalpur", "Aland", "Arsikere", "Athani", "Bagalkot", "Ballari", "Basavakalyan",
        "Belagavi", "Bengaluru", "Bhalki", "Bhatkal", "Bidar", "Challakere",
        "Channarayapatna", "Chikkamagaluru", "Chincholi", "Chitradurga", "Davanagere",
        "Gadag", "Gokak", "Gubbi", "Hassan", "Holalkere", "Hosadurga", "Hospet",
        "Hungund", "Hunsur", "Hubballi", "Ilkal", "Jamkhandi", "Kadur", "Kalaburagi",
        "Kanakapura", "Karwar", "Karkala", "Kolar", "Koppal", "Krishnarajanagara",
        "Kundapura", "Lingasugur", "Maddur", "Magadi", "Malavalli", "Mandya",
        "Mangaluru", "Manvi", "Moodbidri", "Mudhol", "Mudigere", "Mysuru",
        "Nanjangud", "Nelamangala", "Puttur", "Rabkavi", "Raichur", "Ramanagara",
        "Savadatti", "Sedam", "Shahabad", "Shivamogga", "Sindhanur", "Sirsi",
        "Srirangapatna", "Sullia", "Tarikere", "Tiptur", "Tumakuru", "Udupi",
        "Vijayapura", "Yadgir"

    ],

    "Kerala": [
        "Adoor", "Alappuzha", "Attingal", "Chavakkad", "Chengannur", "Cherpulassery",
        "Devikulam", "Feroke", "Guruvayur", "Haripad", "Idukki", "Irinjalakuda",
        "Iritty", "Kalpetta", "Kanhangad", "Karunagappally", "Kasaragod",
        "Kayamkulam", "Kilimanoor", "Kochi", "Kodungallur", "Kollam",
        "Kondotty", "Kottarakkara", "Kottayam", "Kozhikode", "Kunnamkulam",
        "Kuthuparamba", "Malappuram", "Mananthavady", "Manjeri", "Mannarkkad",
        "Mavelikkara", "Munnar", "Nedumangad", "Nilambur", "Ottapalam",
        "Palakkad", "Pandalam", "Paravur", "Pathanamthitta", "Payyannur",
        "Perinthalmanna", "Ponnani", "Punalur", "Quilandy", "Ramanattukara",
        "Shoranur", "Sulthan Bathery", "Taliparamba", "Tanur", "Thalassery",
        "Thiruvananthapuram", "Thrissur", "Tirur", "Vadakara", "Valanchery",
        "Varkala", "Wayanad"

    ],

    "Madhya Pradesh": [
        "Agar Malwa", "Anuppur", "Ashoknagar", "Balaghat", "Barwani", "Betul", "Bhind",
        "Bhopal", "Bina", "Burhanpur", "Chhatarpur", "Chhindwara", "Churhat", "Damoh",
        "Datia", "Dewas", "Dindori", "Gadarwara", "Guna", "Gwalior", "Hoshangabad",
        "Indore", "Itarsi", "Jabalpur", "Jabalpur Cantonment", "Jaithari", "Katangi",
        "Katni", "Khandwa", "Khargone", "Khurai", "Kotma", "Lakhnadon", "Lateri",
        "Maihar", "Mandla", "Mandsaur", "Morena", "Multai", "Nagod", "Narsinghpur",
        "Neemuch", "Niwari", "Pali", "Pandhurna", "Panna", "Pipariya", "Rahatgarh",
        "Rajgarh", "Ratlam", "Rewa", "Sagar", "Sehore", "Seoni", "Shahdol", "Shajapur",
        "Sheopur", "Shivpuri", "Sidhi", "Singrauli", "Sironj", "Satna", "Tendukheda",
        "Tikamgarh", "Ujjain", "Umaria", "Unchehara", "Vidisha", "Waidhan"

    ],

    "Maharashtra": [
        "Ahmednagar", "Akola", "Alibaug", "Amalner", "Amravati", "Aurangabad",
        "Badlapur", "Baramati", "Beed", "Bhiwandi", "Buldhana", "Chalisgaon",
        "Chandrapur", "Daund", "Dhule", "Dombivli", "Gondia", "Hingoli",
        "Ichalkaranji", "Indapur", "Jalgaon", "Kalyan", "Karjat", "Khopoli",
        "Kolhapur", "Kudal", "Latur", "Lonar", "Lonavala", "Malegaon",
        "Malkapur", "Manchar", "Mangalvedhe", "Miraj", "Mumbai", "Nagpur",
        "Nanded", "Nandurbar", "Nashik", "Navi Mumbai", "Osmanabad",
        "Pachora", "Palghar", "Pandharpur", "Panvel", "Parbhani", "Pune",
        "Raigad", "Ratnagiri", "Risod", "Sangli", "Satara", "Sawantwadi",
        "Shegaon", "Shirur", "Sindhudurg", "Sinnar", "Solapur", "Tasgaon",
        "Thane", "Ulhasnagar", "Vasai", "Virar", "Wardha", "Washim",
        "Yavatmal"

    ],


    "Odisha": [
        "Angul", "Aska", "Athgarh", "Athmallik", "Aul", "Balasore", "Banarpal",
        "Banki", "Barbil", "Bargarh", "Baripada", "Berhampur", "Bhadrak",
        "Bhubaneswar", "Biramitrapur", "Bolangir", "Boudh", "Chhatrapur",
        "Cuttack", "Deogarh", "Dhenkanal", "Digapahandi", "Gajapati",
        "Ganjam", "Gunupur", "Hinjilicut", "Jagatsinghpur", "Jeypore",
        "Jharsuguda", "Joda", "Kandhamal", "Karanjia", "Kendrapara",
        "Keonjhar", "Khurda", "Koraput", "Malkangiri", "Mayurbhanj",
        "Nayagarh", "Nuapada", "Padampur", "Paradeep", "Parlakhemundi",
        "Pattamundai", "Phulbani", "Polasara", "Puri", "Rairangpur",
        "Rajgangpur", "Rayagada", "Rourkela", "Salipur", "Sambalpur",
        "Sonepur", "Sundargarh", "Sunabeda", "Talcher", "Titlagarh"

    ],

    "Punjab": [
        "Abohar", "Amritsar", "Barnala", "Bathinda", "Dhuri", "Faridkot", "Fazilka",
        "Firozpur", "Gurdaspur", "Hoshiarpur", "Jalandhar", "Kapurthala", "Khanna",
        "Kotkapura", "Ludhiana", "Malerkotla", "Moga", "Mohali", "Morinda", "Muktsar",
        "Nabha", "Nakodar", "Pathankot", "Patiala", "Phagwara", "Rajpura", "Ropar",
        "Samana", "Sangrur", "Sunam", "Tarn Taran", "Zirakpur"

    ],

    "Rajasthan": [
        "Ajmer", "Alwar", "Anupgarh", "Banswara", "Baran", "Barmer", "Bayana",
        "Beawar", "Bharatpur", "Bhilwara", "Bikaner", "Bundi", "Chittorgarh",
        "Churu", "Dausa", "Deeg", "Didwana", "Dungarpur", "Fatehpur",
        "Gangapur City", "Hanumangarh", "Hindaun", "Jaipur", "Jaisalmer",
        "Jalore", "Jhalawar", "Jhunjhunu", "Jodhpur", "Karauli", "Karanpur",
        "Kekri", "Kishangarh", "Kota", "Kotputli", "Lachhmangarh", "Makrana",
        "Mandawa", "Mount Abu", "Nagaur", "Nadbai", "Nasirabad",
        "Nawalgarh", "Neem Ka Thana", "Padampur", "Pali", "Phulera",
        "Pilani", "Pratapgarh", "Raisinghnagar", "Rajsamand",
        "Ratangarh", "Sadulpur", "Sadulshahar", "Sambhar",
        "Sawai Madhopur", "Shahpura", "Sikar", "Sirohi",
        "Sri Ganganagar", "Sujangarh", "Surajgarh", "Todabhim",
        "Tonk", "Udaipur", "Viratnagar", "Vijaynagar", "Weir"

    ],

    "Tamil Nadu": [
        "Ambur", "Arakkonam", "Ariyalur", "Aruppukkottai", "Attur", "Avadi",
        "Bhavani", "Chengalpattu", "Chennai", "Coimbatore", "Coonoor",
        "Cuddalore", "Devakottai", "Dharmapuri", "Dindigul", "Erode",
        "Gobichettipalayam", "Gudiyatham", "Hosur", "Kallakurichi",
        "Kanchipuram", "Karaikudi", "Karur", "Krishnagiri", "Kumbakonam",
        "Madurai", "Madurantakam", "Manamadurai", "Mayiladuthurai",
        "Mettupalayam", "Nagapattinam", "Nagercoil", "Namakkal",
        "Neyveli", "Ooty", "Palani", "Palladam", "Panruti",
        "Paramakudi", "Perambalur", "Pollachi", "Pudukkottai",
        "Rajapalayam", "Ramanathapuram", "Ranipet", "Rasipuram",
        "Salem", "Sankarankovil", "Sathyamangalam", "Sivakasi",
        "Srivilliputhur", "Tambaram", "Thanjavur", "Theni",
        "Thoothukudi", "Thiruvallur", "Tindivanam", "Tenkasi",
        "Tiruchengode", "Tiruchirappalli", "Tirunelveli",
        "Tirupattur", "Tiruppur", "Udumalaipettai", "Ulundurpet",
        "Vaniyambadi", "Vellore", "Villupuram", "Virudhunagar"
    ],

    "Telangana": [
        "Achampet", "Adilabad", "Alwal", "Asifabad", "Bhadrachalam", "Bhainsa",
        "Bhongir", "Bellampalli", "Bollaram", "Chegunta", "Chevella",
        "Devarakonda", "Dornakal", "Dubbak", "Gadwal", "Gajwel",
        "Godavarikhani", "Hyderabad", "Huzurabad", "Huzurnagar",
        "Jadcherla", "Jagtial", "Jammikunta", "Kalwakurthy",
        "Kagaznagar", "Karimnagar", "Khammam", "Kodad",
        "Kothagudem", "Korutla", "Kukatpally", "LB Nagar",
        "Mahabubabad", "Mahbubnagar", "Malkajgiri", "Mancherial",
        "Medak", "Metpally", "Miryalaguda", "Mudhole",
        "Nagarkurnool", "Nalgonda", "Narayanpet", "Nirmal",
        "Nizamabad", "Palvancha", "Parigi", "Patancheru",
        "Peddapalli", "Quthbullapur", "Ramagundam", "Sangareddy",
        "Secunderabad", "Shadnagar", "Siddipet", "Sircilla",
        "Suryapet", "Tandur", "Uppal", "Vemulawada",
        "Vikarabad", "Wanaparthy", "Warangal", "Yadagirigutta",
        "Yellandu", "Zaheerabad"

    ],

    "Uttar Pradesh": [
        "Agra", "Aligarh", "Amethi", "Amroha", "Auraiya", "Ayodhya",
        "Azamgarh", "Bahraich", "Ballia", "Balrampur", "Banda",
        "Barabanki", "Bareilly", "Basti", "Bhadohi", "Bijnor",
        "Bulandshahr", "Chandauli", "Chitrakoot", "Deoria",
        "Etah", "Etawah", "Faizabad", "Farrukhabad", "Fatehpur",
        "Firozabad", "Ghaziabad", "Ghazipur", "Gonda", "Gorakhpur",
        "Hamirpur", "Hapur", "Hardoi", "Jaunpur", "Jalaun",
        "Jhansi", "Kannauj", "Kanpur", "Kanpur Dehat", "Kasganj",
        "Kaushambi", "Kushinagar", "Lakhimpur", "Lalitpur",
        "Lucknow", "Maharajganj", "Mahoba", "Mainpuri", "Mathura",
        "Mau", "Meerut", "Mirzapur", "Moradabad", "Noida",
        "Orai", "Padrauna", "Pilibhit", "Pratapgarh",
        "Prayagraj", "Raebareli", "Rampur", "Robertsganj",
        "Saharanpur", "Sant Kabir Nagar", "Sambhal",
        "Shahjahanpur", "Shravasti", "Sitapur", "Sonbhadra",
        "Sultanpur", "Unnao", "Varanasi"
    ],

    "West Bengal": [
        "Alipurduar", "Amta", "Arambagh", "Asansol", "Bagnan", "Baidyabati",
        "Balurghat", "Bankura", "Bansberia", "Barasat", "Bardhaman",
        "Barrackpore", "Baruipur", "Basirhat", "Birpara", "Bishnupur",
        "Bolpur", "Bongaon", "Canning", "Chanchal", "Chandannagar",
        "Chinsurah", "Contai", "Cooch Behar", "Dankuni", "Diamond Harbour",
        "Digha", "Domjur", "Dubrajpur", "Durgapur", "Egra", "Falakata",
        "Gangarampur", "Garbeta", "Garia", "Haldia", "Halisahar",
        "Hasimara", "Hooghly", "Howrah", "Islampur", "Jalpaiguri",
        "Jhalda", "Jhargram", "Kalyani", "Kharagpur", "Khatra",
        "Kolkata", "Krishnanagar", "Malda", "Mathabhanga", "Midnapore",
        "Naihati", "Nalhati", "Nandakumar", "New Town", "Panskura",
        "Purulia", "Raghunathpur", "Raiganj", "Rampurhat", "Ranaghat",
        "Rajarhat", "Rishra", "Serampore", "Siliguri", "Sonamukhi",
        "Sonarpur", "Suri", "Tamluk", "Tarakeswar", "Tufanganj",
        "Uluberia", "Uttarpara"
    ],

    # Union Territories
    "Delhi": [
        "Chhatarpur", "Delhi Cantt", "Dwarka", "Janakpuri",
        "Kalkaji", "Karol Bagh", "Laxmi Nagar", "Mayur Vihar",
        "Narela", "New Delhi", "Pitampura", "Punjabi Bagh",
        "Rohini", "Saket", "Shahdara", "Vasant Kunj"
    ],

    "Jammu and Kashmir": [
        "Anantnag", "Bandipora", "Bani", "Baramulla",
        "Batote", "Bhaderwah", "Doda", "Ganderbal",
        "Jammu", "Kathua", "Kishtwar", "Kulgam",
        "Kupwara", "Poonch", "Pulwama", "Rajouri",
        "Reasi", "Shopian", "Sopore", "Srinagar",
        "Udhampur"
    ],

    "Ladakh": [
        "Diskit", "Drass", "Kargil", "Leh",
        "Nubra", "Turtuk"
    ],

    "Puducherry": [
        "Karaikal", "Mahe", "Puducherry", "Yanam"
    ],

    "Chandigarh": [
        "Chandigarh"
    ],

    "Andaman and Nicobar Islands": [
        "Campbell Bay", "Car Nicobar", "Diglipur",
        "Havelock", "Neil Island", "Port Blair", "Rangat"
    ],

    "Dadra and Nagar Haveli and Daman and Diu": [
        "Amal", "Daman", "Diu",
        "Kachigam", "Moti Daman", "Silvassa"
    ]
}
