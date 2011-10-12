// Run with
// asy -f pdf -o ../Figures/Adsorption_Model_Matrix.pdf adsorption_model_matrix.asy
size(6cm);

pen mypen = linewidth(2.0);

draw( (0,0.5)--(2,0.5), mypen);
draw( (1.0,0)--(1.0,1), mypen);
label("Langmuir", (0.5, 0.75), Center);
label("RSA", (1.5, 0.75), Center);
label("Michael et al.", (0.5, 0.25), Center);
label("Brusatori et al.", (1.5, 0.25), Center);

