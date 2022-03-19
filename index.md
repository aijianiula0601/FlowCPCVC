---
title: FlowCPCVC
layout: default
nav_order: 1
---
# <center> FlowCPCVC: A contrastive predictive coding supervised flow framework for any-to-any voice conversion </center>

<center> Jiahong Huang, Wen Xu, Yule Li, Junshi Liu, Dongpeng Ma,Wei Xiang </center>

## Abstract 

Recently, the research of any-to-any voice conversion(VC) has developed rapidly. However, they often suffer from unsatisfactory quality and require two stages for training, in which a spectrum generation process is indispensable. In this paper, we propose the FlowCPCVC system, which results in higher speech naturalness and timbre similarity. FlowCPCVC is the first one-stage training system for any-to-any task in our knowledge by taking the advantage of VAE and contrastive learning. We employ a speaker encoder to extract timbre information, and a contrastive predictive coding(CPC) based contend extractor to guide the flow module to discard the timbre and keeping the linguistic information. Our method directly incorporates the vocoder into the training, thus avoiding the loss of spectral information as in two-stage training. With a fancy method in training any-to-any task, we can also get robust result when using it in any-to-many conversion. Experiments show that the FlowCPCVC system can get better results than other any-to-any voice conversion systems.

## Compared systems

- Fragmentvc: Any-to-any voice conversion by end-to-end extracting and fusing fine-grained voice fragments with attention.
- MediumVC: Any-to-any voice conversion using synthetic specific-speaker speeches as intermedium features.  
- VQMIVC: Vector Quantization and Mutual Information-Based Unsupervised Speech Representation Disentanglement for One-shot Voice Conversion. Disong Wang et al.
- FlowCPCVC(Ours)

---
## Any-to-Any task
 
speakers come from vctk in test-dataset, all speakers are unseen during training

### Man-to-female

<table>
<tr>
<th>source</th>
<th>target</th>
<th>FragmentVC</th>
<th>MediumVC</th>
<th>VQMIVC</th>
<th>FlowCPCVC</th>
</tr>
<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/source_target_wavs/p284_213_to_p340_388/p284_213.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2vctk/source_target_wavs/p284_213_to_p340_388/p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/fragementvc/p284_213_to_p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/mediumvc/p284_213_to_p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/vqmivc/p284_213_to_p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/flowcpcvc/p284_213_to_p340_388.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/source_target_wavs/p334_210_to_p314_236/p334_210.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2vctk/source_target_wavs/p334_210_to_p314_236/p314_236.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/fragementvc/p334_210_to_p314_236.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/mediumvc/p334_210_to_p314_236.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/vqmivc/p334_210_to_p314_236.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/flowcpcvc/p334_210_to_p314_236.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/source_target_wavs/p251_010_to_p340_388/p251_010.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2vctk/source_target_wavs/p251_010_to_p340_388/p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/fragementvc/p251_010_to_p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/mediumvc/p251_010_to_p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/vqmivc/p251_010_to_p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/flowcpcvc/p251_010_to_p340_388.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/source_target_wavs/p360_189_to_p239_009/p360_189.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2vctk/source_target_wavs/p360_189_to_p239_009/p239_009.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/fragementvc/p360_189_to_p239_009.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2vctk/mediumvc/p360_189_to_p239_009.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2vctk/vqmivc/p360_189_to_p239_009.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2vctk/flowcpcvc/p360_189_to_p239_009.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/source_target_wavs/p326_294_to_p262_054/p326_294.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2vctk/source_target_wavs/p326_294_to_p262_054/p262_054.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/fragementvc/p326_294_to_p262_054.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2vctk/mediumvc/p326_294_to_p262_054.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2vctk/vqmivc/p326_294_to_p262_054.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2vctk/flowcpcvc/p326_294_to_p262_054.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/source_target_wavs/p274_247_to_p340_388/p274_247.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2vctk/source_target_wavs/p274_247_to_p340_388/p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2vctk/fragementvc/p274_247_to_p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2vctk/mediumvc/p274_247_to_p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2vctk/vqmivc/p274_247_to_p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2vctk/flowcpcvc/p274_247_to_p340_388.wav">
</audio>
</td>
</tr>
</table>

### female-to-Man

<table>
<tr>
<th>source</th>
<th>target</th>
<th>FragmentVC</th>
<th>MediumVC</th>
<th>VQMIVC</th>
<th>FlowCPCVC</th>
</tr>
<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p231_406_to_p273_026/p231_406.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p231_406_to_p273_026/p273_026.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/fragementvc/p231_406_to_p273_026.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/mediumvc/p231_406_to_p273_026.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/vqmivc/p231_406_to_p273_026.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/flowcpcvc/p231_406_to_p273_026.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p293_287_to_p302_012/p293_287.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p293_287_to_p302_012/p302_012.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/fragementvc/p293_287_to_p302_012.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/mediumvc/p293_287_to_p302_012.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/vqmivc/p293_287_to_p302_012.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/flowcpcvc/p293_287_to_p302_012.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p231_406_to_p243_148/p231_406.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p231_406_to_p243_148/p243_148.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/fragementvc/p231_406_to_p243_148.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/mediumvc/p231_406_to_p243_148.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/vqmivc/p231_406_to_p243_148.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/flowcpcvc/p231_406_to_p243_148.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p293_287_to_p273_026/p293_287.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p293_287_to_p273_026/p273_026.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/fragementvc/p293_287_to_p273_026.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/mediumvc/p293_287_to_p273_026.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/vqmivc/p293_287_to_p273_026.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/flowcpcvc/p293_287_to_p273_026.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p293_287_to_p270_103/p293_287.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p293_287_to_p270_103/p270_103.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/fragementvc/p293_287_to_p270_103.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/mediumvc/p293_287_to_p270_103.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/vqmivc/p293_287_to_p270_103.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/flowcpcvc/p293_287_to_p270_103.wav">
</audio>
</td>
</tr>
</table>>


## female-to-female or Man-to-Man

<table>
<tr>
<th>source</th>
<th>target</th>
<th>FragmentVC</th>
<th>MediumVC</th>
<th>VQMIVC</th>
<th>FlowCPCVC</th>
</tr>
<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p284_213_to_p243_148/p284_213.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p284_213_to_p243_148/p243_148.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/fragementvc/p284_213_to_p243_148.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/mediumvc/p284_213_to_p243_148.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/vqmivc/p284_213_to_p243_148.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/flowcpcvc/p284_213_to_p243_148.wav">
</audio>
</td>
</tr>

<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p334_210_to_p270_103/p334_210.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p334_210_to_p270_103/p270_103.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/fragementvc/p334_210_to_p270_103.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/mediumvc/p334_210_to_p270_103.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/vqmivc/p334_210_to_p270_103.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/flowcpcvc/p334_210_to_p270_103.wav">
</audio>
</td>
</tr>

<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p251_010_to_p270_103/p251_010.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p251_010_to_p270_103/p270_103.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/fragementvc/p251_010_to_p270_103.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/mediumvc/p251_010_to_p270_103.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/vqmivc/p251_010_to_p270_103.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/flowcpcvc/p251_010_to_p270_103.wav">
</audio>
</td>
</tr>

<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p293_287_to_p225_328/p293_287.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p293_287_to_p225_328/p225_328.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/fragementvc/p293_287_to_p225_328.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/mediumvc/p293_287_to_p225_328.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/vqmivc/p293_287_to_p225_328.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/flowcpcvc/p293_287_to_p225_328.wav">
</audio>
</td>
</tr>

<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p293_287_to_p262_054/p293_287.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p293_287_to_p262_054/p262_054.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/fragementvc/p293_287_to_p262_054.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/mediumvc/p293_287_to_p262_054.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/vqmivc/p293_287_to_p262_054.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/flowcpcvc/p293_287_to_p262_054.wav">
</audio>
</td>

</tr>

<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p293_287_to_p340_388/p293_287.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/source_target_wavs/p293_287_to_p340_388/p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/fragementvc/p293_287_to_p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/mediumvc/p293_287_to_p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/vqmivc/p293_287_to_p340_388.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2any/vctk2vctk/flowcpcvc/p293_287_to_p340_388.wav">
</audio>
</td>
</tr>
</table>

## Audios of target come from libritts, which is another dataset different to vctk 

--------
#### Speakers of target in libritts and speakers of source in test-dataset come from vctk. All speakers are unseen during training. We train the model only with vctk.

<table>
<tr>
<th>source</th>
<th>target</th>
<th>FragmentVC</th>
<th>MediumVC</th>
<th>VQMIVC</th>
<th>FlowCPCVC</th>
</tr>
<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p231_406_to_7127_75947_000082_000005/p231_406.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p231_406_to_7127_75947_000082_000005/7127_75947_000082_000005.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/fragementvc/p231_406_to_7127_75947_000082_000005.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/mediumvc/p231_406_to_7127_75947_000082_000005.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/vqmivc/p231_406_to_7127_75947_000082_000005.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/flowcpcvc/p231_406_to_7127_75947_000082_000005.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p231_406_to_8555_284447_000039_000002/p231_406.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p231_406_to_8555_284447_000039_000002/8555_284447_000039_000002.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/fragementvc/p231_406_to_8555_284447_000039_000002.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/mediumvc/p231_406_to_8555_284447_000039_000002.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/vqmivc/p231_406_to_8555_284447_000039_000002.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/flowcpcvc/p231_406_to_8555_284447_000039_000002.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p251_010_to_6829_68771_000042_000002/p251_010.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p251_010_to_6829_68771_000042_000002/6829_68771_000042_000002.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/fragementvc/p251_010_to_6829_68771_000042_000002.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/mediumvc/p251_010_to_6829_68771_000042_000002.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/vqmivc/p251_010_to_6829_68771_000042_000002.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/flowcpcvc/p251_010_to_6829_68771_000042_000002.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p274_247_to_2830_3979_000021_000000/p274_247.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p274_247_to_2830_3979_000021_000000/2830_3979_000021_000000.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/fragementvc/p274_247_to_2830_3979_000021_000000.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/mediumvc/p274_247_to_2830_3979_000021_000000.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/vqmivc/p274_247_to_2830_3979_000021_000000.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/flowcpcvc/p274_247_to_2830_3979_000021_000000.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p284_213_to_1995_1826_000031_000003_16k/p284_213.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p284_213_to_1995_1826_000031_000003_16k/1995_1826_000031_000003_16k.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/fragementvc/p284_213_to_1995_1826_000031_000003_16k.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/mediumvc/p284_213_to_1995_1826_000031_000003_16k.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/vqmivc/p284_213_to_1995_1826_000031_000003_16k.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/flowcpcvc/p284_213_to_1995_1826_000031_000003_16k.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p293_287_to_121_127105_000041_000001/p293_287.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p293_287_to_121_127105_000041_000001/121_127105_000041_000001.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/fragementvc/p293_287_to_121_127105_000041_000001.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/mediumvc/p293_287_to_121_127105_000041_000001.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/vqmivc/p293_287_to_121_127105_000041_000001.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/flowcpcvc/p293_287_to_121_127105_000041_000001.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p326_294_to_121_127105_000041_000001/p326_294.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p326_294_to_121_127105_000041_000001/121_127105_000041_000001.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/fragementvc/p326_294_to_121_127105_000041_000001.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/mediumvc/p326_294_to_121_127105_000041_000001.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/vqmivc/p326_294_to_121_127105_000041_000001.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/flowcpcvc/p326_294_to_121_127105_000041_000001.wav">
</audio>
</td>
</tr>


<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p334_210_to_237_126133_000011_000000_16k/p334_210.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/source_target_wavs/p334_210_to_237_126133_000011_000000_16k/237_126133_000011_000000_16k.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/vctk2libritts/fragementvc/p334_210_to_237_126133_000011_000000_16k.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/mediumvc/p334_210_to_237_126133_000011_000000_16k.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/vqmivc/p334_210_to_237_126133_000011_000000_16k.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/vctk2libritts/flowcpcvc/p334_210_to_237_126133_000011_000000_16k.wav">
</audio>
</td>
</tr>
</table> 

## Results of emotional voice conversion

#### The mood swing of source audios are high. The source audios come from libritts or other dataset instead of vckt and audios of target come from libritts. Both of them are unseen in training. 

<table>
<tr>
<th>source</th>
<th>target</th>
<th>FragmentVC</th>
<th>MediumVC</th>
<th>VQMIVC</th>
<th>FlowCPCVC</th>
</tr>
<tr>
<td>
    <audio id="audio" controls="" preload="none">
          <source id="wav" src="any2any/yuqi/source_target_wavs/0012_000656_to_en-US-AriaNeural_1624612591339/0012_000656.wav">
    </audio>
</td>
<td>
    <audio id="audio" controls="" preload="none">
           <source id="wav" src="any2any/yuqi/source_target_wavs/0012_000656_to_en-US-AriaNeural_1624612591339/en-US-AriaNeural_1624612591339.wav">
    </audio>
</td>
<td>
    <audio id="audio" controls="" preload="none">
          <source id="wav" src="any2any/yuqi/fragementvc/0012_000656_to_en-US-AriaNeural_1624612591339.wav">
    </audio>
</td>
<td>
    <audio id="audio" controls="" preload="none">
           <source id="wav" src="any2any/yuqi/mediumvc/0012_000656_to_en-US-AriaNeural_1624612591339.wav">
    </audio>
</td>
<td>
    <audio id="audio" controls="" preload="none">
          <source id="wav" src="any2any/yuqi/vqmivc/0012_000656_to_en-US-AriaNeural_1624612591339.wav">
    </audio>
</td>
<td>
    <audio id="audio" controls="" preload="none">
           <source id="wav" src="any2any/yuqi/flowcpcvc/0012_000656_to_en-US-AriaNeural_1624612591339.wav">
    </audio>
</td>
</tr>

<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/yuqi/source_target_wavs/0011_001750_to_20_205_000031_000000/0011_001750.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/yuqi/source_target_wavs/0011_001750_to_20_205_000031_000000/20_205_000031_000000.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/yuqi/fragementvc/0011_001750_to_20_205_000031_000000.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/yuqi/mediumvc/0011_001750_to_20_205_000031_000000.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/yuqi/vqmivc/0011_001750_to_20_205_000031_000000.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/yuqi/flowcpcvc/0011_001750_to_20_205_000031_000000.wav">
</audio>
</td>
</tr>

<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/yuqi/source_target_wavs/男2_to_10011/男2.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/yuqi/source_target_wavs/男2_to_10011/10011.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/yuqi/fragementvc/男2_to_10011.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/yuqi/mediumvc/男2_to_10011.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/yuqi/vqmivc/男2_to_10011.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/yuqi/flowcpcvc/男2_to_10011.wav">
</audio>
</td>
</tr>

<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/yuqi/source_target_wavs/EMD6_to_p231_012/EMD6.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/yuqi/source_target_wavs/EMD6_to_p231_012/p231_012.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/yuqi/fragementvc/EMD6_to_p231_012.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/yuqi/mediumvc/EMD6_to_p231_012.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/yuqi/vqmivc/EMD6_to_p231_012.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/yuqi/flowcpcvc/EMD6_to_p231_012.wav">
</audio>
</td>
</tr>

<tr>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/yuqi/source_target_wavs/obm2_to_en-US-ElizabethNeural_1624631702559/obm2.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/yuqi/source_target_wavs/obm2_to_en-US-ElizabethNeural_1624631702559/en-US-ElizabethNeural_1624631702559.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/yuqi/fragementvc/obm2_to_en-US-ElizabethNeural_1624631702559.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/yuqi/mediumvc/obm2_to_en-US-ElizabethNeural_1624631702559.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
      <source id="wav" src="any2any/yuqi/vqmivc/obm2_to_en-US-ElizabethNeural_1624631702559.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2any/yuqi/flowcpcvc/obm2_to_en-US-ElizabethNeural_1624631702559.wav">
</audio>
</td>
</tr>
</table>

---
## Any-to-Many

### Audios of source come from libritts and timbre of target come from vctk in training dataset.

#### Some examples for target timbre  
<table>
<tr>
<th>p236</th>
<th>p264</th>
<th>p269</th>
<th>p263</th>
<th>p259</th>
<th>p256</th>
</tr>
<tr>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2many/flowcpcvc/target_tone_wavs/p236_482.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2many/flowcpcvc/target_tone_wavs/p264_460.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2many/flowcpcvc/target_tone_wavs/p269_391.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2many/flowcpcvc/target_tone_wavs/p263_430.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2many/flowcpcvc/target_tone_wavs/p259_440.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
       <source id="wav" src="any2many/flowcpcvc/target_tone_wavs/p256_278.wav">
</audio>
</td>
</tr>
</table>

#### Converted results

<table>
<tr>
<th>source</th>
<th>to_p236</th>
<th>to_p264</th>
<th>to_p269</th>
<th>to_p263</th>
<th>to_p259</th>
<th>to_p256</th>
</tr>
<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2many/flowcpcvc/8825_292252_000018_000000_22050.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/8825_292252_000018_000000_22050_to_p236.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/8825_292252_000018_000000_22050_to_p264.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/8825_292252_000018_000000_22050_to_p269.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/8825_292252_000018_000000_22050_to_p263.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/8825_292252_000018_000000_22050_to_p259.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/8825_292252_000018_000000_22050_to_p256.wav">
</audio>
</td>
</tr>
<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2many/flowcpcvc/4145_104606_000026_000000.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/4145_104606_000026_000000_to_p236.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/4145_104606_000026_000000_to_p264.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/4145_104606_000026_000000_to_p269.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/4145_104606_000026_000000_to_p263.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/4145_104606_000026_000000_to_p259.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/4145_104606_000026_000000_to_p256.wav">
</audio>
</td>
</tr>
<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2many/flowcpcvc/8163_274549_000005_000001.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/8163_274549_000005_000001_to_p236.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/8163_274549_000005_000001_to_p264.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/8163_274549_000005_000001_to_p269.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/8163_274549_000005_000001_to_p263.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/8163_274549_000005_000001_to_p259.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/8163_274549_000005_000001_to_p256.wav">
</audio>
</td>
</tr>
<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2many/flowcpcvc/7967_104986_000035_000000.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/7967_104986_000035_000000_to_p236.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/7967_104986_000035_000000_to_p264.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/7967_104986_000035_000000_to_p269.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/7967_104986_000035_000000_to_p263.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/7967_104986_000035_000000_to_p259.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/7967_104986_000035_000000_to_p256.wav">
</audio>
</td>
</tr>
<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2many/flowcpcvc/6497_234106_000052_000000_22050.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/6497_234106_000052_000000_22050_to_p236.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/6497_234106_000052_000000_22050_to_p264.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/6497_234106_000052_000000_22050_to_p269.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/6497_234106_000052_000000_22050_to_p263.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/6497_234106_000052_000000_22050_to_p259.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/6497_234106_000052_000000_22050_to_p256.wav">
</audio>
</td>
</tr>
<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2many/flowcpcvc/882_123267_000043_000004.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/882_123267_000043_000004_to_p236.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/882_123267_000043_000004_to_p264.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/882_123267_000043_000004_to_p269.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/882_123267_000043_000004_to_p263.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/882_123267_000043_000004_to_p259.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/882_123267_000043_000004_to_p256.wav">
</audio>
</td>
</tr>
<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2many/flowcpcvc/4719_25766_000057_000001_22050.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/4719_25766_000057_000001_22050_to_p236.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/4719_25766_000057_000001_22050_to_p264.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/4719_25766_000057_000001_22050_to_p269.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/4719_25766_000057_000001_22050_to_p263.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/4719_25766_000057_000001_22050_to_p259.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/4719_25766_000057_000001_22050_to_p256.wav">
</audio>
</td>
</tr>
<tr>
<td>
<audio id="audio" controls="" preload="none">
<source id="wav" src="any2many/flowcpcvc/1776_139035_000002_000000_22050.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/1776_139035_000002_000000_22050_to_p236.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/1776_139035_000002_000000_22050_to_p264.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/1776_139035_000002_000000_22050_to_p269.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/1776_139035_000002_000000_22050_to_p263.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/1776_139035_000002_000000_22050_to_p259.wav">
</audio>
</td>
<td>
<audio id="audio" controls="" preload="none">
 <source id="wav" src="any2many/flowcpcvc/1776_139035_000002_000000_22050_to_p256.wav">
</audio>
</td>
</tr>
</table>