# VIP CUP 2023 OLIVES Biomarker Detection


***

This work was done in the [Omni Lab for Intelligent Visual Engineering and Science (OLIVES) @ Georgia Tech](https://ghassanalregib.info/). 
This competition is based on the [OLIVES](https://proceedings.neurips.cc/paper_files/paper/2022/hash/3be60b4a739b95a07a944a1a2c41e05e-Abstract-Datasets_and_Benchmarks.html) dataset published at NeurIPS 2022.
Feel free to check our lab's [Website](https://ghassanalregib.info/publications) 
and [GitHub](https://github.com/olivesgatech) for other interesting work!!!

***

## Citation

Prabhushankar, M., Kokilepersaud, K., Logan, Y. Y., Trejo Corona, S., AlRegib, G., & Wykoff, C. (2022). Olives dataset: Ophthalmic labels for investigating visual eye semantics. Advances in Neural Information Processing Systems, 35, 9201-9216.

## Data

The data for this competition can be downloaded at ...

Training_Biomarker_Data.csv : Biomarker labels in training set.

Training_Unlabeled_Clinical_Data.xlsx : Provides the clinical labels for all the data without biomarker information.

test_set_submission_template.csv : This provides the structure by which all submissions should be organized. 
This includes the image path and the associated 6 biomarkers.

PRIME_FULL and TREX DME are the training sets.

RECOVERY is the test set. The ground truth biomarker labels are held out, but the images and clinical data are provided.

## Submission

To submit please fill out the provided template using the model output for each image in the test set. 
There should be the file path followed by a one or zero for the presence or absenece of each of 6 biomarkers for the associated image.

Submit this csv file to the following server ...

## Starter Code Usage

Download and run the final_submission.ipynb file on Kaggle after adding the VIP dataset.


## Baseline Results

With this repository, a ResNet-50 model, and 100 epochs of training, we achieved a macro-averaged F1-Score of .6256.

### Acknowledgements

This work was done in collaboration with the [Retina Consultants of Texas](https://www.retinaconsultantstexas.com/).
This codebase utilized was partly constructed with code from the [Supervised Contrastive Learning](https://github.com/HobbitLong/SupContrast) Github.
