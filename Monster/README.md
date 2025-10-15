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

---

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
  "MonsterType": 0,     // Loại quái (0=thường, 11=Golden)
  "HP": 30,            // Máu
  "MP": 0,             // Mana
  "DmgMin": 1,         // Damage tối thiểu
  "DmgMax": 4,         // Damage tối đa
  "Def": 1,            // Defense vật lý
  "mDe": 2,            // Magic Defense
  "AttRate": 8,        // Tỷ lệ đánh trúng
  "BloRate": 1,        // Tỷ lệ block
  "DetractPct": 0,     // Phần trăm giảm damage
  "SumderArmorPct": 0, // Phần trăm xuyên giáp
  "Ran": 2,            // Tầm đánh
  "AT": "0",           // Attack Type
  "AR": 1,             // Attack Range
  "VR": 6,             // View Range
  "MoSpeed": 400,      // Tốc độ di chuyển
  "AtSpeed": 1800,     // Tốc độ tấn công
  "Regen": 12,         // Tốc độ hồi máu
  "Att": 2,            // Attribute
  "IT": 120,           // Intelligence
  "MR": 20,            // Magic Resistance
  "MIL": 6,            // Magic Intelligence Level
  "SKI": 0,            // Skill
  "ICE": 0,            // Ice Resistance
  "POI": 0,            // Poison Resistance
  "LIG": 0,            // Lightning Resistance
  "FIR": 0,            // Fire Resistance
  "nExpPer": 100       // Phần trăm EXP
}
```

### Các loại MonsterType
- `0`: Quái vật thường
- `11`: Golden Boss
- Các giá trị khác: Boss đặc biệt

---

## 2. Golden Boss System

### 2.1 GoldenBOSS.json

**Mô tả**: Cấu hình chi tiết 89 loại Golden Boss khác nhau.

**Các loại Golden Boss**:
- Golden Baby Dragon (Level 10-32)
- Golden Goblin (Level 20-24)  
- Golden Rabbit (Level 30-39)
- Golden Dark Knight (Level 42-60)
- Golden Mermaid (Level 43-61)
- Golden Wizard King (Level 63-83)
- Golden Demon (Level 47-72)
- Golden Destroy Knight (Level 72-93)
- Golden Iron Wheel Warrior (Level 96-145)
- Golden Orc (Level 72-108)
- Golden Lone Step Demon (Level 82-84)
- Golden Dubu Yao (Level 85-130)
- Golden Fire Dragon King (Level 200)

**Ví dụ cấu hình**:
```json
{
  "Index": 68,
  "MonsterIndex": 542,
  "Rate": 1,
  "Name": "Golden Fire Dragon King",
  "Lvl": 200,
  "MonsterType": 11,
  "HP": 300000000,        // 300 triệu HP
  "MP": 0,
  "DmgMin": 5500,
  "DmgMax": 9000,
  "Def": 3000,
  "mDe": 0,
  "AttRate": 3000,
  "BloRate": 2000,
  "nExpPer": 100,
  "nDropID": 200          // ID drop tương ứng
}
```

### 2.2 Config_GoldenBossReffresh.json

**Mô tả**: Cấu hình vị trí spawn của Golden Boss.

**Cấu trúc**:
```json
{
  "RefreshID": 1,         // ID refresh point
  "BOSSID": 542,          // ID của boss
  "BossType": 1,          // Loại boss (0= GoldBoss , 1=WorldBoss , 2 = DungeonBoss,	//	InstanceBoss)
  "FreshLoc": "[1,7,76]", // Vị trí [map, x, y]
  "RandomRange": 1,       // Phạm vi spawn ngẫu nhiên
  "Reborn": 0             // Thời gian respawn (0=theo lịch)
}
```

**Các vị trí spawn hiện tại**:
- Map 1 (Lorencia): Các tọa độ khác nhau
- Map 9: Nhiều điểm spawn với RandomRange 5

### 2.3 BOSSTimeFresh.json

**Mô tả**: Cấu hình thời gian xuất hiện của Golden Boss theo lịch.

**Cấu trúc**:
```json
{
  "RefreshID": 1,
  "sServerLine": "[0,2]",     // Server lines
  "Week": "[5]",              // Ngày trong tuần (0=CN, 1=T2, ..., 6=T7)
  "Time": 11,                 // Giờ xuất hiện (24h format)
  "BossID": "[542,221]",      // Danh sách boss ID
  "FreshType": 1,             // Loại spawn (1=theo thời gian)
  "RefrshNotice": "Golden Fire Dragon King xuất hiện tại Ice Wind Valley!"
}
```

**Lịch spawn hiện tại**:
- **Thứ 6, 11:00**: Golden Fire Dragon King tại Ice Wind Valley
- **Thứ 6 & Chủ nhật, 20:00**: Golden Fire Dragon King tại nhiều map

---

## 3. Drop System

### 3.1 GoldenBossDropRate.json

**Mô tả**: Cấu hình tỷ lệ drop của Golden Boss (200 entries).

**Cấu trúc**:
```json
{
  "GoldenDropID": 1,        // ID drop tương ứng với nDropID
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

### 3.2 GoldenBOSSEquipDrop.json

**Mô tả**: Cấu hình equipment drop chi tiết với 427 entries.

**Các loại equipment**:
- Weapons: 10xxx series
- Armor: 11xxx-21xxx series
- Accessories: 12xxx, 14xxx, 15xxx, 16xxx series
- Special Items: 23xxx series

**Drop Level Ranges**:
- Level 20-210: Các equipment khác nhau
- Higher levels: Better equipment với stats cao hơn

---

## 4. Regular Monster Drop System

### 4.1 MonsterItemDropRate.json
**Mô tả**: Tỷ lệ drop item của quái vật thường (1 dòng dài, cần format để đọc).

### 4.2 MonsterDropAdd.json
**Mô tả**: Drop bổ sung cho các quái vật (1 dòng dài, cần format để đọc).

### 4.3 MonsterInSceneAttr.json
**Mô tả**: Thuộc tính đặc biệt của quái trong scene cụ thể.

---

## 5. Boss Folder

### Mô tả
Chứa cấu hình drop đặc biệt cho các boss cụ thể:

- **boss_huang_jin_huo_long_wang.json**: Golden Fire Dragon King drops
- **boss_treasure_map_advanced.json**: Advanced Treasure Map boss
- **boss_treasure_map_normal.json**: Normal Treasure Map boss  
- **boss_zhi_zhu.json**: Spider boss

**Format**:
```json
[
  {"Id": 22015, "Quantity": 1, "Rate": 10},
  {"Id": 24013, "Quantity": 1, "Rate": 10},
  {"Id": 24014, "Quantity": 1, "Rate": 10}
]
```

---

## 6. Hướng dẫn chỉnh sửa (Modification Guide)

### 6.1 Thêm Golden Boss mới
1. Thêm entry vào `GoldenBOSS.json` với Index mới
2. Cấu hình drop trong `GoldenBossDropRate.json`
3. Thêm vị trí spawn trong `Config_GoldenBossReffresh.json`
4. Cấu hình thời gian trong `BOSSTimeFresh.json` (nếu cần)

### 6.2 Chỉnh sửa thống kê quái
- Sửa file `MonsterInfo.json`
- Tìm theo `Index` hoặc `Name`
- Chỉnh sửa các thuộc tính: HP, MP, Damage, Defense, etc.

### 6.3 Chỉnh sửa drop rate
- Golden Boss: `GoldenBossDropRate.json`
- Regular monsters: `MonsterItemDropRate.json`
- Equipment drops: `GoldenBOSSEquipDrop.json`

### 6.4 Thay đổi thời gian spawn
- Sửa `BOSSTimeFresh.json`
- `Week`: [0-6] (0=Chủ nhật)
- `Time`: 0-23 (24h format)

---

## 7. Lưu ý quan trọng (Important Notes)

1. **Backup**: Luôn backup các file trước khi chỉnh sửa
2. **JSON Format**: Đảm bảo format JSON đúng cú pháp
3. **Index Unique**: Mỗi monster phải có Index duy nhất
4. **Drop ID Mapping**: nDropID trong GoldenBOSS.json phải tương ứng với GoldenDropID trong GoldenBossDropRate.json
5. **Server Restart**: Cần restart server sau khi thay đổi cấu hình
6. **Testing**: Test kỹ trên server test trước khi áp dụng production

---

## 8. Troubleshooting

### Lỗi thường gặp:
1. **Boss không spawn**: Kiểm tra BOSSTimeFresh.json và Config_GoldenBossReffresh.json
2. **Không drop item**: Kiểm tra nDropID mapping và drop rates
3. **Stats không đúng**: Kiểm tra MonsterInfo.json hoặc GoldenBOSS.json
4. **JSON Error**: Sử dụng JSON validator để kiểm tra cú pháp

### Debug Tips:
- Kiểm tra server logs để tìm lỗi cấu hình
- Sử dụng tools JSON formatter để kiểm tra file
- Test với một boss đơn giản trước khi cấu hình phức tạp

---

*Tài liệu được tạo tự động - Cập nhật lần cuối: $(date)*


============================================Note BY Pug============================
1, Thời gian theo BOSSTimeFresh
  "FreshType": 1, 
    1: theo tuần , giờ
    0: theo time reset : fai đọc config xem như nào
    