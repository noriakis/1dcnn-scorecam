## Application of score-weighted class activation mapping (Score-CAM) on one dimensional convolutional neural networks (1D-CNN).
I applied the Score-CAM on 1D-CNN classifying the electrocardiogram (ECG). For the intepretability I classified the normal ECG and ECG with Premature Ventricular Complex (PVC).

## Dataset
- The publicly available dataset, PTB-XL; Wagner, P., Strodthoff, N., Bousseljot, RD. et al. [PTB-XL, a large publicly available electrocardiography dataset. Sci Data 7, 154 (2020).](https://doi.org/10.1038/s41597-020-0495-6)
- One must apply for the credential access to obtain and use the data.

## Results
### Accuracy
```
loss: 0.049, acc: 0.988
```
![confusion_matrix](images/cm.png "confusion_matrix")

### Example visualization
The highlighted background indicates CAM values below 90th percentile of all the CAM value. The algorithm seems to capture where the PVC occurs.
