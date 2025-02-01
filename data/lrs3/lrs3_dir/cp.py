"""
新建一个文件夹里面放对应的gt，facetts,hcdtts，txt这样，图片就不放了
"""

import os
import shutil

case = []
with open(
    "/home/zjli/work/test/face_tts/tool/case3.txt", "r", encoding="utf-8"
) as file:
    for line in file:
        # print(line.strip())  # 每次读取一行，适合大文件
        case.append(line.strip())
facetts_root = "/disk1/zjli/tts_data/LSR3/test_data/facetts_test_all"
ft_root = "/home/zjli/work/test/output_wav/test_ft_all/align_ckpt/random_orgin_2024-10-31_21-36_last_checkpoint"
orgin_root = "/disk1/zjli/tts_data/LSR3/test_data/test_all_spk"
output_root = "/home/zjli/work/test/face_tts/mess/final/lrs3_dir/dir"
face_root = "/disk1/zjli/tts_data/LSR3/test_content/test_select_sharp_img"
# for spk in case:
#     os.makedirs(output_root, spk)
output_root_wav = "/home/zjli/work/test/face_tts/mess/final/lrs3_dir/gt_dir_wav"
os.makedirs(output_root, exist_ok=True)

for spk in case:
    source_folder = os.path.join(orgin_root, spk)
    # 获取 source_folder 里的所有 `.wav` 文件并排序
    wav_files = sorted([f for f in os.listdir(source_folder) if f.endswith(".wav")])

    if wav_files:
        # 选择第一个 wav 文件
        first_wav = wav_files[0]
        source_file_path = os.path.join(source_folder, first_wav)
    shutil.copy(
        source_file_path, os.path.join(output_root_wav, spk + ".wav")
    )  # 移动gt wav


"""移动图片"""
# shutil.copy(
#     os.path.join(face_root, spk + ".jpg"), os.path.join(output_root, spk + ".jpg")
# )
