/* This script reads gridded data and plots a surface in three dimensions.  The data consists
of a 1D array of x values, a 1D array of y values, and a 2D array of z values z(x,y).  The 
data is stored in a file in XDR format, in the following order:

double len(x)
array of x data
double len(y)
array of y data
z row 1
z row 2
...
z row n

Z is stored in row-major order, so row 1 contains values (x1,y1), (x1,y2), etc.
*/
import graph3;
import contour;

defaultpen(fontsize(10));

write("Plotting...");

real theta_max = 0.53;
real z_min = -7;
string noLabels(real z) {
    return "";
    }

currentprojection=orthographic(-4,0.9,30); // Coefficient b

currentlight=(0,1,1);

size(8cm, 8cm, keepAspect=false);

file xdr_input_file=xinput("./coeff_plot_data.xdr");
int xlen = xdr_input_file;
real[] x = xdr_input_file.dimension(xlen);
int ylen = xdr_input_file;
real[] y = xdr_input_file.dimension(ylen);

real [][] z;
for(int i=0; i <=xlen; ++i) {
    z[i] = xdr_input_file.dimension(ylen);
}

draw(surface(z,x,y,monotonic), lightgray+opacity(0.3), meshpen=black, nolight);

// Coefficient b
xaxis3(Label("$h$", align=Relative((-1,-1))), Bounds(Both, Min), ticks=InTicks);
xaxis3(Bounds(Min, Max), ticks=InTicks(ticklabel=noLabels));

yaxis3(Label("$\theta$", position=(0.5,0), align=Relative((1,-1))), 0, theta_max,
    axis=Bounds(Both, Min), ticks=InTicks(beginlabel=false, endlabel=true));
yaxis3(Bounds(Max, Max), ticks=OutTicks(ticklabel=noLabels));

zaxis3(Label("$k_2$", position=(0.5,0), align=Relative((0.75,0.0))), 
    axis=Bounds(Both, Min), ticks=InTicks);
zaxis3(axis=Bounds(Max,Max), ticks=OutTicks(ticklabel=noLabels));

write("Saving plot...");

