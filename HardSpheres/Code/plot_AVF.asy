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

real phi_theta_fit3(real theta) {
    real theta_bar = theta/0.547;
    return (1.-theta_bar)**3/(1.-0.812*theta_bar + 0.2336*theta_bar**2 + 0.0845*theta_bar**3);
}

real theta_max = 0.53;
string noLabels(real z) {
    return "";
    }

write("Plotting...");

currentprojection=orthographic(-2,1,1);
currentlight=(0,1,1);

size(10cm, 10cm, keepAspect=false);

file xdr_input_file=xinput("./AVF_plot_data.xdr");
int xlen = xdr_input_file;
real[] x = xdr_input_file.dimension(xlen);
int ylen = xdr_input_file;
real[] y = xdr_input_file.dimension(ylen);

real [][] z;
for(int i=0; i <=xlen; ++i) {
    z[i] = xdr_input_file.dimension(ylen);
}

draw(surface(z,x,y,monotonic), lightgray+opacity(0.5), meshpen=black, nolight);

// Add RSA blocking function
real [] rsa_values;
real [] zeros;
for (int i=0; i<ylen; ++i) {
    rsa_values[i] = phi_theta_fit3(y[i]);
    zeros[i] = 0.0;
}

pen rsa_pen = red+linetype("5 5") + 2.0;        // Red, dashed, width 2.0 PostScript units

path3 rsa_path = graph(zeros, y, rsa_values); 

draw(rsa_path, p=rsa_pen);

xaxis3(Label("$h$", position=(0.5,0)), axis=Bounds(Both, Min), ticks=InTicks);

yaxis3(Label("$\theta$", position=(0.5,0), align=Relative((1.0,-0.5))), 0, 
    theta_max, axis=Bounds(Both, Min), InTicks(endlabel=false));

zaxis3(Label("$AVF(h,\theta)$", position=(0.5,0), align=Relative((0.75,0.0))),
    0, 1, axis=Bounds(Both, Min), InTicks(n=1));

zaxis3(axis=Bounds(Max, Max), OutTicks(ticklabel=noLabels, n=1));

write("Saving plot...");

