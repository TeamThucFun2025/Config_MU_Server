# 📦 Items Folder Analysis - MU Online Game Server

This document provides a detailed breakdown of all files in the `Items/` directory for the MU Online game server configuration.

## 📊 File Overview

| File | Size | Lines | Description |
|------|------|-------|-------------|
| ItemInfo.json | 1.8MB | 101,403 | Master item database with all game items |
| ItemOptionInfo.json | 285KB | 15,025 | Item special options and attributes |
| ItemDropInfo.json | 18KB | 1,029 | Item drop rates from monsters |
| Box.json | 1.2KB | 53 | Treasure chest configurations |
| BlessingAngelLevel.json | 2.4KB | 120 | Blessing levels and effects |
| TitleInfo.json | 5.8KB | 1 (long) | Player title configurations |
| ItemSetInfo.json | 11KB | 696 | Item set configurations |
| Config_SocketItemOptionSet.json | 5.5KB | - | Socket item set options |
| Config_SocketItemOption.json | 8.1KB | - | Individual socket item options |
| TreasureChest.json | 1.8KB | - | Treasure chest references |
| ItemBuyMoney.json | 0B | 0 | Empty (potential item pricing config) |

## 📋 Detailed File Descriptions

### 1. ItemInfo.json
**Primary Function**: Comprehensive database of all game items
**Structure**: JSON array of item objects
**Key Fields**:
- `Id`: Unique item identifier
- `Name`: Item display name
- `Type`: Item category (weapon, armor, consumable, etc.)
- `ReqLvl`: Required level to use
- `Str`, `Agi`, `Vit`, `Ene`: Stat requirements
- `DmgMin`, `DmgMax`: Damage range for weapons
- `Def`: Defense value for armor
- `Value`: Base value/cost
- `DW`, `DK`, `ELF`, `MG`, `DL`, `SUM`, `MONK`: Class usability flags
#### cấu trúc
```json
 {
    "Id": 24512,
    "Name": "Golden Chest",
    "nDropIndex": 0, // định nghĩa dropid
    "Load": 1,       // 0: ko load lên, 1 load lên
    "Type": 22,      // là type trang bị ở ô nào
                      // enum class EItemType : int32_t
                      // {
                      // ITEM_TYPE_SWORDS = 1,           // Kiếm
                      // ITEM_TYPE_AXES = 2,              // Rìu  
                      // ITEM_TYPE_MACES = 3,             // Vũ khí cùn (Gậy/Chùy)
                      // ITEM_TYPE_SPEARS = 4,            // Giáo
                      // ITEM_TYPE_BOWS = 5,              // Cung
                      // ITEM_TYPE_CROSSBOWS = 6,         // Nỏ
                      // ITEM_TYPE_BOWARROW = 7,          // Mũi tên cho cung
                      // ITEM_TYPE_CROSSBOW_ARROW = 8,   // Mũi tên cho nỏ
                      // ITEM_TYPE_STAFFS = 9,            // Gậy phép

                      // ITEM_TYPE_SHIELDS = 10,          // Khiên
                      // ITEM_TYPE_HELMS = 11,            // Mũ
                      // ITEM_TYPE_ARMORS = 12,           // Áo giáp
                      // ITEM_TYPE_PANTS = 13,            // Quần
                      // ITEM_TYPE_GLOVES = 14,           // Găng tay
                      // ITEM_TYPE_BOOTS = 15,            // Giày
                      // ITEM_TYPE_NECKLACE = 16,        // Dây chuyền
                      // ITEM_TYPE_RINGS = 17,            // Nhẫn

                      // ITEM_TYPE_WINGS = 18,            // Cánh
                      // ITEM_TYPE_CAPE = 19,             // Áo choàng
                      // ITEM_TYPE_GUARD = 20,            // Bảo vệ (Guardian)

                      // ITEM_TYPE_SKILL_BOOKS = 21,      // Sách kỹ năng
                      // ITEM_TYPE_CONSUMABLES = 22,      // Vật phẩm tiêu hao
                      // ITEM_TYPE_PET = 23,              // Thú cưng
                      // ITEM_TYPE_MOUNTS = 24,           // Cưỡi thú
                      // ITEM_TYPE_SPLINTER = 25,        // Mảnh vỡ (Fragment)
                      // ITEM_TYPE_NOT_USE_CONSUMABLES = 26,  // Vật phẩm tiêu hao không sử dụng được

                      // ITEM_DARKLORD_SCEPTER = 27,      // Quyền trượng của Dark Lord
                      // ITEM_SUMMONER_BOOK = 28,         // Sách thế giới khác của Summoner
                      // ITEM_SUMMONER_STAFF = 29,        // Gậy phép của Summoner
                      // };
    "Discard": 1,   // Có thể bỏ nó đi được không? 0: có , 1: ko
    "CanSell": 0,   // ban shop npc 0: ko , 1: có
    "Stack": 99,    // có thể gồng chồng tối đa bao nhiêu
    "IsDoubleOwn": 0, //// Hai tay: 0.Vũ khí một tay 1.Vũ khí hai tay
    "Drop": 0,         //*tính năng thả vật phẩm: 1: cho drop, 0: ko drop
    "DropRate": 100.0, // tỷ lệ drop
    "DropLvl": 0,      //  *Drop Level(Item Number 0-12, 14-15)，Minimum Monster Level0-255
    "DW": 1,           // class nào có thể dùng
    "DK": 1,
    "ELF": 1,
    "MG": 1,
    "DL": 1,
    "SUM": 1,
    "MONK": 1,
    "Slot": -1,     //vi tri ô trang bị
    "Skill": 0,     // kill theo vũ khí
    "X": 1,         // ô chứa vật phẩm sẽ chiến theo X   
    "Y": 1,         // ô chứa vật phẩm sẽ chiến theo Y
    "Opt": 0,       //Option: = giá trị mô tả các dòng thuộc tính đặc biệt trên item (normal, excellent, socket, ancient).
    "CanDropStrength": 0, /// Does it drop enhancement level
    "Grade": 0,             // Mức thẩm định Thiết bị hạng thấp, hạng cao
    "Value": 0,             // giá trị thêm, phụ thuộc theo từng slot mà sử dụng
    "DmgMin": 0,            //weapon dame min
    "DmgMax": 0,            //weapon dame max
    "Def": 0,                //Weapon Defense
    "DefRate": 0,           // Weapon Defense rate
    "AttackSpeed": 0,       // Attack Speed(Weapon/Gauntlet)
    "Dur": 0,               //Item Maximum Durability : độ bền trang bị
    "MagDmg": 0,             // Magic Damage
    "MagicAttackBFB": 0,     //  Increases Magic Attack Power by percentage
    "CurseAttackBFB": 0,    //	Increases Curse Attack by percentage
    "EagleAttackBFB": 0,    
    "OptionBase": "",       //// Thuộc tính cơ bản
    "Quantity": 1,          //Current Item Quantity
    "BaseBuyMoney": 100,    //Base Purchase Price Value from Configuration Table，No Need to Display
    "ReqLvl": 0,            //// *Required Level to Equip
    "Str": 0,
    "Agi": 0,
    "Vit": 0,
    "Ene": 0,
    "Com": 0,
    "StrUp": 0,
    "AgiUp": 0,
    "VitUp": 0,
    "EneUp": 0,
    "ComUp": 0,
    "Is380": 0,
    "kit": 0,   //// Thiết bị có cùng affixid
    "nSetEquipID": 0, //// SetID
    "UseMethod": "UseItemTreasureBox", //Method open box hoặc sử dụng một hàm riêng, có thể config để mở quà box
    "CanDropLucky": 0,  //Does it drop Luck attribute
    "Live": 0,
    "Sealed": 0
  },
```


### 2. ItemOptionInfo.json
**Primary Function**: Special item attributes and bonuses
**Structure**: JSON array of option configurations
**Key Fields**:
- `Index`: Option identifier
- `OptionType`: Category of option
- `Name`: Display name (Vietnamese)
- `Rate`: Probability/rate of occurrence
- `Property`: Affected stat property
- `Value0`-`Value16`: Numerical values for the option level
```json
{
    "Index": 1,     //index
    "OptionType": 7, 
                            //     enum class EItemOptionType : int32_t
                            // {
                            // 	ITEM_OPTION_TYPE_INVALID					= 0,
                            // 	ITEM_OPTION_TYPE_EXCELLENCE_WEAPON          = 1,	    // Excellent Weapon
                            // 	ITEM_OPTION_TYPE_EXCELLENCE_ARMOR_RINGS     = 2,		// Excellent Armor Ring
                            // 	ITEM_OPTION_TYPE_EXCELLENCE_WING			= 3,		// Excellent Wings
                            // 	ITEM_OPTION_TYPE_REGENERATION_WEAPON		= 4,		// Rebirth Weapon
                            // 	ITEM_OPTION_TYPE_REGENERATION_STAFFS		= 5,		// Rebirth Staff Weapons
                            // 	ITEM_OPTION_TYPE_REGENERATION_ARMOR			= 6,		// Rebirth Armor 
                            // 	ITEM_OPTION_TYPE_380						= 7,		// 380 Item
                            // 	ITEM_OPTION_TYPE_EXCELLENCE_WEAPON_STAFFS   = 8,		// Excellent Staff Weapons
                            // 	ITEM_OPTION_TYPE_EXCELLENCE_PA_NECKLACE     = 9,		// Excellent Physical Attack Necklace 
                            // 	ITEM_OPTION_TYPE_SET						= 10,		// Set 
                            // 	ITEM_OPTION_TYPE_EXCELLENCE_MA_NECKLACE		= 11,		// Excellent Magic Attack Necklace 
                            // };
    "Name": "Tỷ lệ tấn công người tăng +10", //name mô tả chỉ số
    "DisplayPos": 0,                         //
    "Remark": "",
    "Method": "",                           //method callback tùy item tinh chỉnh thuộc tính
    "Rate": 25,                             ////Xác suất xảy ra
    "ReqLevel": 0,
    "LevelMax": 0,
    "Property": "21",                       //EntityProp là tất cả các dòng thuộc tính của player 192
    "Value0": 10,
    "Value1": 0,
    "Value2": 0,
    "Value3": 0,
    "Value4": 0,
    "Value5": 0,
    "Value6": 0,
    "Value7": 0,
    "Value8": 0,
    "Value9": 0,
    "Value10": 0,
    "Value11": 0,
    "Value12": 0,
    "Value13": 0,
    "Value14": 0,
    "Value15": 0,
    "Value16": 0
  }
```



### 3. ItemDropInfo.json
**Primary Function**: Monster drop rate configurations
**Structure**: JSON array of drop rate entries
**Key Fields**:
- `ItemIndex`: Reference to ItemInfo.json
- `SceneID`: Game scene/map identifier
- `MonsterIndex`: Monster identifier
- `DropRate`: Probability of drop (higher = more common)

### 4. Box.json
**Primary Function**: Treasure chest item configurations
**Structure**: JSON array of box definitions
**Key Fields**:
- `BoxID`: Unique chest identifier
- `BoxName`: Display name (e.g., "Golden Treasure Chest")
- `BoxItems`: Array of item IDs contained
- `BoxItemsRate`: Drop rates for each item
- `NumLimit`: Maximum number of items from this chest
- `Rows`    : Số ô hành trang cần có để mở rương (nếu không đủ chỗ thì không cho mở)

### 5. BlessingAngelLevel.json
**Primary Function**: Blessing system level configurations
**Structure**: JSON array of blessing levels
**Key Fields**:
- `id`: Blessing identifier
- `level`: Blessing level
- `affected_Item_id`: Items affected by this blessing
- `rate`: Activation rate
- `attr_id`: Attribute ID being modified
- `attr_value`: Modification value
- `name`: Display name (Vietnamese)

{
    "id": 1,   //id
    "level": 1, //Level
    "affected_Item_id": "[10039,14027,12020]",
    "rate": 50,     // Cơ hội nâng cấp %
    "attr_id": 64,  // AttributeID 
    "attr_value": 10, // Attribute Value
    "name": "Tăng sát thương +10%"
  }


### 6. TitleInfo.json
**Primary Function**: Player title system configurations
**Structure**: JSON array of title definitions (single-line format)
**Key Fields**:
- `nTitleID`: Title identifier
- `nTitleName`: Title display name
- `nTitleValidityDay`: Duration in days
- `lTitleProIDList`: List of affected properties
- `lTitleProNumList`: Property modification values

### 7. ItemSetInfo.json
**Primary Function**: Item set bonus configurations
**Structure**: JSON array of set definitions
**Key Fields**:
- `Index`: Set identifier
- `Name`: Set display name (Vietnamese)
- `AllSet`: Array of item IDs in the set
- `Option1`-`Option10`: Set bonus options
- `FullOption`: Full set bonus properties

### 8. Config_SocketItemOptionSet.json
**Primary Function**: Socket gem combination effects
**Structure**: JSON array of socket set configurations
**Key Fields**:
- `Id`: Set identifier
- `Type`: Socket type
- `Name`: Effect description (Vietnamese)
- `Rate`: Activation rate
- `Value`: Effect value
- `Socket1`-`Socket5`: Required socket combinations

### 9. Config_SocketItemOption.json
**Primary Function**: Individual socket gem effects
**Structure**: JSON array of socket option configurations
**Key Fields**:
- `Id`: Option identifier
- `Type`: Socket type category
- `ReqLevel`: Required level
- `Name`: Effect description (Vietnamese)
- `Rate`: Activation rate
- `Level1`-`Level10`: Effect values per gem level



### 10. TreasureChest.json
**Primary Function**: Treasure chest metadata and references
**Structure**: JSON array of chest references
**Key Fields**:
- `Id`: Chest identifier
- `Min`, `Max`: Item quantity range
- `DropExcellentBFB`, `DropLuckyBFB`, `DropSetBFB`: Special item drop rates
- `Path`: Path to detailed chest configuration file
```json
{
    "Id": 24120,         //id
    "Min": 1,
    "Max": 3,
    "DropExcellentBFB": 4,  //Drop Excellent Attribute Percentage
    "DropLuckyBFB": 4,      //Drop Lucky Attribute Percentage
    "DropSetBFB": 10,       // Drop Set Attribute Percentage
    "OpenAll": 0,           // Can Obtain All Items from the Box, 1:lấy hết item
    "Path": "conf/Items/TreasureChest/24120.json"
  }
```



### 11. TreasureChest/ Subdirectory
**Contents**: 13 detailed treasure chest configuration files
- `24120.json`, `24121.json`, `24154.json`, `24155.json`, `24156.json`
- `24300.json`, `24350.json`, `24360.json`, `24370.json`, `50007.json`
- `CangBaoTuXiangZi.json`, `XueSeXiangZi.json`, `ZaiShengLiHe.json`

### 12. ItemBuyMoney.json
**Status**: Empty file (0 bytes)
**Potential Use**: Item purchase pricing configurations

## 🎮 System Integration

These files work together to create a comprehensive item system:

1. **ItemInfo.json** provides the base item definitions
2. **ItemOptionInfo.json** adds special attributes and bonuses
3. **ItemDropInfo.json** controls how items are obtained from monsters
4. **Box.json** and **TreasureChest/** files manage loot chests
5. **ItemSetInfo.json** enables set bonus mechanics
6. **Socket config files** handle gem and socket systems
7. **BlessingAngelLevel.json** and **TitleInfo.json** provide character progression systems

## 🔧 Technical Notes

- All configuration files use JSON format
- Vietnamese language is used for display text
- Numeric IDs are used for internal references between files
- The system supports complex item interactions through property IDs and values
- Drop rates use large numbers (e.g., 300000) for probability calculations

This item system provides the foundation for MU Online's extensive equipment, loot, and progression mechanics.
