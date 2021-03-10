# FEA-using-DNN
The input data is generated via FEA to train a DNN. The DNN learns the curve force-displacement.

## Geometry

The figure below shows a star-dome like 3D truss with 24 bars of different cross sectional areas.  The highly nonlinear response, leading to a snap-through effect, makes the structure widely explored as a benchmark for new algorithmighly nonlinear response, leading to a snap-through effect, makes the structure widely explored as a benchmark for new algorithms, quite explored in the literature.

![Star_Geometry](https://user-images.githubusercontent.com/47003542/106145665-94692d00-6154-11eb-93bf-7429f30e523a.png)

The geometry is defined by a random set of 24 different cross section areas. Then, the structure is loaded and analysed in the commercial FE software Abaqus. A table with displacement of the central node and reactions - is provided as output.

For the NN, the areas are the input data and the displacements  and reactions are the output.

## Data Upload

Three files are available to upload in the folder *Datasets*:
1. the dataset containing the areas, `areas24.csv`;
2. displacements and reaction force along the time, `FinalResult.csv`;
3. the dataset with all models with snap-back instability behaviour,  `Snapback.csv`.

See that `FinalResult.csv` is a huge file, so, it is compressed into 2 parts.

If you prefer to generate your own data, we suggest to use the student version of the software [Abaqus](https://edu.3ds.com/en/software/abaqus-student-edition). The following files are available here in the folder *DatasetGeneration*:
 1. To generate random areas `gera_areas_24.py`;
 2. Script to run in Abaqus to generate data `24-bar-truss.py`;
 3. Basic geometry to be called by the script mentioned in item 2 `Job-24-bar.inp`.
