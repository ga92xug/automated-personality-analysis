# Automated Personality Analysis

## Introduction
Automated personality analysis is the task of predicting the personality of a person from text or a video without the need for a questionnaire.

For additional details, please see our paper:  
"[Name of your paper](https://github.com/flo-stilz/3D-Visual-Grounding-with-Transformers/blob/lang-det/paper%20%26%20figures/final_submission_3D_visual_grounding_with_transformers.pdf)" (add paper)
by [Stefan Frisch](https://github.com/ga92xug) and [Hakan Akyürek](https://github.com/add_your_github/)
from the [Technical University of Munich](https://www.tum.de/en/). 

## Setup + Dataset
We explored automated personality analysis for 3 different datasets.

[Essays Big Five personality factors](https://github.com/ga92xug/personality-prediction/tree/master/data/essays)

[MyPersonality Myers-Briggs type indicator](https://www.kaggle.com/datasets/haisamrafid/mypersonality)

Twitter Myers-Briggs type indicator: for the queries to get this data from Twitter please check our paper.

## Method
We have tried 2 different methods to solve this automated personality analysis task:

### Classification
During classification we tried several language encoders (Bert, Longformer, Distillbert) with the output of these and a MLP on top we predicted the personality type of an individual from text/tweets. 

### Siamese
todo

## Results
todo

<table>
    <col>
    <col>
    <colgroup span="2"></colgroup>
    <col>
    <tr>
        <th rowspan=2>Name</th>
        <th rowspan=2>Command</th>
        <th colspan=2 scope="colgroup">Overall</th>
        <th rowspan=2>Comments</th>
    </tr>
    <tr>
        <td>Acc<!-- -->@<!-- -->0.25IoU</td>
        <td>Acc<!-- -->@<!-- -->0.5IoU</td>
    </tr>
    <tr>
        <td>ScanRefer (Baseline)</td>
        <td><pre lang="shell">python scripts/train.py 
        --use_color --lr 1e-3 --batch_size 14</pre></td>
        <td>37.05</td>
        <td>23.93</td>
        <td>xyz + color + height</td>
    </tr>
    <tr>
        <td>ScanRefer with pretrained VoteNet (optimized Baseline)</td>
        <td><pre lang="shell">python scripts/train.py 
        --use_color --use_chunking 
        --use_pretrained "pretrained_VoteNet" 
        --lr 1e-3 --batch_size 14</pre></td>
        <td>37.11</td>
        <td>25.21</td>
        <td>xyz + color + height</td>
    </tr>
    <tr>
        <td>Ours (pretrained 3DETR-m + GRU + vTransformer) </td>
        <td><pre lang="shell">python scripts/train.py 
        --use_color --use_chunking 
        --detection_module 3detr 
        --match_module transformer
        --use_pretrained "pretrained_3DETR"
        --no_detection </pre></td>
        <td>37.08</td>
        <td>26.56</td>
        <td>xyz + color + height</td>
    </tr>

</table>
