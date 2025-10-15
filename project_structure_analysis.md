# Phân Tích Cấu Trúc Project Game Server

## Tổng Quan
Đây là project cấu hình cho một game server (có vẻ như Mu Online), được tổ chức theo cấu trúc thư mục phân chia chức năng rõ ràng.

## Chi Tiết Các Thư Mục

### 🔄 ActiveEvents
Chứa các cấu hình cho các sự kiện đang hoạt động trong game:
- `ActiveEvents.json`: Danh sách sự kiện đang chạy
- `Currency.json`: Cấu hình tiền tệ trong sự kiện
- `ExpAndGold.json`: Cấu hình kinh nghiệm và vàng thưởng
- `PrizeLucky.json`: Cấu hình phần thưởng may mắn
- `PrizePools.json`: Hồ phần thưởng
- `Ranking.json`: Bảng xếp hạng sự kiện
- `Rebates.json`: Cấu hình hoàn tiền

### ⚓ Anchor
- `Anchor.json`: Cấu hình điểm neo/điểm đánh dấu trong game

### ⚔️ Arena
Hệ thống đấu trường:
- `ArenaRankReward.json`: Phần thưởng xếp hạng đấu trường
- `ArenaRoomManagerInfo.json`: Thông tin quản lý phòng đấu trường
- `ArenaTimeInfo.json`: Thời gian hoạt động đấu trường
- `Terrain/Terrain.json`: Địa hình đấu trường

### 🏰 Dungeon
Cấu hình các dungeon và địa hạ thành:
- **ChaosCastle**: Đấu trường hỗn loạn
  - `IGC_ChaosCastle_Monster.xml`: Quái vật trong Chaos Castle
  - `IGC_ChaosCastle.xml`: Cấu hình Chaos Castle
- `DungeonInfo.json`, `DungeonInfo1.json`: Thông tin dungeon
- `DungeonMoveInfo.json`: Thông tin di chuyển trong dungeon
- **Monster/boss/**: Cấu hình boss trong dungeon (7 files)
- **Move/**: Cấu hình di chuyển (8 files)
- **RoomManager/**: Quản lý phòng (18 files)
- **SafeArea/**: Khu vực an toàn trong dungeon (2 files)
- **SpawnPoint/**: Điểm sinh ra trong dungeon (19 files)
- **Terrain/**: Địa hình dungeon (9 files)

### 🎉 Events
Các sự kiện đặc biệt:
- `LastManStanding.xml`: Sự kiện "Người sống sót cuối cùng"
- `SafeAreaBFG1.json`, `SafeAreaBFG2.json`: Khu vực an toàn trong sự kiện
- `SiegeBattle.json`: Sự kiện công thành

### 👨‍👩‍👧‍👦 Family
- `Prestige.json`: Cấu hình uy tín gia tộc

### ⚙️ Cấu Hình Game Server
Các file INI cấu hình chính:
- `GameServerInfo.ini`: Cấu hình chính game server
- `GameServerInfo_Attribute.ini`: Cấu hình thuộc tính
- `GameServerInfo_Attribute_Point_Cards.ini`: Thẻ điểm thuộc tính
- `GameServerInfo_Game.ini`: Cấu hình game
- `GameServerInfo_Game_Point_Cards.ini`: Thẻ điểm game
- `GameServerInfo_Item.ini`: Cấu hình vật phẩm

### 📦 Items
Hệ thống vật phẩm:
- `BlessingAngelLevel.json`: Cấp độ thiên thần chúc phúc
- `Box.json`: Cấu hình hộp vật phẩm
- `Config_SocketItemOption.json`: Tùy chọn socket vật phẩm
- `Config_SocketItemOptionSet.json`: Bộ tùy chọn socket
- `ItemBuyMoney.json`: Giá mua vật phẩm
- `ItemDropInfo.json`: Thông tin rơi vật phẩm
- `ItemInfo.json`: Thông tin vật phẩm
- `ItemOptionInfo.json`: Tùy chọn vật phẩm
- `ItemSetInfo.json`: Thông tin set vật phẩm
- `TitleInfo.json`: Thông tin danh hiệu
- **TreasureChest/**: Rương kho báu (13 files)

### 🎰 Lottery
Hệ thống quay thưởng:
- `PrizePool.json`: Hồ phần thưởng chính
- `PrizePoolFirst.json`: Hồ phần thưởng lần đầu
- `PrizePoolSecond.json`: Hồ phần thưởng lần thứ hai

### 🐍 Lua Scripts
- `ExpCalc.lua`: Tính toán kinh nghiệm
- **redis/**: Scripts Redis (8 files .lua + 2 files .txt)
- **Skills/**: Scripts kỹ năng (2 files)

### 👹 Monster
Hệ thống quái vật:
- **boss/**: Cấu hình boss (4 files)
- `BOSSTimeFresh.json`: Thời gian làm mới boss
- `Config_GoldenBossReffresh.json`: Làm mới boss vàng
- `GoldenBOSS.json`: Boss vàng
- `GoldenBossDropRate.json`: Tỷ lệ rơi của boss vàng
- `GoldenBOSSEquipDrop.json`: Trang bị rơi từ boss vàng
- `MonsterDropAdd.json`: Thêm rơi vật phẩm từ quái
- `MonsterInfo.json`: Thông tin quái vật
- `MonsterInSceneAttr.json`: Thuộc tính quái trong scene
- `MonsterItemDropRate.json`: Tỷ lệ rơi vật phẩm từ quái

### 🐎 Mounts
- `Mounts.json`: Cấu hình thú cưỡi

### 🗺️ Move
Hệ thống di chuyển:
- `Area.json`: Cấu hình khu vực
- `MoveArea.json`: Khu vực di chuyển
- `SceneMoveInfo.json`: Thông tin di chuyển giữa scene

### 👥 NPC
- `NpcGoods.json`: Hàng hóa của NPC
- `NpcInfo.json`: Thông tin NPC
- **Synthesis/**: Hệ thống tổng hợp (1 file)

### 🐾 Pet
- `PetInfo.json`: Thông tin pet

### 📜 Quest
Hệ thống nhiệm vụ:
- `CareerChangingTask.json`: Nhiệm vụ chuyển nghề
- `Config_NoviceTask.json`: Nhiệm vụ tân thủ
- `Config_UpgradeTask.json`: Nhiệm vụ nâng cấp
- `LineQuest.json`: Nhiệm vụ tuyến tính
- `QuestInfo.json`: Thông tin nhiệm vụ

### 🏆 Ranking
- `GameRanking.json`: Bảng xếp hạng game

### 🔄 Reset
- `Reset.xml`: Cấu hình reset nhân vật

### 🎭 Role
Thông tin nhân vật:
- `InitialItems.json`: Vật phẩm khởi tạo
- `InitialItemsDARKLORD.json`: Vật phẩm khởi tạo Dark Lord
- `InitialItemsELF.json`: Vật phẩm khởi tạo Elf
- `InitialItemsKNIGHT.json`: Vật phẩm khởi tạo Knight
- `InitialItemsMAGUMSA.json`: Vật phẩm khởi tạo Magumsa
- `InitialItemsSUMMONER.json`: Vật phẩm khởi tạo Summoner
- `InitialItemsWIZARD.json`: Vật phẩm khởi tạo Wizard
- `RoleInfo.json`: Thông tin nhân vật

### 🛡️ SafeArea
Khu vực an toàn (21 files):
- `SafeArea1.json` đến `SafeArea21.json`: Các khu vực an toàn khác nhau
- `SafeArea201.json`, `SafeArea301.json`, `SafeArea302.json`: Khu vực đặc biệt

### 🛒 Shop
Hệ thống cửa hàng (12 files):
- `Shop10001.json` đến `Shop10024.json`: Các cửa hàng khác nhau

### ⚡ Skill
Hệ thống kỹ năng:
- `Config_Buff.json`: Cấu hình buff
- `MasterSkillTree.xml`: Cây kỹ năng master
- `SkillInfo.json`: Thông tin kỹ năng
- `SkillList.xml`: Danh sách kỹ năng

### 📍 SpawnPoint
Điểm sinh ra:
- **Monster/**: Điểm sinh quái vật (69 files)
- **Npc/**: Điểm sinh NPC (21 files)
- **TreasureMap/**: Điểm sinh bản đồ kho báu (5 files)

### 🔧 System
Cấu hình hệ thống:
- `Anchor.json`: Neo hệ thống
- `Cangbaoge.json`: Có thể là kho báu
- `Code.json`: Mã code hệ thống
- **FirstChargePackage/**: Gói nạp lần đầu (3 files)
- `Guaji.json`: Chế độ treo máy
- `GuajiSpend.json`: Chi tiêu treo máy
- `NewMall.json`: Mall mới
- **RechargePackage/**: Gói nạp tiền (5 files)
- `RedName.json`: Tên đỏ (PK)
- `Synthesis.json`: Tổng hợp
- `SystemMail.json`: Thư hệ thống
- `TextContent.json`: Nội dung văn bản
- `Title.json`: Danh hiệu
- `WorldEXP.json`: Kinh nghiệm thế giới

### 🌍 Terrain
Địa hình (24 files):
- Các file JSON định nghĩa địa hình cho các map khác nhau

## Files Khác
- `Config_Scene.json`: Cấu hình scene
- `add_monsters_simple.py`: Script Python thêm quái vật đơn giản

## Tổng Kết
Project này được tổ chức rất có hệ thống với việc phân chia rõ ràng các chức năng:
- **Gameplay**: Events, Dungeon, Arena, Quest
- **Characters**: Role, Skill, Mounts, Pet
- **Economy**: Items, Shop, Lottery, Currency
- **World**: Terrain, Move, SafeArea, SpawnPoint
- **Systems**: System, Ranking, Reset
- **NPC/Monsters**: Monster, Npc, Boss

Mỗi thư mục chứa các file cấu hình JSON/XML phù hợp với chức năng của nó.
