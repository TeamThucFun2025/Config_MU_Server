# Monster Configuration System Documentation

## Tổng quan (Overview)

Thư mục `Monster/` chứa tất cả các file cấu hình liên quan đến hệ thống quái vật trong game MU Server, bao gồm:
- Quái vật thường (Regular Monsters)
- Boss Golden (Golden Bosses)
- Hệ thống drop item
- Thời gian spawn và respawn

## Cấu trúc thư mục (Directory Structure)

```
Monster/
├── MonsterInfo.json              # Cấu hình quái vật chính
├── GoldenBOSS.json              # Cấu hình Golden Boss
├── Config_GoldenBossReffresh.json # Vị trí spawn Golden Boss
├── BOSSTimeFresh.json           # Thời gian spawn Boss
├── MonsterItemDropRate.json     # Tỷ lệ drop item của quái
├── MonsterDropAdd.json          # Drop bổ sung
├── MonsterInSceneAttr.json      # Thuộc tính quái trong scene
├── GoldenBossDropRate.json      # Tỷ lệ drop của Golden Boss
├── GoldenBOSSEquipDrop.json     # Equipment drop của Golden Boss
└── boss/                        # Cấu hình boss đặc biệt
    ├── boss_huang_jin_huo_long_wang.json
    ├── boss_treasure_map_advanced.json
    ├── boss_treasure_map_normal.json
    └── boss_zhi_zhu.json
```

===================================================================================
## 1. MonsterInfo.json

### Mô tả
File cấu hình chính chứa thông tin của tất cả quái vật trong game (23,599 dòng).

### Cấu trúc dữ liệu
```json
{
  "Index": 3,           // ID duy nhất của quái
  "Rate": 1,            // Tỷ lệ spawn
  "Name": "Spider",     // Tên quái
  "Lvl": 2,            // Level
  "MonsterType": 0,     // Loại quái (0=thường, 11=Golden, 12=Kundun)
  "HP": 30,            // Máu
  "MP": 0,             // Mana
  "DmgMin": 1,         // Damage tối thiểu
  "DmgMax": 4,         // Damage tối đa
  "Def": 1,            // Defense vật lý
  "mDe": 2,            // Magic Defense
  "AttRate": 8,        // Tỷ lệ đánh trúng
  "BloRate": 1,        // Tỷ lệ né tránh
  "DetractPct": 0,     // Phần trăm giảm damage
  "SumderArmorPct": 0, // Phần trăm xuyên giáp
  "Ran": 2,            // Tầm đánh
  "AT": "0",           // Attack Type , set skill cho quái xem qua bảng skill, có thể sqet nhiều skill ( idskill1,idskill2,...)
  "AR": 1,             // Attack Range
  "VR": 6,             // View Range
  "MoSpeed": 400,      // Tốc độ di chuyển
  "AtSpeed": 1800,     // Tốc độ tấn công
  "Regen": 12,         // Thời gian hồi sinh đang là 12s
  "Att": 2,            // chỉ số attack thêm (chưa thấy dùng trong code, đã thêm vào thêm bao nhiêu điểm sát thương)
  "IT": 120,           // tỷ lệ rớt vật phẩm item
  "MR": 20,            // tỷ lệ rớt Zen
  "MIL": 6,            // Max item level
  "SKI": 0,            // Skill
  "ICE": 0,            // Ice Resistance
  "POI": 0,            // Poison Resistance
  "LIG": 0,            // Lightning Resistance
  "FIR": 0,            // Fire Resistance
  "nExpPer": 100       // tỉ lệ kinh nghiệm EXP
}
```
===================================END=============================================



===================================================================================
## 2. MonsterInSceneAttr.json

### Mô tả
File cấu hình Thuộc tính đặc biệt của quái trong scene cụ thể.
 ==> tóm lại dùng khi nào muốn tăng/giảm chỉ số chung cho quái cả scene đó cho nhanh 

### Cấu trúc dữ liệu
```json
{
    "Id": 1,  // ID của Scene (bản đồ, dungeon, event...)
    "ExpPct": 100,  // Tỉ lệ EXP mà quái cho (%)
    "DamageMinPct": 100, // Tỉ lệ % sát thương tối thiểu
    "DamageMaxPct": 100, // Tỉ lệ % sát thương tối đa
    "HpPct": 100,  // Tỉ lệ % HP của quái
    "DefPct": 100 // Tỉ lệ % phòng thủ
  },
```
===================================END=============================================



===================================================================================
## 3. MonsterItemDropRate.json

###Mô tả### : Cấu hình tỷ lệ drop % các loại vật phẩm theo LEVEL của monster để random theo mong muốn
              có thể cấu hình tối đa là 400 cấp, code mặc định 400 
            VD: ở cấp thấp thì chỉ được rơi vật phẩm khác k rơi đá hoặc skillbook
### Cấu trúc dữ liệu
```json
  {
    "MonsterLevel": 6,      //level của quái , file hiện tại mới định nghĩa đến 300 level sau này cần thì update thêm
    "SkillBook": 0.006223,  //tỷ lệ drop Sách kỹ năng (Skill Books), khi đọc vào nó sẽ mặc định được nhân 1.000.000
    "BlessingGems": 0.0,    //tỷ lệ drop Ngọc Chao (Blessing Gem), khi đọc vào nó sẽ mặc định được nhân 1.000.000
    "SoulGems": 0.0,        //tỷ lệ drop Ngọc Tâm Linh (Soul Gem), khi đọc vào nó sẽ mặc định được nhân 1.000.000
    "MayaGems": 0.0,        //tỷ lệ drop Ngọc Hỗn Nguyên / Ngọc Ma Dũng (Maya Gem), khi đọc vào nó sẽ mặc định được nhân 1.000.000
    "AnimaGems": 0.0,       //tỷ lệ drop Ngọc Sinh Mệnh (Life Gem), khi đọc vào nó sẽ mặc định được nhân 1.000.000
    "CreateGems": 0.0,      //tỷ lệ drop Ngọc Sáng Tạo (Creation Gem), khi đọc vào nó sẽ mặc định được nhân 1.000.000
    "Other": 0.993777,      //tỷ lệ drop Vật phẩm khác (Others), khi đọc vào nó sẽ mặc định được nhân 1.000.000
    "Pet": 0.0,             //tỷ lệ drop Thú nuôi (Pets – ví dụ: Panda, Skeleton Pet…), khi đọc vào nó sẽ mặc định được nhân 1.000.000
    "DropRate": 1.0         //tỷ lệ drop tổng
  }
```
===================================END=============================================


===================================================================================
## 4 MonsterDropAdd.json

###Mô tả### : Cấu hình tỷ lệ drop trang bị của Monster - cho equip

### Cấu trúc dữ liệu
```json
  {
    "nDropID": 1,         //ID của drop
    "tDropMap": "[301]",         //Danh sách bản đồ có thể rơi vật phẩm, [id,id,..]
    "tMonsterID": "[432,433,434,435,436,437,438,439,440,441,442,443]\n",         //Danh sách ID monster ở map này được rơi đồ
    "nMonLevMin": 1,         //Cấp độ thấp nhất của quái 
    "nMonLevMax": 150,         //Cấp độ tối đa của quái 
    "nPlayerMinLev": 1,         //Cấp độ tối thiểu của người chơi để nhận drop
    "nPlayerMaxLev": 400,         //Cấp độ tối đa của người chơi để nhận drop
    "nItemType": 2,         //Kiểu vật phẩm ( 1: ItemID (nếu là 1 thì sẽ lấy itemid bên dưới để rơi), 2: Nhóm IDgroup (sẽ random 1 trong nhóm nDropIndex cùng value ở file ItemInfo.json ))
    "nItemID": 2801,         // ID vật phẩm hoặc ID nhóm
    "nItemLevel": 2,         // Độ hiếm / cấp độ đặc biệt của item
    "nDropValue": 105,         //Giá trị rơi (Drop Value) sẽ lấy nDropValue/nDropBaseValue để xác định tỷ lệ rơi, tăng cao thì sẽ dễ rơi
    "nDropBaseValue": 1000000,         //Tỷ lệ cơ bản rơi vật phẩm (Drop Rate Base)
    "tQianghuaLev": "[-1]",         //Danh sách cấp độ cường hóa (+0 ~ +15)
    "tQianghuaPro": "[-1]",         //Xác suất xuất hiện các cấp cường hóa, tương ứng đúng theo giá trị của biến tQianghuaLev, khi rơi thì random 1 biến , chạy từ index 0 lên của biến này, biến random < tổng rate cộng lại thì dừng cho cường hóa cấp đó
    "tZhuoyueContent": "[-1]",         //danh sách số lượng dòng hoàn hảo (Excellent Option Count)
    "tZhuoyuePro": "[-1]",         //Tỷ lệ xuất hiện dòng hoàn hảo
    "tZhuijiaLev": "[-1]",         //Danh sách cấp độ cộng thêm (+4 ~ +28)
    "tZhuijiaPro": "[-1]",         //Tỷ lệ xuất hiện cấp cộng thêm, tương tự như các dòng trước
    "nLuckyPro": 0,         //Xác suất có dòng May Mắn (Luck: +5% chí mạng, +5% ghép ngọc thành công) 
    "nSkillPro": 0         //Xác suất có dòng Kỹ năng (Skill Option: vũ khí có skill)`
  },
```
===================================END=============================================







-------------------------GoldenBoss-------------------------------------------------------------------------------------------------------------------------

===================================================================================
## 5 GoldenBOSS.json 
###Mô tả### : Cấu hình Golden Boss
              Tương tự monsterinfo chỉ thêm 2 trường MonsterIndex là id monster 
              chỉnh lại các chỉ số mạnh hơn


### Cấu trúc dữ liệu
```json
{
    "Index": 1,                     //~
    "MonsterIndex": 3001,                       //id quái bên monsterinfo.json
    "Rate": 1,                      //~
    "Name": "Golden Baby Dragon",                       //~
    "Lvl": 10,                      //~
    "MonsterType": 11,                      //~
    "HP": 220000,                       //~
    "MP": 0,                        //~
    "DmgMin": 120,                      //~
    "DmgMax": 125,                      //~
    "Def": 45,                      //~
    "mDe": 0,                       //~
    "AttRate": 75,                      //~
    "BloRate": 30,                      //~
    "DetractPct": 0,                        //~
    "SumderArmorPct": 0,                        //~
    "Ran": 3,                       //~
    "AT": "0",                      //~
    "AR": 1,                        //~
    "VR": 7,                        //~
    "MoSpeed": 400,                     //~
    "AtSpeed": 1400,                        //~
    "Regen": 7200,                      //~
    "Att": 2,                       //~
    "IT": 10,                       //~
    "MR": 20,                       //~
    "MIL": 0,                       //~
    "SKI": 0,                       //~
    "ICE": 2,                       //~
    "POI": 2,                       //~
    "LIG": 2,                       //~
    "FIR": 2,                       //~
    "nExpPer": 100,                     //~
    "nDropID": 10                       //~ custom drop chỉ dùng boss
  }
```
===================================END=============================================


===================================================================================
## 6 GoldenBossDropRate.json
###Mô tả### : Cấu hình tỷ lệ drop của Golden Boss (200 entries).
              định nghĩa nhóm drop id cho file Goldenboss.json - nDropID


### Cấu trúc dữ liệu
```json
{
  "GoldenDropID": 1,        // ID drop tương ứng với nDropID file goldenboss.json
  "nMinDropNum": 1,         // Số lượng drop tối thiểu
  "nMaxDropNum": 2,         // Số lượng drop tối đa
  "EquipmentID1": 0,        // ID equipment 1
  "nEquipIDDropPro1": 0,    // Tỷ lệ drop equipment 1
  "EquipmentID2": 0,        // ID equipment 2
  "nEquipIDDropPro2": 0,    // Tỷ lệ drop equipment 2
  "EquipmentID3": 0,        // ID equipment 3
  "nEquipIDDropPro3": 0,    // Tỷ lệ drop equipment 3
  "BlessingGems": 10000,    // Tỷ lệ drop Blessing Gems 
  "SoulGems": 10000,        // Tỷ lệ drop Soul Gems
  "MayaGems": 10000,        // Tỷ lệ drop Maya Gems
  "AnimaGems": 10000,       // Tỷ lệ drop Anima Gems
  "CreateGems": 10000,      // Tỷ lệ drop Create Gems
  "Pet": 0,                 // Tỷ lệ drop Pet
  "SkillBook": 0,           // Tỷ lệ drop Skill Book
  "GoldBaseNum": 0          // Số gold cơ bản
}
```
===================================END=============================================



===================================================================================
## 7 GoldenBOSSEquipDrop.json
###Mô tả### : Cấu hình tỷ lệ drop của Golden Boss (200 entries). cho equip
              định nghĩa nhóm drop id cho file Goldenboss.json - nDropID

### Cấu trúc dữ liệu
```json
 {
    "Index": 1,                    // ID của vật phẩm rơi
    "ItemID": 17005,               // ID trang bị (tra trong file item_infor)
    "nDropLevel": 100,             // Tỷ lệ rơi (Drop Rate)
    "tQianghuaLev": "0",           // Danh sách cấp độ cường hóa
    "tQianghuaPro": "0",           // Tỷ lệ xuất hiện cấp cường hóa
    "tZhuoyueContent": "[0,1,2,3]",// Số lượng dòng thuộc tính hoàn hảo (Excellent Option Count)
    "tZhuoyuePro": "[0,70,20,10]", // Tỷ lệ xuất hiện các dòng hoàn hảo tương ứng (Excellent Probability)
    "tZhuijiaLev": "0",            // Danh sách cấp độ cộng thêm (Additional Level)
    "tZhuijiaPro": "0",            // Tỷ lệ xuất hiện cấp cộng thêm
    "nLuckyPro": 8,                // Xác suất có dòng May Mắn (Luck)
    "nSkillPro": 0                 // Xác suất có dòng Kỹ năng (Skill Option)
  },
```
===================================END=============================================



===================================================================================
## 8 BOSSTimeFresh.json
###Mô tả### : Cấu hình thời gian xuất hiện của Golden Boss theo lịch.
             
### Cấu trúc dữ liệu
```json
{
  "RefreshID": 1,              // tạo ra id index để gán
  "sServerLine": "[0,2]",     // Server lines, tức pk, nonpk , trade .. định nghĩa theo line này
  "Week": "[5]",              // Ngày trong tuần (0=CN, 1=T2, ..., 6=T7)
  "Time": 11,                 // Giờ xuất hiện (24h format) chỉ dùng cho FreshType là 1 giờ cố định  trong ngày của tuần
  "BossID": "[542,221]",      // Danh sách boss ID qua bossid ở file Config_GoldenBossReffresh.json lấy
  "FreshType": 1,             // 0：Resurrection Rebirth ->  Quái hồi sinh lại sau một khoảng thời gian cố định tính từ lúc chết
                               // 1 = Fixed Time Respawn -> Quái chỉ hồi sinh vào thời điểm nhất định trong ngày / theo timer chung của server.
  "RefrshNotice": "Golden Fire Dragon King xuất hiện tại Ice Wind Valley!"
}
```
===================================END=============================================



===================================================================================
## 8 Config_GoldenBossReffresh.json
###Mô tả### : Cấu hình thời gian xuất hiện của Golden Boss theo lịch.
             
### Cấu trúc dữ liệu
```json
 {
        "RefreshID": 1,  //id 
        "BOSSID": 542,   // bossid tướng ứng với bossid, hay id của monsterid
        "BossType": 1,   // 0: GoldenBoss 1: WorldBoss 2: DungeonBoss
        "FreshLoc": "[1,7,76]", // tọa độ idmap, X, Y
        "RandomRange": 1,       //phạm vi ngẫu nhiên khi spawn boss.
        "Reborn": 0             // thời gian hồi sinh, tính theo giây tính cho con boss theo kiểu FreshType=0 sau chết bao nhiêu lâu hồi sinh
    },
```

===================================END=============================================