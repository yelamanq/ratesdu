from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates multiple user accounts from a list of usernames'

    def handle(self, *args, **options):
        usernames = [['abay.nazhimov', 'Abay', 'Nazhimov', ''],
['abdibek.ydyrys', 'Abdibek', 'Ydyrys', ''],
['abdulkarim.abdulrakhmanuly', 'Abdulkarim', 'Abdulrakhmanuly', ''],
['abylay.akay', 'Abylay', 'Akay', ''],
['abzal.omirzakov', 'Abzal', 'Omirzakov', ''],
['adem.ozkan', 'Adem', 'Ozkan', ''],
['adilzhan.anay', 'Adilzhan', 'Anay', ''],
['ahmet.yildiztas', 'Ahmet', 'Yildiztas', ''],
['aibek.smagul', 'Aibek', 'Smagul', ''],
['aida.baigarayeva', 'Aida', 'Baigarayeva', ''],
['aida.yergaliyeva', 'Aida', 'Yergaliyeva', ''],
['aidana.osserbay', 'Aidana', 'Osserbay', ''],
['aidana.shapambayeva', 'Aidana', 'Shapambayeva', ''],
['aidos.myrzabek', 'Aidos', 'Myrzabek', ''],
['aidos.shalbayev', 'Aidos', 'Shalbayev', ''],
['aidyn.adilbekova', 'Aidyn', 'Adilbekova', ''],
['aierke.myrzabayeva', 'Aierke', 'Myrzabayeva', ''],
['aigerim.anarbekova', 'Aigerim', 'Anarbekova', ''],
['aigerim.azimbekova', 'Aigerim', 'Azimbekova', ''],
['aigerim.bogyrbayeva', 'Aigerim', 'Bogyrbayeva', ''],
['aigerim.dauletiyarova', 'Aigerim', 'Dauletiyarova', ''],
['aigerim.kenzhegarina', 'Aigerim', 'Kenzhegarina', ''],
['aigerim.orynbassarova', 'Aigerim', 'Orynbassarova', ''],
['aigerim.raissova', 'Aigerim', 'Raissova', ''],
['aigerim.tursynbekova', 'Aigerim', 'Tursynbekova', ''],
['aigul.dauletkulova', 'Aigul', 'Dauletkulova', ''],
['aigul.kassenova', 'Aigul', 'Kassenova', ''],
['aigul.malikova', 'Aigul', 'Malikova', ''],
['aigul.shotanova', 'Aigul', 'Shotanova', ''],
['aiken.kazin', 'Aiken', 'Kazin', ''],
['aiman.shakulikova', 'Aiman', 'Shakulikova', ''],
['ainur.abdrazakova', 'Ainur', 'Abdrazakova', ''],
['ainur.aliyeva', 'Ainur', 'Aliyeva', ''],
['ainur.ilyubayeva', 'Ainur', 'Ilyubayeva', ''],
['ainura.yespanova', 'Ainura', 'Yespanova', ''],
['aisaule.bazarkulova', 'Aisaule', 'Bazarkulova', ''],
['aishabibi.dukenbayeva', 'Aishabibi', 'Dukenbayeva', ''],
['aisulu.aubakir', 'Aisulu', 'Aubakir', ''],
['aisulu.baibekova', 'Aisulu', 'Baibekova', ''],
['aisulu.gatiat', 'Aisulu', 'Gatiat', ''],
['aisulu.saduakassova', 'Aisulu', 'Saduakassova', ''],
['aisulu.utemuratova', 'Aisulu', 'Utemuratova', ''],
['aiyana.orynbassarova', 'Aiyana', 'Orynbassarova', ''],
['aiym.sagdoldanova', 'Aiym', 'Sagdoldanova', ''],
['aizada.nuriddenova', 'Aizada', 'Nuriddenova', ''],
['aizhan.asylbek', 'Aizhan', 'Asylbek', ''],
['aizhan.kopbayeva', 'Aizhan', 'Kopbayeva', ''],
['akbope.aidos', 'Akbope', 'Aidos', ''],
['akbota.abiyr', 'Akbota', 'Abiyr', ''],
['akbota.tolbayeva', 'Akbota', 'Tolbayeva', ''],
['akerke.yessenbekova', 'Akerke', 'Yessenbekova', ''],
['akmanet.ashenova', 'Akmanet', 'Ashenova', ''],
['akmaral.davletova', 'Akmaral', 'Davletova', ''],
['akmaral.turysbekova', 'Akmaral', 'Turysbekova', ''],
['akmaral.zharmagambetova', 'Akmaral', 'Zharmagambetova', ''],
['akmarzhan.nogaibayeva', 'Akmarzhan', 'Nogaibayeva', ''],
['aksholpan.rassil', 'Aksholpan', 'Rassil', ''],
['aksholpan.saparova', 'Aksholpan', 'Saparova', ''],
['aleksei.kavokin', 'Aleksei', 'Kavokin', ''],
['alexandr.ivanov', 'Alexandr', 'Ivanov', ''],
['alfarabi.serik', 'Alfarabi', 'Serik', ''],
['ali.baigelenov', 'Ali', 'Baigelenov', ''],
['alibek.orynbassar', 'Alibek', 'Orynbassar', ''],
['alikhan.nurlanuly', 'Alikhan', 'Nurlanuly', ''],
['alina.bedelkhanova', 'Alina', 'Bedelkhanova', ''],
['alina.fazilova', 'Alina', 'Fazilova', ''],
['alisher.duzmagambetov', 'Alisher', 'Duzmagambetov', ''],
['alisher.uali', 'Alisher', 'Uali', ''],
['aliya.imankulova', 'Aliya', 'Imankulova', ''],
['aliya.zakariya', 'Aliya', 'Zakariya', ''],
['aliya.zhunis', 'Aliya', 'Zhunis', ''],
['almas.sabitov', 'Almas', 'Sabitov', ''],
['almash.seidikenova', 'Almash', 'Seidikenova', ''],
['almat.abdrashit', 'Almat', 'Abdrashit', ''],
['altynay.kaibullayeva', 'Altynay', 'Kaibullayeva', ''],
['altynay.omirzakova', 'Altynay', 'Omirzakova', ''],
['altyngul.khadyl', 'Altyngul', 'Khadyl', ''],
['amirkhan.orazbay', 'Amirkhan', 'Orazbay', ''],
['anastassiya.nesterova', 'Anastassiya', 'Nesterova', ''],
['andrey.bogdanchikov', 'Andrey', 'Bogdanchikov', ''],
['arailym.serikbay', 'Arailym', 'Serikbay', ''],
['araitang.zhanuzak', 'Araitang', 'Zhanuzak', ''],
['aray.tlepbergenova', 'Aray', 'Tlepbergenova', ''],
['ardak.korzhinbayeva', 'Ardak', 'Korzhinbayeva', ''],
['ardak.shalkarbayuly', 'Ardak', 'Shalkarbay-uly', ''],
['arman.argynbayev', 'Arman', 'Argynbayev', ''],
['aruzhan.altynbekova', 'Aruzhan', 'Altynbekova', ''],
['aruzhan.kutzhan', 'Aruzhan', 'Kutzhan', ''],
['aruzhan.seitmagambet', 'Aruzhan', 'Seitmagambet', ''],
['aruzhan.zhorabekova', 'Aruzhan', 'Zhorabekova', ''],
['askar.aitkulov', 'Askar', 'Aitkulov', ''],
['askar.dzhumadildaev', 'Askar', 'Dzhumadildaev', ''],
['askhan.shametov', 'Askhan', 'Shametov', ''],
['askhat.yerkimbay', 'Askhat', 'Yerkimbay', ''],
['assel.aitimbetova', 'Assel', 'Aitimbetova', ''],
['assel.tolep', 'Assel', 'Tolep', ''],
['assel.yembergenova', 'Assel', 'Yembergenova', ''],
['assem.kaliyeva', 'Assem', 'Kaliyeva', ''],
['assem.kuanishbayeva', 'Assem', 'Kuanishbayeva', ''],
['assem.talasbek', 'Assem', 'Talasbek', ''],
['assyl.abilakim', 'Assyl', 'Abilakim', ''],
['assyl.meyrambek', 'Assyl', 'Meyrambek', ''],
['ayatola.gabdulin', 'Ayatola', 'Gabdulin', ''],
['ayazhan.azhigulova', 'Ayazhan', 'Azhigulova', ''],
['azamat.amangeldiyev', 'Azamat', 'Amangeldiyev', ''],
['azamat.bakytzhan', 'Azamat', 'Bakytzhan', ''],
['azamat.korzhumbayev', 'Azamat', 'Korzhumbayev', ''],
['azamat.serek', 'Azamat', 'Serek', ''],
['azamat.tuleuov', 'Azamat', 'Tuleuov', ''],
['azamat.zhamanov', 'Azamat', 'Zhamanov', ''],
['azat.kali', 'Azat', 'Kali', ''],
['azatzhan.baitekov', 'Azatzhan', 'Baitekov', ''],
['aziza.aipenova', 'Aziza', 'Aipenova', ''],
['babur.rashidov', 'Babur', 'Rashidov', ''],
['bagdaulet.mukhammedov', 'Bagdaulet', 'Mukhammedov', ''],
['bagila.uskenbaeva', 'Bagila', 'Uskenbaeva', ''],
['bakdaulet.aidarbekov', 'Bakdaulet', 'Aidarbekov', ''],
['bakhtiyar.nurumov', 'Bakhtiyar', 'Nurumov', ''],
['bakhtiyor.meraliyev', 'Bakhtiyor', 'Meraliyev', ''],
['bakhyt.sydykhov', 'Bakhyt', 'Sydykhov', ''],
['bakyt.akhmetzhanova', 'Bakyt', 'Akhmetzhanova', ''],
['balym.aidarkyzy', 'Balym', 'Aidarkyzy', ''],
['balzhan.tursynova', 'Balzhan', 'Tursynova', ''],
['bashaga.salayev', 'Bashaga', 'Salayev', ''],
['batyrkhan.omarov', 'Batyrkhan', 'Omarov', ''],
['bauyrzhan.berlikozha', 'Bauyrzhan', 'Berlikozha', ''],
['bauyrzhan.sartayev', 'Bauyrzhan', 'Sartayev', ''],
['bauyrzhan.yedgenov', 'Bauyrzhan', 'Yedgenov', ''],
['bayan.bekbolat', 'Bayan', 'Bekbolat', ''],
['bayan.kerimbekova', 'Bayan', 'Kerimbekova', ''],
['bektur.baizhanov', 'Bektur', 'Baizhanov', ''],
['bekzat.zhakhayev', 'Bekzat', 'Zhakhayev', ''],
['benedicta.chukwuekwu.nwaefido', 'Benedicta', 'Chukwuekwu Nwaefido', ''],
['berdak.bayimbetov', 'Berdak', 'Bayimbetov', ''],
['bereke.zhumakayeva', 'Bereke', 'Zhumakayeva', ''],
['bibizhamal.amangeldi', 'Bibizhamal', 'Amangeldi', ''],
['binara.imankulova', 'Binara', 'Imankulova', ''],
['birzhan.ayanbayev', 'Birzhan', 'Ayanbayev', ''],
['birzhan.moldagaliyev', 'Birzhan', 'Moldagaliyev', ''],
['bissenbay.dauletbayev', 'Bissenbay', 'Dauletbayev', ''],
['bizhigit.sagidolla', 'Bizhigit', 'Sagidolla', ''],
['bolat.shaimenov', 'Bolat', 'Shaimenov', ''],
['bolat.tatibekov', 'Bolat', 'Tatibekov', ''],
['bota.khassen', 'Bota', 'Khassen', ''],
['bota.zhumakayeva', 'Bota', 'Zhumakayeva', ''],
['cemal.ozdemir', 'Cemal', 'Ozdemir', ''],
['cemil.turan', 'Cemil', 'Turan', ''],
['chingis.rustemov', 'Chingis', 'Rustemov', ''],
['daiana.murzakanova', 'Daiana', 'Murzakanova', ''],
['damir.kurmanbay', 'Damir', 'Kurmanbay', ''],
['damir.yessimbekov', 'Damir', 'Yessimbekov', ''],
['dana.anarbayeva', 'Dana', 'Anarbayeva', ''],
['dana.moldabayeva', 'Dana', 'Moldabayeva', ''],
['dana.molzhigit', 'Dana', 'Molzhigit', ''],
['danara.raikhanova', 'Danara', 'Raikhanova', ''],
['daniyar.mukhanov', 'Daniyar', 'Mukhanov', ''],
['daniyar.sydykov', 'Daniyar', 'Sydykov', ''],
['darkhan.kuanyshbay', 'Darkhan', 'Kuanyshbay', ''],
['darkhan.orynbassarov', 'Darkhan', 'Orynbassarov', ''],
['darmen.kariboz', 'Darmen', 'Kariboz', ''],
['dastan.ramankulov', 'Dastan', 'Ramankulov', ''],
['dauren.ayazbayev', 'Dauren', 'Ayazbayev', ''],
['davronzhon.gaipov', 'Davronzhon', 'Gaipov', ''],
['diana.nitto', 'Diana', 'Nitto', ''],
['diana.tashanova', 'Diana', 'Tashanova', ''],
['didar.zhanel', 'Didar', 'Zhanel', ''],
['dilnara.kassymova', 'Dilnara', 'Kassymova', ''],
['dilyara.khamidullina', 'Dilyara', 'Khamidullina', ''],
['dina.kengesbay', 'Dina', 'Kengesbay', ''],
['dinara.khashimova', 'Dinara', 'Khashimova', ''],
['dinara.yertargynkyzy', 'Dinara', 'Yertargynkyzy', ''],
['diyar.nurmetov', 'Diyar', 'Nurmetov', ''],
['dmitriy.cherkassov', 'Dmitriy', 'Cherkassov', ''],
['dossay.oryspayev', 'Dossay', 'Oryspayev', ''],
['doszhan.kaliyev', 'Doszhan', 'Kaliyev', ''],
['duman.telman', 'Duman', 'Telman', ''],
['durdona.yussupova', 'Durdona', 'Yussupova', ''],
['dzhanbulat.kayinbaev', 'Dzhanbulat', 'Kayinbaev', ''],
['elif.derya.ozdemir', 'Elif', 'Derya Ozdemir', ''],
['elmira.ospankulova', 'Elmira', 'Ospankulova', ''],
['elmira.zabirova', 'Elmira', 'Zabirova', ''],
['elnura.nabigazinova', 'Elnura', 'Nabigazinova', ''],
['emine.ozkan', 'Emine', 'Ozkan', ''],
['evgeny.morozov', 'Evgeny', 'Morozov', ''],
['farikha.nauruzbayeva', 'Farikha', 'Nauruzbayeva', ''],
['farkhat.mashurov', 'Farkhat', 'Mashurov', ''],
['farukh.mashurov', 'Farukh', 'Mashurov', ''],
['fatma.eraslan', 'Fatma', 'Eraslan', ''],
['gahwar.bhatti', 'Gahwar', 'Bhatti', ''],
['gaini.serim', 'Gaini', 'Serim', ''],
['galym.zhussipbek', 'Galym', 'Zhussipbek', ''],
['galymbek.kereibayev', 'Galymbek', 'Kereibayev', ''],
['galymzhan.zupiruly', 'Galymzhan', 'Zupiruly', ''],
['gaukhar.alimbekova', 'Gaukhar', 'Alimbekova', ''],
['gaukhar.alipbay', 'Gaukhar', 'Alipbay', ''],
['gaukhar.arepova', 'Gaukhar', 'Arepova', ''],
['gaziza.otarbayeva', 'Gaziza', 'Otarbayeva', ''],
['guldana.muzdybayeva', 'Guldana', 'Muzdybayeva', ''],
['guldana.talgat', 'Guldana', 'Talgat', ''],
['gulera.makhat', 'Gulera', 'Makhat', ''],
['gulfarida.tulemissova', 'Gulfarida', 'Tulemissova', ''],
['gulim.yessengaliyeva', 'Gulim', 'Yessengaliyeva', ''],
['guliya.nurmagambetova', 'Guliya', 'Nurmagambetova', ''],
['gulmira.bekenova', 'Gulmira', 'Bekenova', ''],
['gulmira.biteshova', 'Gulmira', 'Biteshova', ''],
['gulmira.myshbayeva', 'Gulmira', 'Myshbayeva', ''],
['gulnar.nurseitova', 'Gulnar', 'Nurseitova', ''],
['gulnara.kassymova', 'Gulnara', 'Kassymova', ''],
['gulnara.netaliyeva', 'Gulnara', 'Netaliyeva', ''],
['gulnara.saimassay', 'Gulnara', 'Saimassay', ''],
['gulnaz.toguzbayeva', 'Gulnaz', 'Toguzbayeva', ''],
['gulnura.arzanbekova', 'Gulnura', 'Arzanbekova', ''],
['gulsara.sadyrbekova', 'Gulsara', 'Sadyrbekova', ''],
['gulsim.darkenbayeva', 'Gulsim', 'Darkenbayeva', ''],
['gulsim.rysbayeva', 'Gulsim', 'Rysbayeva', ''],
['gulzha.orazgali', 'Gulzha', 'Orazgali', ''],
['gulzhaina.nurmanova', 'Gulzhaina', 'Nurmanova', ''],
['gulzhazira.kanashayeva', 'Gulzhazira', 'Kanashayeva', ''],
['gulzhaіna.kassymova', 'Gulzhaіna', 'Kassymova', ''],
['guncham.nurakhunova', 'Guncham', 'Nurakhunova', ''],
['idayatulla.adikhanov', 'Idayatulla', 'Adikhanov', ''],
['idrissmusa.garba', 'IdrissMusa', 'Garba', ''],
['igibek.koishybayev', 'Igibek', 'Koishybayev', ''],
['ildys.akhmedova', 'Ildys', 'Akhmedova', ''],
['ilyas.imachikov', 'Ilyas', 'Imachikov', ''],
['indira.kutbanbayeva', 'Indira', 'Kutbanbayeva', ''],
['ingkar.yersari', 'Ingkar', 'Yersari', ''],
['inkar.shoganova', 'Inkar', 'Shoganova', ''],
['inzura.nurshanova', 'Inzura', 'Nurshanova', ''],
['jekho.song', 'Jekho', 'Song', ''],
['jeongok.lim', 'Jeongok', 'Lim', ''],
['jomart.aldamuratov', 'Jomart', 'Aldamuratov', ''],
['kalzhan.rakish', 'Kalzhan', 'Rakish', ''],
['kamila.orynbekova', 'Kamila', 'Orynbekova', ''],
['kanat.khazimov', 'Kanat', 'Khazimov', ''],
['kanat.syzdykov', 'Kanat', 'Syzdykov', ''],
['katira.karymsakova', 'Katira', 'Karymsakova', ''],
['khafiza.ordabekova', 'Khafiza', 'Ordabekova', ''],
['khaled.mohamad', 'Khaled', 'Mohamad', ''],
['khurshida.patullayeva', 'Khurshida', 'Patullayeva', ''],
['kuanysh.yergaliyev', 'Kuanysh', 'Yergaliyev', ''],
['kuanyshbek.mamay', 'Kuanyshbek', 'Mamay', ''],
['kuanyshbek.zhubandykov', 'Kuanyshbek', 'Zhubandykov', ''],
['kuatkan.zhensikbayev', 'Kuatkan', 'Zhensikbayev', ''],
['kudaiberdi.bagasharov', 'Kudaiberdi', 'Bagasharov', ''],
['kulyan.konarbayeva', 'Kulyan', 'Konarbayeva', ''],
['kumis.zhaiykbay', 'Kumis', 'Zhaiykbay', ''],
['kundyzay.omirzak', 'Kundyzay', 'Omirzak', ''],
['kuralay.apseit', 'Kuralay', 'Apseit', ''],
['kurmangazy.kongratbayev', 'Kurmangazy', 'Kongratbayev', ''],
['kurmangazy.sadykbekov', 'Kurmangazy', 'Sadykbekov', ''],
['kymbat.smakova', 'Kymbat', 'Smakova', ''],
['larissa.bazarbayeva', 'Larissa', 'Bazarbayeva', ''],
['laura.beisekulova', 'Laura', 'Beisekulova', ''],
['lazzat.nuraliyeva', 'Lazzat', 'Nuraliyeva', ''],
['leila.mirzoyeva', 'Leila', 'Mirzoyeva', ''],
['lyaila.iskakova', 'Lyaila', 'Iskakova', ''],
['lyazzat.atymtayeva', 'Lyazzat', 'Atymtayeva', ''],
['madi.mrzabay', 'Madi', 'Mrzabay', ''],
['madina.ashirimbetova', 'Madina', 'Ashirimbetova', ''],
['madina.kalaman', 'Madina', 'Kalaman', ''],
['madina.kenzhegaranova', 'Madina', 'Kenzhegaranova', ''],
['madina.kossay', 'Madina', 'Kossay', ''],
['madina.ostemirova', 'Madina', 'Ostemirova', ''],
['madina.suleimen', 'Madina', 'Suleimen', ''],
['magzhan.kairanbay', 'Magzhan', 'Kairanbay', ''],
['magzhan.zhailau', 'Magzhan', 'Zhailau', ''],
['maigul.abilova', 'Maigul', 'Abilova', ''],
['maira.zholshayeva', 'Maira', 'Zholshayeva', ''],
['makhinur.atakeyeva', 'Makhinur', 'Atakeyeva', ''],
['maksat.aitbek', 'Maksat', 'Aitbek', ''],
['maksat.galiyev', 'Maksat', 'Galiyev', ''],
['maksat.maratov', 'Maksat', 'Maratov', ''],
['maksut.gatiat', 'Maksut', 'Gatiat', ''],
['marat.urmanov', 'Marat', 'Urmanov', ''],
['marat.yestemirov', 'Marat', 'Yestemirov', ''],
['marekmarian.pionka', 'Marek', 'Marian Pionka', ''],
['mariya.li', 'Mariya', 'Li', ''],
['mariya.yesselevapionka', 'Mariya', 'YesselevaPionka', ''],
['marziya.shaikym', 'Marziya', 'Shaikym', ''],
['maulen.abdrakhmanov', 'Maulen', 'Abdrakhmanov', ''],
['maxat.baitugulov', 'Maxat', 'Baitugulov', ''],
['mehmet.tas', 'Mehmet', 'Tas', ''],
['meirambek.zhaparov', 'Meirambek', 'Zhaparov', ''],
['meiramgul.yesbossyn', 'Meiramgul', 'Yesbossyn', ''],
['meirbek.slyamkhan', 'Meirbek', 'Slyamkhan', ''],
['meirman.syzdykbayev', 'Meirman', 'Syzdykbayev', ''],
['menkebanu.nursultan', 'Menkebanu', 'Nursultan', ''],
['meraryslan.meraliyev', 'Meraryslan', 'Meraliyev', ''],
['meriyem.syurmen', 'Meriyem', 'Syurmen', ''],
['meruyert.baimukhambetova', 'Meruyert', 'Baimukhambetova', ''],
['meruyert.birleskyzy', 'Meruyert', 'Birleskyzy', ''],
['mohammedalaafadhil.alhadeethi', 'MohammedAlaaFadhil', 'Al-Hadeethi', ''],
['moldir.malshy', 'Moldir', 'Malshy', ''],
['moldir.sanatkyzy', 'Moldir', 'Sanatkyzy', ''],
['mukhametzhan.seitzhapparuly', 'Mukhametzhan', 'Seitzhapparuly', ''],
['mukhtar.amirkumar', 'Mukhtar', 'Amirkumar', ''],
['mukhtar.bimurat', 'Mukhtar', 'Bimurat', ''],
['mukhtar.ismagulov', 'Mukhtar', 'Ismagulov', ''],
['murat.turbek', 'Murat', 'Turbek', ''],
['mustafa.abdulbakiogly', 'Mustafa', 'Abdulbakiogly', ''],
['n/a', 'N', 'A', ''],
['nailya.uteubayeva', 'Nailya', 'Uteubayeva', ''],
['nargiza.tazabekova', 'Nargiza', 'Tazabekova', ''],
['nauryzbay.sapargali', 'Nauryzbay', 'Sapargali', ''],
['nazarali.aitjanov', 'Nazarali', 'Aitjanov', ''],
['nazerke.makhsatbekkyzy', 'Nazerke', 'Makhsatbekkyzy', ''],
['nazerke.sultanova', 'Nazerke', 'Sultanova', ''],
['nazgul.abdrakhynova', 'Nazgul', 'Abdrakhynova', ''],
['nazym.kenges', 'Nazym', 'Kenges', ''],
['nazym.sergazy', 'Nazym', 'Sergazy', ''],
['nazym.shaikhina', 'Nazym', 'Shaikhina', ''],
['nuraly.otegen', 'Nuraly', 'Otegen', ''],
['nuray.dauletkhan', 'Nuray', 'Dauletkhan', ''],
['nurbek.sagyndyk', 'Nurbek', 'Sagyndyk', ''],
['nurbol.aidarbayev', 'Nurbol', 'Aidarbayev', ''],
['nurbol.sabitov', 'Nurbol', 'Sabitov', ''],
['nurdaulet.shynarbek', 'Nurdaulet', 'Shynarbek', ''],
['nurgissa.yessirkegenov', 'Nurgissa', 'Yessirkegenov', ''],
['nuri.balta', 'Nuri', 'Balta', ''],
['nuri.gassanov', 'Nuri', 'Gassanov', ''],
['nurlan.dairbekov', 'Nurlan', 'Dairbekov', ''],
['nurlan.ismailov', 'Nurlan', 'Ismailov', ''],
['nurmukhammed.abeuov', 'Nurmukhammed', 'Abeuov', ''],
['nursat.bakyt', 'Nursat', 'Bakyt', ''],
['nursezim.salamat', 'Nursezim', 'Salamat', ''],
['nurzhainar.rassayeva', 'Nurzhainar', 'Rassayeva', ''],
['nurzhan.mukashev', 'Nurzhan', 'Mukashev', ''],
['olzhas.umbetbayev', 'Olzhas', 'Umbetbayev', ''],
['omirbek.maishykov', 'Omirbek', 'Maishykov', ''],
['orynay.zhubayeva', 'Orynay', 'Zhubayeva', ''],
['oxana.syurmen', 'Oxana', 'Syurmen', ''],
['perizat.azhiyeva', 'Perizat', 'Azhiyeva', ''],
['perizat.yessenova', 'Perizat', 'Yessenova', ''],
['qaswabintefirdous.wani', 'Qaswa', 'Binte-Firdous Wani', ''],
['rabiya.seiit', 'Rabiya', 'Seiit', ''],
['rabiya.yaylaci', 'Rabiya', 'Yaylaci', ''],
['raikhan.abnassyrova', 'Raikhan', 'Abnassyrova', ''],
['ramis.akhmedov', 'Ramis', 'Akhmedov', ''],
['rmkul.barkibayeva', 'Rmkul', 'Barkibayeva', ''],
['roza.kalikbergenova', 'Roza', 'Kalikbergenova', ''],
['roza.orazalina', 'Roza', 'Orazalina', ''],
['roza.tulegenova', 'Roza', 'Tulegenova', ''],
['roza.zhilkibayeva', 'Roza', 'Zhilkibayeva', ''],
['ruslan.dochshanov', 'Ruslan', 'Dochshanov', ''],
['sabina.sarsembayeva', 'Sabina', 'Sarsembayeva', ''],
['saltanat.karimsattar', 'Saltanat', 'Karimsattar', ''],
['saltanat.nurgaliyeva', 'Saltanat', 'Nurgaliyeva', ''],
['samat.maxutov', 'Samat', 'Maxutov', ''],
['samgat.yermekbayev', 'Samgat', 'Yermekbayev', ''],
['sandugash.abdyrakhimova', 'Sandugash', 'Abdyrakhimova', ''],
['sanzhar.organov', 'Sanzhar', 'Organov', ''],
['satilmis.yilmaz', 'Satilmis', 'Yilmaz', ''],
['saule.narenova', 'Saule', 'Narenova', ''],
['saule.tulepova', 'Saule', 'Tulepova', ''],
['saule.zhardayeva', 'Saule', 'Zhardayeva', ''],
['saulet.borambayeva', 'Saulet', 'Borambayeva', ''],
['saya.baisultanova', 'Saya', 'Baisultanova', ''],
['selcuk.cankurt', 'Selcuk', 'Cankurt', ''],
['sergei.golunov', 'Sergei', 'Golunov', ''],
['shakhizat.matayev', 'Shakhizat', 'Matayev', ''],
['shakhnazarsultan.manbay', 'Shakhnazar', 'Sultan Manbay', ''],
['shatlyk.amanov', 'Shatlyk', 'Amanov', ''],
['shattygul.yerkhozhina', 'Shattygul', 'Yerkhozhina', ''],
['shokhrukh.shakirov', 'Shokhrukh', 'Shakirov', ''],
['sholpan.kuandykova', 'Sholpan', 'Kuandykova', ''],
['sholpan.sabidolda', 'Sholpan', 'Sabidolda', ''],
['shynar.auyelbekova', 'Shynar', 'Auyelbekova', ''],
['shynggys.zhanbolatuly', 'Shynggys', 'Zhanbolatuly', ''],
['shyngys.adilkhan', 'Shyngys', 'Adilkhan', ''],
['slushash.tulenova', 'Slushash', 'Tulenova', ''],
['sufyan.mustafa', 'Sufyan', 'Mustafa', ''],
['sumeyra.varol', 'Sumeyra', 'Varol', ''],
['sumeyrabetul.polat', 'SumeyraBetul', 'Polat', ''],
['sunggat.amangeldiyev', 'Sunggat', 'Amangeldiyev', ''],
['suraiyo.raziyeva', 'Suraiyo', 'Raziyeva', ''],
['svetlana.lukashova', 'Svetlana', 'Lukashova', ''],
['svetlana.shuinshina', 'Svetlana', 'Shuinshina', ''],
['symbat.moldabekova', 'Symbat', 'Moldabekova', ''],
['syndar.zhenis', 'Syndar', 'Zhenis', ''],
['tahir.muhammad', 'Tahir', 'Muhammad', ''],
['talshyn.baimuldanova', 'Talshyn', 'Baimuldanova', ''],
['taukekhan.mustakhov', 'Taukekhan', 'Mustakhov', ''],
['torgyn.ayazbay', 'Torgyn', 'Ayazbay', ''],
['toty.aitzhan', 'Toty', 'Aitzhan', ''],
['ualikhan.sadyk', 'Ualikhan', 'Sadyk', ''],
['ulpetay.niyetbay', 'Ulpetay', 'Niyetbay', ''],
['ulykbek.amir', 'Ulykbek', 'Amir', ''],
['ulzhalgas.abdirova', 'Ulzhalgas', 'Abdirova', ''],
['ulzhan.mukasheva', 'Ulzhan', 'Mukasheva', ''],
['ulzhan.urazaliyeva', 'Ulzhan', 'Urazaliyeva', ''],
['usame.ozyurt', 'Usame', 'Ozyurt', ''],
['yakup.doganay', 'Yakup', 'Doganay', ''],
['yedilkhan.amirgaliyev', 'Yedilkhan', 'Amirgaliyev', ''],
['yelnur.alimova', 'Yelnur', 'Alimova', ''],
['yelnur.mutaliyev', 'Yelnur', 'Mutaliyev', ''],
['yelnura.autalipova', 'Yelnura', 'Autalipova', ''],
['yerbol.baigarayev', 'Yerbol', 'Baigarayev', ''],
['yerbol.bugybayev', 'Yerbol', 'Bugybayev', ''],
['yergali.issakulov', 'Yergali', 'Issakulov', ''],
['yerimbet.aitzhanov', 'Yerimbet', 'Aitzhanov', ''],
['yerkebulan.akberdiyev', 'Yerkebulan', 'Akberdiyev', ''],
['yerkebulan.sairambay', 'Yerkebulan', 'Sairambay', ''],
['yerkegali.raibek', 'Yerkegali', 'Raibek', ''],
['yerkin.shaimerdenov', 'Yerkin', 'Shaimerdenov', ''],
['yerkin.zhaksylykov', 'Yerkin', 'Zhaksylykov', ''],
['yerlan.sharipov', 'Yerlan', 'Sharipov', ''],
['yernar.akhmetbek', 'Yernar', 'Akhmetbek', ''],
['yershat.sapazhanov', 'Yershat', 'Sapazhanov', ''],
['yerzhan.abdramanov', 'Yerzhan', 'Abdramanov', ''],
['yerzhan.chongarov', 'Yerzhan', 'Chongarov', ''],
['yerzhan.syzdykov', 'Yerzhan', 'Syzdykov', ''],
['yessengazy.turalin', 'Yessengazy', 'Turalin', ''],
['yessengul.kap', 'Yessengul', 'Kap', ''],
['zanipa.bekmambetova', 'Zanipa', 'Bekmambetova', ''],
['zarina.kaulenova', 'Zarina', 'Kaulenova', ''],
['zhadyra.zhalgassova', 'Zhadyra', 'Zhalgassova', ''],
['zhainagul.duisebekova', 'Zhainagul', 'Duisebekova', ''],
['zhalgas.serimbetov', 'Zhalgas', 'Serimbetov', ''],
['zhamilya.yeleussizova', 'Zhamilya', 'Yeleussizova', ''],
['zhanagul.turumbetova', 'Zhanagul', 'Turumbetova', ''],
['zhanar.mukash', 'Zhanar', 'Mukash', ''],
['zhanbolat.khumarkhan', 'Zhanbolat', 'Khumarkhan', ''],
['zhanel.sabirova', 'Zhanel', 'Sabirova', ''],
['zhanel.shaikhy', 'Zhanel', 'Shaikhy', ''],
['zhangyl.abilbek', 'Zhangyl', 'Abilbek', ''],
['zhaniya.medeuova', 'Zhaniya', 'Medeuova', ''],
['zhansaya.zhengis', 'Zhansaya', 'Zhengis', ''],
['zharkynay.ongarova', 'Zharkynay', 'Ongarova', ''],
['zhasdauren.duisebekov', 'Zhasdauren', 'Duisebekov', ''],
['zhassulan.akhmetov', 'Zhassulan', 'Akhmetov', ''],
['zholdasbek.mambetov', 'Zholdasbek', 'Mambetov', ''],
['zhuldyz.nurzhanova', 'Zhuldyz', 'Nurzhanova', ''],
['zhumaniyaz.mamatnabiyev', 'Zhumaniyaz', 'Mamatnabiyev', ''],
['ziyada.kozhakhmetova', 'Ziyada', 'Kozhakhmetova', ''],
['zukhra.syzdykova', 'Zukhra', 'Syzdykova', '']]

        for username in usernames:
            if User.objects.filter(username=username[0]).exists():
                self.stdout.write(self.style.WARNING(f'User {username[0]} already exists.'))
            else:
                User.objects.create_user(username=username[0], password='teacherPassword#', first_name=username[1], last_name=username[2], is_staff=True)
                self.stdout.write(self.style.SUCCESS(f'User {username[0]} created successfully.'))

