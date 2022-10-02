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

MyPersonality
<table>
    <col>
    <col>
    <col>
    <col>
    <tr>
        <th rowspan=1>MyPersonality</th>
        <th rowspan=1>E/I</th>
        <th rowspan=1>S/N</th>
        <th rowspan=1>T/F</th>
        <th rowspan=1>J/P</th>
    </tr>
    <tr>
        <td>Random guessing</td>
        <td>76.96</td>
        <td>86.20</td>
        <td>54.11</td>
        <td>60.41</td>
    </tr>
    <tr>
        <td>[Mehta et al.](https://github.com/yashsmehta/personality-prediction) variable training</td>
        <td>78.30</td>
        <td>86.40</td>
        <td>74.40</td>
        <td>64.40</td>
    </tr>
    <tr>
        <td>Ours 4 epochs training Bert 512 tokens</td>
        <td>82.68</td>
        <td>89.51</td>
        <td>83.53</td>
        <td>77.65</td>
    </tr>
</table>

Essays
<table>
    <col>
    <col>
    <col>
    <col>
    <tr>
        <th rowspan=1>Essays</th>
        <th rowspan=1>EXT</th>
        <th rowspan=1>NEU</th>
        <th rowspan=1>AGR</th>
        <th rowspan=1>CON</th>
        <th rowspan=1>OPN</th>
    </tr>
    <tr>
        <td>Random guessing</td>
        <td>51.68</td>
        <td>50.02</td>
        <td>53.06</td>
        <td>50.83</td>
        <td>51.52</td>
    </tr>
    <tr>
        <td>[Mehta et al.](https://github.com/yashsmehta/personality-prediction) 7 epochs training</td>
        <td>54.56</td>
        <td>55.78</td>
        <td>56.10</td>
        <td>56.79</td>
        <td>60.03</td>
    </tr>
    <tr>
        <td>Ours 5 epochs training Bert 512 tokens</td>
        <td>55.56</td>
        <td>54.85</td>
        <td>58.26</td>
        <td>55.86</td>
        <td>63.57</td>
    </tr>
</table>
