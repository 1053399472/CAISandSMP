1. Directory

```python
├── CAIS                                                       #CAIS datasets
│   ├── dataLoder                                              #Different forms of CAIS datasets loading method
│   │   ├── GlobalPointerDataloder.py
│   │   ├── mergeCAISDataloder.py
│   │   └── sourceDataloder.py
│   ├── GlobalPointerCAIS                                      #The location of the original datasets entity to represent
│   │   ├── dev.json
│   │   ├── test.json
│   │   └── train.json
│   ├── mergeCAIS                                              #Fill in the intention of the original datasets with the slot and merge
│   │   ├── dev.txt
│   │   ├── test.txt
│   │   └── train.txt
│   ├── source                                                 #original datasets
│   │   ├── test
│   │   │   ├── ch.test
│   │   │   └── ch.test.intent
│   │   ├── train
│   │   │   ├── ch.train
│   │   │   └── ch.train.intent
│   │   └── valid
│   │       ├── ch.valid
│   │       └── ch.valid.intent
│   └── SourceToGlobalPointer.py                                 #datasets conversion program
├── README.md
└── SMP
    ├── GlobalPointer                                            #The location of the original datasets entity to represent
    │   ├── GlobalPointerSMP2019
    │   │   ├── dev.json
    │   │   ├── test.json
    │   │   └── train.json
    │   └── GlobalPointerSMP2020
    │       ├── dev.json
    │       ├── test.json
    │       └── train.json
    ├── source                                                   #original datasets
    │   ├── 2019train.json
    │   └── 2020train.json
    └── sourceToGlobalPointer.py

```

2. Introduction：

- CAIS：

CAIS Origin from the paper[ CM-Net: A Novel Collaborative Memory Network for Spoken Language Understanding](https://arxiv.org/abs/1909.06937#:~:text=Title%3ACM-Net%3A A Novel Collaborative Memory Network for Spoken,filling%2C which are generally modeled jointly in existing)，CAIS dataset includes 7,995 training, 994 validation and 1024 test utterances.Original data can be downloaded from [Github](https://github.com/Adaxry/CM-Net)

 

|          model           | Slot(F1) | Intent(Acc) | Overall |
| :----------------------: | :------: | :---------: | :-----: |
|        Slot-Gated        |          |             |         |
|      SF-ID Network       |          |             |         |
|          CM-Net          |  86.16   |    94.56    |    -    |
|    Stack-Propagation     |          |             |         |
| Multi-Level Word Adapter |          |             |         |

- SMP：

SMP comes from[8th National Social Media Processing Conference (SMP 2019)](https://mp.weixin.qq.com/s/Gij10octDVBHjgKy1plXaQ)和[Ninth National Social Media Processing Conference (SMP 2020))](https://smp2020.aconf.cn/smp.html#3)Evaluate Chinese Dialogue Technology  (ECDT) task.Because the competition has ended, it is divided into the training datasets。According to the number of intentions, the original training set is divided into a training set at the ratio of 8: 1: 1, and the verification set and test set。SMP2019 dataset includes 2,053 training, 256 validation and 270 test utterances.SMP2020 dataset includes 4,011 training, 493 validation and 520 test utterances.



|          model           | Slot(F1) | Intent(Acc) | Overall |
| :----------------------: | :------: | :---------: | :-----: |
|        Slot-Gated        |          |             |         |
|      SF-ID Network       |          |             |         |
|          CM-Net          |    -     |      -      |    -    |
|    Stack-Propagation     |          |             |         |
| Multi-Level Word Adapter |          |             |         |