Joint Disfluency Detection and Constituency Parsing
------------------------------------------------------------
A joint disfluency detection and constituency parsing model for transcribed speech based on [Neural Constituency Parsing of Speech Transcripts](https://www.aclweb.org/anthology/N19-1282) from NAACL 2019, with additional changes (e.g. self-training and ensembling) as described in [Improving Disfluency Detection by Self-Training a Self-Attentive Model](https://www.aclweb.org/anthology/2020.acl-main.346/) from ACL 2020.

This repository updated the original repository to focus on inferencing using the pretrained [`swbd_fisher_bert_Edev.0.9078.pt`](https://github.com/pariajm/joint-disfluency-detector-and-parser/releases/download/naacl2019/swbd_fisher_bert_Edev.0.9078.pt) model.

### Installation
```bash
$ pip install disfluency-constituency-parser
```

### Usage
```bash
$ wget https://github.com/pariajm/joint-disfluency-detector-and-parser/releases/download/naacl2019/swbd_fisher_bert_Edev.0.9078.pt
$ wget https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased-vocab.txt
$ wget https://s3.amazonaws.com/models.huggingface.co/bert/bert-base-uncased.tar.gz
```


```python
from dc_parser import DC_Model
model = DC_Model(model_path = "/path/to/swbd_fisher_bert_Edev.0.9078.pt",
                bert_model_path = "/path/to/bert-base-uncased.tar.gz",
                bert_vocab_path = "/path/to/bert-base-uncased-vocab.txt",)
model.parse(["Today is a very good day!"])
```

### Citation
If you use this model, please cite the following papers:
```
@inproceedings{jamshid-lou-2019-neural,
    title = "Neural Constituency Parsing of Speech Transcripts",
    author = "Jamshid Lou, Paria and Wang, Yufei and Johnson, Mark",
    booktitle = "Proceedings of the 2019 Conference of the North {A}merican Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)",
    month = "June",
    year = "2019",
    address = "Minneapolis, Minnesota",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/N19-1282",
    doi = "10.18653/v1/N19-1282",
    pages = "2756--2765"
}
```

```
@inproceedings{jamshid-lou-2020-improving,
    title = "Improving Disfluency Detection by Self-Training a Self-Attentive Model",
    author = "Jamshid Lou, Paria and Johnson, Mark",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = "jul",
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.346",
    pages = "3754--3763"
}
```