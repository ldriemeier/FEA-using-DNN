# FEA-using-DNN
The input data is generated via FEA to train a DNN. The DNN learns the curve force-displacement.

## Geometry

The figure below shows a star-dome like 3D truss with 24 bars of different cross sectional areas.  The highly nonlinear response, leading to a snap-through effect, makes the structure widely explored as a benchmark for new algorithmighly nonlinear response, leading to a snap-through effect, makes the structure widely explored as a benchmark for new algorithms, quite explored in the literature.

![Star_Geometry](https://user-images.githubusercontent.com/47003542/106145665-94692d00-6154-11eb-93bf-7429f30e523a.png)

The geometry is defined by a random set of 24 different cross section areas. Then, the structure is loaded and analysed in the commercial FE software Abaqus. A table with displacement of the central node and reactions - is provided as output.

For the NN, the areas are the input data and the displacements  and reactions are the output.
