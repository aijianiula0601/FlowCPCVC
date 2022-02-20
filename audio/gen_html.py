import os
import sys

pdj = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pdj)
print(pdj)

speaker_info_file = "/Users/jia/Downloads/speaker-info.txt"
speaker_gender_dic = {}
with open(speaker_info_file, 'r', encoding='utf-8') as f:
    i = 0
    for line in f.readlines():
        if i < 1:
            i += 1
            continue

        parts = line.split("  ")
        spn = "p" + parts[0]
        gender = parts[2]
        speaker_gender_dic[spn] = gender
        i += 1

test_speaker_name = ['p231', 'p284', 'p334', 'p251', 'p326', 'p274', 'p293', 'p360', 'p258', 'p374', 'p271', 'p262',
                     'p314', 'p239', 'p243', 'p225', 'p273', 'p302', 'p270', 'p340']

M_sp_cl = []
F_sp_cl = []

for sp in test_speaker_name:
    if speaker_gender_dic[sp] == "M":
        M_sp_cl.append(sp)
    else:
        F_sp_cl.append(sp)

print("男性speaker_name:", M_sp_cl)
print("女性speaker_name:", F_sp_cl)


def gen_tb_html(vits_save_base_dir, vq_save_base_dir, source_wav_name, target_wav_name):
    tb_html = f"""
    <tr>
        <td>
            <audio id="audio" controls="" preload="none">
                  <source id="wav" src="{vits_save_base_dir}/{source_wav_name}_to_{target_wav_name}/{source_wav_name}.wav">
            </audio>
        </td>
        <td>
            <audio id="audio" controls="" preload="none">
                   <source id="wav" src="{vits_save_base_dir}/{source_wav_name}_to_{target_wav_name}/{target_wav_name}.wav">
            </audio>
        </td>
        <td>
            <audio id="audio" controls="" preload="none">
                  <source id="wav" src="{vits_save_base_dir}/{source_wav_name}_to_{target_wav_name}/{source_wav_name}_to_{target_wav_name}.wav">
            </audio>
        </td>
        <td>
            <audio id="audio" controls="" preload="none">
                   <source id="wav" src="{vq_save_base_dir}/{source_wav_name}_to_{target_wav_name}/{source_wav_name}_to_{target_wav_name}.wav">
            </audio>
        </td>
    </tr>
    """
    return tb_html


base_dir = "/Users/jia/Downloads"
vits_save_base_dir = "audio/vits_vctk_vc_to_vctk"
vq_save_base_dir = "audio/vqmivc_vctk_vc_to_vctk"


def process_data(source_wav_name, target_wav_name):
    tq_html = gen_tb_html(vits_save_base_dir, vq_save_base_dir, source_wav_name, target_wav_name)
    print(tq_html)
    os.system(
        f"cp -rf {base_dir}/{vits_save_base_dir.split('/')[-1]}/{source_wav_name}_to_{target_wav_name} {pdj}/{vits_save_base_dir}/ && cp -rf {base_dir}/{vq_save_base_dir.split('/')[-1]}/{source_wav_name}_to_{target_wav_name} {pdj}/{vq_save_base_dir}/")


# # M2F
# to_sp = "p284_213_to_p340_388"
# source_wav_name = to_sp.split("_to_")[0]
# target_wav_name = to_sp.split("_to_")[1]
# process_data(source_wav_name,target_wav_name)
# # ------------------------------------------------
# to_sp = "p334_210_to_p314_236"
# source_wav_name = to_sp.split("_to_")[0]
# target_wav_name = to_sp.split("_to_")[1]
# process_data(source_wav_name,target_wav_name)
# # ------------------------------------------------
# to_sp = "p251_010_to_p340_388"
# source_wav_name = to_sp.split("_to_")[0]
# target_wav_name = to_sp.split("_to_")[1]
# process_data(source_wav_name,target_wav_name)
# # ------------------------------------------------
# to_sp = "p360_189_to_p239_009"
# source_wav_name = to_sp.split("_to_")[0]
# target_wav_name = to_sp.split("_to_")[1]
# process_data(source_wav_name,target_wav_name)
# # ------------------------------------------------
# to_sp="p326_294_to_p262_054"
# source_wav_name = to_sp.split("_to_")[0]
# target_wav_name = to_sp.split("_to_")[1]
# process_data(source_wav_name,target_wav_name)
# # ------------------------------------------------
# to_sp="p274_247_to_p340_388"
# source_wav_name = to_sp.split("_to_")[0]
# target_wav_name = to_sp.split("_to_")[1]
# process_data(source_wav_name,target_wav_name)
# # ------------------------------------------------

# F2M
# to_sp="p231_406_to_p273_026"
# source_wav_name = to_sp.split("_to_")[0]
# target_wav_name = to_sp.split("_to_")[1]
# process_data(source_wav_name,target_wav_name)
# #--------------------------------------------------------------
# to_sp="p293_287_to_p302_012"
# source_wav_name = to_sp.split("_to_")[0]
# target_wav_name = to_sp.split("_to_")[1]
# process_data(source_wav_name,target_wav_name)
# #--------------------------------------------------------------
# to_sp="p231_406_to_p243_148"
# source_wav_name = to_sp.split("_to_")[0]
# target_wav_name = to_sp.split("_to_")[1]
# process_data(source_wav_name,target_wav_name)
# #--------------------------------------------------------------
# to_sp="p293_287_to_p273_026"
# source_wav_name = to_sp.split("_to_")[0]
# target_wav_name = to_sp.split("_to_")[1]
# process_data(source_wav_name,target_wav_name)
# #--------------------------------------------------------------
# to_sp="p293_287_to_p270_103"
# source_wav_name = to_sp.split("_to_")[0]
# target_wav_name = to_sp.split("_to_")[1]
# process_data(source_wav_name,target_wav_name)


# femal-to-Man or Man-to-Man
to_sp = "p284_213_to_p243_148"
source_wav_name = to_sp.split("_to_")[0]
target_wav_name = to_sp.split("_to_")[1]
process_data(source_wav_name, target_wav_name)
# --------------------------------------------------------------
to_sp = "p334_210_to_p270_103"
source_wav_name = to_sp.split("_to_")[0]
target_wav_name = to_sp.split("_to_")[1]
process_data(source_wav_name, target_wav_name)
# --------------------------------------------------------------
to_sp = "p251_010_to_p270_103"
source_wav_name = to_sp.split("_to_")[0]
target_wav_name = to_sp.split("_to_")[1]
process_data(source_wav_name, target_wav_name)
# --------------------------------------------------------------
to_sp = "p293_287_to_p225_328"
source_wav_name = to_sp.split("_to_")[0]
target_wav_name = to_sp.split("_to_")[1]
process_data(source_wav_name, target_wav_name)
# --------------------------------------------------------------
to_sp = "p293_287_to_p262_054"
source_wav_name = to_sp.split("_to_")[0]
target_wav_name = to_sp.split("_to_")[1]
process_data(source_wav_name, target_wav_name)
# --------------------------------------------------------------
to_sp = "p293_287_to_p340_388"
source_wav_name = to_sp.split("_to_")[0]
target_wav_name = to_sp.split("_to_")[1]
process_data(source_wav_name, target_wav_name)
