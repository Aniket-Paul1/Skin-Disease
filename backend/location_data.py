# backend/location_data.py

STATE_CITY_MAP = {

    "Andhra Pradesh": [
    "Visakhapatnam", "Vijayawada", "Guntur", "Nellore", "Kurnool",
    "Tirupati", "Rajahmundry", "Anantapur", "Kadapa", "Eluru",
    "Ongole", "Chittoor", "Machilipatnam", "Tenali", "Proddatur",
    "Hindupur", "Srikakulam", "Vizianagaram", "Bhimavaram",
    "Narasaraopet", "Tadepalligudem", "Kakinada", "Amaravati",
    "Puttaparthi", "Madanapalle", "Palakollu", "Gudur",
    "Markapur", "Nandyal", "Rayachoti", "Pulivendula",
    "Bapatla", "Mangalagiri", "Addanki", "Pithapuram",
    "Samalkot", "Tanuku", "Yemmiganur", "Gooty",
    "Dharmavaram", "Tadipatri", "Venkatagiri",
    "Atmakur", "Kavali", "Sullurpeta", "Naidupeta",
    "Pileru", "Nagari", "Salur", "Parvathipuram",
    "Ichchapuram", "Amalapuram", "Ramachandrapuram",
    "Kandukur", "Podili", "Kanigiri", "Narsipatnam",
    "Palasa", "Mandapeta", "Jammalamadugu",
    "Mydukur", "Badvel", "Guntakal", "Yerraguntla",
    "Kadiri", "Penukonda", "Chilakaluripet",
    "Sattenapalle", "Repalle", "Ponnur"
    ],
  
    "Arunachal Pradesh": [
        "Itanagar", "Naharlagun", "Pasighat", "Tawang",
        "Ziro", "Bomdila", "Along", "Tezu", "Roing"
    ],

    "Assam": [
        "Guwahati", "Dibrugarh", "Silchar", "Jorhat", "Tezpur",
        "Nagaon", "Tinsukia", "Sivasagar", "Goalpara",
        "Barpeta", "Dhubri", "Karimganj"
    ],

    "Bihar": [
    "Patna", "Gaya", "Bhagalpur", "Muzaffarpur", "Darbhanga",
    "Purnia", "Arrah", "Begusarai", "Katihar", "Munger",
    "Chhapra", "Sasaram", "Hajipur", "Samastipur",
    "Motihari", "Siwan", "Buxar", "Jamalpur",
    "Nawada", "Sitamarhi", "Madhubani", "Araria",
    "Kishanganj", "Supaul", "Madhepura", "Saharsa",
    "Khagaria", "Sheikhpura", "Lakhisarai",
    "Jehanabad", "Aurangabad", "Bettiah", "Bagaha",
    "Narkatiaganj", "Forbesganj", "Rosera",
    "Dalsinghsarai", "Barh", "Bakhtiyarpur",
    "Danapur", "Phulwari Sharif", "Masaurhi",
    "Maner", "Fatuha", "Hilsa",
    "Bihar Sharif", "Rajgir", "Islampur",
    "Nalanda", "Silao", "Warisliganj",
    "Gopalganj", "Mirganj", "Barauli",
    "Maharajganj", "Revelganj", "Chapra",
    "Raxaul", "Sugauli", "Ramgarh",
    "Bhabua", "Mohania", "Dumraon",
    "Tekari", "Belaganj", "Wazirganj",
    "Benipur", "Jale", "Hayaghat",
    "Singhwara", "Baheri"
    ],

    "Chhattisgarh": [
        "Raipur", "Bilaspur", "Durg", "Bhilai", "Korba",
        "Raigarh", "Jagdalpur", "Ambikapur", "Rajnandgaon",
        "Dhamtari"
    ],

    "Goa": [
        "Panaji", "Margao", "Vasco da Gama", "Mapusa",
        "Ponda", "Bicholim", "Curchorem", "Sanquelim"
    ],

"Gujarat": [
    "Ahmedabad", "Surat", "Vadodara", "Rajkot", "Bhavnagar",
    "Jamnagar", "Junagadh", "Gandhinagar", "Anand",
    "Navsari", "Morbi", "Surendranagar", "Bharuch",
    "Mehsana", "Palanpur", "Porbandar", "Godhra",
    "Valsad", "Vapi", "Amreli", "Botad", "Veraval",
    "Jetpur", "Kalol", "Dahod", "Patan",
    "Deesa", "Himatnagar", "Modasa", "Idar",
    "Visnagar", "Unjha", "Kadi", "Sanand",
    "Dholka", "Viramgam", "Mandvi", "Bhuj",
    "Anjar", "Gandhidham", "Mundra", "Nakhatrana",
    "Khambhalia", "Dwarka", "Okha",
    "Jasdan", "Gondal", "Upleta",
    "Rajula", "Savarkundla", "Talaja",
    "Mahuva", "Songadh", "Vyara",
    "Bardoli", "Chikhli", "Gandevi",
    "Bilimora", "Pardi", "Umbergaon",
    "Kapadvanj", "Balasinor", "Lunawada",
    "Santrampur", "Limkheda", "Halol",
    "Kalol (PMS)", "Petlad", "Borsad",
    "Khambhat", "Anklav"
    ],

    "Haryana": [
        "Gurugram","Faridabad","Panipat","Ambala","Hisar","Rohtak","Karnal","Sonipat",
        "Yamunanagar","Panchkula","Bhiwani","Sirsa","Bahadurgarh","Jind","Thanesar",
        "Kaithal","Rewari","Palwal","Hansi","Narnaul","Fatehabad","Tohana","Gohana",
        "Samalkha","Ellenabad","Narwana","Pehowa","Ratia","Kalanaur","Ladwa"
    ],

    "Himachal Pradesh": [
        "Shimla","Solan","Dharamshala","Mandi","Kullu","Manali","Una","Nahan",
        "Hamirpur","Bilaspur","Chamba","Palampur","Sundarnagar","Kangra",
        "Paonta Sahib","Nalagarh","Jogindernagar","Theog","Rampur","Rohru"
    ],

    "Jharkhand": [
        "Ranchi","Jamshedpur","Dhanbad","Bokaro","Hazaribagh","Deoghar","Giridih",
        "Ramgarh","Phusro","Medininagar","Chirkunda","Godda","Sahebganj",
        "Dumka","Chaibasa","Lohardaga","Pakur","Latehar","Jhumri Telaiya"
    ],
    
    "Karnataka": [
    "Bengaluru", "Mysuru", "Mangaluru", "Hubballi", "Belagavi",
    "Shivamogga", "Ballari", "Davanagere", "Tumakuru",
    "Udupi", "Chitradurga", "Raichur", "Bidar",
    "Hassan", "Mandya", "Kolar", "Chikkamagaluru",
    "Bagalkot", "Gadag", "Koppal", "Yadgir",
    "Kalaburagi", "Vijayapura", "Hospet", "Sirsi",
    "Karwar", "Bhatkal", "Kundapura", "Puttur",
    "Sullia", "Moodbidri", "Karkala", "Channarayapatna",
    "Arsikere", "Tiptur", "Gubbi", "Nelamangala",
    "Ramanagara", "Magadi", "Kanakapura",
    "Malavalli", "Maddur", "Srirangapatna",
    "Nanjangud", "Hunsur", "Krishnarajanagara",
    "Athani", "Gokak", "Savadatti",
    "Jamkhandi", "Mudhol", "Rabkavi",
    "Ilkal", "Hungund", "Sindhanur",
    "Manvi", "Lingasugur", "Basavakalyan",
    "Bhalki", "Chincholi", "Aland",
    "Shahabad", "Sedam", "Afzalpur",
    "Challakere", "Holalkere", "Hosadurga",
    "Tarikere", "Kadur", "Mudigere"
    ],

    "Kerala": [
    "Thiruvananthapuram", "Kochi", "Kozhikode", "Thrissur",
    "Kollam", "Alappuzha", "Palakkad", "Malappuram",
    "Kannur", "Kasaragod", "Kottayam", "Pathanamthitta",
    "Idukki", "Wayanad", "Perinthalmanna", "Ponnani",
    "Manjeri", "Tirur", "Tanur",
    "Nilambur", "Kondotty", "Valanchery",
    "Chavakkad", "Guruvayur", "Irinjalakuda",
    "Kodungallur", "Kunnamkulam", "Ottapalam",
    "Shoranur", "Cherpulassery", "Mannarkkad",
    "Pattambi", "Kayamkulam", "Mavelikkara",
    "Haripad", "Chengannur", "Adoor",
    "Pandalam", "Punalur", "Kottarakkara",
    "Karunagappally", "Paravur",
    "Attingal", "Nedumangad", "Varkala",
    "Kilimanoor", "Kanhangad", "Payyannur",
    "Taliparamba", "Iritty", "Thalassery",
    "Kuthuparamba", "Vadakara", "Quilandy",
    "Feroke", "Ramanattukara", "Koyilandy",
    "Sulthan Bathery", "Kalpetta", "Mananthavady",
    "Munnar", "Devikulam"
    ],

    "Madhya Pradesh": [
    "Indore", "Bhopal", "Gwalior", "Jabalpur", "Ujjain",
    "Sagar", "Rewa", "Satna", "Ratlam", "Dewas",
    "Katni", "Chhindwara", "Vidisha", "Sehore",
    "Shivpuri", "Morena", "Neemuch", "Mandsaur",
    "Burhanpur", "Khandwa", "Khargone", "Barwani",
    "Rajgarh", "Shajapur", "Agar Malwa",
    "Hoshangabad", "Itarsi", "Pipariya",
    "Betul", "Multai", "Guna",
    "Ashoknagar", "Datia", "Bhind",
    "Sheopur", "Chhatarpur", "Panna",
    "Tikamgarh", "Niwari", "Damoh",
    "Jabalpur Cantonment", "Mandla", "Dindori",
    "Balaghat", "Seoni", "Pandhurna",
    "Lakhnadon", "Narsinghpur", "Gadarwara",
    "Tendukheda", "Maihar", "Nagod",
    "Unchehara", "Shahdol", "Anuppur",
    "Umaria", "Singrauli", "Waidhan",
    "Sidhi", "Churhat", "Kotma",
    "Jaithari", "Pali", "Katangi",
    "Bina", "Khurai", "Rahatgarh",
    "Sironj", "Lateri"
    ],

    "Maharashtra": [
    "Mumbai", "Pune", "Nagpur", "Nashik", "Aurangabad",
    "Solapur", "Kolhapur", "Thane", "Navi Mumbai",
    "Kalyan", "Dombivli", "Amravati", "Akola",
    "Jalgaon", "Latur", "Sangli", "Satara",
    "Ahmednagar", "Chandrapur", "Parbhani",
    "Nanded", "Beed", "Osmanabad", "Wardha",
    "Buldhana", "Yavatmal", "Gondia", "Ratnagiri",
    "Sindhudurg", "Sawantwadi", "Kudal",
    "Panvel", "Raigad", "Alibaug",
    "Vasai", "Virar", "Palghar",
    "Bhiwandi", "Ulhasnagar", "Badlapur",
    "Karjat", "Khopoli", "Lonavala",
    "Baramati", "Daund", "Indapur",
    "Shirur", "Manchar", "Sinnar",
    "Malegaon", "Dhule", "Nandurbar",
    "Chalisgaon", "Amalner", "Pachora",
    "Ichalkaranji", "Miraj", "Tasgaon",
    "Pandharpur", "Mangalvedhe",
    "Hingoli", "Washim", "Risod",
    "Lonar", "Shegaon", "Malkapur"
    ],


    "Odisha": [
    "Bhubaneswar", "Cuttack", "Rourkela", "Sambalpur",
    "Puri", "Berhampur", "Balasore", "Baripada",
    "Bhadrak", "Jharsuguda", "Jeypore", "Angul",
    "Dhenkanal", "Kendrapara", "Jagatsinghpur",
    "Paradeep", "Khurda", "Nayagarh",
    "Bolangir", "Titlagarh", "Patnagarh",
    "Bargarh", "Padampur", "Nuapada",
    "Koraput", "Sunabeda", "Malkangiri",
    "Rayagada", "Gunupur", "Phulbani",
    "Kandhamal", "Gajapati", "Parlakhemundi",
    "Ganjam", "Aska", "Hinjilicut",
    "Chhatrapur", "Digapahandi", "Polasara",
    "Mayurbhanj", "Rairangpur", "Karanjia",
    "Keonjhar", "Barbil", "Joda",
    "Sundargarh", "Rajgangpur", "Biramitrapur",
    "Deogarh", "Boudh", "Sonepur",
    "Athmallik", "Talcher", "Banarpal",
    "Pattamundai", "Aul", "Salipur",
    "Banki", "Athgarh"
    ],

    "Punjab": [
        "Ludhiana","Amritsar","Jalandhar","Patiala","Bathinda","Mohali",
        "Hoshiarpur","Pathankot","Moga","Abohar","Malerkotla","Phagwara",
        "Kapurthala","Muktsar","Faridkot","Firozpur","Gurdaspur",
        "Barnala","Sangrur","Rajpura","Zirakpur","Tarn Taran",
        "Fazilka","Kotkapura","Sunam","Nabha","Khanna",
        "Morinda","Samana","Dhuri","Ropar","Nakodar"
    ],

    "Rajasthan": [
    "Jaipur", "Jodhpur", "Udaipur", "Ajmer", "Kota",
    "Bikaner", "Alwar", "Bharatpur", "Sikar",
    "Pali", "Bhilwara", "Chittorgarh", "Tonk",
    "Nagaur", "Barmer", "Jaisalmer",
    "Hanumangarh", "Sri Ganganagar", "Jhunjhunu",
    "Churu", "Banswara", "Dungarpur",
    "Pratapgarh", "Rajsamand", "Sawai Madhopur",
    "Dausa", "Karauli", "Bundi",
    "Jhalawar", "Baran", "Jalore",
    "Sirohi", "Mount Abu", "Beawar",
    "Kishangarh", "Nasirabad", "Kekri",
    "Didwana", "Makrana", "Nawalgarh",
    "Mandawa", "Fatehpur", "Lachhmangarh",
    "Neem Ka Thana", "Surajgarh", "Pilani",
    "Sadulpur", "Ratangarh", "Sujangarh",
    "Anupgarh", "Padampur", "Raisinghnagar",
    "Sadulshahar", "Karanpur", "Vijaynagar",
    "Shahpura", "Gangapur City", "Hindaun",
    "Todabhim", "Bayana", "Deeg",
    "Nadbai", "Weir", "Phulera",
    "Sambhar", "Kotputli", "Viratnagar"
    ],

    "Tamil Nadu": [
    "Chennai", "Coimbatore", "Madurai", "Tiruchirappalli", "Salem",
    "Erode", "Tirunelveli", "Vellore", "Thoothukudi", "Dindigul",
    "Thanjavur", "Cuddalore", "Kanchipuram", "Nagercoil",
    "Karur", "Namakkal", "Hosur", "Ranipet", "Tiruppur",
    "Sivakasi", "Mayiladuthurai", "Nagapattinam", "Pudukkottai",
    "Ramanathapuram", "Virudhunagar", "Ariyalur", "Perambalur",
    "Dharmapuri", "Krishnagiri", "Theni", "Tenkasi",
    "Kumbakonam", "Pollachi", "Udumalaipettai", "Palani",
    "Gobichettipalayam", "Sathyamangalam", "Bhavani",
    "Mettupalayam", "Ooty", "Coonoor", "Gudiyatham",
    "Ambur", "Vaniyambadi", "Tirupattur", "Arakkonam",
    "Srivilliputhur", "Rajapalayam", "Sankarankovil",
    "Aruppukkottai", "Paramakudi", "Manamadurai",
    "Karaikudi", "Devakottai", "Thiruvallur",
    "Avadi", "Tambaram", "Chengalpattu",
    "Madurantakam", "Ulundurpet", "Villupuram",
    "Tindivanam", "Panruti", "Neyveli",
    "Kallakurichi", "Attur", "Rasipuram",
    "Tiruchengode", "Palladam"
    ],

    "Telangana": [
    "Hyderabad", "Warangal", "Nizamabad", "Karimnagar",
    "Khammam", "Ramagundam", "Mahbubnagar",
    "Nalgonda", "Adilabad", "Mancherial",
    "Siddipet", "Jagtial", "Sircilla",
    "Peddapalli", "Godavarikhani", "Korutla",
    "Metpally", "Vemulawada", "Huzurabad",
    "Jammikunta", "Sangareddy", "Medak",
    "Zaheerabad", "Patancheru", "Bollaram",
    "Gajwel", "Dubbak", "Chegunta",
    "Mahabubabad", "Dornakal", "Yellandu",
    "Kothagudem", "Palvancha", "Bhadrachalam",
    "Asifabad", "Kagaznagar", "Bellampalli",
    "Nirmal", "Bhainsa", "Mudhole",
    "Narayanpet", "Gadwal", "Wanaparthy",
    "Achampet", "Nagarkurnool", "Kalwakurthy",
    "Shadnagar", "Jadcherla", "Kodad",
    "Suryapet", "Huzurnagar", "Miryalaguda",
    "Devarakonda", "Bhongir", "Yadagirigutta",
    "Malkajgiri", "Uppal", "LB Nagar",
    "Secunderabad", "Kukatpally", "Quthbullapur",
    "Alwal", "Tandur", "Vikarabad",
    "Parigi", "Chevella"
    ],

    "Uttar Pradesh": [
    "Lucknow", "Kanpur", "Varanasi", "Agra", "Prayagraj",
    "Noida", "Ghaziabad", "Meerut", "Aligarh",
    "Bareilly", "Moradabad", "Saharanpur",
    "Gorakhpur", "Faizabad", "Ayodhya",
    "Jhansi", "Mathura", "Firozabad",
    "Rampur", "Shahjahanpur", "Hapur",
    "Bulandshahr", "Sitapur", "Hardoi",
    "Unnao", "Raebareli", "Amethi",
    "Sultanpur", "Pratapgarh", "Basti",
    "Deoria", "Kushinagar", "Padrauna",
    "Maharajganj", "Ballia", "Mau",
    "Azamgarh", "Jaunpur", "Mirzapur",
    "Chandauli", "Sonbhadra", "Robertsganj",
    "Ghazipur", "Bhadohi", "Sant Kabir Nagar",
    "Etawah", "Mainpuri", "Farrukhabad",
    "Kannauj", "Auraiya", "Kanpur Dehat",
    "Jalaun", "Orai", "Hamirpur",
    "Mahoba", "Lalitpur", "Chitrakoot",
    "Banda", "Kaushambi", "Fatehpur",
    "Barabanki", "Gonda", "Balrampur",
    "Bahraich", "Shravasti", "Lakhimpur",
    "Pilibhit", "Bijnor", "Amroha",
    "Sambhal", "Kasganj", "Etah"
    ],

    "West Bengal": [
    "Kolkata", "Howrah", "Durgapur", "Asansol",
    "Siliguri", "Malda", "Bardhaman",
    "Kharagpur", "Haldia", "Krishnanagar",
    "Ranaghat", "Balurghat", "Jalpaiguri",
    "Cooch Behar", "Alipurduar",
    "Raiganj", "Islampur", "Gangarampur",
    "Chanchal", "Tufanganj", "Mathabhanga",
    "Falakata", "Birpara", "Hasimara",
    "Suri", "Rampurhat", "Bolpur",
    "Dubrajpur", "Nalhati", "Bishnupur",
    "Bankura", "Sonamukhi", "Khatra",
    "Arambagh", "Tarakeswar", "Chinsurah",
    "Serampore", "Rishra", "Baidyabati",
    "Uttarpara", "Bansberia", "Chandannagar",
    "Hooghly", "Dankuni", "Domjur",
    "Uluberia", "Bagnan", "Amta",
    "Contai", "Digha", "Tamluk",
    "Panskura", "Nandakumar", "Egra",
    "Midnapore", "Jhargram", "Garbeta",
    "Purulia", "Raghunathpur", "Jhalda",
    "Barasat", "Barrackpore", "Kalyani",
    "Naihati", "Halisahar", "Bongaon",
    "Basirhat", "Diamond Harbour", "Baruipur",
    "Sonarpur", "Canning", "Garia",
    "New Town", "Rajarhat"
    ],

    # Union Territories
    "Delhi": [
        "New Delhi","Delhi Cantt","Dwarka","Rohini","Saket","Pitampura",
        "Janakpuri","Vasant Kunj","Shahdara","Karol Bagh","Mayur Vihar",
        "Laxmi Nagar","Punjabi Bagh","Narela","Kalkaji","Chhatarpur"
    ],

    "Jammu and Kashmir": [
    "Srinagar", "Jammu", "Anantnag", "Baramulla",
    "Pulwama", "Shopian", "Sopore", "Kulgam","Kupwara", "Bandipora",
    "Ganderbal", "Udhampur", "Kathua", "Rajouri",
    "Poonch", "Reasi", "Doda", "Kishtwar", "Bani","Batote","Bhaderwah"
    ],

    "Ladakh": ["Leh", "Kargil", "Drass", "Nubra", "Diskit","Turtuk"],

    "Puducherry": ["Puducherry", "Karaikal", "Mahe", "Yanam"],

    "Chandigarh": ["Chandigarh"],

    "Andaman and Nicobar Islands": [
        "Port Blair","Havelock","Neil Island","Car Nicobar",
        "Diglipur","Rangat","Campbell Bay"
    ],

    "Dadra and Nagar Haveli and Daman and Diu": [
        "Daman","Silvassa","Diu","Amal","Kachigam","Moti Daman"
    ],

    "Lakshadweep": [
    "Kavaratti", "Agatti", "Amini", "Andrott",
    "Kalpeni", "Minicoy"
]

}

