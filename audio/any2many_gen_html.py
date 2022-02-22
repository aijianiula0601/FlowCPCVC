import os
import sys
from pathlib import Path

pdj = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(pdj)
print(pdj)

speaker_name_cl = ['p236', 'p264', 'p269', 'p263', 'p259', 'p256']


def gen_tr():
    print("<tr>")
    print(f"<th>source</th>")
    for sp in speaker_name_cl:
        print(f"<th>to_{sp}</th>")
    print("</tr>")


def gen_tb_html(any2many_save_dir, source_wav_name, converted_wav_name_cl):
    tb_html = f"""
    <tr>
    <td>
        <audio id="audio" controls="" preload="none">
              <source id="wav" src="{any2many_save_dir}/{source_wav_name}.wav">
        </audio>
    </td>
    """
    print(tb_html)

    for converted_wav_name in converted_wav_name_cl:
        tb_str = f"""
        <td>
        <audio id="audio" controls="" preload="none">
               <source id="wav" src="{any2many_save_dir}/{converted_wav_name}.wav">
        </audio>
        </td>
        """
        print(tb_str)
    print("</tr>")


# 更高难度的
base_dir = "/Users/jiahong/Downloads"
source_wav_dir = f"{base_dir}/any2many_source_wavs_libritts"
converted_wav_dir = f"{base_dir}/vits_any2many_wavs_libritts"
any2many_save_dir = f"{pdj}/audio/vits_any2many_vc"

os.system(f"mkdir -p {any2many_save_dir}")

gen_tr()
for fp in Path(source_wav_dir).glob("*.wav"):
    source_wav_name = fp.name.replace(".wav", "")
    converted_wav_name_cl = []
    for tn in speaker_name_cl:
        converted_fp = f"{converted_wav_dir}/{source_wav_name}_to_{tn}.wav"
        assert os.path.exists(converted_fp)
        converted_wav_name_cl.append(Path(converted_fp).name.replace(".wav", ""))
        cmd = f"cp -rf {converted_fp} {any2many_save_dir}"
        os.system(cmd)

    cmd = f"cp -rf {str(fp)} {any2many_save_dir}"
    os.system(cmd)
    gen_tb_html(any2many_save_dir, source_wav_name, converted_wav_name_cl)
