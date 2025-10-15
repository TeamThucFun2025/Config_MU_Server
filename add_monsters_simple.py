#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script để thêm quái ngay sau từng dòng trong tất cả file MonsterSpawnPoint
và update trực tiếp lên file đó (không tạo file mới)
"""

import json
import random
import os
import glob

def add_monsters_after_each_line(file_path):
    """Thêm quái ngay sau từng dòng với tọa độ random cho một file"""
    
    # Đọc file gốc
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_data = json.load(f)
    except FileNotFoundError:
        print(f"Không tìm thấy file: {file_path}")
        return False
    except json.JSONDecodeError as e:
        print(f"Lỗi đọc JSON file {file_path}: {e}")
        return False
    
    print(f"\nĐang xử lý file: {file_path}")
    print(f"File gốc có {len(original_data)} spawn points")
    
    # Tạo dữ liệu mới
    new_data = []
    
    for i, point in enumerate(original_data):
        # Thêm dòng gốc
        new_data.append(point)
        
        # Random có cho tạo ko (0 = bỏ qua, 1 = tạo monster mới)
        should_create = random.randint(0, 1) == 1
        
        if should_create:
            # Tạo quái mới với tọa độ random
            offset_x = random.randint(-8, 8)
            offset_y = random.randint(-8, 8)
            
            new_point = {
                "Index": point["Index"],
                "PositionX": point["PositionX"] + offset_x,
                "PositionY": point["PositionY"] + offset_y,
                "Direction": point["Direction"]
            }
            
            # Thêm dòng mới ngay sau dòng gốc
            new_data.append(new_point)
            
            if i < 5:  # Chỉ hiển thị 5 dòng đầu để không spam console
                print(f"  Dòng {i+1}: Thêm quái {point['Index']} tại ({new_point['PositionX']}, {new_point['PositionY']})")
        else:
            if i < 5:  # Chỉ hiển thị 5 dòng đầu để không spam console
                print(f"  Dòng {i+1}: Bỏ qua quái {point['Index']}")
        
        if i == 5:
            print("  ... (đang xử lý các dòng còn lại)")
    
    # Lưu trực tiếp lên file gốc
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(new_data, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Đã update file: {file_path}")
        print(f"  Tổng spawn points: {len(new_data)} (gốc: {len(original_data)}, thêm: {len(new_data) - len(original_data)})")
        return True
        
    except Exception as e:
        print(f"✗ Lỗi khi lưu file {file_path}: {e}")
        return False

def process_all_monster_spawn_files():
    """Xử lý tất cả file MonsterSpawnPoint trong folder"""
    
    # Đường dẫn folder
    folder_path = "SpawnPoint/Monster"
    
    # Tìm tất cả file có tên chứa "MonsterSpawnPoint"
    pattern = os.path.join(folder_path, "*MonsterSpawnPoint*.json")
    files = glob.glob(pattern)
    
    if not files:
        print(f"Không tìm thấy file nào chứa 'MonsterSpawnPoint' trong folder {folder_path}")
        return
    
    print(f"Tìm thấy {len(files)} file MonsterSpawnPoint:")
    for file in files:
        print(f"  - {file}")
    
    print(f"\nBắt đầu xử lý {len(files)} file...")
    
    success_count = 0
    for file_path in files:
        if add_monsters_after_each_line(file_path):
            success_count += 1
    
    print(f"\n=== KẾT QUẢ ===")
    print(f"Thành công: {success_count}/{len(files)} file")
    print(f"Thất bại: {len(files) - success_count}/{len(files)} file")

if __name__ == "__main__":
    process_all_monster_spawn_files()
